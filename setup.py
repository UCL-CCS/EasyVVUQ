from setuptools import setup, find_packages

setup(
    name='easyvvuq',

    version='0.0.1.dev1',

    description=('Library to facilitate simple Verification, Validation and '
                 'Uncertainty Quantification of simulation codes'),

    long_description='Copy from README file',

    url='http://ccs.chem.ucl.ac.uk',

    author='CCS',

    install_requires=['numpy', 'pandas', 'pytest', 'SQLAlchemy', 'chaospy',
                      'sqlalchemy-utils', 'matplotlib'],

    packages=find_packages(),

    include_package_data=True,
)
