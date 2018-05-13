#!/usr/bin/env python3
import subprocess
def startmpv():
    print('Starting MPV Library...')
    subprocess.Popen('mpv --idle --input-ipc-server=/tmp/LMST-MPV-socket', shell=True, encoding='UTF-8')