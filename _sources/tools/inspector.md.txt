# GTK Inspector

The GTK inspector is the built-in interactive debugging support in GTK.

The Inspector is extremely powerful, and allows designers and application
developers to test CSS changes on-the-fly, magnify widgets to see even the
smallest details, and check the structure of the UI and the properties of each
object.

```{image} images/inspector-main-light.png
:align: center
:alt: The main window of the GTK inspector
:class: only-light
```

```{image} images/inspector-main-dark.png
:align: center
:alt: The main window of the GTK inspector
:class: only-dark
```

## Enabling the GTK Inspector

To enable the GTK inspector, you can use the {kbd}`Control` + {kbd}`Shift` + {kbd}`I`
or {kbd}`Control` + {kbd}`Shift` + {kbd}`D` keyboard shortcuts, or set the
`GTK_DEBUG=interactive` environment variable.

There are a few more environment variables that can be set to influence
how the inspector renders its UI. `GTK_INSPECTOR_DISPLAY` and
`GTK_INSPECTOR_RENDERER` determine the GDK display and the GSK
renderer that the inspector is using.

In some situations, it may be inappropriate to give users access to
the GTK inspector. The keyboard shortcuts can be disabled with the
`enable-inspector-keybinding` key in the `org.gtk.Settings.Debug`
GSettings schema.

## Objects

The main entry point of the Inspector is the *Objects* page:

```{image} images/inspector-objects-tree-light.png
:align: center
:alt: The UI scene graph
:class: only-light
```

```{image} images/inspector-objects-tree-dark.png
:align: center
:alt: The UI scene graph
:class: only-dark
```

You can see the structure of the window, with each widget, its siblings and
children, as well as ancillary objects like event controllers and layout
managers.

:::{note}
You can use the target icon to select a widget to inspect with your
pointing device.
:::

Once you select an object, you can inspect its type, state, builder id,
reference count, geometry:

```{image} images/inspector-objects-misc-light.png
:align: center
:alt: The state of a widget
:class: only-light
```

```{image} images/inspector-objects-misc-dark.png
:align: center
:alt: The state of a widget
:class: only-dark
```

The object properties, with the ability to modify their value:

```{image} images/inspector-objects-properties-light.png
:align: center
:alt: The properties of a widget
:class: only-light
```

```{image} images/inspector-objects-properties-dark.png
:align: center
:alt: The properties of a widget
:class: only-dark
```

The CSS properties for a widget, including the CSS selectors hierarchy:

```{image} images/inspector-objects-css-nodes-light.png
:align: center
:alt: The CSS nodes of a widget
:class: only-light
```

```{image} images/inspector-objects-css-nodes-dark.png
:align: center
:alt: The CSS nodes of a widget
:class: only-dark
```

The {doc}`actions </tutorials/actions>` installed by the object:

```{image} images/inspector-objects-actions-light.png
:align: center
:alt: The actions of a widget
:class: only-light
```

```{image} images/inspector-objects-actions-dark.png
:align: center
:alt: The actions of a widget
:class: only-dark
```

The event controllers used by the widget:

```{image} images/inspector-objects-controllers-light.png
:align: center
:alt: The event controllers of a widget
:class: only-light
```

```{image} images/inspector-objects-controllers-dark.png
:align: center
:alt: The event controllers of a widget
:class: only-dark
```

The accessibility role, attributes, and bounds:

```{image} images/inspector-objects-a11y-light.png
:align: center
:alt: The accessibility information of a widget
:class: only-light
```

```{image} images/inspector-objects-a11y-dark.png
:align: center
:alt: The accessibility information of a widget
:class: only-dark
```

You can also zoom the widget, with different levels of magnification, as a
helpful tool to ensure that the rendering is accurate:

```{image} images/inspector-objects-magnifier-light.png
:align: center
:alt: The widget magnifier
:class: only-light
```

```{image} images/inspector-objects-magnifier-dark.png
:align: center
:alt: The widget magnifier
:class: only-dark
```

## Global

The *Global* page contains information related to the version and configuration
of GTK:

```{image} images/inspector-global-light.png
:align: center
:alt: The Global page of the inspector
:class: only-light
```

```{image} images/inspector-global-dark.png
:align: center
:alt: The Global page of the inspector
:class: only-dark
```

You can also find the global state of your application, like its
{doc}`application ID </tutorials/application-id>`, or the resource path for
automatically loading `GResource` bundles.

## CSS

The *CSS* page allows you to load CSS rules, like new classes, and apply them
instantenously. This page is useful for experimenting with styling and
overrides.

```{image} images/inspector-css-light.png
:align: center
:alt: The Global page of the inspector
:class: only-light
```

```{image} images/inspector-css-dark.png
:align: center
:alt: The Global page of the inspector
:class: only-dark
```

## Recorder

The *Recorder* page allows you to record the rendering pipeline of a GTK
application, and inspect the render nodes, their state, and their contents:

```{image} images/inspector-recorder-light.png
:align: center
:alt: The Recorder page of the inspector
:class: only-light
```

```{image} images/inspector-recorder-dark.png
:align: center
:alt: The Recorder page of the inspector
:class: only-dark
```

:::{tip}
The recording can be saved into a file, and used when reporting rendering
bugs to GTK.
:::

## Extra pages

The GTK inspector is extensible through GIO extension points; applications can
register their own inspector pages that GTK will add to the main inspector
window.

### Adwaita

Applications using libadwaita will automatically show an *Adwaita* page with
additional settings and controls:

```{image} images/inspector-adwaita-light.png
:align: center
:alt: The Adwaita page of the inspector
:class: only-light
```

```{image} images/inspector-adwaita-dark.png
:align: center
:alt: The Adwaita page of the inspector
:class: only-dark
```
