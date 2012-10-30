git clone git://github.com/kennethreitz/autoenv.git ~/.autoenv
echo 'source ~/.autoenv/activate.sh' >> ~/.bashrc

sudo apt-get install python-pip
sudo pip install virtualenvwrapper
sudo mkdir /home/djangoprojects
echo 'export WORKON_HOME=~/.virtualenvs' >> ~/.bashrc
echo 'export PROJECT_HOME=/home/djangoprojects' >> ~/.bashrc
echo 'source /usr/local/bin/virtualenvwrapper.sh' >> ~/.bashrc


export DATABASE_URL="mysql://outlets_dev:outlets_dev@192.168.106.10/outlets_dev"
