from os import path
import setuptools.command.build_py
from setuptools import setup, find_packages
import distutils
import versioneer
import subprocess
import os


class BuildCannonsimCommand(distutils.cmd.Command):
    description = 'build cannonsim'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        self.announce('Building cannonsim')
        subprocess.check_call(['make'], cwd=os.path.abspath('./tests/cannonsim/src'))


class BuildNotebooks(distutils.cmd.Command):
    description = 'build tutorials as Jupyter notebooks'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        self.announce('Building tutorial as Jupyter notebooks')
        tutorials = ['basic_tutorial.rst', 'cooling_coffee_cup.rst']
        for tutorial in tutorials:
            subprocess.check_call(['rst2ipynb', tutorial, '-o', os.path.splitext(tutorial)[0] + '.ipynb'], cwd=os.path.abspath('./docs'))


class BuildPyCommand(setuptools.command.build_py.build_py):
    def run(self):
        setuptools.command.build_py.build_py.run(self)

# read the contents of README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

cmdclass = versioneer.get_cmdclass()
cmdclass['build_cannonsim'] = BuildCannonsimCommand
cmdclass['build_notebooks'] = BuildNotebooks
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
