# Switches

% image:: ../../img/tutorials/switch.png

A switch is a UI control that has two states, On and Off.

The switch widget state is tracked by the `GtkSwitch:active` property.

- [Interface guidelines](https://developer.gnome.org/hig/patterns/controls/switches.html)

## Labelling a switch

A section outlining some functionality

```{eval-rst}
.. tabs::

   .. code-tab:: c

      GtkWidget *box = gtk_box_new (GTK_ORIENTATION_HORIZONTAL, 6);

      GtkWidget *label = gtk_label_new ("Enable awesomeness");
      GtkWidget *sw = gtk_switch_new ();

      gtk_box_append (GTK_BOX (box), label);
      gtk_box_append (GTK_BOX (box), sw);

      // The switch__notify_active() function is defined elsewhere
      g_signal_connect (sw, "notify::active",
                        G_CALLBACK (switch__notify_active),
                        NULL);

   .. code-tab:: python

      box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)

      label = Gtk.Label(text="Enable awesomeness")
      sw = Gtk.Switch()

      box.append(label)
      box.append(sw)

      # The switch__notify_active() method is defined elsewhere
      sw.connect("notify::active", self.switch__notify_active)

   .. code-tab:: vala

      var box = new Gtk.Box (Gtk.Orientation.HORIZONTAL, 6);

      var label = new Gtk.Label ("Enable awesomeness");
      var sw = new Gtk.Switch ();

      box.append (label);
      box.append (sw);

      // The switch__notify_active() method is defined elsewhere
      sw.notify["active"].connect (switch__notify_active);

   .. code-tab:: js

      const box = new Gtk.Box({
        orientation: Gtk.Orientation.HORIZONTAL,
        spacing: 6,
      });

      const label = new Gtk.Label({ label: "Enable awesomeness" });
      const sw = new Gtk.Switch();

      box.append(label);
      box.append(sw);

      // The switch__notify_active() method is defined elsewhere
      sw.connect("notify::active", switch__notify_active);

```

## Useful methods for the component

- Labels with mnemonics should call `set_mnemonic_widget()` to activate
  the switch; see the tutorial for the {doc}`Label <label>` component.
- The `GtkSwitch::state-set` signal can be used to control the state of the
  switch before the `GtkSwitch:active` property is changed.

## API references

In the examples we used the following classes:

- [GtkSwitch](https://docs.gtk.org/gtk4/class.Switch.html)
