import subprocess


if __name__ == '__main__':
    subprocess.run(['python3', '-m', 'venv', 'venv'])

    subprocess.run(["venv/bin/pip", "install", "-r", 'requirements.txt'])

    subprocess.run(["venv/bin/python3", "-m", "alembic", "upgrade", 'head'])

    input_commands = 'from database_filling import fill_database\n' \
                     'fill_database()\n'

    subprocess.run('venv/bin/python3', input=input_commands, text=True, shell=True)

    subprocess.run(["venv/bin/python3", "-m", "uvicorn", "src.main:app", '--reload', '--host', '127.0.0.1', '--port', '8000'])