<!---
  Copyright and other protections apply. Please see the accompanying LICENSE file for
  rights and restrictions governing use of this software. All rights not expressly
  waived or licensed are reserved. If that file is missing or appears to be modified
  from its original, then please contact the author before viewing or using this
  software in any capacity.

  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  !!!!!!!!!!!!!!! IMPORTANT: READ THIS BEFORE EDITING! !!!!!!!!!!!!!!!
  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  Please keep each sentence on its own unwrapped line.
  It looks like crap in a text editor, but it has no effect on rendering, and it allows much more useful diffs.
  Thank you!
-->

# ``#!python numerary.protocol`` package reference

!!! warning "Experimental"

    This package is an attempt to ease compatibility between Python’s numbers and types.
    If that sounds like it shouldn’t be a thing, you won’t get any argument out of me.
    Anyhoo, this package should be considered experimental.
    I am working toward stability as quickly as possible, but be warned that future release may introduce incompatibilities or remove this package altogether.
    [Feedback, suggestions, and contributions](contrib.md) are desperately appreciated.

``numerary`` has donated its core caching protocol implementation to (and now depends on) [``beartype``](https://github.com/beartype/beartype).
``beartype`` is *awesome*, and its author is even *awesomer*.[^1]
``numerary``’s version (in this package) augments that implementation to allow for runtime check overrides.

[^1]:

    I acknowledge that the subject of who is awesomer, beartype or the man who made it, is [hotly contested](https://github.com/beartype/beartype/issues/66#issuecomment-960495976).

::: numerary.protocol
    rendering:
      show_if_no_docstring: false
      show_root_heading: false
      show_root_toc_entry: false
    selection:
      members:
        - "CachingProtocolMeta"
