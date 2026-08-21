from typing import Literal

from fastapi import FastAPI
from pydantic import BaseModel


class HealthResponse(BaseModel):
    """APIの稼働状態を表すレスポンス。"""

    status: Literal["ok"] = "ok"


def health_check() -> HealthResponse:
    """APIがリクエストを処理できる状態であることを返す。"""
    return HealthResponse()


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

    return application


app = create_app()
