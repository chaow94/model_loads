#!/usr/bin/env python
import os
import sys
from distutils.core import setup

from setuptools import find_packages


def setup_package():
    src_path = os.path.dirname(os.path.abspath(__file__))
    os.chdir(src_path)
    sys.path.insert(0, src_path)

    # The f2py scripts that will be installed
    if sys.platform == 'win32':
        raise Exception("Not support windows pytorch yet!")

    else:
        setup(name='model_loads',
              version='0.1',
              description='Loads GPU or CPU pytorch models',
              author='wangchao',
              author_email='chaowanghs@gmail.com',
              url='http://towardsdeeplearning.com/blog/',
              packages=find_packages(),
              )



if __name__ == "__main__":
    setup_package()
