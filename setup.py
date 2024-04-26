from setuptools import find_packages, setup
from typing import List
d_dot = '-e .'
def get_requirements(file_path:str)->List[str]:
    #this function will return the list of requirements
    requirements = []
    with open(file_path,'r') as f:
        for line in f.readlines():
            requirements.append(line.strip())
            if d_dot in requirements:
                requirements.remove(d_dot)
    return requirements   
         
setup(
name = 'ML_project',
version = '0.0.1',
author = 'Brindha',
author_email = 'mailtobrindhaganesh@gmail.com',
packages = find_packages(),
#install_requires = ['numpy','pandas','matplotlib','seaborn','sklearn','tensorflow','keras'],
install_requires = get_requirements('requirements.txt'),
)