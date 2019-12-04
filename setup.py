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


class BuildPyCommand(setuptools.command.build_py.build_py):
    def run(self):
        self.run_command('build_cannonsim')
        setuptools.command.build_py.build_py.run(self)

# read the contents of README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

cmdclass = versioneer.get_cmdclass()
cmdclass['build_cannonsim'] = BuildCannonsimCommand
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

    install_requires=['numpy', 'pandas>=0.24', 'scipy',
                      'pytest', 'SQLAlchemy', 'chaospy',
                      'sqlalchemy-utils', 'jsonpickle',
                      'cerberus', 'SALib'],

    packages=find_packages(),

    include_package_data=True,
)
