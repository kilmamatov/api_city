import subprocess
import database_filling
import sys
import platform
from pathlib import Path


if __name__ == '__main__':
    venv_dir = Path(__file__).parent / 'venv'
    python_executable = venv_dir / 'bin' / 'python'
    subprocess.run([sys.executable, '-m', 'venv', str(venv_dir)])
    subprocess.run([str(python_executable), '-m', 'pip', 'install', '-r', 'requirements.txt'])
    subprocess.run(['alembic', 'revision', '--autogenerate'])
    subprocess.run(['alembic', 'upgrade', 'head'])
    database_filling.fill_database()
    subprocess.run(['uvicorn', 'src.main:app', '--reload', '--host', '127.0.0.1', '--port', '8000'])

