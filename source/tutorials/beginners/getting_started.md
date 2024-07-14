# Getting Started

In order to start writing an application for the GNOME desktop environment, you
should follow these steps:

```{image} images/getting-started-new-project.png
:align: center
:alt: New project creation dialog in GNOME Builder
:class: only-light
```

```{image} images/getting-started-new-project-dark.png
:align: center
:alt: New project creation dialog in GNOME Builder
:class: only-dark
```

1. download and install the latest version of [GNOME Builder](https://wiki.gnome.org/Apps/Builder)

2. in the *Welcome* screen, select *Create new project…*

3. configure the project options

   - write "text-viewer" as the project's name
   - write "com.example.TextViewer" as the project's {doc}`application id </tutorials/application-id>`.
   - select GPL-3.0-or-later as the licensing terms for your project

4. select the *GNOME Application* template

```{image} images/getting-started-project-files.png
:align: center
:alt: Initial project contents in GNOME Builder
:class: only-light
```

```{image} images/getting-started-project-files-dark.png
:align: center
:alt: Initial project contents in GNOME Builder
:class: only-dark
```

Once Builder finishes creating your application's project, you will find the
following files:

`com.example.TextViewer.json`

: This is the [Flatpak](https://flatpak.org) manifest for your application.
  You can use the manifest to define your project's dependencies. The default
  manifest depends on the lastest stable of the GNOME platform. You can also
  include additional dependencies not provided by the GNOME run time.

`meson.build`

: This is the main [Meson](https://mesonbuild.com) build file, which
  defines how and what to build in your application.

`src`

: This is the directory with the sources of your application, as well as
  the UI definition files for its widgets.

`src/text-viewer.gresource.xml`

: The [GResource](https://docs.gtk.org/gio/struct.Resource.html#description)
  manifest for assets that will be built into the project using
  `glib-compile-resources`.

`po/POTFILES`

: The list of files containing {doc}`translatable </guidelines/localization>`,
  user-visible strings.

`data/com.example.TextViewer.gschema.xml`

: The schema file for the [settings](https://docs.gtk.org/gio/class.Settings.html)
  of the application.

`data/com.example.TextViewer.desktop.in`

: The {doc}`desktop entry file </guidelines/maintainer/integrating>` for the
  application.

`data/com.example.TextViewer.appdata.xml.in`

: The [application metadata](https://www.freedesktop.org/software/appstream/docs/chap-Quickstart.html)
  used by app stores and application distributors.

If you want to, you can now build and run the application by pressing the
*Run Project* button, or {kbd}`Shift` + {kbd}`Ctrl` + {kbd}`Space`.

:::{note}
The code in this tutorial is available on [GitLab](https://gitlab.gnome.org/Teams/documentation/getting-started-tutorial).
:::

```{toctree}
:hidden: true
:maxdepth: 1

getting_started/content_view.rst
getting_started/opening_files.rst
getting_started/cursor_position.rst
getting_started/saving_files.rst
getting_started/saving_state.rst
getting_started/adding_toasts.rst
getting_started/dark_mode.rst
```
