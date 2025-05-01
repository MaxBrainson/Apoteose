import subprocess
import webbrowser
import time

def runserver():
    subprocess.Popen(['python', 'manage.py', 'runserver'])

def open_apoteose():
    webbrowser.open('http://127.0.0.1:8000/')

if __name__ == '__main__':
    runserver()
    time.sleep(3)
    open_apoteose()

    



