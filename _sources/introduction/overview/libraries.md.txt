# Libraries

An overview of GNUstep platform libraries.

## Foundational libraries

### Objective-C Runtime (`objc`)

The Objective-C Runtime provides dynamic object-oriented features, such as polymorphism, class creation, dynamic message sending, swizzling, and more. It also provides metadata about classes and protocols which are available, which can be useful to language bindings and advanced features.

There are two Objective-C runtimes supported by GNUstep, the GCC runtime and the `libobjc2` runtime (Apple's `objc4` is also supported when running on macOS). `libobjc2` is much better, but requires using Clang as the compiler and is not packaged by most distributions. However, it's extremely easy to install `libobjc2` and the rest of GNUstep from source on any distribution that packages Clang and GNUstep's dependencies (i.e. almost any distribution supporting GNOME, KDE, or another XDG-compliant desktop).

#### GCC runtime

#### `libobjc2`

### GNUstep Base (`Foundation`)

GNUstep Base provides key data types for working in Objective-C, such as strings, dictionaries, and lists. It also provides networking, configuration storage, file manipulation, and more. It is completely compatible with OpenStep's Foundation Kit (except that it serializes objects differently), and has a very high level of compatibility with macOS's Foundation.

- [Base API Reference (for parts which are compatible with Foundation)](https://wwwmain.gnustep.org/resources/documentation/Developer/Base/Reference/index.html)
- [Base Additions API Reference](https://wwwmain.gnustep.org/resources/documentation/Developer/BaseAdditions/Reference/index.html)
- [Base Programming Manual](https://wwwmain.gnustep.org/resources/documentation/Developer/Base/ProgrammingManual/manual_toc.html)

### Core Foundation (`CoreFoundation`)



## User Interfaces

GNUstep's user interface libraries are used by all GNUstep applications. They
provide everything you need to create a beautiful and easy to use interface for
your app.

### GNUstep GUI (`AppKit`)

[GNUstep GUI](https://github.com/gnustep/libs-gui) is GNUstep's user interface toolkit, and is a
comprehensive resource for creating application user interfaces. It includes
a wide range of user interface widgets, as well as providing access to an array
of system-level features. It has a near-perfect level of compatibility with OpenStep's
Application Kit, and has a high level of compatibility with macOS's AppKit, especially for older apps.

- [GUI API reference (for parts which are compatible with AppKit)](https://wwwmain.gnustep.org/resources/documentation/Developer/Gui/Reference/index.html)
- [GUI Additions API reference](https://wwwmain.gnustep.org/resources/documentation/Developer/Gui/Additions/index.html)
- [GUI Programming Manual](https://wwwmain.gnustep.org/resources/documentation/Developer/Gui/ProgrammingManual/AppKit_toc.html)



## Fonts & Rendering

Simple text display and styling is provided by GNUstep GUI. The GNUstep platform also
will include a set of lower-level font rendering and layout libraries, which apps
may sometimes need to use directly for more specialised font and typographic functionality.

### Fonts & Rendering on the XDG platform

% TODO: Verify this

The following libraries are used by GNUstep on the XDG platform (Linux or other Unix-like systems on X11 or Wayland).

#### Fontconfig

[Fontconfig](https://www.freedesktop.org/wiki/Software/fontconfig/) provides
access to the fonts that are available on the system. It provides detailed
information about available fonts, as well as the ability to match fonts
according to criteria such as language coverage.

#### FreeType

[FreeType](https://www.freetype.org/) is a font rendering library used by
the GNUstep platform. Most applications are unlikely to need to use FreeType
directly. However, it can be useful for specialist font and typographic
features.

#### HarfBuzz

[HarfBuzz](https://harfbuzz.github.io/) is a text shaping library that is
used by the GNUstep platform. Most apps are unlikely to need to use HarfBuzz
directly, unless they include font or typographic features.

#### Pango

Pango is a text layout library. It plays an important role in
internationalization, has full Unicode support, and supports a range of writing
systems. Pango APIs are exposed through GTK and can be used for things like
setting text as bold or italic.

- [Pango API reference](https://docs.gtk.org/Pango/)
- [Pango Cairo API reference](https://docs.gtk.org/PangoCairo/)

## 2D Drawing

### Cairo

Cairo can be used to draw custom 2D graphics. These can be embedded in GNUstep
user interfaces <!-- TODO: How? -->. Graphics can also be outputted to
PDF and SVG. Cairo graphics are resolution-independent and antialiased.

- [Cairo API reference](https://cairographics.org/manual/)

### Opal (`CoreGraphics`)

[Opal](https://github.com/gnustep/libs-opal) is GNUstep's wrapper around Cairo, which provides a similar API to macOS's CoreGraphics/Quartz 2D frameworks. It also provides ways to connect Cairo with GNUstep GUI.

## IPC

### Distributed Objects



### DBusKit

[D-Bus](https://www.freedesktop.org/wiki/Software/dbus/) is one of the
primary IPC systems used in GNUstep, and is used for communication between both
applications and services. Applications can use D-Bus to communicate with
system services, such as hardware-related daemons, or for communication between
their own processes.

GDBus is included in the GIO library, and provides a comprehensive
implementation of the D-Bus protocol, as well as high-level API to implement
both providers and consumers of D-Bus interfaces.

## Settings: Defaults

## Data Storage

The GNUstep platform includes a variety of different data storage libraries,
which are suitable for a range of requirements and needs.

### Foundation XML

### Foundation JSON

### GDL2

**TODO: Is this correct?**

[GDL2](https://github.com/gnustep/libs-gdl2) is a library which provides access to multiple SQL-based relational
databases, including SQLite, MySQL, Postgres, MSAccess and more. Databases can
either be local or remotely hosted. libgda includes a number of tools,
including a SQL console, a data sources administration tool, and a database
browser. GDL2's API is similar to NeXT's Enterprise Objects Framework.

- [GDL2 API reference](https://wwwmain.gnustep.org/resources/documentation/Developer/GDL2/GDL2.html)

## GNUstep CoreData (`CoreData`)

## Networking

GNUstep libraries provide access to a range of networking functionality and
features.

### Foundation Networking

### TLS & DNS support

**TODO: Is this correct?**

Foundation provides support for [TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security)
connections, both client and server side. It also supports resolvers for
proxies, names and services.

- [TLS Overview](https://docs.gtk.org/gio/tls-overview.html)
