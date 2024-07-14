# Messages

% image:: ../../img/tutorials/component.png

A message is a type of dialog window that is used to notify the user about
some action or state change; they can also be used to pose a question or ask
for user confirmation.

- [Interface guidelines](https://developer.gnome.org/hig/patterns/feedback/dialogs.html#message-dialogs)

```{eval-rst}
.. tabs::

   .. code-tab:: c

      GtkDialogFlags flags = GTK_DIALOG_DESTROY_WITH_PARENT
                           | GTK_DIALOG_MODAL;

      // "parent_window" is defined elsewhere
      GtkWidget *dialog =
        gtk_message_dialog_new (parent_window,
                                flags,
                                GTK_MESSAGE_ERROR,
                                GTK_BUTTONS_CLOSE,
                                "Error reading “%s”",
                                // "filename" is defined elsewhere
                                filename);

      // Destroy the dialog when the user responds to it
      g_signal_connect (dialog, "response",
                        G_CALLBACK (gtk_window_destroy),
                        NULL);

   .. code-tab:: python

      # "filename" is defined elsewhere
      dialog = Gtk.MessageDialog(text=f"Error reading \"{filename}\"",
                                 buttons=Gtk.ButtonsType.CLOSE)

      # "parent_window" is defined elsewhere
      dialog.set_transient_for(parent_window)
      dialog.set_destroy_with_parent(True)
      dialog.set_modal(True)

      # Destroy the dialog when the user responds to it
      dialog.connect("response", lambda d: d.destroy())

   .. code-tab:: vala

      Gtk.DialogFlags flags = DESTROY_WITH_PARENT | MODAL;

      // "parent_window" is defined elsewhere
      var dialog = new Gtk.MessageDialog (parent_window,
                                          flags,
                                          Gtk.MessageType.ERROR,
                                          Gtk.ButtonsType.CLOSE,
                                          "Error reading “%s”",
                                          // "filename" is defined elsewhere
                                          filename);

      dialog.response.connect (dialog.destroy);

   .. code-tab:: js

    const dialog = new Gtk.MessageDialog({
      // "parent_window" is defined elsewhere
      transient_for: parent_window,
      destroy_with_parent: true,
      modal: true,
      message_type: Gtk.MessageType.ERROR,
      buttons: Gtk.ButtonsType.CLOSE,
      // "filename" is defined elsewhere
      text: `Error reading “${filename}”`,
    });

    dialog.connect("response", () => {
      dialog.destroy();
    });

    dialog.show();

```

## Useful methods for the component

- If your message contains [Pango markup](https://docs.gtk.org/Pango/pango_markup.html#pango-markup)
  you can set the `GtkMessageDialog:use-markup` property to true.
- A message dialog can also contain a secondary text, which is displayed
  underneath the message specified in the `GtkMessageDialog:text` property.
  You can use the `GtkMessageDialog:secondary-text` property to define the
  secondary text.
- The secondary text can also use Pango markup, as long as you set the
  `GtkMessageDialog:secondary-use-markup` to true.

## API references

In the examples we used the following classes:

- [GtkMessageDialog](https://docs.gtk.org/gtk4/class.MessageDialog.html)
- [GtkDialog](https://docs.gtk.org/gtk4/class.Dialog.html)
- [GtkWindow](https://docs.gtk.org/gtk4/class.Window.html)
