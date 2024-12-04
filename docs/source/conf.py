# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

from sphinx.ext.apidoc import main as apidoc_main
apidoc_main(["--force", "-o", "./_autodoc", "../../easyvvuq"])

autodoc_mock_imports = ['dill', 'SALib', 'cerberus', 'chaospy', 'scipy', 'qcg', 'kubernetes', 'dask', 'sqlalchemy', 'numpoly', 'sklearn']

# -- Project information -----------------------------------------------------

project = 'EasyVVUQ'
copyright = '2020, David W. Wright, Robin A. Richardson, Vytautas Jancauskas, Jalal Lakhlili'
author = 'David W. Wright, Robin A. Richardson, Vytautas Jancauskas, Jalal Lakhlili'

# The full version, including alpha/beta/rc tags
release = '0.8'


# -- General configuration ---------------------------------------------------

master_doc = 'index'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon', 'sphinx.ext.autosectionlabel', 'sphinx.ext.viewcode']

autosectionlabel_prefix_document = True

napoleon_google_docstring = False
napoleon_use_param = False
napoleon_use_ivar = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_favicon = '../images/favicon.ico'

html_theme = 'alabaster'   

html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',
        'searchbox.html',
    ]
}

html_theme_options = {
    "github_user": "UCL-CCS",
    "github_repo": "EasyVVUQ",
    "github_banner": True,
    "description": "Verification, validation and uncertainty quantification for HPC simulations"
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_logo = "../images/circle-logo.png"
