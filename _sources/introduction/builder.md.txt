# GNOME Builder

[Builder](https://wiki.gnome.org/Apps/Builder) is GNOME's integrated development environment. This tool is designed and optimized for creating applications with the GNOME platform. It combines integrated support for GNOME technologies (such as GTK and GLib), with features that any developer will appreciate, like syntax highlighting and snippets.

## Features

Builder has an impressive feature set, which makes it a highly effective development tool. This includes:

- **Syntax highlighting, auto-completion and diagnostics**. These features are available for many of the most popular programming languages and speed up code reading, writing and error detection. Auto-indentation is also available for C, Python, Vala, and XML.
- **Effective working environment**. Builder is a great place to code, with a host of features like side-by-side editors, multi-monitor support, and fast fuzzy text search for both files and symbols. Builder also allows browsing TODOs, and has optional Vim, Emacs, and SublimeText style editing.
- **Tooling integration**. This includes Git integration, as well as integration with a wide range of build systems and tools. Builder is also able to show live previews for HTML, Markdown, reStructuredText, and Sphinx.
- **Profiling and debugging**. This uses an integrated profiler and debugger which can be used for native applications.
- **Build and run projects with Flatpak**. Builder makes it possible to build and run your development project with just the press of button.

## Installation

Builder can be easily installed [from Flathub](https://flathub.org/apps/details/org.gnome.Builder). It is also available from the repos of popular Linux distributions.

## Hello world

To show how easy it is to create, build and run an app using GNOME Builder, let's start a new app using its templating feature.

First, launch Builder. At the first screen, select {guilabel}`Start New Project...`.

At the next screen, we define some properties for the new app. To keep things simple, we'll keep most of these as the defaults.

- For the {guilabel}`Project Name`, enter `hello`
- For the {guilabel}`Application ID`, enter `org.gnome.Hello`
- That's it! Now just press {guilabel}`Create Project`

Builder has now created a new GNOME application for you. The new project is complete with an initialized Git repository and an open source license. In the sidebar, you can see the app's file structure that has been created.

Now all we need to do is build and run the app! To do this, just click the play button in the header bar. If all goes well, you should be greeted with the window of your new app.

```{image} ../img/hello-world.png
```

To see more complex examples in action, try cloning any of the projects listed in the [GNOME newcomers guide](https://wiki.gnome.org/Newcomers).

## Learn more

To learn more about Builder, including how to get the most out of its feature set, see the [Builder documentation](https://builder.readthedocs.io/).
