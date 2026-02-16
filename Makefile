.PHONY: help up down build logs restart migrate-create migrate-up migrate-down seed clean

help:
	@echo "FastAPI Shop - Команды"
	@echo ""
	@echo "Docker:"
	@echo "  make up          - Запуск контейнеров"
	@echo "  make down        - Остановка контейнеров"
	@echo "  make build       - Пересборка и запуск"
	@echo "  make logs        - Просмотр логов"
	@echo "  make restart     - Перезапуск"
	@echo ""
	@echo "Миграции:"
	@echo "  make migrate-create MSG='description' - Создать миграцию"
	@echo "  make migrate-up  - Применить миграции"
	@echo "  make migrate-down - Откатить последнюю миграцию"
	@echo ""
	@echo "Прочее:"
	@echo "  make seed        - Заполнить БД тестовыми данными"
	@echo "  make clean       - Очистка"

up:
	docker-compose up -d

down:
	docker-compose down

build:
	docker-compose up -d --build

logs:
	docker-compose logs -f backend

restart:
	docker-compose restart backend

migrate-create:
	alembic revision --autogenerate -m "$(MSG)"

migrate-up:
	alembic upgrade head

migrate-down:
	alembic downgrade -1

seed:
	python seed_data.py

clean:
	docker-compose down -v
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
