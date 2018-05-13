#!/usr/bin/env python3
import cmd
# Setup CMD commands
class LMSTShell(cmd.Cmd):
    intro = 'Welcome to LMST. Type \'help\' for a list of commands'
    prompt = '(LMST) '
    def do_play(self,arg):
        pass

if __name__ == '__main__':
    LMSTShell().cmdloop()