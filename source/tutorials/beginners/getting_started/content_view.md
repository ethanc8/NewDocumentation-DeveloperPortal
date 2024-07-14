# Adding A Content View

In this lesson, you will learn how to modify the UI definition file of the
application's window to add a text area UI element. The text area will be
used to display the contents of a text file that we are going to load in the
next lesson.

```{image} images/content_view.png
```

Any GNOME application is composed of a hierarchy of UI elements, called
*widgets*; GTK allows defining UI using XML instead of writing them in
code. The default template for GNOME applications provided by Builder uses
a UI definition file for the main application window, and we are going to
edit it like any other file.

1. Open the `text_viewer-window.ui` file under the `src` directory

2. The window is defined as a **template** element for the **TextViewerWindow**
   class

3. The window has **property** elements, which describe the value for the
   various properties; for instance, setting the default title of the window
   will be set using the **title** property

4. The window also has two **child** elements

   - the first **child** element is a **AdwHeaderBar**, and it is used to
     describe the contents of the header bar; in this case, a **GtkMenuButton**
     with the primary menu of the application
   - the second **child** element is the main content area of the window

5. Currently, the main content is provided by a **GtkLabel** widget, with
   a "Hello, World!" label

6. Outside the **template** block, you can find the definition of the menu
   using the **menu** element

## Set the title of the main window

1. Find the **TextViewerWindow** definition
2. Find the **property** elements that define the default width and height
   of the window
3. Add the following property:

```{code-block} xml
:emphasize-lines: 4

<template class="TextViewerWindow" parent="AdwApplicationWindow">
  <property name="default-width">600</property>
  <property name="default-height">300</property>
  <property name="title">Text Viewer</property>
  <property name="content">
    <object class="AdwToolbarView">
```

## Set the development style for the main window

The **devel** style communicate to the user that the application is a
development snapshot.

1. Find the **TextViewerWindow** definition
2. Add the following style:

```{code-block} xml
:emphasize-lines: 5-7

<template class="TextViewerWindow" parent="AdwApplicationWindow">
  <property name="default-width">600</property>
  <property name="default-height">300</property>
  <property name="title">Text Viewer</property>
  <style>
    <class name="devel"/>
  </style>
  <property name="content">
    <object class="AdwToolbarView">
```

## Add a scrollable container

Follow these steps to add a [scrollable container](https://docs.gtk.org/gtk4/class.ScrolledWindow.html)
to the window:

1. First, you need to remove the the UI element that is already in the
   window. Find the **object** element that defines the **GtkLabel**, and
   remove the whole block
2. Add the following UI definition for a scrollable container inside the
   **property** element for the **content** property:

```{code-block} xml
:emphasize-lines: 2-9

<property name="content">
  <object class="GtkScrolledWindow">
    <property name="hexpand">true</property>
    <property name="vexpand">true</property>
    <property name="margin-top">6</property>
    <property name="margin-bottom">6</property>
    <property name="margin-start">6</property>
    <property name="margin-end">6</property>
  </object>
</property>
```

The definition of the scrollable container has the following properties:

- **hexpand** and **vexpand** tell the container to expand to fit the whole
  area of the parent window
- **margin-top**, **margin-bottom** tell the container to add a margin of
  six pixels at the top and bottom edges, respectively
- **margin-start** and **margin-end** tell the container to add a margin of
  six pixels at the leading and trailing edges, respectively; the leading and
  trailing edges are determined by the text direction

## Add a text view

Follow these steps to add a [text view widget](https://docs.gtk.org/gtk4/class.TextView.html)
to the scrollable container:

1. Add a new **property** element for the **child** property:

```{code-block} xml
:emphasize-lines: 9-10

<property name="content">
  <object class="GtkScrolledWindow">
    <property name="hexpand">true</property>
    <property name="vexpand">true</property>
    <property name="margin-top">6</property>
    <property name="margin-bottom">6</property>
    <property name="margin-start">6</property>
    <property name="margin-end">6</property>
    <property name="child">
    </property>
  </object>
</property>
```

2. Add an **object** definition for the **GtkTextView** widget, and assign the
   **main_text_view** as its identifier

```{code-block} xml
:emphasize-lines: 10-12

<property name="content">
  <object class="GtkScrolledWindow">
    <property name="hexpand">true</property>
    <property name="vexpand">true</property>
    <property name="margin-top">6</property>
    <property name="margin-bottom">6</property>
    <property name="margin-start">6</property>
    <property name="margin-end">6</property>
    <property name="child">
      <object class="GtkTextView" id="main_text_view">
        <property name="monospace">true</property>
      </object>
    </property>
  </object>
</property>
```

## Bind the text view in the source code

Templates represent the structure of a UI bound to a specific class; in this
case, the UI definition of the **TextViewerWindow** class. In order to access
a UI element from within the class, you must assign an identifier, using the
**id** XML attribute, to the definition in the XML, and tell GTK to bind the
object with the same identifier to a member in the instance structure.

```{eval-rst}
.. tabs::

   .. tab:: C

      1. Open the ``text_viewer-window.c`` file from the ``src`` directory
      2. Find the definition of the **TextViewerWindow** instance structure near
         the top of the file
      3. Replace the ``GtkLabel *label;`` line with ``GtkTextView *main_text_view;``

      .. code-block:: c
         :emphasize-lines: 7

         struct _TextViewerWindow
         {
           AdwApplicationWindow  parent_instance;

           /* Template widgets */
           AdwHeaderBar *header_bar;
           GtkTextView *main_text_view;
         };


      4. Find the ``text_viewer_window_class_init`` function
      5. Find the ``gtk_widget_class_bind_template_child (widget_class, TextViewerWindow, label);``
         line, and replace ``label`` with ``main_text_view``

         .. code-block:: c
            :emphasize-lines: 8

            static void
            text_viewer_window_class_init (TextViewerWindowClass *klass)
            {
              GtkWidgetClass *widget_class = GTK_WIDGET_CLASS (klass);

              gtk_widget_class_set_template_from_resource (widget_class, "/com/example/TextViewer/text_viewer-window.ui");
              gtk_widget_class_bind_template_child (widget_class, TextViewerWindow, header_bar);
              gtk_widget_class_bind_template_child (widget_class, TextViewerWindow, main_text_view);
            }


   .. tab:: Python

      1. Open the ``window.py`` file
      2. Find the ``TextViewerWindow`` class
      3. Replace the ``label = Gtk.Template.Child()`` line with
         ``main_text_view = Gtk.Template.Child()``

      .. code-block:: python
         :emphasize-lines: 5

         @Gtk.Template(resource_path='/com/example/TextViewer/window.ui')
         class TextViewerWindow(Adw.ApplicationWindow):
             __gtype_name__ = 'TextViewerWindow'

             main_text_view = Gtk.Template.Child()

             def __init__(self, **kwargs):
                 super().__init__(**kwargs)

   .. tab:: Vala

      1. Open the window.vala file
      2. Find the ``Window`` class in the ``TextViewer`` namespace
      3. Replace the ``private unowned Gtk.Label label;`` line with
         ``private unowned Gtk.TextView main_text_view;``

      .. code-block:: vala
         :emphasize-lines: 5

         namespace TextViewer {
             [GtkTemplate (ui = "/org/example/app/window.ui")]
             public class Window : Adw.ApplicationWindow {
                 [GtkChild]
                 private unowned Gtk.TextView main_text_view;

                 public Window (Gtk.Application app) {
                     Object (application: app);
                 }
             }
         }

   .. tab:: JavaScript

      1. Open the ``window.js`` file
      2. Find the ``TextViewerWindow`` class
      3. Replace the ``InternalChildren: ['label'],`` line with
         ``InternalChildren: ['main_text_view'],``

      .. code-block:: js
         :emphasize-lines: 4

         export const TextViewerWindow = GObject.registerClass({
             GTypeName: 'TextViewerWindow',
             Template: 'resource:///com/example/TextViewer/window.ui',
             InternalChildren: ['main_text_view'],
         }, class TextViewerWindow extends Adw.ApplicationWindow {
             constructor(application) {
                 super({ application });
             }
         });

```

Now you can press the **Run** button and verify that the window contains an
empty text area.

In the next lesson, you will learn how to select a file and load its contents
into the text area.
