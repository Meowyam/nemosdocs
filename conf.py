# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "L4"
copyright = "2023, Meng Weng Wong"
author = "Meng Weng Wong, edited and organised by Nemo"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

import os
import sys

sys.path.insert(0, os.path.abspath(".."))

extensions = ["sphinx_design", "sphinxawesome_theme"]

templates_path = ["_templates"]
exclude_patterns = ["_themes", "_build", "Thumbs.db", ".DS_Store", "pdf-version"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinxawesome_theme"
html_theme_path = ["_themes/sphinxawesome_theme/"]
html_static_path = ["_static"]
html_collapsible_definitions = True
