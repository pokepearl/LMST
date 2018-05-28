#!/usr/bin/env python3
import time
import cmd
from mpvhandler import *
from confighandler import *
from dbhandler import *
# Setup CMD commands
class LMSTShell(cmd.Cmd):
    intro = 'Welcome to LMST. Type \'help\' for a list of commands'
    prompt = '(LMST) '
    def emptyline(self):
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd('\n')
    def do_play(self,arg):
        """Plays Songs
        Usage: play song {id}
        """
        try:
            info = arg.split()
            if info[0] == "song":
                songid = info[1]
                readdb('song', songid)
            else:
                print('Invalid argument')
        except IndexError:
            print('Invalid Argument, type song or album')

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
        newfolder = input('Enter the folder path for the Database (including beginning and end slash): ')
        newdb = input('Enter the file name of the Database: ')
        writeconfig('HTTP', 'host', str(newhost))
        writeconfig('HTTP', 'dbdirectory', str(newfolder))
        writeconfig('HTTP', 'dbname', str(newdb))
    def do_updatedb(self,arg):
        """Grab the latest database file from the host."""
        downloaddb(readconfig("HTTP","host"),readconfig("HTTP","dbdirectory"),readconfig("HTTP","dbname"),readconfig("FILE","localdb"))
    def do_stop(self,arg):
        mpv_reset()
if __name__ == '__main__':
    createconfig()
    startmpv()
    LMSTShell().cmdloop()