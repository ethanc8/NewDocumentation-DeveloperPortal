# Saving The Application State

The aim of this lesson is to illustrate how to define new settings starting
from their schema, and bind them to properties on your window in order to
save and restore the size and state of the window across different sessions.

## Add new keys to the settings schema

Settings are stored in a database, and each key is described inside a
schema; the schema contains the type of the value associated with the
key, as well as the default value of the key.

1. Open the `com.example.TextViewer.gschema.xml` file under the `data`
   directory
2. Add a **window-width**, **window-height**, and **window-maximized** keys
   to the schema, including their default values of 600, 400, and false,
   respectively

```{code-block} xml
:emphasize-lines: 3-11

<schemalist gettext-domain="text-viewer">
  <schema id="com.example.TextViewer" path="/com/example/TextViewer/">
    <key name="window-width" type="i">
      <default>600</default>
    </key>
    <key name="window-height" type="i">
      <default>400</default>
    </key>
    <key name="window-maximized" type="b">
      <default>false</default>
    </key>
  </schema>
</schemalist>
```

:::{note}
The schema will be installed automatically in the expected directory
when building the application. This means that the application can only
be run once it's installed.
:::

## Use GSettings

**GSettings** is the object that watches the keys for a specific schema id.
You use the GSettings API to access the value of the keys, as well as get
notified of changes in the settings.

```{eval-rst}
.. tabs::

   .. group-tab:: C

      1. Open the ``text_viewer-window.c`` file
      2. Modify the **TextViewerWindow** instance structure to include a
         **GSettings** instance

      .. code-block:: c
         :emphasize-lines: 5

         struct _TextViewerWindow
         {
           AdwApplicationWindow  parent_instance;

           GSettings *settings;

           /* Template widgets */
           AdwHeaderBar *header_bar;
           GtkTextView *main_text_view;
           GtkButton *open_button;
           GtkLabel *cursor_pos;
         };


      3. Modify the instance initialization function for **TextViewerWindow**
         ``text_viewer_window_init`` to create the **GSettings** instance for
         the ``com.example.TextViewer`` schema id

      .. code-block:: c
         :emphasize-lines: 20

         static void
         text_viewer_window_init (TextViewerWindow *self)
         {
           gtk_widget_init_template (GTK_WIDGET (self));

           g_autoptr (GSimpleAction) open_action = g_simple_action_new ("open", NULL);
           g_signal_connect (open_action, "activate", G_CALLBACK (text_viewer_window__open_file_dialog), self);
           g_action_map_add_action (G_ACTION_MAP (self), G_ACTION (open_action));

           g_autoptr (GSimpleAction) save_action = g_simple_action_new ("save-as", NULL);
           g_signal_connect (save_action, "activate", G_CALLBACK (text_viewer_window__save_file_dialog), self);
           g_action_map_add_action (G_ACTION_MAP (self), G_ACTION (save_action));

           GtkTextBuffer *buffer = gtk_text_view_get_buffer (self->main_text_view);
           g_signal_connect (buffer,
                             "notify::cursor-position",
                             G_CALLBACK (text_viewer_window__update_cursor_position),
                             self);

           self->settings = g_settings_new ("com.example.TextViewer");
         }


      4. Modify the class intialization function for **TextViewerWindow**
         ``text_viewer_window_class_init`` to include a finalization function;
         the ``text_viewer_window_finalize`` function will be called when the
         **TextViewerWindow** instance is going to be freed

      .. code-block:: c
         :emphasize-lines: 5-7

         static void
         text_viewer_window_class_init (TextViewerWindowClass *klass)
         {
           GtkWidgetClass *widget_class = GTK_WIDGET_CLASS (klass);
           GObjectClass *gobject_class = G_OBJECT_CLASS (klass);

           gobject_class->finalize = text_viewer_window_finalize;

           gtk_widget_class_set_template_from_resource (widget_class, "/com/example/TextViewer/text_viewer-window.ui");
           gtk_widget_class_bind_template_child (widget_class, TextViewerWindow, header_bar);
           gtk_widget_class_bind_template_child (widget_class, TextViewerWindow, main_text_view);
           gtk_widget_class_bind_template_child (widget_class, TextViewerWindow, open_button);
           gtk_widget_class_bind_template_child (widget_class, TextViewerWindow, cursor_pos);
         }


      5. Add the ``text_viewer_window_finalize`` function, which clears the
         **GSettings** instance and chains up to the parent implementation

      .. code-block:: c

         static void
         text_viewer_window_finalize (GObject *gobject)
         {
           TextViewerWindow *self = TEXT_VIEWER_WINDOW (gobject);

           g_clear_object (&self->settings);

           G_OBJECT_CLASS (text_viewer_window_parent_class)->finalize (gobject);
         }

   .. group-tab:: Python

      1. Open the ``window.py`` file
      2. Modify the instance initialization function for **TextViewerWindow**
         to create the **GSettings** instance for the ``com.example.TextViewer``
         schema id

      .. code-block:: python
         :emphasize-lines: 15

         def __init__(self, **kwargs):
             super().__init__(**kwargs)

             open_action = Gio.SimpleAction(name="open")
             open_action.connect("activate", self.open_file_dialog)
             self.add_action(open_action)

             save_action = Gio.SimpleAction(name="save-as")
             save_action.connect("activate", self.save_file_dialog)
             self.add_action(save_action)

             buffer = self.main_text_view.get_buffer()
             buffer.connect("notify::cursor-position", self.update_cursor_position)

             self.settings = Gio.Settings(schema_id="com.example.TextViewer")

   .. group-tab:: Vala

      1. Open the ``window.vala`` file
      2. Modify the **TextViewer.Window** class to include a **Settings** property
         and initialize it with the ``com.example.TextViewer`` schema id

      .. code-block:: vala
         :emphasize-lines: 5

         namespace TextViewer {
             public class Window : Adw.ApplicationWindow {
                 // ...

                 private Settings settings = new Settings ("com.example.TextViewer");

                 // ...
             }
         }

   .. group-tab:: JavaScript

      1. Open the ``window.js`` file
      2. Modify the **TextViewerWindow** class to include a **_settings** property
         and initialize it with the ``com.example.TextViewer`` schema id

      .. code-block:: js
         :emphasize-lines: 6

         export const TextViewerWindow = GObject.registerClass({
             GTypeName: 'TextViewerWindow',
             Template: 'resource:///com/example/TextViewer/window.ui',
             InternalChildren: ['main_text_view', 'open_button', 'cursor_pos'],
         }, class TextViewerWindow extends Adw.ApplicationWindow {
             _settings = new Gio.Settings({ schemaId: 'com.example.TextViewer' });

             constructor() {
                 // ...
             }

             // ...
         );

```

## Bind the settings to the window state properties

Keys inside a **GSettings** schema can be bound to **GObject** properties;
bound properties will be automatically saved inside the settings database
whenever they change, and will be restored at creation time.

1. Modify the **TextViewerWindow** instance initialization function
   to bind the **window-width**, **window-height**, and **window-maximize**
   keys to the **default-width**, **default-height**, and **maximized**
   properties, respectively

```{eval-rst}
.. tabs::

   .. code-tab:: c
      :emphasize-lines: 22-30

      static void
      text_viewer_window_init (TextViewerWindow *self)
      {
        gtk_widget_init_template (GTK_WIDGET (self));

        g_autoptr (GSimpleAction) open_action = g_simple_action_new ("open", NULL);
        g_signal_connect (open_action, "activate", G_CALLBACK (text_viewer_window__open), self);
        g_action_map_add_action (G_ACTION_MAP (self), G_ACTION (open_action));

        g_autoptr (GSimpleAction) save_action = g_simple_action_new ("save-as", NULL);
        g_signal_connect (save_action, "activate", G_CALLBACK (text_viewer_window__save), self);
        g_action_map_add_action (G_ACTION_MAP (self), G_ACTION (save_action));

        GtkTextBuffer *buffer = gtk_text_view_get_buffer (self->main_text_view);
        g_signal_connect (buffer,
                          "notify::cursor-position",
                          G_CALLBACK (text_viewer_window__cursor_position),
                          self);

        self->settings = g_settings_new ("com.example.TextViewer");

        g_settings_bind (self->settings, "window-width",
                         G_OBJECT (self), "default-width",
                         G_SETTINGS_BIND_DEFAULT);
        g_settings_bind (self->settings, "window-height",
                         G_OBJECT (self), "default-height",
                         G_SETTINGS_BIND_DEFAULT);
        g_settings_bind (self->settings, "window-maximized",
                         G_OBJECT (self), "maximized",
                         G_SETTINGS_BIND_DEFAULT);
      }

   .. code-tab:: python
      :emphasize-lines: 16-21

      def __init__(self, **kwargs):
          super().__init__(**kwargs)

          open_action = Gio.SimpleAction(name="open")
          open_action.connect("activate", self.open_file_dialog)
          self.add_action(open_action)

          save_action = Gio.SimpleAction(name="save-as")
          save_action.connect("activate", self.save_file_dialog)
          self.add_action(save_action)

          buffer = self.main_text_view.get_buffer()
          buffer.connect("notify::cursor-position", self.update_cursor_position)

          self.settings = Gio.Settings(schema_id="com.example.TextViewer")
          self.settings.bind("window-width", self, "default-width",
                             Gio.SettingsBindFlags.DEFAULT)
          self.settings.bind("window-height", self, "default-height",
                             Gio.SettingsBindFlags.DEFAULT)
          self.settings.bind("window-maximized", self, "maximized",
                             Gio.SettingsBindFlags.DEFAULT)

   .. code-tab:: vala
      :emphasize-lines: 22-24

      namespace TextViewer {
          public class Window : Adw.ApplicationWindow {

              // ...

              public Window (Gtk.Application app) {
                  Object (application: app);
              }

              construct {
                  var open_action = new SimpleAction ("open", null);
                  open_action.activate.connect (this.open_file_dialog);
                  this.add_action (open_action);

                  var save_action = new SimpleAction ("save-as", null);
                  save_action.activate.connect (this.save_file_dialog);
                  self.add_action (save_action);

                  Gtk.TextBuffer buffer = this.text_view.buffer;
                  buffer.notify["cursor-position"].connect (this.update_cursor_position);

                  this.settings.bind ("window-width", this, "default-width", SettingsBindFlags.DEFAULT);
                  this.settings.bind ("window-height", this, "default-height", SettingsBindFlags.DEFAULT);
                  this.settings.bind ("window-maximized", this, "maximized", SettingsBindFlags.DEFAULT);
              }
          }
      }

   .. code-tab:: js
      :emphasize-lines: 13-18

      export const TextViewerWindow = GObject.registerClass({
          GTypeName: 'TextViewerWindow',
          Template: 'resource:///com/example/TextViewer/window.ui',
          InternalChildren: ['main_text_view', 'open_button', 'cursor_pos'],
      }, class TextViewerWindow extends Adw.ApplicationWindow {
          _settings = new Gio.Settings({ schemaId: 'com.example.TextViewer' });

          constructor(application) {
              super({ application });

              // ...

              this._settings.bind(
                  "window-width", this, "default-width", Gio.SettingsBindFlags.DEFAULT);
              this._settings.bind(
                  "window-height", this, "default-height", Gio.SettingsBindFlags.DEFAULT);
              this._settings.bind(
                  "window-maximized", this, "maximized", Gio.SettingsBindFlags.DEFAULT);
          }

          // ...
      });

```

In this lesson you have added keys to the GSettings schema associated with
your application; managed the lifetime of the GSettings instance by tying it
to the application window; and bound the keys in the GSettings database to
the state properties of your application window.
