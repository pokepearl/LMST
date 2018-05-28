- [Description](#description)
- [Install](#install)
    - [Supported OS](#supported-os)
    - [Client](#client)
    - [Server](#server)
        - [WebUI](#webui)
        - [Database Builder](#database-builder)
- [Usage](#usage)
    - [Client](#client)
        - [Command Explanation](#command-explanation)
    - [Server (Database Builder)](#server-database-builder)
    - [Server (WebUI)](#server-webui)
        - [Changing the database name](#changing-the-database-name)
        - [Locating the songID](#locating-the-songid)
- [Credits](#credits)
# Description
This project was made as part of a group assignment for the IFB102 unit at QUT.
LMST is a music streaming client and server system designed to be selfhosted. The client queries a SQLite database to obtain metadata based on a track id provided by the server-side WebUI. MPV is used as the playback backend for the client.
# Install
These instructions were designed for Raspbian on the RPI3, they may not perfectly work on other devices. The install scripts may be used with modifications.
## Supported OS
* Linux
* Mac (Untested)
* No Windows Support, the program requires Linux exclusive programs.
## Client
1. Clone the repo to a folder.
2. Install the `python3` and `python3-pip` packages for your distro.
3. Install the `build-essential libssl-dev libffi-dev libxml2-dev libxslt1-dev zlib1g-dev socat mpv` packages. (These may be different depending on the distro.)
4. Change to the client directory and install the required Python modules with `pip3 install -r requirements.txt`.
5. Install the program using `python3 setup.py install`. This uses CX_Freeze to package and install the scripts.
## Server
### WebUI
1. Clone the repo to a folder.
2. Install the `apache2 php7.0 php7.0-sqlite3 build-essential libssl-dev libffi-dev libxml2-dev libxslt1-dev zlib1g-dev` packages for your system (these may be different depending on your distro).
3. Make a directory to store the PHP and Music files as well as the database (this guide assumes `/opt/LMST/web` is used).
4. Create a new config for LMST in `/etc/apache2/sites-enabled/`.
5. Edit the config to use the directory you specified above for the webserver root and change the http port used if necessary.
6. Add `Listen {PORT}` to `/etc/apache2/ports.conf` to enable it and restart apache.
### Database Builder
1. Change to the database builder folder and run `pip3 install -r requirements.txt` to install required modules.
2. Install the program using `python3 setup.py install`. This uses CX_Freeze to package and install the scripts.
# Usage
## Client
### Command Explanation
* `updatehost` - Configure the address of the remote database and music server.
* `updatedb` - Download the latest copy of the remote database.
* `play` - Start playback of an individual song using the ID provided by the WebUI. Format: `play song {ID}`.
* `pause` - Pause the playback of the song.
* `resume` - Resume the playback of the song.
* `quit` - Safely close the MPV backend and exit the LMST client.
## Server (Database Builder)
**The Database Builder currently only searches for mp3,ogg and opus files. This can be changed in the script itself.**
1. Inside the root of the LMST Webserver directory, create a `Music` directory.
2. Place your music inside the `Music` folder (structure doesn't matter).
3. Run `dbbuilder` from inside the weberver directory to start scanning the music files.
4. The script creates `lmst.db` in the root of the webserver by default with the metadata of each file (it may miss some metadata).

## Server (WebUI)
### Changing the database name
1. Open `config.php`
2. Edit `$conn_dbname = "lmst.db";` to the name of your database.
### Locating the songID
1. Open the WebUI in a browser.
2. Go to the songlist page and scroll untill you find the track.
3. The song ID is the first column, which can be used to instruct the client to play a speciic song.
# Credits

Licence: GPLv3