# Entries

% image:: ../../img/tutorials/component.png

Entries are used for single line text entry and editing.

- [Interface guidelines](https://developer.gnome.org/hig/patterns/controls/text-fields.html)

## Activation

Entries will emit the `GtkEntry::activate` signal every time the user presses
the {kbd}`Return` key.

```{eval-rst}
.. tabs::

   .. code-tab:: c

      GtkWidget *entry = gtk_entry_new ();

      // "on_entry_activate" is defined elsewhere
      g_signal_connect (entry, "activate", G_CALLBACK (on_entry_activate), NULL);

   .. code-tab:: python

      entry = Gtk.Entry()

      # "on_entry_activate" is defined elsewhere
      entry.connect("activate", on_entry_activate)

   .. code-tab:: vala

      var entry = new Gtk.Entry ();

      // "on_entry_activate" is defined elsewhere
      entry.activate.connect (on_entry_activate);

   .. code-tab:: js

      const entry = new Gtk.Entry();

      // "on_entry_activate" is defined elsewhere
      entry.connect("activate", on_entry_activate);

```

The entry can also activate the default widget in the same window, by setting
the `GtkEntry:activates-default` property:

```{eval-rst}
.. tabs::

   .. code-tab:: c

      GtkWidget *entry = gtk_entry_new ();

      gtk_entry_set_activates_default (GTK_ENTRY (entry), TRUE);

   .. code-tab:: python

      entry = Gtk.Entry(activates_default=True)

   .. code-tab:: vala

      var entry = new Gtk.Entry () {
          activates_default = true
      };

   .. code-tab:: js

      const entry = new Gtk.Entry({
        activates_default: true,
      });

```

## Buffers

Entries store their contents inside separate `GtkEntryBuffer` objects. You
can use entry buffers to share content between different entry widgets:

```{eval-rst}
.. tabs::

   .. code-tab:: c

      GtkEntryBuffer *buffer = gtk_entry_buffer_new ("Live, Laugh, Love", -1);

      // All three entries will show "Live, Laugh, Love"
      GtkWidget *live = gtk_entry_new_with_buffer (buffer);
      GtkWidget *laugh = gtk_entry_new_with_buffer (buffer);
      GtkWidget *love = gtk_entry_new_with_buffer (buffer);

   .. code-tab:: python

      buffer = Gtk.EntryBuffer(text="Live, Laugh, Love")

      # All three entries will show "Live, Laugh, Love"
      live = Gtk.Entry(buffer=buffer)
      laugh = Gtk.Entry(buffer=buffer)
      love = Gtk.Entry(buffer=buffer)

   .. code-tab:: vala

      var buffer = new Gtk.EntryBuffer ("Live, Laugh, Love");

      // All three entries will show "Live, Laugh, Love"
      var live = new Gtk.Entry.with_buffer (buffer);
      var laugh = new Gtk.Entry.with_buffer (buffer);
      var love = new Gtk.Entry.with_buffer (buffer);

   .. code-tab:: js

      const buffer = new Gtk.EntryBuffer({
        text: "Live, Laugh, Love",
      });

      // All three entries will show "Live, Laugh, Love"
      const live = new Gtk.Entry({ buffer });
      const laugh = new Gtk.Entry({ buffer });
      const love = new Gtk.Entry({ buffer });

```

## Useful methods for the component

- You should use the `set_input_purpose()` method to specify the purpose of
  the text entry; for instance, if the entry is only supposed to be used to
  input phone numbers, or email addresses.
- You should use the `set_input_hint()` method to include additional hints
  as to the content of the text entry, especially for input methods and
  internationalization.
- If you want to show a hint when the entry is empty and not focused, you
  can use the `GtkEntry:placeholder-text` property.

## API references

In the examples we used the following classes:

- [GtkEntry](https://docs.gtk.org/gtk4/class.Entry.html)
- [GtkEntryBuffer](https://docs.gtk.org/gtk4/class.EntryBuffer.html)
