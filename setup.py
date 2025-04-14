"""
THIS SETUP.py file is an essential part of the packaging and distributing 
python projects. It is used by  setuptools fo your projects, such as its metadata,dependencies,and more

"""
from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    this fucntion will return list of requiremtns
    """
    requirements_list:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            lines=file.readlines()
            for line in lines:
                requirements=line.strip()
                if requirements and requirements!='-e .':
                    requirements_list.append(requirements)
    except FileNotFoundError:
        print('requirements.txt file not found')
    
    return requirements_list

setup(
    name='Networksecutiry',
    version='0.0.1',
    author='himesh',
    author_email='himeshkumar@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)