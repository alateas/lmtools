#!/usr/bin/env bash

#getting script location
SCRIPT=`readlink -f $0`
SCRIPTPATH=`dirname $SCRIPT`

#install autoenv https://github.com/kennethreitz/autoenv
git clone git://github.com/kennethreitz/autoenv.git ~/.autoenv
echo 'source ~/.autoenv/activate.sh' >> ~/.bashrc

#install dependencies for mysql-python lib
sudo apt-get -y update
sudo apt-get -y install libmysqlclient-dev
sudo apt-get -y build-dep python-mysqldb

#install pip
sudo apt-get -y install python-pip

#install and setup virtualenvwrapper http://pypi.python.org/pypi/virtualenvwrapper
sudo pip install virtualenvwrapper
echo 'export WORKON_HOME=~/.virtualenvs' >> ~/.bashrc
echo 'export PIP_VIRTUALENV_BASE=$WORKON_HOME' >> ~/.bashrc
echo 'export PIP_RESPECT_VIRTUALENV=true' >> ~/.bashrc
echo 'source /usr/local/bin/virtualenvwrapper.sh' >> ~/.bashrc

#use virtualenvwrapper
export WORKON_HOME='~/.virtualenvs'
export PIP_VIRTUALENV_BASE=$WORKON_HOME
export PIP_RESPECT_VIRTUALENV=true
source /usr/local/bin/virtualenvwrapper.sh

#create new virtualenv
mkvirtualenv djnew
workon djnew

#install libs to new virtualenv
cd $SCRIPTPATH
pip install -r requirements.txt