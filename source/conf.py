# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
from os.path import join, realpath, dirname
sys.path.insert(0, os.path.abspath('/network/rit/lab/ChenRNALab/awesomeSauce/code/fluctuating_density/'))

USE_CXX_LIB = True

# -- Project information -----------------------------------------------------

project = 'AmberFD'
copyright = '2022, Christopher A. Myers'
author = 'Christopher A. Myers'

# The full version, including alpha/beta/rc tags
release = '0.0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
# extensions = [
#     'sphinx.ext.autodoc', 
#     'sphinx.ext.coverage', 
#     'sphinx.ext.napoleon', 
#     'sphinx.ext.autosummary',
#     'autodocsumm',
#     'sphinx_automodapi.automodapi',
#     ]

extensions = [
    'sphinx.ext.autodoc', 
    'sphinx.ext.coverage', 
    'sphinx.ext.napoleon', 
    'sphinx.ext.autosummary',
    'autodocsumm'
    ]

autosummary_generate = True
autodoc_default_options = {
    "members": True,
    "inherited-members": True,
    "member-order": "bysource",
}

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

if USE_CXX_LIB:
    tags.add('use_cpp')
    extensions += ['breathe', 'exhale']
    breathe_projects = {"AmberFD": "doxygen/gen_docs/xml/"}
    breathe_default_project = "AmberFD"
    exhale_args = {
        # These arguments are required
        "containmentFolder":     "./cpp",
        "rootFileName":          "library_root.rst",
        "rootFileTitle":         "Library API",
        "doxygenStripFromPath":  "..",
        # Suggested optional arguments
        "createTreeView":        True,
        # TIP: if using the sphinx-bootstrap-theme, you need
        # "treeViewIsBootstrap": True,
    }
else:
    exclude_patterns += ['cpp/*']

print("TAGS: ", tags.has('use_cpp'))


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_sidebars = {
    "**": [
        "navigation.html",
    ]
}
