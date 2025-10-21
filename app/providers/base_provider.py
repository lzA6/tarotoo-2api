from abc import ABC, abstractmethod
from typing import Dict, Any, Union
from fastapi.responses import StreamingResponse, JSONResponse

class BaseProvider(ABC):
    @abstractmethod
    async def chat_completion(
        self,
        request_data: Dict[str, Any]
    ) -> Union[StreamingResponse, JSONResponse]:
        pass

    @abstractmethod
    async def get_models(self) -> JSONResponse:
        pass
