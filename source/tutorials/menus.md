# Menus

In order to create [menus](https://developer.gnome.org/hig/patterns/controls/menus.html) in GTK, you
have to describe the menu structure using the `GMenu` API; each menu item is
bound to a {doc}`GAction <actions>`.

It is possible to construct a menu model manually, using the GMenu APIs
directly. This is a somewhat painful:

```{eval-rst}
.. tabs::

   .. code-tab:: c

      GMenu *menu = g_menu_new ();

      // The "Offensive Spells" section
      GMenu *section = g_menu_new ();

      // g_menu_append() creates a menu item for you
      g_menu_append (section, "Incendio", "app.incendio");

      g_menu_append_section (menu, "Offensive Spells", section);
      g_object_unref (section);

      // The "Defensive Charms" section
      section = g_menu_new ();

      // An explicit menu item
      GMenuItem *item = g_menu_item_new ("Expelliarmus", "app.expelliarmus");

      // "defensive_icon" is a GIcon and is defined elsewhere
      g_menu_item_set_icon (item, defensive_icon);
      g_menu_append_item (section, item);

      g_menu_append_section (menu, "Defensive Charms", section);
      g_object_unref (section);

   .. code-tab:: python

      menu = Gio.Menu()

      # The "Offensive Spells" section
      section = Gio.Menu()

      # Gio.Menu.append() creates a menu item for you
      section.append("Incendio", "app.incendio")

      menu.append_section("Offensive Spells", section)

      # The "Defensive Charms" section
      section = Gio.Menu()

      # An explicit menu item
      item = Gio.MenuItem()
      item.set_label("Expelliarmus")
      item.set_detailed_action("app.expelliarmus")

      # "defensive_icon" is a Gio.Icon and is defined elsewhere
      item.set_icon(defensive_icon)
      section.append_item(item)

      menu.append_section("Defensive Charms", section)

   .. code-tab:: js

      const menu = new Gio.Menu();

      // The "Offensive Spells" section
      let section = new Gio.Menu();

      // Gio.Menu.append() creates a menu item for you
      section.append("Incendio", "app.incendio");

      menu.append_section("Offensive Spells", section);

      // The "Defensive Charms" section
      section = new Gio.Menu();

      // An explicit menu item
      const item = new Gio.MenuItem();
      item.set_label("Expelliarmus");
      item.set_detailed_action("app.expelliarmus");

      // "defensive_icon" is a Gio.Icon and is defined elsewhere
      item.set_icon(defensive_icon);
      section.append_item(item);

      menu.append_section("Defensive Charms", section);

   .. code-tab:: vala

      var menu = new Menu ();

      // The "Offensive Spells" section
      var section = new Menu ();

      section.append ("Incendio", "app.incendio");

      menu.append_section ("Offensice Spells", section);

      // The "Defensive Charms" section
      section = new Menu ();

      // an explicit menu item
      var item = new MenuItem () {
        label = "Expelliarmus",
        detailed_action = "app.expelliarmus"
      };

      // "defensive_icon" is a GLib.Icon and is defined elsewhere
      menu.append_section ("Defensive Charms", section);

   .. code-tab:: xml

      <interface>
        <menu id="menu">
          <section>
            <item>
              <attribute name="label" translatable="yes">Incendio</attribute>
              <attribute name="action">app.incendio</attribute>
            </item>
          </section>
          <section>
            <attribute name="label" translatable="yes">Defensive Charms</attribute>
            <item>
              <attribute name="label" translatable="yes">Expelliarmus</attribute>
              <attribute name="action">app.expelliarmus</attribute>
              <attribute name="icon">/usr/share/my-app/poof!.png</attribute>
            </item>
          </section>
        </menu>
      </interface>

```

In your code, you then create the GMenuModel using a GtkBuilder:

```{eval-rst}
.. tabs::

   .. code-tab:: c

      GtkBuilder *builder =
        gtk_builder_new_from_resource ("/my/favourite/spells/menu.ui");

      GMenu *menu =
        G_MENU_MODEL (gtk_builder_get_object ("menu");

   .. code-tab:: python

      builder = Gtk.Builder.new_from_resource("/my/favourite/spells/menu.ui")
      menu = builder.get_object("menu")

   .. code-tab:: js

      const builder = Gtk.Builder.new_from_resource("/my/favourite/spells/menu.ui");
      const menu = builder.get_object("menu");

   .. code-tab:: vala

      var builder = new Gtk.Builder.from_resource ("/my/favourite/spells/menu.ui");
      Menu menu = builder.get_object ("menu");

```

## Primary menus

A common pattern in modern user interfaces is to place a button, often with a
gears icon, in some prominent place (top-right), which will open a menu when
clicked. GTK comes with the :doc\`GtkMenuButton \</tutorials/beginners/menu_button>\`
for this use case:

```{eval-rst}
.. tabs::

   .. code-tab:: c

      GtkBuilder *builder =
        gtk_builder_new_from_resource ("/my/favourite/spells/potions.ui");
      GMenu *menu =
        G_MENU_MODEL (gtk_builder_get_object (builder, "menu"));

      // "menu_button" is defined elsewhere
      gtk_menu_button_set_menu_model (GTK_MENU_BUTTON (menu_button), menu);
      gtk_menu_button_set_primary (GTK_MENU_BUTTON (menu_button), TRUE);

      g_object_unref (builder);

   .. code-tab:: python

      builder = Gtk.Builder.new_from_resource("/my/favourite/spells/potions.ui")
      menu = builder.get_object("menu")

      # "menu_button" is defined elsewhere
      menu_button.set_menu_model(menu)
      menu_button.set_primary(True)

   .. code-tab:: js

      const builder = Gtk.Builder.new_from_resource("/my/favourite/spells/potions.ui");
      const menu = builder.get_object("menu");

      // "menu_button" is defined elsewhere
      menu_button.set_menu_model(menu);
      menu_button.set_primary(true);

   .. code-tab:: vala

      var builder = new Gtk.Builder.from_resource ("/my/favourite/spells/menu.ui");
      Menu menu = builder.get_object ("menu");

      // "menu_button" is defined elsewhere
      menu_button.menu_model = menu;
      menu_button.primary = true;
```

## Menu bars

While uncommon in GNOME applications, it is still possible to create menu bars
by using [GtkPopoverMenuBar](https://docs.gtk.org/gtk4/class.PopoverMenuBar.html).

## Context menus

It is possible to create a 'freestanding' menu from a menu model, using
`gtk_popover_menu_new_from_model()`. This menu can then be used as a context
menu on any widget. The actions you refer to in such a menu can come from the
application or window scopes. You can also introduce a more localized scope,
using `gtk_widget_insert_action_group()`. The actions from such a local scope
can be used in any menu that is attached below this local scope.

## Icons

In order to add an icon to a menu item, you must specify the `icon` attribute
on the items in your menu model; when the menu is constructed, the icon will be
properly placed in the UI. The expected value for this attribute is a serialized
GIcon. Luckily, the GIcon serialization format is convenient for this use—for
instance:

```xml
<attribute name="icon">/path/to/my/icon.png</attribute>
```

is a valid serialization for a [GFileIcon](https://docs.gtk.org/gio/class.FileIcon.html)
for the file at the given path, and:

```xml
<attribute name="icon">preferences-desktop-locale-symbolic</attribute>
```

is a valid serialization for a [GThemedIcon](https://docs.gtk.org/gio/class.ThemedIcon.html)
for the `preferences-desktop-locale-symbolic` symbolic icon.
