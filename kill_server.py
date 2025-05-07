import os
# Error handling: LBYL vs EAFP
# - LBYL: Look before you leap
# - EAFP: Easier to ask forgiveness than permission
# In Python we prefer EAFP (but, cost of error)


def kill_server(pid_file):
    """Terminate server from pid written in PID file"""
    with open(pid_file) as fp:
        data = fp.read()

    pid = int(data)
    print(f'killing server with pid {pid}')
    os.remove(file_name)


file_name = 'app.pid'
try:
    kill_server(file_name)
except (FileNotFoundError, OSError):
    print(f'warning: no such file {file_name} ')
except ValueError as err:
    print(f'error: bad pid file {file_name} - {err}, removing')
    os.remove(file_name)


print('DONE')
