import json
import time
import uuid
import asyncio
import cloudscraper
from typing import Dict, Any, AsyncGenerator

from fastapi import HTTPException
from fastapi.responses import StreamingResponse, JSONResponse
from loguru import logger

from app.core.config import settings
from app.providers.base_provider import BaseProvider
from app.utils.sse_utils import create_sse_data, create_chat_completion_chunk, DONE_CHUNK

class TarotooProvider(BaseProvider):
    def __init__(self):
        self.scraper = cloudscraper.create_scraper()
        self.api_url = "https://tarotoo.com/wp-json/openai/v1/chat-message"
        logger.info("TarotooProvider 初始化完成，使用 Cloudscraper 作为 HTTP 客户端。")

    async def chat_completion(self, request_data: Dict[str, Any]) -> StreamingResponse:
        
        async def stream_generator() -> AsyncGenerator[bytes, None]:
            request_id = f"chatcmpl-{uuid.uuid4()}"
            model_name = request_data.get("model", settings.DEFAULT_MODEL)
            
            try:
                headers = self._prepare_headers()
                payload = self._prepare_payload(request_data)
                
                logger.info(f"正在向上游发送请求: {self.api_url}")
                logger.debug(f"Payload: {payload}")

                # 使用 Cloudscraper 执行同步请求
                # 在 FastAPI 的异步视图中，对于 I/O 密集型操作，这是可接受的
                response = self.scraper.post(
                    self.api_url, 
                    headers=headers, 
                    json=payload,
                    timeout=settings.API_REQUEST_TIMEOUT
                )

                logger.info(f"上游响应状态码: {response.status_code}")
                response.raise_for_status()
                
                response_data = response.json()
                logger.debug(f"上游响应数据: {response_data}")
                
                full_content = response_data.get("content")
                if full_content is None:
                    raise ValueError("上游响应中缺少 'content' 字段。")

                # 应用【模式：伪流式生成】
                for char in full_content:
                    chunk = create_chat_completion_chunk(request_id, model_name, char)
                    yield create_sse_data(chunk)
                    await asyncio.sleep(settings.PSEUDO_STREAM_DELAY)
                
                final_chunk = create_chat_completion_chunk(request_id, model_name, "", "stop")
                yield create_sse_data(final_chunk)

            except Exception as e:
                logger.error(f"处理流时发生错误: {e}", exc_info=True)
                error_message = f"内部服务器错误: {str(e)}"
                error_chunk = create_chat_completion_chunk(request_id, model_name, error_message, "stop")
                yield create_sse_data(error_chunk)
            finally:
                yield DONE_CHUNK
                logger.info(f"请求 {request_id} 的流式响应结束。")

        return StreamingResponse(stream_generator(), media_type="text/event-stream")

    def _prepare_headers(self) -> Dict[str, str]:
        # cloudscraper 会自动管理 User-Agent 和 Cookie
        return {
            "accept": "*/*",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
            "content-type": "application/json",
            "origin": "https://tarotoo.com",
            "referer": "https://tarotoo.com/psychic",
            "sec-ch-ua": '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
        }

    def _prepare_payload(self, request_data: Dict[str, Any]) -> Dict[str, Any]:
        messages = request_data.get("messages", [])
        if not messages:
            raise HTTPException(status_code=400, detail="请求体中缺少 'messages' 字段或为空。")
        
        # 精确复制上游API所需的payload结构
        return {
            "messages": messages,
            "currentSiteLang": "en"
        }

    async def get_models(self) -> JSONResponse:
        model_data = {
            "object": "list",
            "data": [
                {"id": name, "object": "model", "created": int(time.time()), "owned_by": "lzA6"}
                for name in settings.KNOWN_MODELS
            ]
        }
        return JSONResponse(content=model_data)

