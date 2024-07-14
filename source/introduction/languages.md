# Programming Languages

GNOME applications can be written in a range of languages, including C++, Javascript, Python, Rust and Vala. This page provides an overview of the languages that are available, with links to the relevant developer documentation.

## Overview

GNOME platform libraries are primarily written in C, and provide a machine-readable description of their API and ABI through [GObject-Introspection](https://gi.readthedocs.io/en/latest/). This means that C is the "default" platform language, and that the upstream documentation for each library typically references C, but it is possible to use multiple programming languages to write applications for GNOME.

GObject-Introspection allows GNOME to easily provide support for a range of high level languages. In each case, this support is provided by a separate project, which provides its own documentation and support.

Language support typically needs to be installed as part of your development environment. Packages are available for most Linux distributions. In some cases, Flatpak runtime extensions are also available.

## Available languages

Here are the most commonly used programming languages available for writing GNOME applications.

:::{tip}
The GNOME project recommends using the C programming language for libraries, as it allows the maximum support across multiple programming languages. Applications, on the other hand, can be written in C or in any programming languages that provides access to the GNOME platform libraries through language bindings.
:::

```{eval-rst}
.. list-table::
  :widths: 10 10 10 70
  :header-rows: 1

  * - Language
    - Project
    - Documentation
    - Notes
  * - C++
    - `gtkmm <https://gtkmm.org/>`__
    - `Documentation overview <https://gtkmm.org/en/documentation.html>`__
    -
  * - JavaScript
    - `GJS <https://gjs.guide/>`__
    - `API references <https://gjs-docs.gnome.org>`__
    - Built on Mozilla’s SpiderMonkey, featuring ES6 (ECMAScript 2015). Applications which use GJS include `Polari <https://gitlab.gnome.org/GNOME/polari/>`_, `Maps <https://gitlab.gnome.org/GNOME/gnome-maps>`_ and `Sound Recorder <https://gitlab.gnome.org/GNOME/gnome-sound-recorder>`_.
  * - Perl
    - `Glib::Object::Introspection <https://metacpan.org/pod/Glib::Object::Introspection>`__
    - `Documentation overview <https://metacpan.org/pod/Glib>`__
    -
  * - Python
    - `PyGObject <https://pygobject.readthedocs.io/en/latest/>`__
    - `API references <http://lazka.github.io/pgi-docs/>`__
    - Works with Python 3.5+, PyPy, and PyPy3. Applications which use PyGObject include `Music <https://gitlab.gnome.org/GNOME/gnome-music>`_, `Lollypop <https://gitlab.gnome.org/World/lollypop>`_ and `Pitivi <https://gitlab.gnome.org/GNOME/pitivi>`_.
  * - Rust
    - `gtk-rs <https://gtk-rs.org>`__
    - `Book <https://gtk-rs.org/gtk4-rs/stable/latest/book/>`__
    - Applications which use gtk-rs include `Authenticator <https://gitlab.gnome.org/World/Authenticator>`_, `Shortwave <https://gitlab.gnome.org/World/Shortwave>`_ and `Video Trimmer <https://gitlab.gnome.org/YaLTeR/video-trimmer>`_.
  * - Vala
    - `Vala <https://vala.dev/>`__
    - `API References <https://valadoc.org/>`__
    - Vala is a programming language which wraps GNOME libraries and outputs C code. Applications which use Vala include `Games <https://gitlab.gnome.org/GNOME/gnome-games/>`_, `Boxes <https://gitlab.gnome.org/World/Shortwave>`_, `Clocks <https://gitlab.gnome.org/GNOME/gnome-clocks/>`_ and `Gitg <https://gitlab.gnome.org/GNOME/gitg>`_.
  * - C#
    - `gir.core <https://gircore.github.io/>`__
    - `Get started <https://gircore.github.io/docs/use.html>`__
    -

```

:::{note}
For more information about applications written in these languages, go to the [Welcome to GNOME website](https://welcome.gnome.org/#contribute-to-an-app).
:::

See the {doc}`Libraries overview <overview/libraries>` for a list of libraries in the GNOME platform, and their documentation.
