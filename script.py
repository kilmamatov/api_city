import os
import platform
import subprocess

# if __name__ == '__main__':
#     subprocess.run(['python3', '-m', 'venv', 'venv'])
#
#     subprocess.run(["venv/bin/pip", "install", "-r", 'requirements.txt'])
#
#     subprocess.run(["venv/bin/python3", "-m", "alembic", "upgrade", 'head'])
#
#     input_commands = 'from database_filling import fill_database\n' \
#                      'fill_database()\n'
#
#     subprocess.run('venv/bin/python3', input=input_commands, text=True, shell=True)
#
#     subprocess.run(["venv/bin/python3", "-m", "uvicorn", "src.main:app", '--reload', '--host', '127.0.0.1', '--port', '8000'])


if __name__ == '__main__':
    venv_name = 'venv'

    if platform.system() == 'Windows':
        subprocess.run(['python', '-m', 'venv', venv_name], shell=True)
        activate_script = os.path.join(venv_name, 'Scripts', 'activate.bat')
    else:
        subprocess.run(['python3', '-m', 'venv', venv_name])
        activate_script = os.path.join(venv_name, 'bin', 'activate')

    subprocess.run(activate_script, shell=True)

    subprocess.run([os.path.join(venv_name, 'bin', 'pip'), 'install', '-r', 'requirements.txt'])

    subprocess.run([os.path.join(venv_name, 'bin', 'python'), '-m', 'alembic', 'upgrade', 'head'])
    input_commands = 'from database_filling import fill_database\nfill_database()\n'
    subprocess.run([os.path.join(venv_name, 'bin', 'python'), '-c', input_commands])

    subprocess.run(
        [os.path.join(venv_name, 'bin', 'python'), '-m', 'uvicorn', 'src.main:app', '--reload', '--host', '127.0.0.1',
         '--port', '8000'])
