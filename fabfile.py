from fabric.api import local, lcd
def hello(name,value):
    print '%s = %s' %(name,value)

def lsfab():
    with lcd('.'):
        local('dir')