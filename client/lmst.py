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
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd('\n')
    def do_play(self,arg):
        """NOT YET IMPLEMENTED"""
        pass
    def do_quit(self, arg):
        """
        Exit LMST. Safely quits MPV and shuts down.
        """
        stopmpv()
        time.sleep(3)
        raise SystemExit(0)
    def do_pause(self,args):
        """
        Pause Current Playback
        """
        mpv_pause()
    def do_resume(self,args):
        """
        Pause Current Playback
        """
        mpv_resume()
    def do_playdebug(self,args):
        """
        DEBUG COMMAND:
        Play a file from a HTTP link.
        Format:
        * playdebug [link]
        """
        http = args.split()
        mpv_playhttp(http[0])
    def do_updatehost(self,args):
        """Update the location of the Database."""
        newhost = input('Enter the base URL for the Database: ')
        newfolder = input('Enter the folder path for the Database: ')
        newdb = input('Enter the file name of the Database: ')
        pass
    def do_updatedb(self):
        """Grab the latest database file from the host."""
        pass

if __name__ == '__main__':
    createconfig()
    startmpv()
    LMSTShell().cmdloop()