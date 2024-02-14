import uvicorn
from fastapi import FastAPI

app = FastAPI(
    version="0.1.0"
)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",  # noqa: S104
        port=8000,
    )
