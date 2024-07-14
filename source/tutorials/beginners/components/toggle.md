# Toggles

% image:: ../../img/tutorials/component.png

A toggle button is a type of button which remains “pressed-in” when clicked.

Clicking it again will cause the toggle button to return to its normal state.

- [Interface guidelines](https://developer.gnome.org/hig/patterns/controls/buttons.html#toggle-buttons)

```{eval-rst}
.. tabs::

   .. code-tab:: c

      static void
      on_toggle (GtkToggleButton *toggle,
                 gpointer user_data)
      {
        if (gtk_toggle_button_get_active (toggle))
          gtk_button_set_label (GTK_BUTTON (toggle), "Goodbye");
        else
          gtk_button_set_label (GTK_BUTTON (toggle), "Hello");
      }

      // ...

      GtkWidget *toggle = gtk_toggle_button_new_with_label ("Hello");

      g_signal_connect (toggle, "toggled", G_CALLBACK (on_toggle), NULL);

   .. code-tab:: python

      def on_toggle (toggle):
          if toggle.props.active:
              toggle.props.label = "Goodbye"
          else:
              toggle.props.label = "Hello"

      # ...

      toggle = Gtk.ToggleButton(label="Hello")
      toggle.connect("toggled", on_toggle)

   .. code-tab:: vala

      var toggle = new Gtk.ToggleButton.with_label ("Hello");
      toggle.toggled.connect (() => {
          if (toggle.active)
              toggle.label = "Goodbye";
          else
              toggle.label = "Hello";
      });

   .. code-tab:: js

      const toggle = new Gtk.ToggleButton({ label: "Hello" });
      toggle.connect("toggled", () => {
        if (toggle.active) {
          toggle.label = "Goodbye";
        } else {
          toggle.label = "Hello";
        }
      });

```

## Programmatic toggling

You can use the `GtkToggleButton:active` property to programmatically change
the state of a toggle button.

```{eval-rst}
.. tabs::

   .. code-tab:: c

      GtkWidget *toggle = gtk_toggle_button_new_with_label ("Hello");

      gtk_toggle_button_set_active (GTK_TOGGLE_BUTTON (toggle), TRUE);

   .. code-tab:: python

      toggle = Gtk.ToggleButton(label="Hello")
      toggle.set_active(True)

   .. code-tab:: vala

      var toggle = new Gtk.ToggleButton.with_label ("Hello") {
          active = true
      };

   .. code-tab:: js

      const toggle = new Gtk.ToggleButton({
        label: "Hello",
        active: true,
      });

```

Changing the `GtkToggleButton:active` property will also emit the
`GtkToggleButton::toggled` signal; if you are programmatically changing
the state of the toggle button and you wish to avoid running your own
signal callback, you should block the handler before calling `set_active()`:

```{eval-rst}
.. tabs::

   .. code-tab:: c
      :emphasize-lines: 2,4

      // "toggle" and "on_toggle" are defined elsewhere
      g_signal_handlers_block_by_func (toggle, on_toggle, NULL);
      gtk_toggle_button_set_active (GTK_TOGGLE_BUTTON (toggle), TRUE);
      g_signal_handlers_unblock_by_func (toggle, on_toggle, NULL);

   .. code-tab:: python

      # "toggle" and "on_toggle" are defined elsewhere
      signal_id, _ = GObject.signal_parse_name("toggled", toggle, True)
      flags = GObject.SignalMatchType.ID | GObject.SignalMatchType.CLOSURE
      def dummy(*args):
          pass

      GObject.signal_handlers_block_matched(toggle,
                                            flags,
                                            signal_id=signal_id, detail=0,
                                            closure=on_toggle,
                                            func=dummy, data=dummy)
      toggle.props.active = True
      GObject.signal_handlers_unblock_matched(toggle, flags,
                                              signal_id=signal_id, detail=0,
                                              closure=on_toggle,
                                              func=dummy, data=dammy)

   .. code-tab:: vala

      // "toggle" and "on_toggle" are defined elsewhere

      SignalHandler.block_by_func (toggle, on_toggle, null);
      toggle.active = true;
      SignalHandler.unblock_by_func (toggle, on_toggle, null);

   .. code-tab:: js

      // "toggle" and "on_toggle" are defined elsewhere

      const [, signal_id] = GObject.signal_parse_name("toggled", toggle, true);
      const match = { signal_id, func: on_toggle };

      GObject.signal_handlers_block_matched(toggle, match);
      toggle.active = true;
      GObject.signal_handlers_unblock_matched(toggle, match);

```

## Grouping buttons

Toggle buttons can be grouped together, to form mutually exclusive groups:
only one of the buttons can be toggled at a time, and toggling another one
will switch the currently toggled one off.

```{eval-rst}
.. tabs::

   .. code-tab:: c

      GtkWidget *live = gtk_toggle_button_new_with_label ("Live");
      GtkWidget *laugh = gtk_toggle_button_new_with_label ("Laugh");
      GtkWidget *love = gtk_toggle_button_new_with_label ("Love");

      gtk_toggle_button_set_group (GTK_TOGGLE_BUTTON (laugh),
                                   GTK_TOGGLE_BUTTON (live));
      gtk_toggle_button_set_group (GTK_TOGGLE_BUTTON (love),
                                   GTK_TOGGLE_BUTTON (live));

   .. code-tab:: python

      live = Gtk.ToggleButton(label="Live")
      laugh = Gtk.ToggleButton(label="Laugh", group=live)
      love = Gtk.ToggleButton(label="Love", group=live)

   .. code-tab:: vala

      var live = new Gtk.ToggleButton.with_label ("Live");
      var laugh = new Gtk.ToggleButton.with_label ("Laugh") { group = live };
      var love = new Gtk.ToggleButton.with_label ("Love") { group = live };

   .. code-tab:: js

      const live = new Gtk.ToggleButton({ label: "Live" });
      const laugh = new Gtk.ToggleButton({ label: "Laugh", group: live });
      const love = new Gtk.ToggleButton({ label: "Love", group: live });

   .. code-tab:: xml

      <object class="GtkToggleButton" id="live">
        <property name="label" translatable="yes">Live</property>
      </object>
      <object class="GtkToggleButton" id="laugh">
        <property name="label" translatable="yes">Laugh</property>
        <property name="group">live</property>
      </object>
      <object class="GtkToggleButton" id="love">
        <property name="label" translatable="yes">Love</property>
        <property name="group">live</property>
      </object>

```

## Useful methods for the component

- If you want to add a mnemonic shortuct to your toggle button, you can
  use the `new_with_mnemonic()` constructor.

## API references

In the examples we used the following classes:

- [GtkToggleButton](https://docs.gtk.org/gtk4/class.ToggleButton.html)
