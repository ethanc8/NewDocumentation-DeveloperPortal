# Windows

```{image} images/window.png
```

A minimal GNOME application: a window with a title.

```{eval-rst}
.. tabs::

   .. code-tab:: c

      #include <adwaita.h>

      G_DECLARE_FINAL_TYPE (MyApplication, my_application, MY, APPLICATION, AdwApplication)

      struct _MyApplication {
        AdwApplication parent_instance;
      };

      G_DEFINE_TYPE (MyApplication, my_application, ADW_TYPE_APPLICATION)

      static void
      my_application_activate (GApplication *application)
      {
        // create a Gtk Window belonging to the application itself
        GtkWidget *window =
          gtk_application_window_new (GTK_APPLICATION (application));

        gtk_window_set_title (GTK_WINDOW (window), "Welcome to GNOME");

        gtk_window_present (GTK_WINDOW (window));
      }

      static void
      my_application_class_init (MyApplicationClass *klass)
      {
        G_APPLICATION_CLASS (klass)->activate = my_application_activate;
      }

      static void
      my_application_init (MyApplication *self)
      {
      }

      int
      main (int argc,
            char *argv[])
      {
        GApplication *app =
          g_object_new (my_application_get_type (),
                        "application-id", "com.example.Application",
                        NULL);

        return g_application_run (app, argc, argv);
      }


   .. code-tab:: python

      import gi
      import sys

      gi.require_version('Gtk', '4.0')
      gi.require_version('Adw', '1')

      from gi.repository import Adw, Gtk

      class MyApplication(Adw.Application):
          """The main application."""

          def do_activate(self):
              # create a Gtk Window belonging to the application itself
              window = Gtk.ApplicationWindow(application=self)
              window.set_title("Welcome to GNOME")
              window.present()

      # create and run the application, exit with the value returned by
      # running the program
      app = MyApplication()
      exit_status = app.run(sys.argv)
      sys.exit(exit_status)

   .. code-tab:: vala

      class My.Application : Adw.Application {
          public Application () {
              Object (application_id: "com.example.Application");
          }

          protected override void activate () {
              // create a Gtk Window belonging to the application itself
              var window = new Gtk.ApplicationWindow (this) {
                title = "Welcome to GNOME"
              };
              window.present ();
          }

          /*
           * create and run the application, exit with the value returned by
           * running the program
           */
          public static int main (string[] args) {
              var app = new My.Application ();
              return app.run (args);
          }
      }

   .. code-tab:: js

      import Gtk from "gi://Gtk?version=4.0";
      import Adw from "gi://Adw?version=1";
      import system from "system";

      const application = new Adw.Application({
        application_id: "com.example.Application",
      });

      application.connect("activate", () => {
        // create a Gtk Window belonging to the application itself
        const window = new Gtk.ApplicationWindow({
          application,
          title: "Welcome to GNOME",
        });
        window.present();
      });

      /*
      * Run the application, exit with the value returned by
      * running the program
      */
      const exit_code = application.run([system.programInvocationName, ...ARGV]);
      system.exit(exit_code);

```

## Useful methods for a Window widget

- `set_content()` sets the content of the application window
- `set_default_size(200, 100)` sets the default size of the window to a width
  of 200 and a height of 100; if instead of a positive number we pass -1 we have
  the default size.

## API References

In this sample we used the following:

- [GApplication](https://docs.gtk.org/gio/class.Application.html)
- [GtkApplication](https://docs.gtk.org/gtk4/class.Application.html)
- [AdwApplication](https://gnome.pages.gitlab.gnome.org/libadwaita/doc/1-latest/class.Application.html)
- [GtkApplicationWindow](https://docs.gtk.org/gtk4/class.ApplicationWindow.html)
