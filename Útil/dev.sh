#!/bin/bash
# -*- ENCODING: UTF-8 -*-

# Script para instalar herramientas y ser feliz, muy feliz .
# versión 0.1
# Lista de paquetes a descargar

# Git
# MC
# Curl
# KDevelop
# KDevelop Python
# SyncThing

# Qt Creator
# Qt Designer

# Django



# Limpio pantalla

	clear

# Git

if ! command -v git &> /dev/null
then
	echo " Git no està instalado, procedo a instalarlo "
	sudo apt -y install git
else
	echo " Git està instalado "

fi

# MC

if ! command -v mc &> /dev/null
then
	echo " MC no està instalado, procedo a instalarlo "
	sudo apt -y install mc
else
	echo " MC està instalado "

fi

# Curl

if ! command -v curl &> /dev/null
then
	echo " Curl no està instalado, procedo a instalarlo "
	sudo apt -y install curl
else
	echo " Curl està instalado "

fi

# KDevelop y KDevelop Python

if ! command -v kdevelop &> /dev/null
then
	echo " KDevelop no està instalado, procedo a instalarlo "
	sudo apt -y install kdevelop
	sudo apt -y install kdevelop-python
else
	echo " KDevelop està instalado "

fi

# SyncThing

if ! command -v syncthing &> /dev/null
	then
	echo  " Syncthing no està instalado, procedo a instalarlo "
	
	sudo echo "deb https://apt.syncthing.net/ syncthing stable" | sudo tee /etc/apt/sources.list.d/syncthing.list
	
	curl -s https://syncthing.net/release-key.txt | sudo apt-key add -
	
	sudo apt -y update
	
	sudo apt -y install syncthing
	
else
	echo " Syncthing està instalado "
	echo ""

fi

# Qt Creator

if ! command -v qt-creator &> /dev/null
then
	echo " Qt Creator no està instalado, procedo a instalarlo "
	sudo apt -y install qtcreator
else
	echo " Qt Creator està instalado "
	
fi

# Qt Designer

if ! command -v qttools5-dev-tools &> /dev/null
then
	echo " Qt Designer no està instalado, procedo a instalarlo "
	sudo apt -y install qttools5-dev-tools
else
	echo " Qt Designer està instalado "

fi

# PyQt5

if ! command -v python3-pyqt5 &> /dev/null
then
	echo " PyQt5 no està instalado, procedo a instalarlo "
	sudo apt -y install python3-pyqt5
else
	echo " PyQt5 està instalado "

fi

# Pyuic5

if ! command -v pyqt5-dev-tools &> /dev/null
then
	echo " Pyuic5 no està instalado, procedo a instalarlo "
	sudo apt -y install pyqt5-dev-tools
else
	echo " Pyuic5 està instalado "
		
fi

# Django

if ! command -v python3-django &> /dev/null
then
	echo " Django no està instalado, procedo a instalarlo "
	sudo apt -y install python3-django
else
	echo " Django està instalado "

	exit
fi
