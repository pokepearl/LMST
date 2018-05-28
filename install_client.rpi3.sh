echo "[LMST-Client] Installing Essential Packages"
sudo apt update
sudo apt -y upgrade
sudo apt -y install git python3 python3-pip
echo "[LMST-Client] Downloading code"
cd /tmp
git clone INSERT_GIT_HERE
cd LMST/client
echo "[LMST-Client] Installing Python Packages"
pip3 install -r requirements.txt
pip3 install cx_Freeze
echo "[LMST-Client] Compiling LMST Client"
python3 setup.py install
cd /tmp
rm -rf LMST
echo ""
echo "[LMST-Client] Installation Complete"
echo "[LMST-Client] The client can be run with 'lmst'"