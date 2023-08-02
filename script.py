import subprocess
from database_filling import fill_database

# Создание виртуального окружения
subprocess.run(['python3', '-m', 'venv', 'venv'])

# Установка пакетов внутри виртуального окружения
subprocess.run(["venv/bin/pip", "install", "-r", 'requirements.txt'])

subprocess.run(["venv/bin/python3", "-m", "alembic", "upgrade", 'head'])

fill_database()

subprocess.run(["venv/bin/python3", "-m", "uvicorn", "src.main:app", '--reload', '--host', '0.0.0.0', '--port', '80'])


