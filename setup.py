from os import path
from setuptools import setup, find_packages
import versioneer



# read the contents of README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='easyvvuq',

    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),

    description=('Library to facilitate simple Verification, Validation and '
                 'Uncertainty Quantification of simulation codes'),

    long_description=long_description,
    long_description_content_type='text/markdown',

    url='http://ccs.chem.ucl.ac.uk',

    author='CCS',

    install_requires=['numpy', 'pandas>=0.24', 'scipy==1.2.1', 
                      'pytest', 'SQLAlchemy', 'chaospy',
                      'sqlalchemy-utils', 'matplotlib', 'jsonpickle'],

    packages=find_packages(),

    include_package_data=True,
)
