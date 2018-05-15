#!/usr/bin/env python3
import time
import cmd
from mpvhandler import *
# Setup CMD commands
class LMSTShell(cmd.Cmd):
    intro = 'Welcome to LMST. Type \'help\' for a list of commands'
    prompt = '(LMST) '
    def do_play(self,arg):
        pass
    def do_quit(self, arg):
        stopmpv()
        time.sleep(3)
        raise SystemExit(0)

if __name__ == '__main__':
    startmpv()
    LMSTShell().cmdloop()