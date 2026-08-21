import pytest

from main import main


def test_main_success_prints_greeting(capsys: pytest.CaptureFixture[str]) -> None:
    """mainが標準出力へ期待するメッセージを出力することを確認する。"""
    main()

    assert capsys.readouterr().out == "Hello from gitops-practice!\n"
