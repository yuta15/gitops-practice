from typing import Literal

from fastapi import FastAPI
from pydantic import BaseModel


class HealthResponse(BaseModel):
    """APIの稼働状態を表すレスポンス。"""

    status: Literal["ok"] = "ok"


class HelloResponse(BaseModel):
    message: str = "Hello World"


class HogeResponse(BaseModel):
    message: str = "hogehoeg"


def health_check() -> HealthResponse:
    """APIがリクエストを処理できる状態であることを返す。"""
    return HealthResponse()


def hello_message() -> HelloResponse:
    return HelloResponse()


def hoge() -> HogeResponse:
    return HogeResponse()


def create_app() -> FastAPI:
    """設定済みのFastAPIアプリケーションを生成する。"""
    application = FastAPI(
        title="GitOps Practice API",
        description="GitOps PracticeのバックエンドAPI",
        version="0.1.0",
    )

    application.add_api_route(
        "/health",
        health_check,
        response_model=HealthResponse,
        methods=["GET"],
        tags=["system"],
        summary="APIの稼働状態を確認する",
    )

    application.add_api_route(
        "/hello", hello_message, response_model=HelloResponse, methods=["GET"], tags=["system"], summary="挨拶をする"
    )

    application.add_api_route(
        "/hoge", hoge, response_model=HogeResponse, methods=["GET"], tags=["system"], summary="ほげ"
    )

    return application


app = create_app()
