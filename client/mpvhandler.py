#!/usr/bin/env python3
import subprocess
import time
import os
FNULL = open(os.devnull, 'w')
def startmpv():
    print('Starting MPV Library...')
    subprocess.Popen('mpv --idle --no-input-terminal --input-ipc-server=/tmp/LMST-MPV-socket', shell=True, encoding='UTF-8',stdin=FNULL, stderr=FNULL, stdout=FNULL)
    time.sleep(2)
    pcmd = subprocess.Popen(['/bin/bash', '-c', 'echo \'{ "command": ["client_name"] }\' | socat - /tmp/LMST-MPV-socket'], shell=False, stdout=subprocess.PIPE)
    if '"Connection refused' not in pcmd.communicate()[0].decode('utf-8'):
        pass
    print('MPV Should be Online, if you see \'Connection Refused\' try reinstalling MPV')
def stopmpv():
    print('Stopping MPV...')
    subprocess.Popen(['/bin/bash', '-c', 'echo \'{ "command": ["quit"] }\' | socat - /tmp/LMST-MPV-socket'], shell=False, stdout=subprocess.PIPE)
def mpv_pause():
    print('Pausing...')
    subprocess.Popen(['/bin/bash', '-c', 'echo \'{ "command": ["set_property", "pause", "yes"] }\' | socat - /tmp/LMST-MPV-socket'],shell=False, stdout=subprocess.PIPE)
def mpv_resume():
    print('Resuming Playback...')
    subprocess.Popen(['/bin/bash', '-c', 'echo \'{ "command": ["set_property", "pause", "no"] }\' | socat - /tmp/LMST-MPV-socket'],shell=False, stdout=subprocess.PIPE)
def mpv_playhttp(url):
    print('Starting Playback...')
    subprocess.Popen(['/bin/bash', '-c', 'echo \'{ "command": ["loadfile", "'+url+'"] }\' | socat - /tmp/LMST-MPV-socket'],shell=False, stdin=FNULL, stderr=FNULL, stdout=FNULL)