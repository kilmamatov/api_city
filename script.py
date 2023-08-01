import subprocess
import database_filling
import platform


if __name__ == '__main__':
    if platform.system() == 'Windows':
        subprocess.run(['python', '-m', 'venv', 'venv'])
        subprocess.run(['venv\\Scripts\\activate.bat'])
    else:
        subprocess.run(['python3', '-m', 'venv', 'venv'])
        subprocess.run(['sh', 'venv/bin/activate'])
    subprocess.run(['pip', 'install', '-r', 'requirements.txt'])
    subprocess.run(['alembic', 'revision', '--autogenerate'])
    subprocess.run(['alembic', 'upgrade', 'head'])
    database_filling.fill_database()
    subprocess.run(['uvicorn', 'src.main:app', '--reload', '--host', '127.0.0.1', '--port', '8000'])

