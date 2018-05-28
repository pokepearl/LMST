echo "[LMST-Server] Installing Essential Packages"
sudo apt update
sudo apt -y upgrade
sudo apt -y install apache2 php7.0 php7.0-sqlite3 git python3 python3-pip python3-dev build-essential libssl-dev libffi-dev libxml2-dev libxslt1-dev zlib1g-dev
echo "[LMST-Server] Downloading code"
cd /tmp
git clone INSERT_GIT_HERE
cd LMST/server
# Configuring Apache
echo "[LMST-Server] Copying Webserver files"
sudo mkdir -p /opt/LMST/web
sudo mv *.php /opt/LMST/web
echo "[LMST-Server] Configuring Apache server"
sudo rm /etc/apache2/sites-enabled/lmstweb.conf
sudo cp /etc/apache2/sites-enabled/000-default.conf /etc/apache2/sites-enabled/lmstweb.conf
sudo sed -i 's/Listen 80/Listen 80\nListen 9381/' /etc/apache2/sites-enabled/lmstweb.conf
sudo sed -i 's/:80/:9381/' /etc/apache2/sites-enabled/lmstweb.conf
sudo sed -i 's:/var/www/html:/opt/LMST/web:' /etc/apache2/sites-enabled/lmstweb.conf
sudo sed -i 's:/#ServerName www.example.com:ServerName localhost:' /etc/apache2/sites-enabled/000-default.conf
sudo sed -i 's:#Include conf-available/serve-cgi-bin.conf:#Include conf-available/serve-cgi-bin.conf\n\t<Directory "/opt/LMST/web">\n\t\tRequire all granted\n\t</Directory>:' /etc/apache2/sites-enabled/lmstweb.conf
sudo systemctl restart apache2
echo "[LMST-Server] Compiling Database Builder"
cd /tmp/LMST/server/db_builder/
sudo pip3 install -r requirements.txt
pip3 install cx_Freeze
sudo sudo python3 setup.py install
cd /tmp
sudo rm -rf LMST
echo ""
echo "[LMST-Server] Installation Complete"
echo "[LMST-Server] Webserver accessible at *:9381"
echo "[LMST-Server] Music is to be placed in /opt/LMST/web/Music"
echo "[LMST-Server] Database manager can be run with dbbuilder (FROM THE WEBROOT)"
