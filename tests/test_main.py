from fastapi.routing import APIRoute

from main import HealthResponse, create_app, health_check


def test_health_check_success_returns_ok() -> None:
    """ヘルスチェックが正常状態を返すことを確認する。"""
    response = health_check()

    assert response == HealthResponse(status="ok")


def test_create_app_success_registers_health_route() -> None:
    """生成したアプリケーションにヘルスチェックが登録されることを確認する。"""
    application = create_app()
    api_route_paths = {route.path for route in application.routes if isinstance(route, APIRoute)}

    assert "/health" in api_route_paths
