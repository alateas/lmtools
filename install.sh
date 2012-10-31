git clone git://github.com/kennethreitz/autoenv.git ~/.autoenv
echo 'source ~/.autoenv/activate.sh' >> ~/.bashrc

sudo apt-get install python-pip
sudo pip install virtualenvwrapper
echo 'export WORKON_HOME=~/.virtualenvs' >> ~/.bashrc
echo 'source /usr/local/bin/virtualenvwrapper.sh' >> ~/.bashrc
echo 'export PIP_VIRTUALENV_BASE=$WORKON_HOME' >> ~/.bashrc
echo 'export PIP_RESPECT_VIRTUALENV=true' >> ~/.bashrc

export DATABASE_URL="mysql://outlets_dev:outlets_dev@192.168.106.10/outlets_dev"
