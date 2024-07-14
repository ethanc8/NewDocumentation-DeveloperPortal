# Spinners

% image:: ../../img/tutorials/spinner.png

A spinner is a placeholder for a long-running action happening in the
background.

- [Interface guidelines](https://developer.gnome.org/hig/patterns/feedback/spinners.html)

```{eval-rst}
.. tabs::

   .. code-tab:: c

      static gboolean
      stop_spinner (gpointer data)
      {
        GtkSpinner *spinner = data;

        gtk_spinner_stop (spinner);

        return G_SOURCE_REMOVE;
      }

      GtkWidget *spinner = gtk_spinner_new ();

      gtk_spinner_start (GTK_SPINNER (spinner));

      // Stop spinner after 5 seconds
      g_timeout_add_seconds (5, stop_spinner, spinner);

   .. code-tab:: python

      spinner = Gtk.Spinner()
      spinner.start()

      def stop_spinner(spinner):
          spinner.stop()
          return GLib.SOURCE_REMOVE

      GLib.timeout_add_seconds(5, stop_spinner, spinner)

   .. code-tab:: vala

      var spinner = new Gtk.Spinner ();
      spinner.start ();

      // Stop spinner after 5 seconds
      Timeout.add_seconds (5, () => {
          spinner.stop ();
          return Source.REMOVE;
      });

   .. code-tab:: js

      const spinner = new Gtk.Spinner();
      spinner.start();

      // Stop spinner after 5 seconds
      GLib.timeout_add_seconds(GLib.PRIORITY_DEFAULT, 5, () => {
        spinner.stop();
        return GLib.SOURCE_REMOVE;
      });

```

## API references

In the examples we used the following classes:

- [GtkSpinner](https://docs.gtk.org/gtk4/class.Spinner.html)
