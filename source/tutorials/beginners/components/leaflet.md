# Leaflets

% image:: ../../img/tutorials/component.png

A leaflet is a responsive container that behaves like a {doc}`box <box>` when
there is enough space, or as a {doc}`stack <stack>` if the width available is
not enough.

```xml
<object class="AdwLeaflet" id="leaflet">
  <child>
    <object class="AdwLeafletPage">
      <property name="name">beginning</property>
      <property name="child">
        <!-- ... -->
      </property>
    </object>
  </child>
  <child>
    <object class="AdwLeafletPage">
      <property name="name">end</property>
      <property name="child">
        <!-- ... -->
      </property>
    </object>
  </child>
</object>
```

## API references

In the examples we used the following classes:

- [AdwLeaflet](https://gnome.pages.gitlab.gnome.org/libadwaita/doc/1-latest/class.Leaflet.html)
- [AdwLeafletPage](https://gnome.pages.gitlab.gnome.org/libadwaita/doc/1-latest/class.LeafletPage.html)
