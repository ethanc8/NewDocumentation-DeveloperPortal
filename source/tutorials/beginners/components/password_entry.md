# Password Entries

% image:: ../../img/tutorials/component.png

A password entry is a text field meant to be used for entering secrets. A
password entry will not show its contents by default.

- [Interface guidelines](https://developer.gnome.org/hig/patterns/controls/text-fields.html#password-fields)

```{eval-rst}
.. tabs::

   .. code-tab:: c

      GtkWidget *entry = gtk_password_entry_new ();


   .. code-tab:: python

      entry = Gtk.PasswordEntry()

   .. code-tab:: vala

      var entry = new Gtk.PasswordEntry ();

   .. code-tab:: js

      const entry = new Gtk.PasswordEntry();

```

## Useful methods for the component

- You can use the `GtkPasswordEntry:placeholder-text` property to show a
  placeholder text when the entry is not focused.
- You can disable the "peek contents" icon in the entry by setting the
  `GtkPasswordEntry:show-peek-icon` property to `FALSE`.

## API references

In the examples we used the following classes:

- [GtkPasswordEntry](https://docs.gtk.org/gtk4/class.PasswordEntry.html)
