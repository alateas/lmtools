""" Deployment of your django project.
"""

from fabric.api import *

env.hosts = ['web']
env.user = "user"

def update_django_project():
    """ Updates the remote django project.
    """
    with cd('/home/djangoprojects/lmtools'):
        run('git pull')
        with prefix('source /home/user/.virtualenvs/lmtools/bin/activate'):
            run('pip install -r requirements.txt')
            #run('python src/manage.py syncdb')
            #run('python src/manage.py migrate') # if you use south
            #run('python src/manage.py collectstatic --noinput')

def restart_webserver():
    """ Restarts remote nginx and uwsgi.
    """
    sudo("service uwsgi_lmtools restart")
    sudo("/etc/init.d/nginx restart")

def deploy():
    """ Deploy Django Project.
    """
    update_django_project()
    restart_webserver()
