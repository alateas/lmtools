""" Deployment project.
"""

from fabric.api import *

env.hosts = ['web']
env.user = "user"

def update_project():
    """ Updates the remote project.
    """
    with cd('/opt/lmtools'):
        sudo('git pull')
        with prefix('source /home/user/.virtualenvs/lmtools/bin/activate'):
            run('pip install -r requirements.txt')

def restart_dhcp_daemon():
    env.warn_only = True
    with cd('/opt/lmtools/src/daemons/dhcp_manager'):
        with prefix('source `which virtualenvwrapper.sh`'):
            with prefix('workon lmtools'):
                run('python main.py stop', pty=False)
                run('python main.py start', pty=False)
    env.warn_only = False

def restart_webserver():
    env.warn_only = True
    sudo("stop lmtools_web")
    sudo("cp /opt/lmtools/lmtools_web.conf /etc/init")
    sudo("start lmtools_web")
    env.warn_only = False

def restart_services():
    restart_dhcp_daemon()
    restart_webserver()

def deploy():
    """ Deploy project.
    """
    update_project()
    restart_services()
