# Forcing The Dark Color Scheme

GNOME applications will respect the system setting for the light or dark
theme. It is possible, however, to present the choice of forcing the dark
theme to the user in your application's UI.

```{image} images/dark_mode.png
```

## Add the "Dark Mode" item to the application's menu

1. Open the UI definition file for the **TextViewerWindow** widget
2. Add a menu item for the **app.dark** action, called **Dark Mode**

```{code-block} xml
:emphasize-lines: 7-10

<menu id="primary_menu">
  <section>
    <item>
      <attribute name="label" translatable="yes">Save _as...</attribute>
      <attribute name="action">win.save-as</attribute>
    </item>
    <item>
      <attribute name="label" translatable="yes">_Dark mode</attribute>
      <attribute name="action">app.dark-mode</attribute>
    </item>
```

## Add the dark mode action to the application

1. Open the **TextViewApplication** source
2. Find the **TextViewApplication** instance initialization function
3. Create the **dark-mode** stateful action and connect to its `activate`
   and `change-state` signals
4. Add the action to the application

```{eval-rst}
.. tabs::

   .. code-tab:: c
      :emphasize-lines: 4-10

      static void
      text_viewer_application_init (TextViewerApplication *self)
      {
        g_autoptr (GSimpleAction) dark_action =
          g_simple_action_new_stateful ("dark-mode",
                                        NULL,
                                        g_variant_new_boolean (FALSE));
        g_signal_connect (dark_action, "activate", G_CALLBACK (toggle_dark_mode), self);
        g_signal_connect (dark_action, "change-state", G_CALLBACK (change_color_scheme), self);
        g_action_map_add_action (G_ACTION_MAP (self), G_ACTION (dark_action));

   .. code-tab:: python
      :emphasize-lines: 1, 10-14

      from gi.repository import Adw, Gio, GLib, Gtk
      from .window import PytextViewerWindow, AboutDialog


      class TextViewerApplication(Adw.Application):
          def __init__(self):
              super().__init__(application_id='com.example.TextViewer',
                               flags=Gio.ApplicationFlags.FLAGS_NONE)

              dark_mode_action = Gio.SimpleAction(name="dark-mode",
                                                  state=GLib.Variant.new_boolean(False))
              dark_mode_action.connect("activate", self.toggle_dark_mode)
              dark_mode_action.connect("change-state", self.change_color_scheme)
              self.add_action(dark_mode_action)

   .. code-tab:: vala
      :emphasize-lines: 11-13

      namespace TextViewer {
          public class Application : Adw.Application {
              // ...

              public Application () {
                  Object (application_id: "com.example.TextViewer",
                          flags: ApplicationFlags.FLAGS_NONE);
              }

              construct {
                  var dark_mode_action = new SimpleAction.stateful ("dark-mode", null, new Variant.boolean (false));
                  dark_mode_action.activate.connect (this.toggle_dark_mode);
                  dark_mode_action.change_state.connect (this.change_color_scheme);
              }
          }
      }

   .. group-tab:: JavaScript

      1. Import GLib, since we are going to use `GLib.Variant <https://gjs.guide/guides/glib/gvariant.html>`_

      .. code-block:: js
         :emphasize-lines: 5

         import GObject from 'gi://GObject';
         import Gio from 'gi://Gio';
         import Gtk from 'gi://Gtk?version=4.0';
         import Adw from 'gi://Adw?version=1';
         import GLib from 'gi://GLib';

      2. Create and configure the `dark-mode` action

      .. code-block:: js
         :emphasize-lines: 9-13

         export const TextViewerApplication = GObject.registerClass(
             class TextViewerApplication extends Adw.Application {
                 constructor() {
                     super({application_id: 'com.example.TextViewer', flags: Gio.ApplicationFlags.FLAGS_NONE});

                     this.set_accels_for_action('win.open', [ '<Ctrl>o' ]);
                     this.set_accels_for_action('win.save-as', [ '<Ctrl><Shift>s' ]);

                     const darkModeAction = Gio.SimpleAction.new_stateful(
                         'dark-mode', null, GLib.Variant.new_boolean(false));
                     darkModeAction.connect('activate', this.toggleDarkMode.bind(this));
                     darkModeAction.connect('change-state', this.changeColorScheme.bind(this));
                     this.add_action(darkModeAction);

                     // ...
                 }

                 // ...
             }
         );


```

5. Add the `toggle_dark_mode` callback; this callback toggles the state of
   the **dark-mode** action between "true" and "false"

```{eval-rst}
.. tabs::

   .. code-tab:: c

      static void
      toggle_dark_mode (GSimpleAction *action,
                        GVariant      *parameter G_GNUC_UNUSED,
                        gpointer       user_data G_GNUC_UNUSED)
      {
        GVariant *state = g_action_get_state (G_ACTION (action));
        gboolean old_state = g_variant_get_boolean (state);
        gboolean new_state = !old_state;

        g_action_change_state (G_ACTION (action), g_variant_new_boolean (new_state));

        g_variant_unref (state);
      }

   .. code-tab:: python

      def toggle_dark_mode(self, action, _):
          state = action.get_state()
          old_state = state.get_boolean()
          new_state = not old_state
          action.change_state(GLib.Variant.new_boolean(new_state))

   .. code-tab:: vala

      private void toggle_dark_mode (Action action, Variant? parameter) {
          Variant state = action.state;
          bool old_state = state.get_boolean ();
          bool new_state = !old_state;
          action.change_state (new_state);
      }

   .. code-tab:: js

      toggleDarkMode (action) {
          const oldState = action.state.get_boolean();
          const newState = !oldState;
          action.change_state(GLib.Variant.new_boolean(newState));
      }

```

6. Add the `change_color_scheme` callback; this callback is responsible for
   switching the application's color scheme using the **AdwStyleManager** API

```{eval-rst}
.. tabs::

   .. code-tab:: c

      static void
      change_color_scheme (GSimpleAction         *action,
                           GVariant              *new_state,
                           TextViewerApplication *self)
      {
        gboolean dark_mode = g_variant_get_boolean (new_state);

        AdwStyleManager *style_manager = adw_style_manager_get_default ();

        if (dark_mode)
          adw_style_manager_set_color_scheme (style_manager, ADW_COLOR_SCHEME_FORCE_DARK);
        else
          adw_style_manager_set_color_scheme (style_manager, ADW_COLOR_SCHEME_DEFAULT);

        g_simple_action_set_state (action, new_state);
      }

   .. code-tab:: python

      def change_color_scheme(self, action, new_state):
          dark_mode = new_state.get_boolean()
          style_manager = Adw.StyleManager.get_default()
          if dark_mode:
              style_manager.set_color_scheme(Adw.ColorScheme.FORCE_DARK)
          else:
              style_manager.set_color_scheme(Adw.ColorScheme.DEFAULT)
          action.set_state(new_state)

   .. code-tab:: vala

      private void change_color_scheme (SimpleAction action, Variant? new_state) {
          bool dark_mode = new_state.get_boolean ();
          var style_manager = Adw.StyleManager.get_default ();

          if (dark_mode)
              style_manager.color_scheme = Adw.ColorScheme.FORCE_DARK;
          else
              style_manager.color_scheme = Adw.ColorScheme.DEFAULT;
          action.set_state (new_state);
      }

   .. code-tab:: js

      changeColorScheme(action, newState) {
          const isDarkMode = newState.get_boolean();
          const styleManager = Adw.StyleManager.get_default();

          styleManager.color_scheme = isDarkMode
              ? Adw.ColorScheme.FORCE_DARK
              : Adw.ColorScheme.DEFAULT;

          action.set_state (newState);
      }

```

## Store the dark mode state as a setting

If you want to preserve the chosen color scheme across sessions you can
store it inside GSettings, which you added in {doc}`Saving The Application State <./saving_state>`.

### Add a new key to the settings schema

1. Open the `com.example.TextViewer.gschema.xml` file
2. Add a **dark-mode** boolean key

```{code-block} xml
:emphasize-lines: 13-15

<?xml version="1.0" encoding="UTF-8"?>
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
    <key name="dark-mode" type="b">
      <default>false</default>
    </key>
  </schema>
</schemalist>
```

### Add GSettings to the application

```{eval-rst}
.. tabs::

   .. group-tab:: C

      1. Add a **GSettings** instance to the **TextViewerApplication**

      .. code-block:: c
         :emphasize-lines: 5

         struct _TextViewerApplication
         {
           GtkApplication parent_instance;

           GSettings *settings;
         };


      2. Clear the **GSettings** instance when the **TextViewerApplication**
         instance is disposed

      .. code-block:: c
         :emphasize-lines: 1-9, 15-17

         static void
         text_viewer_application_dispose (GObject *gobject)
         {
           TextViewerApplication *self = TEXT_VIEWER_APPLICATION (gobject);

           g_clear_object (&self->settings);

           G_OBJECT_CLASS (text_viewer_application_parent_class)->dispose (gobject);
         }

         static void
         text_viewer_application_class_init (TextViewerApplicationClass *klass)
         {
           GApplicationClass *app_class = G_APPLICATION_CLASS (klass);
           GObjectClass *gobject_class = G_OBJECT_CLASS (klass);

           gobject_class->dispose = text_viewer_application_dispose;


      3. Initialize the **GSettings** instance alongside the rest of the
         **TextViewerApplication**

      .. code-block:: c
         :emphasize-lines: 4

         static void
         text_viewer_application_init (TextViewerApplication *self)
         {
           self->settings = g_settings_new ("com.example.TextViewer");

           g_autoptr (GSimpleAction) quit_action = g_simple_action_new ("quit", NULL);
           g_signal_connect_swapped (quit_action, "activate", G_CALLBACK (g_application_quit), self);
           g_action_map_add_action (G_ACTION_MAP (self), G_ACTION (quit_action));


   .. group-tab:: Python

      1. Add a **GSettings** instance to your **TextViewerApplication**

      .. code-block:: python
         :emphasize-lines: 6

         class TextViewerApplication(Adw.Application):
             def __init__(self):
                 super().__init__(application_id='com.example.TextViewer',
                                  flags=Gio.ApplicationFlags.FLAGS_NONE)

                 self.settings = Gio.Settings(schema_id="com.example.TextViewer")

   .. group-tab:: Vala

      1. Add a **Settings** instance to your **TextViewer.Application**

      .. code-block:: vala
         :emphasize-lines: 5

         namespace TextViewer {
             public class Application : Adw.Application {
                 // ...

                 private Settings settings = new Settings ("com.example.TextViewer");

                 public Application () {
                     Object (application_id: "com.example.TextViewer",
                             flags: ApplicationFlags.FLAGS_NONE);
                 }

                 // ...
             }
         }

   .. group-tab:: JavaScript

      1. Add a **Gio.Settings** instance to your **TextViewerApplication**

      .. code-block:: js
         :emphasize-lines: 5

         export const TextViewerApplication = GObject.registerClass(
             class TextViewerApplication extends Adw.Application {
                 _settings = new Gio.Settings({ schemaId: 'com.example.TextViewer' });

                 constructor() {
                     // ...
                 }

                 // ...
             }
         );

```

### Set the initial state for the color scheme

1. Retrieve the value of the **dark-mode** GSettings key
2. Set the color scheme using the key's value
3. Initialize the state of the **dark-mode** action with the key's value

```{eval-rst}
.. tabs::

   .. code-tab:: c
      :emphasize-lines: 6-14

      static void
      text_viewer_application_init (TextViewerApplication *self)
      {
        self->settings = g_settings_new ("com.example.TextViewer");

        gboolean dark_mode = g_settings_get_boolean (self->settings, "dark-mode");
        AdwStyleManager *style_manager = adw_style_manager_get_default ();
        if (dark_mode)
          adw_style_manager_set_color_scheme (style_manager, ADW_COLOR_SCHEME_FORCE_DARK);
        else
          adw_style_manager_set_color_scheme (style_manager, ADW_COLOR_SCHEME_DEFAULT);

        g_autoptr (GSimpleAction) dark_action =
          g_simple_action_new_stateful ("dark-mode", NULL, g_variant_new_boolean (dark_mode));
        g_signal_connect (dark_action, "activate", G_CALLBACK (text_viewer_application_toggle_action), self);
        g_signal_connect (dark_action, "change-state", G_CALLBACK (text_viewer_application_dark_mode_changed), self);
        g_action_map_add_action (G_ACTION_MAP (self), G_ACTION (dark_action));


   .. code-tab:: python
      :emphasize-lines: 8-16

      class TextViewerApplication(Adw.Application):
          def __init__(self):
              super().__init__(application_id='com.example.TextViewer',
                               flags=Gio.ApplicationFlags.FLAGS_NONE)

              self.settings = Gio.Settings(schema_id="com.example.TextViewer")

              dark_mode = self.settings.get_boolean("dark-mode")
              style_manager = Adw.StyleManager.get_default()
              if dark_mode:
                  style_manager.set_color_scheme(Adw.ColorScheme.FORCE_DARK)
              else:
                  style_manager.set_color_scheme(Adw.ColorScheme.DEFAULT)

              dark_mode_action = Gio.SimpleAction(name="dark-mode",
                                                  state=GLib.Variant.new_boolean(dark_mode))
              dark_mode_action.connect("activate", self.toggle_dark_mode)
              dark_mode_action.connect("change-state", self.change_color_scheme)
              self.add_action(dark_mode_action)

   .. code-tab:: vala
      :emphasize-lines: 13-20

      namespace TextViewer {
          public class Application : Adw.Application {
              // ...

              private Settings settings = new Settings ("com.example.TextViewer");

              public Application () {
                  Object (application_id: "com.example.TextViewer",
                          flags: ApplicationFlags.FLAGS_NONE);
              }

              construct {
                  bool dark_mode = this.settings.get_boolean ("dark-mode");
                  var style_manager = Adw.StyleManager.get_default ();
                  if (dark_mode)
                      style_manager.color_scheme = Adw.ColorScheme.FORCE_DARK;
                  else
                      style_manager.color_scheme = Adw.ColorScheme.DEFAULT;

                  var dark_mode_action = new SimpleAction.stateful ("dark-mode", null, new Variant.boolean (dark_mode));
                  dark_mode_action.activate.connect (this.toggle_dark_mode);
                  dark_mode_action.change_state.connect (this.change_color_scheme);
                  this.add_action (dark_mode_action);
              }
          }
      }

   .. code-tab:: js
      :emphasize-lines: 11-15, 17

      export const TextViewerApplication = GObject.registerClass(
          class TextViewerApplication extends Adw.Application {
             _settings = new Gio.Settings({ schemaId: 'com.example.TextViewer' });

              constructor() {
                  super({application_id: 'com.example.TextViewer', flags: Gio.ApplicationFlags.FLAGS_NONE});

                  this.set_accels_for_action('win.open', [ '<Ctrl>o' ]);
                  this.set_accels_for_action('win.save-as', [ '<Ctrl><Shift>s' ]);

                  const isDarkMode = this._settings.get_boolean('dark-mode');
                  const styleManager = Adw.StyleManager.get_default();
                  styleManager.color_scheme = isDarkMode
                      ? Adw.ColorScheme.FORCE_DARK
                      : Adw.ColorScheme.DEFAULT;

                  const darkModeAction = Gio.SimpleAction.new_stateful(
                      'dark-mode', null, GLib.Variant.new_boolean(isDarkMode));
                  darkModeAction.connect('activate', this.toggleDarkMode.bind(this));
                  darkModeAction.connect('change-state', this.changeColorScheme.bind(this));
                  this.add_action(darkModeAction);

                  // ...
              }

              // ...
          }
      );

```

### Save the color scheme when it changes

1. Update the **dark-mode** GSettings key using the state of the **dark-mode**
   action whenever it changes.

```{eval-rst}
.. tabs::

   .. code-tab:: c
      :emphasize-lines: 17

      static void
      change_color_scheme (GSimpleAction         *action,
                           GVariant              *value,
                           TextViewerApplication *self)
      {
        gboolean dark_mode = g_variant_get_boolean (value);

        AdwStyleManager *style_manager = adw_style_manager_get_default ();

        if (dark_mode)
          adw_style_manager_set_color_scheme (style_manager, ADW_COLOR_SCHEME_FORCE_DARK);
        else
          adw_style_manager_set_color_scheme (style_manager, ADW_COLOR_SCHEME_DEFAULT);

        g_simple_action_set_state (action, value);

        g_settings_set_boolean (self->settings, "dark-mode", dark_mode);
      }


   .. code-tab:: python
      :emphasize-lines: 9

      def change_color_scheme(self, action, new_state):
          dark_mode = new_state.get_boolean()
          style_manager = Adw.StyleManager.get_default()
          if dark_mode:
              style_manager.set_color_scheme(Adw.ColorScheme.FORCE_DARK)
          else:
              style_manager.set_color_scheme(Adw.ColorScheme.DEFAULT)
          action.set_state(new_state)
          self.settings.set_boolean("dark-mode", dark_mode)

   .. code-tab:: vala
      :emphasize-lines: 11

      private void change_color_scheme (Action action, Variant? new_state) {
          bool dark_mode = new_state.get_boolean ();
          var style_manager = Adw.StyleManager.get_default ();

          if (dark_mode)
              style_manager.color_scheme = Adw.ColorScheme.FORCE_DARK;
          else
              style_manager.color_scheme = Adw.ColorScheme.DEFAULT;
          action.set_state (new_state);

          this.settings.set_boolean ("dark-mode", dark_mode);
      }

   .. code-tab:: js
      :emphasize-lines: 10

      changeColorScheme(action, newState) {
          const isDarkMode = newState.get_boolean();
          const styleManager = Adw.StyleManager.get_default();

          styleManager.color_scheme = isDarkMode
              ? Adw.ColorScheme.FORCE_DARK
              : Adw.ColorScheme.DEFAULT;

          action.set_state (newState);
          this._settings.set_boolean("dark-mode", isDarkMode);
      }

```

In this lesson you have learned how to force the dark color scheme for your
application, and storing it as an application preference.
