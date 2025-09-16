# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
import django
sys.path.insert(0, os.path.abspath('../..'))  # pour trouver le code python

# Indiquer à Django où trouver les settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oc_lettings_site.settings")

# Initialiser Django
django.setup()

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'oclettings'
copyright = '2025, Nicolas F.'
author = 'Nicolas F.'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",      # génère la doc depuis les docstrings
    "sphinx.ext.napoleon",     # support Google/NumPy style docstrings
    "sphinx.ext.viewcode",     # ajoute liens vers le code source
]

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
