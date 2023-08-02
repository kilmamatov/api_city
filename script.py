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
    venv_path = './venv'

    subprocess.run(['python3', '-m', 'venv', venv_path], check=True)

    venv_activate = f'{venv_path}/bin/activate'
    install_command = f'sh {venv_activate} && pip install -r requirements.txt'
    subprocess.run(install_command, shell=True, check=True, executable='/bin/bash')

    alembic_upgrade = f'sh {venv_activate} && alembic upgrade head'
    subprocess.run(alembic_upgrade, shell=True, check=True, executable='/bin/bash')

    fill_database()

    uvicorn = f'sh {venv_activate} && uvicorn src.main:app --reload --host 127.0.0.1 --port 8000'
    subprocess.run(uvicorn, shell=True, check=True, executable='/bin/bash')

