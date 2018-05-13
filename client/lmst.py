#!/usr/bin/env python3
import cmd
# Setup CMD commands
class LMSTShell(cmd.Cmd):
    def do_play(self,arg):
        pass

if __name__ == '__main__':
    LMSTShell().cmdloop()