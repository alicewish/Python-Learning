import pip
from subprocess import call

for dist in pip.get_installed_distributions():
    #call("pip install --upgrade " + dist.project_name, shell=True)
    call("pip install --upgrade --target=/Users/alicewish/anaconda/ " + dist.project_name, shell=True)
