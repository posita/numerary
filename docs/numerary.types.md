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

# ``#!python numerary.types`` package reference

!!! warning "Experimental"

    This package is an attempt to ease compatibility between Python’s numbers and types.
    If that sounds like it shouldn’t be a thing, you won’t get any argument out of me.
    Anyhoo, this package should be considered experimental.
    I am working toward stability as quickly as possible, but be warned that future release may introduce incompatibilities or remove this package altogether.
    [Feedback, suggestions, and contributions](contrib.md) are desperately appreciated.

::: numerary.types
    rendering:
      show_if_no_docstring: false
      show_root_heading: false
      show_root_toc_entry: false
    selection:
      members:
        - "RationalLike"
        - "RationalLikeMethods"
        - "SupportsAbs"
        - "SupportsComplex"
        - "SupportsFloat"
        - "SupportsInt"
        - "SupportsIndex"
        - "SupportsRound"
        - "SupportsConjugate"
        - "SupportsRealImag"
        - "SupportsRealImagAsMethod"
        - "SupportsTrunc"
        - "SupportsFloorCeil"
        - "SupportsDivmod"
        - "SupportsNumeratorDenominator"
        - "SupportsNumeratorDenominatorMethods"
        - "SupportsComplexOps"
        - "SupportsComplexPow"
        - "SupportsRealOps"
        - "SupportsIntegralOps"
        - "SupportsIntegralPow"
        - "Protocol"
        - "real"
        - "imag"
        - "__pow__"
        - "__trunc__"
        - "__floor__"
        - "__ceil__"
        - "numerator"
        - "denominator"

<!---
  See <https://github.com/mkdocstrings/mkdocstrings/issues/333>
-->
::: numerary.types
    rendering:
      show_if_no_docstring: true
      show_root_heading: false
      show_root_toc_entry: false
    selection:
      members:
        - "RationalLikeMixedT"
        - "RationalLikeMixedU"
        - "_SupportsAbs"
        - "_SupportsComplex"
        - "_SupportsFloat"
        - "_SupportsInt"
        - "_SupportsIndex"
        - "_SupportsRound"
        - "_SupportsConjugate"
        - "_SupportsRealImag"
        - "_SupportsRealImagAsMethod"
        - "SupportsRealImagMixedT"
        - "SupportsRealImagMixedU"
        - "_SupportsTrunc"
        - "_SupportsFloorCeil"
        - "_SupportsDivmod"
        - "_SupportsNumeratorDenominator"
        - "_SupportsNumeratorDenominatorMethods"
        - "SupportsNumeratorDenominatorMixedT"
        - "SupportsNumeratorDenominatorMixedU"
        - "_SupportsComplexOps"
        - "_SupportsComplexPow"
        - "_SupportsRealOps"
        - "_SupportsIntegralOps"
        - "_SupportsIntegralPow"
