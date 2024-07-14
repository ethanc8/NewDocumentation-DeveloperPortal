# Radio Buttons

% image:: ../../img/tutorials/component.png

Radio buttons are buttons that display a "selected" indicator next to their
label, and belong to a group of similar buttons. Only one radio button in the
group can be selected.

- [Interface guidelines](https://developer.gnome.org/hig/patterns/controls/radio-buttons.html)

GTK uses {doc}`check buttons <check_box>` in a group to enable the "radio"
behavior.

```{eval-rst}
.. tabs::

   .. code-tab:: c

      GtkWidget *live = gtk_check_button_new_with_label ("Live");
      GtkWidget *laugh = gtk_check_button_new_with_label ("Laugh");
      GtkWidget *love = gtk_check_button_new_with_label ("Love");

      gtk_check_button_set_group (GTK_CHECK_BUTTON (laugh),
                                  GTK_CHECK_BUTTON (live));
      gtk_check_button_set_group (GTK_CHECK_BUTTON (love),
                                  GTK_CHECK_BUTTON (live));

   .. code-tab:: python

      live = Gtk.CheckButton(label="Live")
      laugh = Gtk.CheckButton(label="Laugh", group=live)
      love = Gtk.CheckButton(label="Love", group=live)

   .. code-tab:: vala

      var live = new Gtk.CheckButton.with_label ("Live");
      var laugh = new Gtk.CheckButton.with_label ("Laugh");
      var love = new Gtk.CheckButton.with_label ("Love");

      laugh.group = live;
      love.group = live;

   .. code-tab:: js

      const live = new Gtk.CheckButton({ label: "Live" });
      const laugh = new Gtk.CheckButton({ label: "Laugh", group: live });
      const love = new Gtk.CheckButton({ label: "Love", group: live });

   .. code-tab:: xml

      <object class="GtkBox">
        <child>
          <object class="GtkCheckButton" id="live">
            <property name="label">Live</property>
          </object>
        </child>
        <child>
          <object class="GtkCheckButton" id="laugh">
            <property name="label">Laugh</property>
            <property name="group">live</property>
          </object>
        </child>
        <child>
          <object class="GtkCheckButton" id="love">
            <property name="label">Love</property>
            <property name="group">live</property>
          </object>
        </child>
      </object>

```

## Detecting the button that was activated

You can use the "toggled" signal, or you can use the "active" property.

```{eval-rst}
.. tabs::

   .. code-tab:: c

      static void
      on_toggled (GtkCheckButton *button,
                  const char *identifier)
      {
        gboolean is_active = gtk_check_button_get_active (button);

        if (strcmp (identifier, "live") == 0)
          update_live (is_active);   // update_live() is defined elsewhere
        else if (strcmp (identifier, "laugh") == 0)
          update_laugh (is_active);  // update_laugh() is defined elsewhere
        else if (strcmp (identifier, "love") == 0)
          update_love (is_active);   // update_love() is defined elsewhere
      }

      // ...

        // The live, laugh, and love variables are defined like the example above
        g_signal_connect (live, "toggled", G_CALLBACK (on_toggled), "live");
        g_signal_connect (laugh, "toggled", G_CALLBACLK (on_toggled), "laugh");
        g_signal_connect (love, "love", G_CALLBACK (on_toggled), "love");

   .. code-tab:: python

      def on_toggled(button, identifier):
          is_active = button.props.active
          if identifier == "live":
              # update_live() is defined elsewhere
              update_live(is_active)
          elif identifier == "laugh":
              # update_laugh() is defined elsewhere
              update_laugh(is_active)
          elif identifier == "love":
              # update_love() is defined elsewhere
              update_love(is_active)

      # The live, laugh, and love variables are defined like the example above
      live.connect("toggled", on_toggled, "live")
      laugh.connect("toggled", on_toggled, "laugh")
      love.connect("toggled", on_toggled, "love")


```

## Useful methods for the component

- If you want to enable a mnemonic shortcut for your radio button, you can
  use the `new_with_mnemonic()` constructor, or the `set_use_underline()`
  method.

## API references

In the examples we used the following classes:

- [GtkCheckButton](https://docs.gtk.org/gtk4/class.CheckButton.html)
