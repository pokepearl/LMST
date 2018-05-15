#!/usr/bin/env python3
import subprocess
import time
def startmpv():
    print('Starting MPV Library...')
    subprocess.Popen('mpv --idle --input-ipc-server=/tmp/LMST-MPV-socket', shell=True, encoding='UTF-8')
    time.sleep(2)
    pcmd = subprocess.Popen(['/bin/bash', '-c', 'echo \'{ "command": ["client_name"] }\' | socat - /tmp/LMST-MPV-socket'], shell=False, stdout=subprocess.PIPE)
    if '"Connection refused' not in pcmd.communicate()[0].decode('utf-8'):
        pass
    print('MPV Should be Online, if you see \'Connection Refused\' try reinstalling MPV')
def stopmpv():
    print('Stopping MPV...')
    subprocess.Popen(['/bin/bash', '-c', 'echo \'{ "command": ["quit"] }\' | socat - /tmp/LMST-MPV-socket'], shell=False, stdout=subprocess.PIPE)