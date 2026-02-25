from setuptools import setup, find_packages
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
import sys
sys.path.insert(1, os.path.join(dir_path, 'autoref'))
from __version__ import __version__

def read_requirements():
    with open("requirements.txt") as f:
        return f.read().splitlines()

setup(
    name='goopy',
    version=__version__,
    packages=['goopy'],
    install_requires=read_requirements()
)
