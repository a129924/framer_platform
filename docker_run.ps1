docker build -t fastapi_app .

docker run `
    -t `
    -p 8000:8000 `
    -v D:\code\python\framer_platform:/app `
    -w /app fastapi_app