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

## Проверка установки

```bash
curl http://localhost:8000/health
```

## Деактивация окружения

```bash
deactivate
```
