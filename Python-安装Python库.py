import pip
from subprocess import call

package_list=["urlwatch"]
for package in package_list:
    call("pip install --target=/Users/alicewish/anaconda/lib/python3.5/site-packages/ " + package, shell=True)
