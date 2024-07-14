# File Dialogs

% image:: ../../img/tutorials/component.png

You can use the file selection dialog to allow the user to select a file to
load its contents into their application, or to save the current contents of
their application.

:::{note}
GTK has two types of file selection dialogs: one is the "internal" dialog,
provided by the toolkit itself; and the other is a "native" dialog, which
will use the platform's own file selection dialog.

We are going to always use "native" file selection dialogs as they are
also the preferred way to interact with sandboxed environments.
:::

:::{important}
Native file selection dialogs are **not** widgets; you must manage their
lifetime yourself.
:::

## Opening files

```{eval-rst}
.. tabs::

   .. code-tab:: c

      static void
      on_file_open_response (GtkNativeDialog *native,
                             int response_id)
      {
        if (response_id == GTK_RESPONSE_ACCEPT) {
          GtkFileChooser *chooser = GTK_FILE_CHOOSER (native);
          g_autoptr (GFile) file = gtk_file_chooser_get_file (chooser);

          open_file (file);
        }

        g_object_unref (native);
      }

      // ...

      GtkFileChooserNative *native =
        gtk_file_chooser_native_new ("Open File",
                                     parent_window,
                                     GTK_FILE_CHOOSER_ACTION_OPEN,
                                     "_Open",
                                     "_Cancel");

      g_signal_connect (native, "response",
                        G_CALLBACK (on_file_open_response),
                        NULL);
      gtk_native_dialog_show (GTK_NATIVE_DIALOG (native));

   .. code-tab:: python

      # Keep a reference on the native dialog; "self", in this case, is
      # the application singleton instance
      self._native = Gtk.FileChooserNative(
          title="Open File",
          # "self.main_window" is defined elsewhere as a Gtk.Window
          transient_for=self.main_window,
          action=Gtk.FileChooserAction.OPEN,
          accept_label="_Open",
          cancel_label="_Cancel",
      )

      def on_file_open_response(native, response):
          if response == Gtk.ResponseType.ACCEPT:
              self.open_file(native.get_file())
          self._native = None

      self._native.connect("response", on_file_open_response)
      self._native.show()

   .. code-tab:: vala

      var native = new Gtk.FileChooserNative ("Open File",
                                              parent_window,
                                              Gtk.FileChooserAction.OPEN,
                                              "_Open",
                                              "_Cancel");

      native.response.connect ((response_id) => {
          if (response_id == Gtk.ResponseType.ACCEPT)
              open_file (native.get_file ());

          native = null;
      };

      native.show ();

   .. code-tab:: js

      const native = new Gtk.FileChooserNative({
        title: "Open File",
        transient_for: parent_window,
        action: Gtk.FileChooserAction.OPEN,
        accept_label: "_Open",
        cancel_label: "_Cancel",
      });

      native.connect("response", (self, response_id) => {
        if (response_id === Gtk.ResponseType.ACCEPT) {
          open_file(native.get_file());
        }
      });

      native.show();

```

## Saving files

```{eval-rst}
.. tabs::

   .. code-tab:: c

      static void
      on_file_save_response (GtkNativeDialog *native,
                             int response_id)
      {
        if (response_id == GTK_RESPONSE_ACCEPT) {
          GtkFileChooser *chooser = GTK_FILE_CHOOSER (native);
          g_autoptr (GFile) file = gtk_file_chooser_get_file (chooser);

          save_file (file);
        }

        g_object_unref (native);
      }

      // ...

      GtkFileChooserNative *native =
        gtk_file_chooser_native_new ("Save File",
                                     parent_window,
                                     GTK_FILE_CHOOSER_ACTION_SAVE,
                                     "_Save",
                                     "_Cancel");

      g_signal_connect (native, "response",
                        G_CALLBACK (on_file_save_response),
                        NULL);
      gtk_native_dialog_show (GTK_NATIVE_DIALOG (native));

   .. code-tab:: python

      # Keep a reference on the native dialog; "self", in this case, is
      # the application singleton instance
      self._native = Gtk.FileChooserNative(
          title="Save File",
          # "self.main_window" is defined elsewhere as a Gtk.Window
          transient_for=self.main_window,
          action=Gtk.FileChooserAction.SAVE,
          accept_label="_Save",
          cancel_label="_Cancel",
      )

      def on_file_save_response(native, response):
          if response == Gtk.ResponseType.ACCEPT:
              self.save_file(native.get_file())
          self._native = None

      self._native.connect("response", on_file_save_response)
      self._native.show()

   .. code-tab:: vala

      var native = new Gtk.FileChooserNative ("Save File",
                                              parent_window,
                                              Gtk.FileChooserAction.SAVE,
                                              "_Save",
                                              "_Cancel");

      native.response.connect ((response_id) => {
          if (response_id == Gtk.ResponseType.ACCEPT)
              save_file (native.get_file ());
      });

      native.show ();

   .. code-tab:: js

      const native = new Gtk.FileChooserNative({
        title: "Save File",
        transient_for: parent_window,
        action: Gtk.FileChooserAction.SAVE,
        accept_label: "_Save",
        cancel_label: "_Cancel",
      });

      native.connect("response", (self, response_id) => {
        if (response_id === Gtk.ResponseType.ACCEPT) {
          save_file(native.get_file());
        }
      });

      native.show();

```

## Choices

File selection dialogs can expose additional controls to the user in the
form of "choices". A choice can either be a boolean "yes or no" option, or
a set of possible values:

```{eval-rst}
.. tabs::

   .. code-tab:: c

      // Boolean choice
      gtk_file_chooser_add_choice (file_chooser, "validate",
                                   "Enable validation on load",
                                   NULL, NULL);
      // Multiple choices
      gtk_file_chooser_add_choice (file_chooser, "action",
                                   "Action when loading",
                                   (const char *[]) {
                                     "live",
                                     "laugh",
                                     "love",
                                     NULL,
                                   },
                                   (const char *[]) {
                                     "Live",
                                     "Laugh",
                                     "Love",
                                     NULL,
                                   });

   .. code-tab:: python

      # Boolean choice
      file_chooser.add_choice("validate", "Enable validation on load", None, None)
      # Multiple choices
      file_chooser.add_choice("action", "Action when loading",
                              ["live", "laugh", "love"],
                              ["Live", "Laugh", "Love"])

   .. code-tab:: vala

      // Boolean choice
      filechooser.add_choice ("validate", "Enable validation on load", null, null);
      // Multiple choice
      filechooser.add_choice ("action",
                              "Action when loading",
                              { "live", "laugh", "love" },
                              { "Live", "Laugh", "Love" });

   .. code-tab:: js

      // Boolean choice
      file_chooser.add_choice("validate", "Enable validation on load", null, null);
      // Multiple choice
      file_chooser.add_choice(
        "action",
        "Action when loading",
        ["live", "laugh", "love"],
        ["Live", "Laugh", "Love"],
      );

```

You can then use the `get_choice()` method in the "response" signal handler
to retrieve the value of the given choice.

## Filters

You can use filters to control what kind of files the dialog should display
to the user. File filters can use:

- MIME types
- patterns matching the file name
- suffixes for matching file extensions

## Useful methods for the component

- When saving files, you can use the `set_current_name()` method to suggest
  a file name to the user.
- In order to select multiple files to open, you can use the
  `set_select_multiple()` method, and then call `get_files()` instead of
  `get_file()` to retrieve the list of all selected files as a list model.

## API references

In the examples we used the following classes:

- [GtkFileChooserNative](https://docs.gtk.org/gtk4/class.FileChooserNative.html)
- [GtkNativeDialog](https://docs.gtk.org/gtk4/class.NativeDialog.html)
- [GtkFileChooser](https://docs.gtk.org/gtk4/iface.FileChooser.html)
- [GtkFileFilter](https://docs.gtk.org/gtk4/class.FileFilter.html)
