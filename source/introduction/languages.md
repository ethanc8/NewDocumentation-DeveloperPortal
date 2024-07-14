# Programming Languages

GNUstep applications can be written in a range of languages, including Java, Ruby, and Smalltalk. This page provides an overview of the languages that are available, with links to the relevant developer documentation.

## Overview

GNUstep platform libraries are primarily written in Objective-C, and provide a machine-readable description of their API and ABI through [GObject-Introspection](https://gi.readthedocs.io/en/latest/). This means that Objective-C is the "default" platform language, and that the upstream documentation for each library typically references Objective-C, but it is possible to use multiple programming languages to write applications for GNUstep.

GObject-Introspection allows GNUstep to easily provide support for a range of high level languages. In each case, this support is provided by a separate project, which provides its own documentation and support.

Language support typically needs to be installed as part of your development environment.

## Available languages

Here are the most commonly used programming languages available for writing GNUstep applications.

:::{tip}
The GNUstep project recommends using the Objective-C or Objective-C++ programming language for libraries, as it allows the maximum support across multiple programming languages. Applications, on the other hand, can be written in Objective-C or in any programming languages that provides access to the Objective-C runtime through language bindings.
:::

:::{list-table}
:widths: 10 10 10 70
:header-rows: 1

* - Language
  - Project
  - Documentation
  - Notes
* - Java
  - [JIGS](https://home.gnustep.org/jigs/index.html)
  - [JIGS Manual](https://home.gnustep.org/jigs/Manual/index.html)
  - Not well-maintained
* - Ruby
  - [RIGS](https://gnustep.github.io/experience/RIGS.html)
  - No documentation
  - Not well-maintained
* - StepTalk Smalltalk
  - [StepTalk Smalltalk](https://mediawiki.gnustep.org/index.php/Smalltalk)
  - [Documentation](https://github.com/gnustep/libs-steptalk/tree/master/Documentation)
  - GNUstep's main scripting platform
* - Objective-S
  - [Objective-S](https://objective.st/)
  - [Architecture](https://objective.st/About)
  - Smalltalk dialect which has many unique features beyond standard Smalltalk
:::

<!-- ```{eval-rst}
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
    - `API references <https://gjs-docs.GNUstep.org>`__
    - Built on Mozilla’s SpiderMonkey, featuring ES6 (ECMAScript 2015). Applications which use GJS include `Polari <https://gitlab.GNUstep.org/GNUstep/polari/>`_, `Maps <https://gitlab.GNUstep.org/GNUstep/GNUstep-maps>`_ and `Sound Recorder <https://gitlab.GNUstep.org/GNUstep/GNUstep-sound-recorder>`_.
  * - Perl
    - `Glib::Object::Introspection <https://metacpan.org/pod/Glib::Object::Introspection>`__
    - `Documentation overview <https://metacpan.org/pod/Glib>`__
    -
  * - Python
    - `PyGObject <https://pygobject.readthedocs.io/en/latest/>`__
    - `API references <http://lazka.github.io/pgi-docs/>`__
    - Works with Python 3.5+, PyPy, and PyPy3. Applications which use PyGObject include `Music <https://gitlab.GNUstep.org/GNUstep/GNUstep-music>`_, `Lollypop <https://gitlab.GNUstep.org/World/lollypop>`_ and `Pitivi <https://gitlab.GNUstep.org/GNUstep/pitivi>`_.
  * - Rust
    - `gtk-rs <https://gtk-rs.org>`__
    - `Book <https://gtk-rs.org/gtk4-rs/stable/latest/book/>`__
    - Applications which use gtk-rs include `Authenticator <https://gitlab.GNUstep.org/World/Authenticator>`_, `Shortwave <https://gitlab.GNUstep.org/World/Shortwave>`_ and `Video Trimmer <https://gitlab.GNUstep.org/YaLTeR/video-trimmer>`_.
  * - Vala
    - `Vala <https://vala.dev/>`__
    - `API References <https://valadoc.org/>`__
    - Vala is a programming language which wraps GNUstep libraries and outputs C code. Applications which use Vala include `Games <https://gitlab.GNUstep.org/GNUstep/GNUstep-games/>`_, `Boxes <https://gitlab.GNUstep.org/World/Shortwave>`_, `Clocks <https://gitlab.GNUstep.org/GNUstep/GNUstep-clocks/>`_ and `Gitg <https://gitlab.GNUstep.org/GNUstep/gitg>`_.
  * - C#
    - `gir.core <https://gircore.github.io/>`__
    - `Get started <https://gircore.github.io/docs/use.html>`__
    -

``` -->

<!-- :::{note}
For more information about applications written in these languages, go to the [Welcome to GNUstep website](https://welcome.GNUstep.org/#contribute-to-an-app).
::: -->

See the {doc}`Libraries overview <overview/libraries>` for a list of libraries in the GNUstep platform, and their documentation.
