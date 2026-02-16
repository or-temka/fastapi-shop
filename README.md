# FastAPI Shop - PostgreSQL

## Требования

- Python 3.11+
- PostgreSQL 16+
- Docker (опционально)

## Установка

### 1. Клонирование репозитория

```bash
git clone <repository-url>
cd <project-name>
```

### 2. Настройка переменных окружения

```bash
cp .env.example .env
```

Отредактируйте `.env` при необходимости.

### 3. Создание виртуального окружения

```bash
python -m venv .venv
```

### 4. Активация виртуального окружения

**Windows:**
```bash
.venv\Scripts\activate
```

**PowerShell:**
```powershell
.venv\Scripts\Activate.ps1
```

**Linux/macOS:**
```bash
source .venv/bin/activate
```

### 5. Установка зависимостей

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Запуск с PostgreSQL

### Вариант 1: Docker Compose (рекомендуется)

**Запуск:**
```bash
docker-compose up -d
```

**Остановка:**
```bash
docker-compose down
```

**Просмотр логов:**
```bash
docker-compose logs -f backend
```

**Пересборка после изменений:**
```bash
docker-compose up -d --build
```

### Вариант 2: Локальный PostgreSQL

1. Установите PostgreSQL 16
2. Создайте базу данных:

```sql
CREATE DATABASE shop_db;
CREATE USER shop_user WITH PASSWORD 'shop_password';
GRANT ALL PRIVILEGES ON DATABASE shop_db TO shop_user;
```

3. Примените миграции:

```bash
alembic upgrade head
```

4. Запустите приложение:

```bash
python run.py
```

## Миграции (Alembic)

### Создание новой миграции

```bash
alembic revision --autogenerate -m "description"
```

### Применение миграций

```bash
alembic upgrade head
```

### Откат последней миграции

```bash
alembic downgrade -1
```

### История миграций

```bash
alembic history
```

### Текущая версия БД

```bash
alembic current
```

## Заполнение тестовыми данными

```bash
python seed_data.py
```

## Проверка работы

```bash
curl http://localhost:8000/health
```

API docs: http://localhost:8000/api/docs

## Структура проекта

```
.
├── alembic/               # Миграции БД
│   ├── versions/         # Файлы миграций
│   ├── env.py           # Конфигурация Alembic
│   └── script.py.mako   # Шаблон миграций
├── app/
│   ├── models/          # SQLAlchemy модели
│   ├── repositories/    # Слой работы с БД
│   ├── routes/          # API endpoints
│   ├── schemas/         # Pydantic схемы
│   ├── services/        # Бизнес-логика
│   ├── config.py        # Настройки
│   ├── database.py      # Подключение к БД
│   └── main.py          # Точка входа FastAPI
├── static/              # Статические файлы
├── alembic.ini          # Конфигурация Alembic
├── docker-compose.yml   # Docker Compose
├── Dockerfile           # Docker образ
├── requirements.txt     # Зависимости Python
├── seed_data.py         # Скрипт заполнения данных
└── run.py              # Запуск в dev режиме
```

## Архитектура

**Слоистая архитектура:**
- **Routes** → валидация, HTTP
- **Services** → бизнес-логика
- **Repositories** → работа с БД
- **Models** → SQLAlchemy ORM

**Технологии:**
- FastAPI 0.115+
- SQLAlchemy 2.0 (modern style)
- Pydantic v2
- PostgreSQL 16
- Alembic (миграции)
- Docker Compose

## Деактивация окружения

```bash
deactivate
```
