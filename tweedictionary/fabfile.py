from fabric.api import local

def deploy():
    with lcd('/srv/www/tweedictionary/'):
        local('sudo git pull /home/git/tweedictionary.git/')
        local('python manage.py migrate tweedictionary')
        local('python managa.py test tweedictionary')
        local('service apache2 reload')
