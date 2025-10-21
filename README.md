# 🔮 tarotoo-2api: 赛博塔罗牌 AI 算命大师 API 代理

<div align="center">
  
  <p>
    <b>将 tarotoo.com 匿名聊天功能转换为兼容 OpenAI 格式 API 的高性能代理</b>
  </p>
  
  <p>
    <span>✨ 内置 Cloudflare 穿透</span> • 
    <span>💨 伪流式生成</span> • 
    <span>🚀 零配置启动</span>
  </p>

  <p>
    <a href="https://github.com/lzA6/tarotoo-2api/blob/main/LICENSE">
      <img src="https://img.shields.io/github/license/lzA6/tarotoo-2api?style=flat-square&color=blue" alt="License">
    </a>
    <a href="https://github.com/lzA6/tarotoo-2api/stargazers">
      <img src="https://img.shields.io/github/stars/lzA6/tarotoo-2api?style=flat-square&color=yellow" alt="Stars">
    </a>
    <a href="https://github.com/lzA6/tarotoo-2api/issues">
      <img src="https://img.shields.io/github/issues/lzA6/tarotoo-2api?style=flat-square&color=red" alt="Issues">
    </a>
    <a href="https://hub.docker.com/">
      <img src="https://img.shields.io/badge/Docker-Ready-2496ED?style=flat-square&logo=docker" alt="Docker Ready">
    </a>
    <a href="https://fastapi.tiangolo.com/">
      <img src="https://img.shields.io/badge/FastAPI-0.68.0-009688?style=flat-square&logo=fastapi" alt="FastAPI">
    </a>
  </p>
</div>

---

> **【开发者沉思 🤔】**
>
> 在代码的海洋中，我们常扮演"数字炼金术士"的角色。我们不创造黄金，却能将一种形态的"价值"转化为另一种。`tarotoo-2api` 就是这样一次有趣的炼金实验：它将充满神秘色彩的在线塔罗牌网站，炼成了开发者熟悉且能轻松驾驭的"数字黄金"——OpenAI 格式的 API。
>
> 这不仅是技术转换，更是"可能性"的延伸。它让我们思考：能否为互联网上每个有趣但封闭的角落，都开启通往自动化世界的大门？这扇门，就是 API。
>
> 本项目献给所有充满好奇心、热爱探索、坚信"万物皆可 API"的开发者。愿你在探索中不仅收获技术，更能感受创造的喜悦和开源精神的真谛。

---

## ✨ 项目简介

`tarotoo-2api` 是一个轻量级、高性能的代理服务，核心使命是：**将 [tarotoo.com](https://tarotoo.com/psychic) 网站的匿名 AI 聊天功能，封装成完全兼容 OpenAI `v1/chat/completions` API 格式的服务。**

现在你可以用任何支持 OpenAI API 的客户端、软件或代码库，与这位"赛博算命大师"对话，无需关心背后复杂的网站结构和 Cloudflare 防护。

### 🎯 核心特性

| 特性 | 描述 | 图标 |
|------|------|------|
| **一键部署** | Docker Compose 打包，零配置启动 | 🚀 |
| **Cloudflare 穿透** | 内置 `cloudscraper`，绕过反爬虫机制 | 🛡️ |
| **流式输出** | 模拟逐字打印的"打字机"效果 | 💨 |
| **标准化 API** | 严格遵循 OpenAI API 格式规范 | 📊 |
| **安全认证** | 支持 API Key 保护，防止滥用 | 🔑 |

## 🎯 解决的核心问题

想象你在网上发现了一个有趣的 AI 聊天服务，但只有简陋的网页界面。想集成到 Discord 机器人、个人网站或自动化流程中时，却面临重重障碍：

1. **🔄 无官方 API** - 只能手动操作网页界面
2. **🚫 反爬虫防护** - Cloudflare 5秒盾、JS 挑战阻挡普通爬虫
3. **📦 非标准格式** - 需要编写复杂的数据解析代码

`tarotoo-2api` 就是为解决这些痛点而生！它如同"万能转换插头"，将特殊接口转换为全球通用的"OpenAI 标准插座"。

### 💼 应用场景

- **🤖 娱乐机器人** - 集成到 Discord、Telegram、Slack 机器人中
- **⚡ 快速原型** - 免费、无需注册的 AI 聊天后端
- **🎓 学习研究** - API 代理、反爬虫、异步编程的绝佳案例
- **🔮 个人项目** - 需要神秘 AI 对话伙伴的创新应用

## 🚀 快速开始

### 前置要求

- 🐳 **Docker** & **Docker Compose**
- 📁 **Git**（可选，用于克隆仓库）

### 四步部署指南

**步骤 1：获取代码**
```bash
git clone https://github.com/lzA6/tarotoo-2api.git
cd tarotoo-2api
```

**步骤 2：配置环境**
```bash
# Linux/macOS
cp .env.example .env

# Windows
copy .env.example .env
```

编辑 `.env` 文件：
```ini
# ====================================================================
# tarotoo-2api 配置文件
# ====================================================================

# 安全密钥（建议修改为复杂字符串）
API_MASTER_KEY=your-super-secret-key-here

# 服务端口（如被占用可修改）
NGINX_PORT=8087
```

**步骤 3：启动服务**
```bash
docker-compose up -d
```

**步骤 4：测试 API**
```bash
curl -X POST http://localhost:8087/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-super-secret-key-here" \
  -d '{
    "model": "tarotoo-psychic-chat",
    "messages": [
      {
        "role": "user",
        "content": "你好，请帮我算算今天的运势？"
      }
    ],
    "stream": true
  }'
```

看到 `data: {...}` 格式的流式响应？恭喜！部署成功！🎉

## 🏗️ 系统架构

<div align="center">

```mermaid
graph TB
    subgraph "外部网络"
        User[👤 用户/客户端]
    end
    
    subgraph "tarotoo-2api 服务栈"
        Nginx[🔄 Nginx 反向代理<br/>端口: 8087]
        FastAPI[🐍 FastAPI 应用<br/>端口: 8000]
    end
    
    subgraph "目标服务"
        Cloudflare[🛡️ Cloudflare 防护]
        Tarotoo[🔮 tarotoo.com API]
    end
    
    User -->|"1. HTTP 请求"| Nginx
    Nginx -->|"2. 代理转发"| FastAPI
    FastAPI -->|"3. Cloudscraper"| Cloudflare
    Cloudflare -->|"4. 真实请求"| Tarotoo
    
    Tarotoo -->|"5. AI 响应"| Cloudflare
    Cloudflare -->|"6. 绕过检测"| FastAPI
    FastAPI -->|"7. 格式转换"| Nginx
    Nginx -->|"8. 流式输出"| User
    
    style User fill:#e1f5fe
    style Nginx fill:#f3e5f5
    style FastAPI fill:#e8f5e8
    style Cloudflare fill:#fff3e0
    style Tarotoo fill:#fce4ec
```

</div>

### 架构组件详解

| 组件 | 角色 | 核心技术 | 功能特点 |
|------|------|----------|----------|
| **Nginx** | 🚪 API 网关 | 反向代理、负载均衡 | `ip_hash` 会话保持、流式传输优化 |
| **FastAPI** | 🧠 业务逻辑核心 | 异步 Web 框架、Pydantic | OpenAI 兼容接口、请求验证 |
| **Cloudscraper** | 🎭 反爬虫穿透 | 浏览器模拟、JS 执行 | 绕过 Cloudflare 挑战 |
| **SSE 生成器** | 💬 流式响应 | 异步生成器、Server-Sent Events | 伪流式输出模拟 |

## 🔧 技术实现深度解析

### 核心代码流程

```python
# 简化的核心处理流程
async def chat_completion_stream(request: ChatCompletionRequest):
    # 1. 认证验证
    await verify_api_key(request)
    
    # 2. 构造上游请求
    headers = _prepare_headers()
    payload = _prepare_payload(request.messages)
    
    # 3. 发送请求（绕过 Cloudflare）
    response = self.scraper.post(upstream_url, headers=headers, json=payload)
    
    # 4. 提取响应内容
    content = extract_content_from_response(response)
    
    # 5. 伪流式输出
    for char in content:
        chunk = create_chat_completion_chunk(char)
        yield create_sse_data(chunk)
        await asyncio.sleep(0.02)  # 模拟打字效果
```

### 关键技术特性

#### 🛡️ Cloudflare 穿透机制
```python
# 使用 cloudscraper 模拟真实浏览器
self.scraper = cloudscraper.create_scraper(
    browser={
        'browser': 'chrome',
        'platform': 'windows',
        'mobile': False
    }
)
# 自动处理 JS 挑战、Cookie 管理等
```

#### 💨 伪流式输出
```python
async def stream_generator(content: str):
    """将完整响应转换为流式输出"""
    for index, char in enumerate(content):
        chunk = {
            "id": f"chatcmpl-{uuid4()}",
            "object": "chat.completion.chunk",
            "created": int(time.time()),
            "model": "tarotoo-psychic-chat",
            "choices": [
                {
                    "index": 0,
                    "delta": {"content": char},
                    "finish_reason": None
                }
            ]
        }
        yield f"data: {json.dumps(chunk)}\n\n"
        await asyncio.sleep(0.02)  # 控制输出速度
    
    # 结束标记
    yield "data: [DONE]\n\n"
```

#### 🔐 安全认证层
```python
async def verify_api_key(api_key: str = Depends(api_key_header)):
    """验证 API Key 中间件"""
    if api_key != settings.API_MASTER_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key"
        )
```

## 📊 技术栈评估

| 技术组件 | 用途 | 复杂度 | 评价 |
|----------|------|--------|------|
| **FastAPI** | API 框架 | ⭐⭐ | 现代异步框架，自动文档生成 |
| **Cloudscraper** | 反爬虫穿透 | ⭐⭐⭐ | 可靠的 Cloudflare 绕过方案 |
| **Docker Compose** | 容器编排 | ⭐⭐ | 简化部署，环境一致性 |
| **Nginx** | 反向代理 | ⭐⭐⭐ | 生产级负载均衡和缓存 |
| **异步生成器** | 流式响应 | ⭐⭐⭐⭐ | 高性能伪流式实现 |

## 🌟 项目优势与局限

### ✅ 核心优势

1. **🎯 开箱即用** - 五分钟内完成部署和测试
2. **🔌 广泛兼容** - 任何 OpenAI 生态工具均可接入
3. **🆓 完全免费** - 无需付费订阅或账号注册
4. **🎪 卓越体验** - 流式输出提升交互感受

### ⚠️ 潜在局限

1. **🔗 第三方依赖** - 服务稳定性依赖 tarotoo.com
2. **⏱️ 性能约束** - 响应速度受上游网站限制
3. **⚖️ 使用规范** - 请遵守合理使用原则

## 🚀 未来发展路线图

### 近期规划
- [ ] **多提供商支持** - 抽象 Provider 接口，支持更多网站
- [ ] **异步优化** - 使用 `asyncio.to_thread` 优化同步调用
- [ ] **缓存机制** - Redis 缓存提升重复请求响应速度

### 长期愿景
- [ ] **配置化模型** - 支持 temperature、top_p 等参数映射
- [ ] **Web UI 界面** - 内置聊天界面，降低使用门槛
- [ ] **健康监控** - 服务状态检测和自动恢复

## 📁 项目结构

```
tarotoo-2api/
├── 🐳 Dockerfile                 # 应用容器配置
├── 🎯 docker-compose.yml         # 服务编排配置
├── ⚙️ nginx.conf                 # Nginx 反向代理配置
├── 🔧 requirements.txt           # Python 依赖管理
├── 📄 main.py                    # FastAPI 应用入口
├── 🌟 .env.example               # 环境配置模板
└── 📂 app/                       # 应用核心代码
    ├── 📂 core/                  # 核心配置模块
    │   ├── __init__.py
    │   └── config.py             # Pydantic 配置模型
    ├── 📂 providers/             # 服务提供商抽象
    │   ├── __init__.py
    │   ├── base_provider.py      # 提供商基类
    │   └── tarotoo_provider.py   # Tarotoo 具体实现
    └── 📂 utils/                 # 工具函数
        └── sse_utils.py          # SSE 流式数据处理
```

## 🛠️ 故障排除

### 常见问题解决方案

| 问题 | 症状 | 解决方案 |
|------|------|----------|
| **端口冲突** | `Address already in use` | 修改 `.env` 中的 `NGINX_PORT` |
| **认证失败** | `401 Unauthorized` | 检查 `API_MASTER_KEY` 配置 |
| **服务无响应** | `Connection refused` | 确认 Docker 服务正常运行 |
| **Cloudflare 阻挡** | 长时间无响应 | 等待后重试，或更新 cloudscraper |

### 日志查看
```bash
# 查看服务日志
docker-compose logs -f

# 查看特定服务日志
docker-compose logs nginx
docker-compose logs app
```

## 🤝 参与贡献

我们欢迎各种形式的贡献！包括但不限于：

- 🐛 **问题反馈** - 提交 Bug 报告或使用问题
- 💡 **功能建议** - 提出新功能或改进建议
- 📝 **文档完善** - 改进文档或翻译
- 🔧 **代码提交** - 修复问题或实现新功能

请参考 [GitHub Issues](https://github.com/lzA6/tarotoo-2api/issues) 了解当前的任务列表。

---

<div align="center">

## 🌟 探索 • 创造 • 分享

**带着好奇心探索未知，用代码创造可能，以开源精神分享价值**

[⭐ Star 这个项目](https://github.com/lzA6/tarotoo-2api) 如果你觉得它有趣！

*让数字炼金术继续闪耀 ✨*

</div>

---

**维护者**: [lzA6](https://github.com/lzA6)  
**项目链接**: [https://github.com/lzA6/tarotoo-2api](https://github.com/lzA6/tarotoo-2api)

> **免责声明**: 本项目仅供学习和娱乐目的使用。请遵守相关网站的使用条款，合理使用 API 资源。
