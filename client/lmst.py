#!/usr/bin/env python3
import time
import cmd
from mpvhandler import *
from confighandler import *
# Setup CMD commands
class LMSTShell(cmd.Cmd):
    intro = 'Welcome to LMST. Type \'help\' for a list of commands'
    prompt = '(LMST) '

    def emptyline(self):
        """Called when an empty line is entered in response to the prompt.
        If this method is not overridden, it repeats the last nonempty
        command entered.
        """
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd('\n')
    def do_play(self,arg):
        pass
    def do_quit(self, arg):
        stopmpv()
        time.sleep(3)
        raise SystemExit(0)
    def do_pause(self,args):
        mpv_pause()
    def do_resume(self,args):
        mpv_resume()
    def do_playdebug(self,args):
        http = args.split()
        mpv_playhttp(http[0])

if __name__ == '__main__':
    createconfig()
    startmpv()
    LMSTShell().cmdloop()