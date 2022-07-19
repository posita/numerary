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

## [0.4.3](https://github.com/posita/numerary/releases/tag/v0.4.3)

* Migrates from [``setuptools_scm``](https://pypi.org/project/setuptools-scm/) to [``versioningit``](https://pypi.org/project/versioningit/) for more flexible version number formatting.
* Adds work-around for [posita/numerary#16](https://github.com/posita/numerary/issues/16).
* Allows deployments to PyPI from CI based on tags.

## [0.4.2](https://github.com/posita/numerary/releases/tag/v0.4.2)

* Fixes issue where ``numpy`` lacks ``float128`` on certain Windows installation.

## [0.4.1](https://github.com/posita/numerary/releases/tag/v0.4.1)

* Minor corrections to required Python version.

## [0.4.0](https://github.com/posita/numerary/releases/tag/v0.4.0)

* Now relies on ``#!python beartype.typing.Protocol`` as the underlying caching protocol implementation.
  This means that ``beartype`` has emerged as ``numerary``’s sole runtime dependency.
  (``numerary`` still layers on its own runtime override mechanism via [CachingProtocolMeta][numerary.protocol.CachingProtocolMeta], which derives from ``beartype``’s.)
  It also means that ``numerary`` loses Python 3.7 support, but that was largely illusory anyway.

  This decision was not made lightly.
  ``numerary`` is intended as a temporary work-around.
  It’s obsolescence will be something to celebrate.
  Caching protocols, however, have much broader performance applications.
  They deserve more.
  ``beartype`` will provide what ``numerary`` was never meant to: a loving, stable, and permanent home.

## [0.3.0](https://github.com/posita/numerary/releases/tag/v0.3.0)

* ~~Removes misleading advice that SCUs offer a performance benefit over merely using caching protocols.
  They *could* under very specific circumstances (where ``numerary`` probably isn’t going to be helpful anyway), but not always, and probably aren’t worth the trouble if performance is the only concern.~~
  Actually, removes SCUs altogether and documents a surgical example for those rare occasions where it might be needed.
* Finally removes ``SupportsNumeratorDenominatorProperties`` as promised.

## [0.2.1](https://github.com/posita/numerary/releases/tag/v0.2.1)

* Fixes trailing issues for `sympy` import issue resulting in `ValueError`s being thrown on import in some environments.

## [0.2.0](https://github.com/posita/numerary/releases/tag/v0.2.0)

* ``numerary`` goes beta!
* Splits [``SupportsRealImagAsMethod``][numerary.types.SupportsRealImagAsMethod] out of [``SupportsRealImag``][numerary.types.SupportsRealImag] and provides the [``real``][numerary.types.real] and [``imag``][numerary.types.imag] helper functions for better support of ``sympy``’s number primitives.
* Renames ``SupportsNumeratorDenominatorProperties`` to [``SupportsNumeratorDenominator``][numerary.types.SupportsNumeratorDenominator] to mirror [``SupportsRealImag``][numerary.types.SupportsRealImag] and reflect that it captures the numeric tower interface.
  ``SupportsNumeratorDenominatorProperties`` and ``SupportsNumeratorDenominatorPropertiesSCU`` are maintained as aliases for limited backward compatibility and will be removed in the next version.
* Removes ``enum.Flag`` from testing as a non-sequitur.
  (It matches none of the presented protocols.)
* Introduces [``__pow__``][numerary.types.__pow__] helper function and renames ``trunc``, ``floor``, and ``ceil`` to [``__trunc__``][numerary.types.__trunc__], [``__floor__``][numerary.types.__floor__], and [``__ceil__``][numerary.types.__ceil__], respectively.
* Fixes `sympy` import issue resulting in `AttributeError`s being thrown on import in some environments.

## [0.1.1](https://github.com/posita/numerary/releases/tag/v0.1.1)

* Removes obsoleted ``…SCT`` aliases.
* Corrects release notes which erroneously identified version 0.1.0 as 0.0.6.
* Adds ``enum.IntEnum``, ``enum.IntFlag``, and ``enum.Flag`` to testing.
* Merges ``SupportsFloor`` and ``SupportsCeil`` into [``SupportsFloorCeil``][numerary.types.SupportsFloorCeil].
* Gets rid of ``MANIFEST.in`` nonsense since we’re not distributing sources via PyPI anymore.
* Adds a ton of examples to protocol docs.
* Better identifies false positives in tests.

## [0.1.0](https://github.com/posita/numerary/releases/tag/v0.1.0)

* Adds [``CachingProtocolMeta.includes``][numerary.protocol.CachingProtocolMeta.includes],
  [``CachingProtocolMeta.excludes``][numerary.protocol.CachingProtocolMeta.excludes], and
  [``CachingProtocolMeta.reset_for``][numerary.protocol.CachingProtocolMeta.reset_for]
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
