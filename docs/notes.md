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

# ``numerary`` release notes

## [0.1.2](https://github.com/posita/numerary/releases/tag/v0.1.2)

* Splits [``SupportsRealImagAsMethod``][numerary.types.SupportsRealImagAsMethod] out of [``SupportsRealImag``][numerary.types.SupportsRealImag] and provides the [``real``][numerary.types.real] and [``imag``][numerary.types.imag] helper functions for better support of ``sympy.core.numbers`` primitives.
* Renames ``SupportsNumeratorDenominatorProperties`` to [``SupportsNumeratorDenominator``][numerary.types.SupportsNumeratorDenominator] to mirror [``SupportsRealImag``][numerary.types.SupportsRealImag] and reflect that it captures the numeric tower interface.
  ``SupportsNumeratorDenominatorProperties`` and ``SupportsNumeratorDenominatorPropertiesSCU`` are maintained as aliases for limited backward compatibility and will be removed in the next version.
* Removes ``enum.Flag`` from testing as a non-sequitur.
  (It matches none of the presented protocols.)
* Introduces [``__pow__``][numerary.types.__pow__] helper function and renames ``trunc``, ``floor``, and ``ceil`` to [``__trunc__``][numerary.types.__trunc__], [``__floor__``][numerary.types.__floor__], and [``__ceil__``][numerary.types.__ceil__], respectively.

## [0.1.1](https://github.com/posita/numerary/releases/tag/v0.1.1)

* Removes obsoleted ``…SCT`` aliases.
* Corrects release notes which erroneously identified version 0.1.0 as 0.0.6.
* Adds ``enum.IntEnum``, ``enum.IntFlag``, and ``enum.Flag`` to testing.
* Merges ``SupportsFloor`` and ``SupportsCeil`` into [``SupportsFloorCeil``][numerary.types.SupportsFloorCeil].
* Gets rid of ``MANIFEST.in`` nonsense since we’re not distributing sources via PyPI anymore.
* Adds a ton of examples to protocol docs.
* Better identifies false positives in tests.

## [0.1.0](https://github.com/posita/numerary/releases/tag/v0.1.0)

* Adds [``CachingProtocolMeta.includes``][numerary.types.CachingProtocolMeta.includes],
  [``CachingProtocolMeta.excludes``][numerary.types.CachingProtocolMeta.excludes], and
  [``CachingProtocolMeta.reset_for``][numerary.types.CachingProtocolMeta.reset_for]
  cache override functions.
* Retires ``…SCT`` tuples as unnecessary, especially in light of cache overrides.
  (Runtime ``isinstance`` protocol checking is fast enough.)
  For limited backward compatibility, they are now merely type aliases for similarly named protocols and will be removed in the next version.
* Updates docs.
* Custom runtime comparison implementation allows composition to lean on base types’ caches.
  (⚠️ WARNING: Severe jank alert! ⚠️)

## [0.0.5](https://github.com/posita/numerary/releases/tag/v0.0.5)

* Updates license to the [MIT License](https://opensource.org/licenses/MIT).
* Gets rid of ``self`` redundancy in ``__isinstance__`` checks.

## [0.0.4](https://github.com/posita/numerary/releases/tag/v0.0.4)

* ``numerary`` *finally* leaves the [``dyce``](https://github.com/posita/dyce/) nest to become its own library!
  It didn’t *quite* leave before because its maintainer is a bonehead who doesn’t understand setuptools’ multitude of oh-so-simple packaging mechanisms.
  No, it stuck around most weekends to do laundry while eating all of ``dyce``’s food.
  *Now* it has *officially* left the nest.