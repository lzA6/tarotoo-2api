# ====================================================================
# Dockerfile for tarotoo-2api (v1.1 - EOL & Concurrency Fixed)
# ====================================================================

# 使用一个更现代且受支持的 Debian 版本 "Bullseye" 作为基础
FROM python:3.10-slim-bullseye

# 设置环境变量
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 安装 cloudscraper 所需的系统依赖
# Bullseye 的源是活跃的，无需修改
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential curl && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# 安装 Python 依赖
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 复制应用代码
COPY . .

# 创建并切换到非 root 用户
RUN useradd --create-home appuser && \
    chown -R appuser:appuser /app
USER appuser

# 暴露端口并以单 Worker 模式启动，以保证会话一致性
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1"]

