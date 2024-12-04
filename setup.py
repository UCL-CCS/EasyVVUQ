from os import path
import setuptools.command.build_py
from setuptools import setup, find_packages
import distutils
import versioneer
import subprocess

class BuildPyCommand(setuptools.command.build_py.build_py):
    def run(self):
        setuptools.command.build_py.build_py.run(self)

# read the contents of README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

cmdclass = versioneer.get_cmdclass()
cmdclass['build_py'] = BuildPyCommand

setup(
    name='easyvvuq',

    version=versioneer.get_version(),
    cmdclass=cmdclass,

    description=('Library to facilitate simple Verification, Validation and '
                 'Uncertainty Quantification of simulation codes'),

    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://readthedocs.org/projects/easyvvuq/',

    author='CCS',

    install_requires=open("requirements.txt", "r").readlines(),

    packages=find_packages(),

    include_package_data=True,
)
