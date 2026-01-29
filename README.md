# Установка и запуск проекта

## Требования

- Python 3.14
- pip

## Установка

### 1. Клонирование репозитория

```bash
git clone <repository-url>
cd <project-name>
```

### 2. Создание виртуального окружения

**venv (встроенный)**

```bash
python -m venv .venv
```

### 3. Активация виртуального окружения

**Windows:**

```bash
.venv\Scripts\activate
```

**PowerShell:**

```powershell
venv\Scripts\Activate.ps1
```

### 4. Обновление pip

```bash
python -m pip install --upgrade pip
```

### 5. Установка зависимостей

```bash
pip install -r requirements.txt
```

## Запуск

### Development

```bash
python run.py
```

### Docker

**Билд и запуск:**

```bash
docker build -t fastapi-shop .
docker run -d -p 8000:8000 --name fastapi-shop-container fastapi-shop
```

**С Docker Compose:**

```bash
docker-compose up -d
```

**Остановка:**

```bash
docker stop fastapi-shop-container
# или
docker-compose down
```

**Просмотр логов:**

```bash
docker logs -f fastapi-shop-container
# или
docker-compose logs -f
```

## Проверка установки

```bash
curl http://localhost:8000/health
```

## Деактивация окружения

```bash
deactivate
```
