import os

import uvicorn
from fastapi import FastAPI

from .routes import router

app = FastAPI()

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(
        app,
        host=os.getenv("APP_HOST", "0.0.0.0"),
        port=int(os.getenv("APP_PORT", 8000)),
    )
