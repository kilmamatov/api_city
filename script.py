import subprocess
from database_filling import fill_database
import sys
import platform
from pathlib import Path


# venv_dir = Path(__file__).parent / 'venv'
# python_executable = venv_dir / 'bin' / 'python'
# subprocess.run([sys.executable, '-m', 'venv', str(venv_dir)])
# subprocess.run([str(python_executable), '-m', 'pip', 'install', '-r', 'requirements.txt'])
# subprocess.run(['alembic', 'revision', '--autogenerate'])
# subprocess.run(['alembic', 'upgrade', 'head'])
# database_filling.fill_database()
# subprocess.run(['uvicorn', 'src.main:app', '--reload', '--host', '127.0.0.1', '--port', '8000'])

if __name__ == '__main__':

    subprocess.run(['python3', '-m', 'venv', 'venv'], check=True)

    install_command = 'source venv/bin/activate ' \
                      '&& pip install -r requirements.txt'
    subprocess.run(install_command, shell=True, check=True)

    alembic_upgrade = 'source venv/bin/activate ' \
                      '&& alembic upgrade head'
    subprocess.run(alembic_upgrade, shell=True, check=True)

    fill_database()

    uvicorn = 'source venv/bin/activate ' \
              '&& uvicorn src.main:app --reload --host 127.0.0.1 --port 8000'
    subprocess.run(uvicorn, shell=True, check=True)

