
from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
import sys
import os

path = Path(os.getcwd())
sys.path.extend([str(path.parent.absolute())])

from app.config import settings

from app.routers.users import router as users_router


def create_app() -> FastAPI:
    middleware = [
        Middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
    ]
    app = FastAPI(
        title="Fast API Starter",
        description="API to start your development in Fast API.",
        openapi_url="/swagger.json",
        middleware=middleware)
    app.include_router(users_router)
    
    return app

app = create_app()


@app.get("/api/v1/healthcheck")
async def healthcheck():
    return "200 OK"


@app.on_event("startup")
async def startup_event():
    print('Startup called')



if __name__ == "__main__":
    host = ""
    if settings.env == 'develop' or settings.env == 'local':
        host = "localhost"
    else:
        host = "0.0.0.0"
    uvicorn.run('main:app', host=host, port=8000, reload=True, root_path="/")
