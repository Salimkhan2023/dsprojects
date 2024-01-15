from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    """
    this function will return list of requirements
    """
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',"") for req in requirements]
    return requirements

setup(
name='dsprojects',
version='0.0.1',
author='salim',
author_email='salim.khan81@yahoo.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)