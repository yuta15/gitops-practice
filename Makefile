.DEFAULT_GOAL := help

.PHONY: help setup install-hooks format format-check lint lint-imports pyright test check pre-commit dev run

help: ## 利用できるコマンドを表示する
	@awk 'BEGIN {FS = ":.*## "} /^[a-zA-Z_-]+:.*## / {printf "%-16s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

setup: ## 開発依存を同期し、Gitのpre-commit hookをインストールする
	uv sync --all-groups
	uv run --no-sync pre-commit install

install-hooks: ## Gitのpre-commit hookをインストールする
	uv run --no-sync pre-commit install

format: ## Ruffで自動修正とフォーマットを行う
	uv run --no-sync ruff check --fix .
	uv run --no-sync ruff format .

format-check: ## Ruffのフォーマット差分を検査する
	uv run --no-sync ruff format --check .

lint: ## Ruffで静的解析を行う
	uv run --no-sync ruff check .

pyright: ## Pyrightで型を検査する
	uv run --no-sync pyright

test: ## pytestを実行する
	uv run --no-sync pytest

check: lint format-check pyright lint-imports test ## すべての検査を実行する

pre-commit: ## 全ファイルに対してpre-commitを実行する
	uv run --no-sync pre-commit run --all-files

dev: ## FastAPI開発サーバーを自動リロード付きで起動する
	PYTHONPATH=src uv run --no-sync fastapi dev src/main.py

run: ## FastAPIサーバーを起動する
	PYTHONPATH=src uv run --no-sync fastapi run src/main.py
