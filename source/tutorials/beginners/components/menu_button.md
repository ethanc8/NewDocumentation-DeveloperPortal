# Menu Buttons

% image:: ../../img/tutorials/component.png

Menu buttons let you show a menu whenever the user activates the button.

Menus are defined using {doc}`GMenu </tutorials/menus>`, and each item in the
menu will activate an {doc}`action </tutorials/actions>` associated to it.

- [Interface guidelines](https://developer.gnome.org/hig/patterns/controls/menus.html)

```{eval-rst}
.. tabs::

   .. code-tab:: c

      GtkWidget *button = gtk_menu_button_new ();

      gtk_menu_button_set_icon_name (GTK_MENU_BUTTON (button), "open-menu-symbolic");

      // "menu" is defined elsewhere
      gtk_menu_button_set_menu_model (GTK_MENU_BUTTON (button), menu);

   .. code-tab:: python

      # "menu" is defined elsewhere
      button = Gtk.MenuButton(icon_name="open-menu-symbolic", menu_model=menu)

   .. code-tab:: vala

      // "menu" is defined elsewhere
      var button = new Gtk.MenuButton () {
          icon_name = "open-menu-symbolic",
          menu_model = menu
      };

   .. code-tab:: js

      // "menu" is defined elsewhere
      const button = new Gtk.MenuButton({
        icon_name: "open-menu-symbolic",
        menu_model: menu,
      });

   .. code-tab:: xml

      <object class="GtkMenuButton" id="primary-menu-button">
        <property name="icon-name">open-menu-symbolic</property>
        <property name="menu-model">primary_menu_model</property>
      </object>

```

## Useful methods for the component

- By default, a GtkMenuButton will only display a downward arrow icon; you can
  use `set_label()` and `set_icon_name()` to specify a label or an icon,
  respectively.
- If you want to show a more complex button, you can use the `set_child()`
  method with a custom widget.
- If you display a label, an icon, or even a custom widget as the button's
  child, you can still request GtkMenuButton to show an arrow by using the
  `set_always_show_arrow()` method.
- If the menu button should act as the primary menu button for your window,
  and respond to the {kbd}`F10` keyboard shortcut, you can use the
  `set_primary()` method.

## API references

In the examples we used the following classes:

- [GtkMenuButton](https://docs.gtk.org/gtk4/class.MenuButton.html)
- [GMenuModel](https://docs.gtk.org/gio/class.MenuModel.html)
