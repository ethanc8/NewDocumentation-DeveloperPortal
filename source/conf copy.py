# SPDX-FileCopyrightText: 2021 GNOME Foundation
#
# SPDX-License-Identifier: CC0-1.0

# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Project information -----------------------------------------------------
project = 'GNOME Developer Documentation'
copyright = '2021, Emmanuele Bassi'
author = 'Emmanuele Bassi'

# -- General configuration ---------------------------------------------------
sys.path.append(os.path.abspath("./_ext"))
extensions = [
    "fix-secnum",
    "gobject_docs",
    "sphinx_tabs.tabs",
    "sphinxext.opengraph",
]
source_suffix = {
    '.rst': 'restructuredtext'
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']
exclude_patterns = []

# Set the explicit title of the HTML output
html_title = 'GNOME Developer Documentation'

# -- Options for gi-docgen roles extension -----------------------------------
gobject_docs_base_url = {
    "glib": "https://docs.gtk.org/glib/",
    "gobject": "https://docs.gtk.org/gobject/",
    "gio": "https://docs.gtk.org/gio/",
    "pango": "https://docs.gtk.org/Pango/",
    "pixbuff": "https://docs.gtk.org/gdk-pixbuf/",
    # GTK
    "gtk3": "https://docs.gtk.org/gtk3/",
    "gtk4": "https://docs.gtk.org/gtk4/",
    # GSK
    "gsk4": "https://docs.gtk.org/gsk4/",
    # GDK
    "gdk3": "https://docs.gtk.org/gdk3/",
    "gdk3-x11": "https://docs.gtk.org/gdk3-x11/",
    "gdk4": "https://docs.gtk.org/gdk4/",
    "gdk4-wayland": "https://docs.gtk.org/gdk4-wayland/",
    "gdk4-x11": "https://docs.gtk.org/gdk4-x11/",
    # libadwaita
    "adw": "https://gnome.pages.gitlab.gnome.org/libadwaita/doc/main/"
}

# -- Options for HTML output -------------------------------------------------
html_theme = 'furo'
html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#4a86cf",
        "color-brand-content": "#4a86cf",
    },
    "source_edit_link": "https://gitlab.gnome.org/Teams/Websites/developer.gnome.org/-/edit/main/source/{filename}",
}

html_static_path = ['_static']
html_css_files = ['gnome.css']
html_show_copyright = 0
html_show_sphinx = 0
show_source = 0

# -- Options for opengraph ---------------------------------------------------
ogp_site_url = "https://developer.gnome.org/documentation/"
ogp_image = "_static/card.png"
