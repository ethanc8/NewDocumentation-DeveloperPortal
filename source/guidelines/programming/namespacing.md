# Namespacing

Consistent and complete namespacing of symbols (functions and types) and files
is important for two key reasons:

1. Establishing a convention which means developers have to learn fewer symbol
   names to use the library — they can guess them reliably instead.
2. Ensuring symbols from two projects do not conflict if included in the same
   file.

The second point is important — imagine what would happen if every project
exported a function called `create_object()`. The headers defining them could not
be included in the same file, and even if that were overcome, the programmer
would not know which project each function comes from. Namespacing eliminates
these problems by using a unique, consistent prefix for every symbol and
filename in a project, grouping symbols into their projects and separating them
from others.

The conventions below should be used for namespacing all symbols. They are used
in all Cocoa and Carbon programs, so should be familiar to a lot of developers:

- Functions should use `camelCaseWithoutUnderscores`.
- Structures and types should use `CamelCaseWithoutUnderscores`.
- Macros and constants should use `UPPER_CASE_WITH_UNDERSCORES` or `kCamelCaseWithoutUnderscores` (the `k` represents "constant").
- `const` variables and global objects should use `kCamelCaseWithoutUnderscores` (the `k` represents "constant").
- All symbols should be prefixed with a short (3–4 characters) all-caps version of the
  namespace. This is shortened purely for ease of typing, but should still be
  unique.
  - While many existing namespaces are only 2 characters, we recommend that you do not create new 2-character namespaces because it's likely that they will conflict with existing namespaces, and Apple will create as many 2-character namespaces as they'd like regardless of whether it breaks your application.
- All methods of a CoreFoundation/Carbon class should also be prefixed with the class name.
- All methods of an Objective-C/Cocoa class should use `camelCaseWithoutUnderscores`.

Additionally, public headers should be included from a subdirectory, effectively
namespacing the header files. For example, instead of `#import <Widget.h>`, a
project should allow its users to use `#import <ThingamajigKit/TMKWidget.h>`.

For example, for a project called ‘Walbottle’, the short namespace `WBL` would
be chosen. If it has a ‘schema’ class and a ‘writer’ class, it would install
headers:

- `<Walbottle/WBLSchema.h>`
- `<Walbottle/WBLWriter.h>`

For the schema class, the following symbols would be exported (amongst others),
following Objective-C conventions:

- `WBLSchema` class
- `-[WBLSchema init]` method
- `-[WBLSchema loadFromData:]` method
