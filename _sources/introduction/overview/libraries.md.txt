# Libraries

An overview of GNOME platform libraries.

## User Interfaces

GNOME's user interface libraries are used by all GNOME applications. They
provide everything you need to create a beautiful and easy to use interface for
your app.

### GTK

[GTK](https://www.gtk.org) is GNOME's user interface toolkit, and is a
comprehensive resource for creating application user interfaces. It includes
a wide range of user interface widgets, as well as providing access to an array
of system-level features.

- [GTK4 API reference](https://docs.gtk.org/gtk4/)

### libadwaita

Libadwaita supplements GTK with additional widgets and classes. It is used to
implement the standard GNOME design patterns as documented in the GNOME
Human Interface Guidelines.

- [Libadwaita API reference](https://gnome.pages.gitlab.gnome.org/libadwaita/doc/)

### WebKitGTK

WebKitGTK allows adding web functionality to applications, such as HTML
rendering and embedded web views.

- [WebKitGTK API reference](https://webkitgtk.org/reference/webkit2gtk/stable/index.html)

## Fonts & Rendering

Simple text display and styling is provided by GTK. The GNOME platform also
includes a set of lower-level font rendering and layout libraries, which apps
may sometimes need to use directly for more specialised font and typographic functionality.

### Fontconfig

[Fontconfig](https://www.freedesktop.org/wiki/Software/fontconfig/) provides
access to the fonts that are available on the system. It provides detailed
information about available fonts, as well as the ability to match fonts
according to criteria such as language coverage.

### FreeType

[FreeType](https://www.freetype.org/) is a font rendering library used by
the GNOME platform. Most applications are unlikely to need to use FreeType
directly. However, it can be useful for specialist font and typographic
features.

### HarfBuzz

[HarfBuzz](https://harfbuzz.github.io/) is a text shaping library that is
used by the GNOME platform. Most apps are unlikely to need to use HarfBuzz
directly, unless they include font or typographic features.

### Pango

Pango is a text layout library. It plays an important role in
internationalization, has full Unicode support, and supports a range of writing
systems. Pango APIs are exposed through GTK and can be used for things like
setting text as bold or italic.

- [Pango API reference](https://docs.gtk.org/Pango/)
- [Pango Cairo API reference](https://docs.gtk.org/PangoCairo/)

## Image Loading

### gdk-pixbuf

gdk-pixbuf is an image loading library which is used by GTK. For simple loading
and display of images, GTK can typically used on its own. However, gdk-pixbuf
does provide useful functionality for operating on images as pixel buffers,
such as changing colors or creating composites from multiple images, and saving
the result.

- [gdk-pixbuf API reference](https://docs.gtk.org/gdk-pixbuf/)

### librsvg

librsvg is a library that renders Scalable Vector Graphics (SVG).  It
can be used to display static SVG assets from GTK and gdk-pixbuf, or
to render SVG documents to [Cairo](https://cairographics.org) surfaces in general.

- [librsvg API reference](https://gnome.pages.gitlab.gnome.org/librsvg/Rsvg-2.0/index.html)

### glycin

Glycin allows to decode images into [GdkTextures](https://docs.gtk.org/gdk4/class.Texture.html) and to extract image metadata.
The image decoding happens in sandboxed, modular image loaders.

- [Glycin project page](https://gitlab.gnome.org/sophie-h/glycin)
- [Glycin Rust API reference](https://docs.rs/glycin/latest/glycin/)
- [Glycin C API reference](https://sophie-h.pages.gitlab.gnome.org/glycin/c-api/)

## 2D Drawing: Cairo

Cairo can be used to draw custom 2D graphics. These can be embedded in GTK
user interfaces, by drawing on GTK widgets. Graphics can also be outputted to
PDF and SVG. Cairo graphics are resolution-independent and antialiased.

- [Cairo API reference](https://cairographics.org/manual/)

## File System Access & Operations: GFile

GIO provides a powerful virtual file system abstraction layer. Its GFile
interface can be used to read information from the filesystem (such as
traversing directories, querying file metadata, and so on) as well as and
carrying out file operations. GFile can also be used to monitor files and
directories for changes.

- [GFile API Reference](https://docs.gtk.org/gio/iface.File.html)

## IPC: GDBus

[D-Bus](https://www.freedesktop.org/wiki/Software/dbus/) is one of the
primary IPC systems used in GNOME, and is used for communication between both
applications and services. Applications can use D-Bus to communicate with
system services, such as hardware-related daemons, or for communication between
their own processes.

GDBus is included in the GIO library, and provides a comprehensive
implementation of the D-Bus protocol, as well as high-level API to implement
both providers and consumers of D-Bus interfaces.

## Multimedia: GStreamer

GTK 4 includes its own built-in video playback capability, which can be used
for simple video playback. For other multimedia requirements, GStreamer is an
integrated part of the GNOME platform, and can be used for simple audio
and video playback, through to complex non-linear multimedia editing.

- [GStreamer API reference](https://gstreamer.freedesktop.org/documentation/)

## Settings: GSettings

GSettings is the GNOME library for reading and writing user settings. It
allows storing a variety of settings types, including integers and arrays of
strings.

- [GSettings API reference](https://docs.gtk.org/gio/class.Settings.html)

## Data Storage

The GNOME platform includes a variety of different data storage libraries,
which are suitable for a range of requirements and needs.

### GMarkup

GMarkup is an XML parser which can be used to read/write simple XML. It is
appropriate for data which is read and written by the same app and not shared
between programs.

- [GMarkup API reference](https://docs.gtk.org/glib/struct.MarkupParseContext.html)

### libxml2

Libxml2 is a highly compliant XML parser/generator. It is suited to reading and
writing XML that is shared between different projects, and has a defined
specification and XML schema. Example uses of libxml2 include document rendering
and editing.

- [Libxml2 reference manual](http://www.xmlsoft.org/html/index.html)

### Keyfiles

Key-value files are [INI-like](https://en.wikipedia.org/wiki/INI_file) files
that can be used to store (grouped) key/value pairs. An example of key-value
files are the [desktop files](https://specifications.freedesktop.org/desktop-entry-spec/desktop-entry-spec-latest.html)
used to describe applications.

- [GKeyFile API reference](https://docs.gtk.org/glib/struct.KeyFile.html)

### JSON-GLib

JSON-GLib implements a full JSON parser and generator using GLib and GObject,
and integrates JSON with GLib data types.

- [JSON-GLib API reference](https://gnome.pages.gitlab.gnome.org/json-glib/)

### GDA

libgda is a library which provides access to multiple SQL-based relational
databases, including SQLite, MySQL, Postgres, MSAccess and more. Databases can
either be local or remotely hosted. libgda includes a number of tools,
including a SQL console, a data sources administration tool, and a database
browser.

- [GDA project page](https://gitlab.gnome.org/GNOME/libgda)

### GOM

GOM is a [data mapper](https://en.m.wikipedia.org/wiki/Data_mapper_pattern)
for SQLite. It supports asynchronoous fetching and many-to-many tables, and
helps with building search queries and database migrations.

- [GOM project page](https://gitlab.gnome.org/GNOME/gom)

### Tracker SPARQL

libtracker-sparql allows your app to store, query and publish structured data
using [RDF](https://en.wikipedia.org/wiki/Resource_Description_Framework).
It is based around [SQLite](http://sqlite.org/) with a SPARQL translation
layer that adds many additional features.

- [Tracker SPARQL documentation](https://gnome.pages.gitlab.gnome.org/tracker/docs/developer/index.html)

## Networking

GNOME libraries provide access to a range of networking functionality and
features.

### GSocket

GIO includes high-level network features, such as monitoring the network state
of the system, creating network connections, implementing network services, and
accepting client connections.

GIO also provides a comprehensive set of low level networking APIs to abstract
sockets, addresses, and proxies.

- [GSocket documentation](https://docs.gtk.org/gio/class.Socket.html)

### TLS & DNS support

GIO provides support for [TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security)
connections, both client and server side. It also supports resolvers for
proxies, names and services.

- [TLS Overview](https://docs.gtk.org/gio/tls-overview.html)

### Avahi

[Avahi](http://avahi.org/) implements [Zeroconf Networking](https://en.wikipedia.org/wiki/Zero-configuration_networking).
It allows programs to discover services like printers on local networks without
prior configuration. It also allows applications to set up services that are
reachable through the local network without configuration; for example, a chat
program that "finds" other chat users in a LAN without having to set up a
central chat server first.

### Soup

Soup is an HTTP library designed to be used in graphical applications. It uses
asynchronous operations to avoid blocking the user interface while network
requests are being made.

Soup provides functionality for using HTTP cookies, SSL encrypted connections,
and the XML-RPC protocol based on HTTP.

- [Soup reference manual](https://libsoup.org/libsoup-3.0/index.html)
