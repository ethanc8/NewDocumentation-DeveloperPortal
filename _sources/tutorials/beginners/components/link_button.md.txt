# Link Buttons

% image:: ../../img/tutorials/component.png

A button showing an hyper link to a resource.

```{eval-rst}
.. tabs::

   .. code-tab:: c

      GtkWidget *link = gtk_link_button_new ("https://developer.gnome.org");

      gtk_button_set_label (GTK_BUTTON (link), "Developer Documentation");

   .. code-tab:: python

      link = Gtk.LinkButton(uri="https://developer.gnome.org",
                            label="Developer Documentation")

   .. code-tab:: vala

      var link = new Gtk.LinkButton.with_label ("https://developer.gnome.org",
                                                "Developer Documentation");

   .. code-tab:: js

      const link = new Gtk.LinkButton({
        uri: "https://developer.gnome.org",
        label: "Developer Documentation",
      });

```

It is possible to use a link to any resource that has a URI scheme with a
handler defined in the operating system; for instance, this button will
open the help browser:

```{eval-rst}
.. tabs::

   .. code-tab:: c

      GtkWidget *help = gtk_link_button_new ("help:devhelp");

      gtk_button_set_label (GTK_BUTTON (help), "Open the Devhelp documentation");

   .. code-tab:: python

      help = Gtk.LinkButton(uri="help:devhelp", label="Open the Devhelp documentation")

   .. code-tab:: vala

      var help = new Gtk.LinkButton.with_label ("help:devhelp",
                                                "Open the Devhelp documentation");

   .. code-tab:: js

      const help = new Gtk.LinkButton({
         uri: "help:devhelp",
         label: "Open the Devhelp documentation"
      });

```

## Useful methods for the component

- If you want to know whether the user clicked the button and visited the
  URL, then you can use the `get_visited()` method. If you change the URL
  of the link button, the `GtkLinkButton:visited` property will be reset.

## API references

In the examples we used the following classes:

- [GtkLinkButton](https://docs.gtk.org/gtk4/class.LinkButton.html)
