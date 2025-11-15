# we do this setup so that our ML Project can be easily installed and managed as a package.
# my entire project development will be in the 'src' folder, also when we create any new folders, there also we will be using this file 
# so that internal folders can also be treated as packages.
from setuptools import find_packages, setup 
from typing import List


variable='-e .'
def get_requirements(file_path: str) -> List[str]:      # this fn will return a list of requirements from the requirements.txt file
    
    requirements=[]
    with open (file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]   # to remove the new line character from each requirement
        
        if variable in requirements:
            requirements.remove(variable)   # we do this to remove the '-e .' from the requirements list
    
    return requirements 

setup(
    name= 'MLProject',
    version='0.1.0',
    author='Pratham ',
    author_email= 'prathammittal2014@gmail.com',
    packages=find_packages(),                                 # we do this to automatically find all packages and sub-packages
    install_requires=get_requirements('requirements.txt') ,  # we do this to install all the dependencies listed in requirements.txt
    
     )