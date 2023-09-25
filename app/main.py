from typing import List
from fastapi import FastAPI
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware

from middlewares.authentication import AuthenticationMiddleware


def make_middleware() -> List[Middleware]:
    middleware = [
        Middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        ),
        # Middleware(
        #     AuthenticationMiddleware,
        #     backend=AuthBackend()
        # )
    ]

    return middleware


def get_application() -> FastAPI:
    # TODO: app setting 함수 작성
    # settings = get_app_setting()

    application = FastAPI(
        title="Infrastruct",
        version="0.1.0",
        summary="Infrastruct Template",
        middleware=make_middleware(),
    )

    # TODO: create start app handler 함수 작성
    # application.add_event_handler(
    #     "startup", create_start_app_handler(application, settings),
    # )

    # TODO: create stop app handler 함수 작성
    # application.add_event_handler(
    #     "shutdown", create_stop_app_handler(application)
    # )

    return application


app = get_application()
