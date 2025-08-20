#!/bin/bash

if [ $(id -u) -ne 0 ]; then
	printf "Script must be run as root. Try 'sudo ./install.sh'\n"
	exit 1
fi


WORKING_DIR=`pwd`

apt update
apt install -y python-pip
pip install pypng pyserial

cd $WORKING_DIR/library
sudo python setup.py install
cd $WORKING_DIR

cd $WORKING_DIR/daemon
./install.sh
cd $WORKING_DIR
