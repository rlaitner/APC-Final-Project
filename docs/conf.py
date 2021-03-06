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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('../docs'))

# -- Project information -----------------------------------------------------

project = 'APC 524 Final Project: Path Finding Algorithm Solver'
copyright = '2021 Princeton University'
author = 'K. Andrade, R. Laitner, L.H. Lam, S. Sarwar, M. Zhang'

# The full version, including alpha/beta/rc tags
release = '1.0'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.napoleon',
    'sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
    'sphinx.ext.imgmath',
]

# -- Intersphinx --------------------------------------------------------------

intersphinx_mapping = {
    "https://docs.python.org/3": None,
    "https://numpy.org/doc/stable/": None,
}

# -- Napoleon Settings --------------------------------------------------------
# See sphinx-doc.org/en/master/usage/extensions/napoleon.html#module-sphinx.ext.napoleon
# For settings and explanations

napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = False
napoleon_type_aliases = None
napoleon_attr_annotations = True

# -- LaTeX Customization -------------------------------------------------------

latex_engine = 'pdflatex'
latex_elements = {
	'sphinxsetup': 'hmargin={1in,1.5in}, vmargin={1.5in,1in}, marginpar=1in',	
}

# Grouping the document tree into LaTeX files 
# latex_documents = {
# 	("index", etc.),
#
# }

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Turn off prepending module names
add_module_names = False

# Sort members by time
autodoc_member_order = 'groupwise'

# Document __init__, __repr__, and __str__methods 
def skip(app, what, name, obj, would_skip, options):
	if name in ("__init__", "__repr__", "__str__"):
		return False
	return would_skip

def setup(app):
	app.connect("autodoc-skip-member", skip) 

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

html_theme = 'alabaster'

html_theme_options = {
	'description': 'Final Project for APC 524',
	'github_user': 'rlaitner',
	'github_repo': 'APC-Final-Project',
	}
	


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Extension configuration -------------------------------------------------

