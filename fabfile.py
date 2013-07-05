""" Deployment project.
"""

from fabric.api import *

env.hosts = ['web']
env.user = "user"


#dev

def start_local_dhcp_daemon():
    stop_local_dhcp_daemon()
    local('python /home/alateas/lmtools/src/daemons/dhcp_manager/main.py start')

def start_local_webserver():
    with lcd('/home/alateas/lmtools/src/web'):
        local('./run_web.sh', shell='/bin/bash')

def stop_local_dhcp_daemon():
    with settings(warn_only=True):
        local('python /home/alateas/lmtools/src/daemons/dhcp_manager/main.py stop')

def loc():
    start_local_dhcp_daemon()
    start_local_webserver()

#production

def update_project():
    """ Updates the remote project.
    """
    with cd('/opt/lmtools'):
        sudo('git pull')
        with prefix('source /home/user/.virtualenvs/lmtools/bin/activate'):
            run('pip install -r requirements.txt')

def restart_dhcp_daemon():
    with cd('/opt/lmtools/src/daemons/dhcp_manager'):
        with prefix('source `which virtualenvwrapper.sh`'):
            with prefix('workon lmtools'):
                with settings(warn_only=True):
                    run('python main.py stop', pty=False)
                run('python main.py start', pty=False)

def restart_webserver():
    with settings(warn_only=True):
        sudo("stop lmtools_web")
    sudo("cp /opt/lmtools/lmtools_web.conf /etc/init")
    sudo("start lmtools_web")

def restart_services():
    restart_dhcp_daemon()
    restart_webserver()

def deploy():
    """ Deploy project.
    """
    update_project()
    restart_services()
