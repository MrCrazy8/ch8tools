#!/bin/bash
#Crazy8 ~ Ali.A
clear
echo -e "\ninstall py2 and module\n"

sleep 3
notify-send "start installation"

apt-get install python2
echo -e "\n\n\n"
clear
apt-get install python2-pip
echo -e "\n\n\n"
clear
pip install setuptools
pip2 install requests
echo -e "\n\n\n"
clear
pip2 install pyfiglet
echo -e "\n\n\n"
clear
pip2 install hashlib
clear
echo -e "\n\n\n"
pip2 install pyinstaller
clear
echo -e "\ninstall c tools\n"

apt-get install make
apt install gcc
apt install mingw-w64*
apt-get install build-essential
make
echo " "
clear
echo -e "\ninstall tools :\n"
apt-get install git
apt install unzip
apt install ruby
gem install ocra
sleep 3
notify-send "Download is over" "Code By : Mr Crazy8" -u critical
python2 ch8.py
