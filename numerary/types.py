# ======================================================================================
# Copyright and other protections apply. Please see the accompanying LICENSE file for
# rights and restrictions governing use of this software. All rights not expressly
# waived or licensed are reserved. If that file is missing or appears to be modified
# from its original, then please contact the author before viewing or using this
# software in any capacity.
# ======================================================================================

from __future__ import annotations

import logging
import math
import sys
import traceback
from abc import abstractmethod
from decimal import Decimal
from fractions import Fraction
from typing import TYPE_CHECKING, Any, Generic, Optional
from typing import Protocol as _Protocol
from typing import Tuple, Type, TypeVar, Union, overload, runtime_checkable

from beartype.typing import SupportsAbs as _SupportsAbs
from beartype.typing import SupportsComplex as _SupportsComplex
from beartype.typing import SupportsFloat as _SupportsFloat
from beartype.typing import SupportsIndex as _SupportsIndex
from beartype.typing import SupportsInt as _SupportsInt
from beartype.typing import SupportsRound as _SupportsRound

from .bt import beartype
from .protocol import CachingProtocolMeta

if TYPE_CHECKING:
    from typing import Protocol
else:
    from beartype.typing import Protocol


__all__ = (
    "IntegralLike",
    "RealLike",
)

r"""
<!-- BEGIN MONKEY PATCH --

>>> from typing import Any
>>> _: Any

  -- END MONKEY PATCH -->
"""

# ---- Types ---------------------------------------------------------------------------


_T_co = TypeVar("_T_co", covariant=True)


def _assert_isinstance(*num_ts: type, target_t: type) -> None:
    assert issubclass(
        target_t.__class__, CachingProtocolMeta
    ), f"{target_t.__class__} is not subclass of {CachingProtocolMeta}"

    for num_t in num_ts:
        assert isinstance(num_t(0), target_t), f"{num_t!r}, {target_t!r}"


@runtime_checkable
class SupportsAbs(
    _SupportsAbs[_T_co],
    Protocol,
    Generic[_T_co],
    metaclass=CachingProtocolMeta,
):
    r"""
    A derivative of ``beartype.typing.SupportsAbs`` with an override-able cache.
    """


_assert_isinstance(int, float, bool, Decimal, Fraction, target_t=SupportsAbs)


@runtime_checkable
class SupportsComplex(
    _SupportsComplex,
    Protocol,
    metaclass=CachingProtocolMeta,
):
    r"""
    A derivative of ``beartype.typing.SupportsComplex`` with an override-able cache.
    """


_assert_isinstance(Decimal, Fraction, target_t=SupportsComplex)


@runtime_checkable
class SupportsFloat(
    _SupportsFloat,
    Protocol,
    metaclass=CachingProtocolMeta,
):
    r"""
    A derivative of ``beartype.typing.SupportsFloat`` with an override-able cache.
    """


_assert_isinstance(int, float, bool, Decimal, Fraction, target_t=SupportsFloat)


@runtime_checkable
class SupportsInt(
    _SupportsInt,
    Protocol,
    metaclass=CachingProtocolMeta,
):
    r"""
    A derivative of ``beartype.typing.SupportsInt`` with an override-able cache.
    """


_assert_isinstance(int, float, bool, target_t=SupportsInt)


@runtime_checkable
class SupportsIndex(
    _SupportsIndex,
    Protocol,
    metaclass=CachingProtocolMeta,
):
    r"""
    A derivative of ``beartype.typing.SupportsIndex`` with an override-able cache.
    """


_assert_isinstance(int, bool, target_t=SupportsIndex)


@runtime_checkable
class SupportsRound(
    _SupportsRound[_T_co],
    Protocol,
    Generic[_T_co],
    metaclass=CachingProtocolMeta,
):
    r"""
    A derivative of ``beartype.typing.SupportsRound`` with an override-able cache.
    """


_assert_isinstance(int, float, bool, Decimal, Fraction, target_t=SupportsRound)


@runtime_checkable
class _SupportsConjugate(_Protocol):
    r"""
    The non-caching version of
    [``SupportsConjugate``][numerary.types.SupportsConjugate].
    """

    @abstractmethod
    def conjugate(self) -> Any:
        pass


@runtime_checkable
class SupportsConjugate(
    _SupportsConjugate,
    Protocol,
    metaclass=CachingProtocolMeta,
):
    r"""
    A caching ABC defining the [``conjugate``
    method](https://docs.python.org/3/library/numbers.html#numbers.Complex.conjugate).

    ([``_SupportsConjugate``][numerary.types._SupportsConjugate] is the raw, non-caching
    version that defines the actual methods.)

    ``` python
    >>> from typing import TypeVar
    >>> from numerary.types import SupportsConjugate
    >>> MyConjugateT = TypeVar("MyConjugateT", bound=SupportsConjugate)

    >>> def conjugate_my_thing(arg: MyConjugateT) -> MyConjugateT:
    ...   assert isinstance(arg, SupportsConjugate)
    ...   return arg.conjugate()

    >>> conjugate_my_thing(3)
    3

    >>> from decimal import Decimal
    >>> conjugate_my_thing(Decimal(2.5))
    Decimal('2.5')

    >>> import sympy
    >>> conjugate_my_thing(sympy.Float(3.5))
    3.5
    >>> type(_)
    <class 'sympy.core.numbers.Float'>

    >>> # error: Value of type variable "MyConjugateT" of "conjugate_my_thing" cannot be "str"
    >>> conjugate_my_thing("not-a-number")  # type: ignore [type-var]
    Traceback (most recent call last):
      ...
    AssertionError

    ```
    """


_assert_isinstance(
    int, float, bool, complex, Decimal, Fraction, target_t=SupportsConjugate
)


@runtime_checkable
class _SupportsRealImag(_Protocol):
    r"""
    The non-caching version of [``SupportsRealImag``][numerary.types.SupportsRealImag].
    """

    @property
    def real(self) -> Any:
        pass

    @property
    def imag(self) -> Any:
        pass


@runtime_checkable
class SupportsRealImag(
    _SupportsRealImag,
    Protocol,
    metaclass=CachingProtocolMeta,
):
    r"""
    A caching ABC defining the
    [``real``](https://docs.python.org/3/library/numbers.html#numbers.Complex.real) and
    [``imag``](https://docs.python.org/3/library/numbers.html#numbers.Complex.imag)
    properties.

    ([``_SupportsRealImag``][numerary.types._SupportsRealImag] is
    the raw, non-caching version that defines the actual methods.)

    ``` python
    >>> from typing import Any, Tuple, TypeVar
    >>> from numerary.types import SupportsRealImag, real, imag
    >>> MyRealImagT = TypeVar("MyRealImagT", bound=SupportsRealImag)

    >>> def real_imag_my_thing(arg: MyRealImagT) -> Tuple[Any, Any]:
    ...   assert isinstance(arg, SupportsRealImag)
    ...   return (real(arg), imag(arg))

    >>> real_imag_my_thing(3)
    (3, 0)

    >>> from decimal import Decimal
    >>> real_imag_my_thing(Decimal(2.5))
    (Decimal('2.5'), Decimal('0'))

    >>> # error: Value of type variable "MyRealImagT" of "real_imag_my_thing" cannot be "str"
    >>> real_imag_my_thing("not-a-number")  # type: ignore [type-var]
    Traceback (most recent call last):
      ...
    AssertionError

    ```
    """


_assert_isinstance(int, float, bool, Decimal, Fraction, target_t=SupportsRealImag)


@runtime_checkable
class _SupportsRealImagAsMethod(_Protocol):
    r"""
    The non-caching version of
    [``SupportsRealImagAsMethod``][numerary.types.SupportsRealImagAsMethod].
    """

    @abstractmethod
    def as_real_imag(self) -> Tuple[Any, Any]:
        pass


@runtime_checkable
class SupportsRealImagAsMethod(
    _SupportsRealImagAsMethod,
    Protocol,
    metaclass=CachingProtocolMeta,
):
    r"""
    A caching ABC defining the ``#!python as_real_imag`` method that returns a 2-tuple.

    ([``_SupportsRealImagAsMethod``][numerary.types._SupportsRealImagAsMethod]
    is the raw, non-caching version that defines the actual methods.)

    See also the [``real``][numerary.types.real] and [``imag``][numerary.types.imag]
    helper functions.

    ``` python
    >>> from typing import Any, Tuple, TypeVar
    >>> from numerary.types import SupportsRealImagAsMethod, real, imag
    >>> MyRealImagAsMethodT = TypeVar("MyRealImagAsMethodT", bound=SupportsRealImagAsMethod)

    >>> def as_real_imag_my_thing(arg: MyRealImagAsMethodT) -> Tuple[Any, Any]:
    ...   assert isinstance(arg, SupportsRealImagAsMethod)
    ...   return (real(arg), imag(arg))

    >>> as_real_imag_my_thing(sympy.Float(3.5))
    (3.5, 0)
    >>> tuple(type(i) for i in _)
    (<class 'sympy.core.numbers.Float'>, <class 'sympy.core.numbers.Zero'>)

    >>> # error: Value of type variable "MyRealImagAsMethodT" of "as_real_imag_my_thing" cannot be "str"
    >>> as_real_imag_my_thing("not-a-number")  # type: ignore [type-var]
    Traceback (most recent call last):
      ...
    AssertionError

    ```
    """


# See <https://github.com/mkdocstrings/mkdocstrings/issues/333>
SupportsRealImagMixedU = Union[
    SupportsRealImag,
    SupportsRealImagAsMethod,
]
rf"""
{SupportsRealImagMixedU!r}
"""
SupportsRealImagMixedT = (
    SupportsRealImag,
    SupportsRealImagAsMethod,
)
rf"""
{SupportsRealImagMixedT!r}
"""
assert SupportsRealImagMixedU.__args__ == SupportsRealImagMixedT  # type: ignore [attr-defined]


@runtime_checkable
class _SupportsTrunc(_Protocol):
    r"""
    The non-caching version of [``SupportsTrunc``][numerary.types.SupportsTrunc].
    """

    @abstractmethod
    def __trunc__(self) -> int:
        pass


@runtime_checkable
class SupportsTrunc(
    _SupportsTrunc,
    Protocol,
    metaclass=CachingProtocolMeta,
):
    r"""
    A caching ABC defining the [``__trunc__``
    method](https://docs.python.org/3/reference/datamodel.html#object.__trunc__).

    See also the [``__trunc__`` helper function][numerary.types.__trunc__].

    ([``_SupportsTrunc``][numerary.types._SupportsTrunc] is the raw, non-caching version
    that defines the actual methods.)

    ``` python
    >>> from typing import Any, Tuple, TypeVar
    >>> from numerary.types import SupportsTrunc, __trunc__
    >>> MyTruncT = TypeVar("MyTruncT", bound=SupportsTrunc)

    >>> def trunc_my_thing(arg: MyTruncT) -> Tuple[Any, Any]:
    ...   assert isinstance(arg, SupportsTrunc)
    ...   return __trunc__(arg)

    >>> trunc_my_thing(3)
    3

    >>> from decimal import Decimal
    >>> trunc_my_thing(Decimal(2.5))
    2

    >>> import sympy
    >>> trunc_my_thing(sympy.Float(3.5))
    3
    >>> type(_)
    <class 'sympy.core.numbers.Integer'>

    >>> # error: Value of type variable "MyTruncT" of "trunc_my_thing" cannot be "str"
    >>> trunc_my_thing("not-a-number")  # type: ignore [type-var]
    Traceback (most recent call last):
      ...
    AssertionError

    ```
    """


_assert_isinstance(int, bool, float, Decimal, Fraction, target_t=SupportsTrunc)


@runtime_checkable
class _SupportsFloorCeil(_Protocol):
    r"""
    The non-caching version of
    [``SupportsFloorCeil``][numerary.types.SupportsFloorCeil].
    """

    @abstractmethod
    def __floor__(self) -> int:
        pass

    @abstractmethod
    def __ceil__(self) -> int:
        pass


@runtime_checkable
class SupportsFloorCeil(
    _SupportsFloorCeil,
    Protocol,
    metaclass=CachingProtocolMeta,
):
    r"""
    A caching ABC defining the
    [``__floor__``](https://docs.python.org/3/reference/datamodel.html#object.__floor__).
    and
    [``__ceil__``](https://docs.python.org/3/reference/datamodel.html#object.__ceil__)
    methods.

    ([``_SupportsFloorCeil``][numerary.types._SupportsFloorCeil] is the raw, non-caching
    version that defines the actual methods.)

    !!! note

        This is of limited value for Python versions prior to 3.9, since ``#!python
        float.__floor__`` and ``#!python float.__ceil__`` were not defined. If support
        for those environments is important, consider using
        [``SupportsFloat``][numerary.types.SupportsFloat] instead.

        See also the [``__floor__``][numerary.types.__floor__] and
        [``__ceil__``][numerary.types.__ceil__] helper functions.

    ``` python
    >>> from typing import Any, Tuple, TypeVar
    >>> from numerary.types import SupportsFloorCeil, __ceil__, __floor__
    >>> MyFloorCeilT = TypeVar("MyFloorCeilT", bound=SupportsFloorCeil)

    >>> def floor_ceil_my_thing(arg: MyFloorCeilT) -> Tuple[int, int]:
    ...   assert isinstance(arg, SupportsFloorCeil)
    ...   return __floor__(arg), __ceil__(arg)

    >>> floor_ceil_my_thing(3)
    (3, 3)

    >>> from decimal import Decimal
    >>> floor_ceil_my_thing(Decimal(2.5))
    (2, 3)

    >>> import sympy
    >>> floor_ceil_my_thing(sympy.Float(3.5))
    (3, 4)
    >>> tuple(type(i) for i in _)
    (<class 'sympy.core.numbers.Integer'>, <class 'sympy.core.numbers.Integer'>)

    >>> # error: Value of type variable "MyFloorCeilT" of "floor_ceil_my_thing" cannot be "str"
    >>> floor_ceil_my_thing("not-a-number")  # type: ignore [type-var]
    Traceback (most recent call last):
      ...
    AssertionError

    ```
    """


# Prior to Python 3.9, floats didn't have an explicit __floor__ method; it was
# "directly" supported in math.floor, so the pure protocol approach thinks they're not
# supported
if sys.version_info < (3, 9):
    SupportsFloorCeil.includes(float)

_assert_isinstance(int, float, bool, Decimal, Fraction, target_t=SupportsFloorCeil)


@runtime_checkable
class _SupportsDivmod(
    _Protocol,
    Generic[_T_co],
):
    r"""
    The non-caching version of [``SupportsDivmod``][numerary.types.SupportsDivmod].
    """

    @abstractmethod
    def __divmod__(self, other: Any) -> Tuple[_T_co, _T_co]:
        pass

    @abstractmethod
    def __rdivmod__(self, other: Any) -> Tuple[_T_co, _T_co]:
        pass


@runtime_checkable
class SupportsDivmod(
    _SupportsDivmod[_T_co],
    Protocol,
    Generic[_T_co],
    metaclass=CachingProtocolMeta,
):
    r"""
    A caching ABC defining the
    [``__divmod__``](https://docs.python.org/3/reference/datamodel.html#object.__divmod__)
    and
    [``__rdivmod__``](https://docs.python.org/3/reference/datamodel.html#object.__rdivmod__)
    methods. Each returns a 2-tuple of covariants.

    ([``_SupportsDivmod``][numerary.types._SupportsDivmod] is the raw, non-caching
    version that defines the actual methods.)

    ``` python
    >>> from typing import Any, Tuple, TypeVar
    >>> from numerary.types import SupportsDivmod
    >>> MyDivmodT = TypeVar("MyDivmodT", bound=SupportsDivmod)

    >>> def divmod_my_thing(arg: MyDivmodT, other: Any) -> Tuple[MyDivmodT, MyDivmodT]:
    ...   assert isinstance(arg, SupportsDivmod)
    ...   return divmod(arg, other)

    >>> divmod_my_thing(2, 1)
    (2, 0)

    >>> from decimal import Decimal
    >>> divmod_my_thing(Decimal(2.5), Decimal(1.5))
    (Decimal('1'), Decimal('1.0'))

    >>> import sympy
    >>> divmod_my_thing(sympy.Float(3.5), sympy.Float(1.5))
    (2, 0.5)
    >>> tuple(type(i) for i in _)
    (<class 'sympy.core.numbers.Integer'>, <class 'sympy.core.numbers.Float'>)

    >>> # error: Value of type variable "MyDivmodT" of "divmod_my_thing" cannot be "str"
    >>> divmod_my_thing("not-a-number", "still-not-a-number")  # type: ignore [type-var]
    Traceback (most recent call last):
      ...
    AssertionError

    ```
    """


# complex defines these methods, but only to raise exceptions
SupportsDivmod.excludes(complex)
_assert_isinstance(int, bool, float, Decimal, Fraction, target_t=SupportsDivmod)


@runtime_checkable
class _SupportsNumeratorDenominator(_Protocol):
    r"""
    The non-caching version of
    [``SupportsNumeratorDenominator``][numerary.types.SupportsNumeratorDenominator].
    """

    @property
    def numerator(self) -> int:
        pass

    @property
    def denominator(self) -> int:
        pass


@runtime_checkable
class SupportsNumeratorDenominator(
    _SupportsNumeratorDenominator,
    Protocol,
    metaclass=CachingProtocolMeta,
):
    r"""
    A caching ABC defining the
    [``numerator``](https://docs.python.org/3/library/numbers.html#numbers.Rational.numerator)
    and
    [``denominator``](https://docs.python.org/3/library/numbers.html#numbers.Rational.denominator)
    properties.

    ([``_SupportsNumeratorDenominator``][numerary.types._SupportsNumeratorDenominator]
    is the raw, non-caching version that defines the actual properties.)

    ``` python
    >>> from typing import Any, Tuple, TypeVar
    >>> from numerary.types import SupportsNumeratorDenominator, denominator, numerator
    >>> MyNumDenomT = TypeVar("MyNumDenomT", bound=SupportsNumeratorDenominator)

    >>> def num_denom_my_thing(arg: MyNumDenomT) -> Tuple[int, int]:
    ...   assert isinstance(arg, SupportsNumeratorDenominator)
    ...   return numerator(arg), denominator(arg)

    >>> num_denom_my_thing(3)
    (3, 1)

    >>> from fractions import Fraction
    >>> num_denom_my_thing(Fraction(2, 3))
    (2, 3)

    >>> import sympy
    >>> num_denom_my_thing(sympy.Rational(3, 4))
    (3, 4)
    >>> tuple(type(i) for i in _)
    (<class 'int'>, <class 'int'>)

    >>> # error: Value of type variable "MyNumDenomT" of "num_denom_my_thing" cannot be "str"
    >>> num_denom_my_thing("not-a-number")  # type: ignore [type-var]
    Traceback (most recent call last):
      ...
    AssertionError

    ```
    """


_assert_isinstance(int, bool, Fraction, target_t=SupportsNumeratorDenominator)


@runtime_checkable
class _SupportsNumeratorDenominatorMethods(_Protocol):
    r"""
    The non-caching version of
    [``SupportsNumeratorDenominatorMethods``][numerary.types.SupportsNumeratorDenominatorMethods].
    """

    @abstractmethod
    def numerator(self) -> SupportsInt:
        pass

    @abstractmethod
    def denominator(self) -> SupportsInt:
        pass


@runtime_checkable
class SupportsNumeratorDenominatorMethods(
    _SupportsNumeratorDenominatorMethods,
    Protocol,
    metaclass=CachingProtocolMeta,
):
    r"""
    A caching ABC defining ``#!python numerator`` and ``#!python denominator`` methods.
    Each returns a [``SupportsInt``][numerary.types.SupportsInt].

    ([``_SupportsNumeratorDenominatorMethods``][numerary.types._SupportsNumeratorDenominatorMethods]
    is the raw, non-caching version that defines the actual methods.)

    See also the [``numerator``][numerary.types.numerator] and
    [``denominator``][numerary.types.denominator] helper functions.
    """


# See <https://github.com/mkdocstrings/mkdocstrings/issues/333>
SupportsNumeratorDenominatorMixedU = Union[
    SupportsNumeratorDenominator,
    SupportsNumeratorDenominatorMethods,
]
rf"""
{SupportsNumeratorDenominatorMixedU!r}
"""
SupportsNumeratorDenominatorMixedT = (
    SupportsNumeratorDenominator,
    SupportsNumeratorDenominatorMethods,
)
rf"""
{SupportsNumeratorDenominatorMixedT!r}
"""
assert SupportsNumeratorDenominatorMixedU.__args__ == SupportsNumeratorDenominatorMixedT  # type: ignore [attr-defined]


@runtime_checkable
class _SupportsComplexOps(
    _Protocol,
    Generic[_T_co],
):
    r"""
    The non-caching version of
    [``SupportsComplexOps``][numerary.types.SupportsComplexOps].
    """

    @abstractmethod
    def __add__(self, other: Any) -> _T_co:
        pass

    @abstractmethod
    def __radd__(self, other: Any) -> _T_co:
        pass

    @abstractmethod
    def __sub__(self, other: Any) -> _T_co:
        pass

    @abstractmethod
    def __rsub__(self, other: Any) -> _T_co:
        pass

    @abstractmethod
    def __mul__(self, other: Any) -> _T_co:
        pass

    @abstractmethod
    def __rmul__(self, other: Any) -> _T_co:
        pass

    @abstractmethod
    def __truediv__(self, other: Any) -> _T_co:
        pass

    @abstractmethod
    def __rtruediv__(self, other: Any) -> _T_co:
        pass

    @abstractmethod
    def __neg__(self) -> _T_co:
        pass

    @abstractmethod
    def __pos__(self) -> _T_co:
        pass


@runtime_checkable
class SupportsComplexOps(
    _SupportsComplexOps[_T_co],
    Protocol,
    Generic[_T_co],
    metaclass=CachingProtocolMeta,
):
    r"""
    A caching ABC defining the [``Complex`` operator
    methods](https://docs.python.org/3/library/numbers.html#numbers.Complex) with
    covariant return values.

    ([``_SupportsComplexOps``][numerary.types._SupportsComplexOps] is the raw,
    non-caching version that defines the actual methods.)

    ``` python
    >>> from typing import Any, Tuple, TypeVar
    >>> from numerary.types import SupportsComplexOps
    >>> MyComplexOpsT = TypeVar("MyComplexOpsT", bound=SupportsComplexOps)

    >>> def complex_ops_my_thing(arg: MyComplexOpsT) -> MyComplexOpsT:
    ...   assert isinstance(arg, SupportsComplexOps)
    ...   return arg * -2 + 5

    >>> complex_ops_my_thing(3)
    -1

    >>> from decimal import Decimal
    >>> complex_ops_my_thing(Decimal("2.5"))
    Decimal('0.0')

    >>> import sympy
    >>> complex_ops_my_thing(sympy.Float(3.5))
    -2.0
    >>> type(_)
    <class 'sympy.core.numbers.Float'>

    >>> # error: Value of type variable "MyComplexOpsT" of "complex_ops_my_thing" cannot be "str"
    >>> complex_ops_my_thing("not-a-number")  # type: ignore [type-var]
    Traceback (most recent call last):
      ...
    AssertionError

    ```
    """


_assert_isinstance(int, float, bool, Decimal, Fraction, target_t=SupportsComplexOps)


@runtime_checkable
class _SupportsComplexPow(_Protocol):
    r"""
    The non-caching version of
    [``SupportsComplexPow``][numerary.types.SupportsComplexPow].
    """

    @abstractmethod
    def __pow__(self, exponent: Any) -> Any:
        pass

    @abstractmethod
    def __rpow__(self, exponent: Any) -> Any:
        pass


@runtime_checkable
class SupportsComplexPow(
    _SupportsComplexPow,
    Protocol,
    metaclass=CachingProtocolMeta,
):
    r"""
    A caching ABC defining the ``#!python Complex`` (i.e., non-modulo) versions of the
    [``__pow__``](https://docs.python.org/3/reference/datamodel.html#object.__pow__) and
    [``__rpow__``](https://docs.python.org/3/reference/datamodel.html#object.__rpow__).

    ([``_SupportsComplexPow``][numerary.types._SupportsComplexPow] is the raw,
    non-caching version that defines the actual methods.)

    ``` python
    >>> from typing import Any, Tuple, TypeVar
    >>> from numerary.types import SupportsComplexPow
    >>> MyComplexPowT = TypeVar("MyComplexPowT", bound=SupportsComplexPow)

    >>> def complex_pow_my_thing(arg: MyComplexPowT) -> MyComplexPowT:
    ...   assert isinstance(arg, SupportsComplexPow)
    ...   return arg ** -2

    >>> complex_pow_my_thing(3)
    0.1111111111111111

    >>> from decimal import Decimal
    >>> complex_pow_my_thing(Decimal("2.5"))
    Decimal('0.16')

    >>> import sympy
    >>> complex_pow_my_thing(sympy.Float(3.5))
    0.0816326530612245
    >>> type(_)
    <class 'sympy.core.numbers.Float'>

    >>> # error: Value of type variable "MyComplexPowT" of "complex_pow_my_thing" cannot be "str"
    >>> complex_pow_my_thing("not-a-number")  # type: ignore [type-var]
    Traceback (most recent call last):
      ...
    AssertionError

    ```
    """


_assert_isinstance(int, float, bool, Decimal, Fraction, target_t=SupportsComplexPow)


@runtime_checkable
class _SupportsRealOps(
    _Protocol,
    Generic[_T_co],
):
    r"""
    The non-caching version of [``SupportsRealOps``][numerary.types.SupportsRealOps].
    """

    @abstractmethod
    def __lt__(self, other: Any) -> bool:
        pass

    @abstractmethod
    def __le__(self, other: Any) -> bool:
        pass

    @abstractmethod
    def __ge__(self, other: Any) -> bool:
        pass

    @abstractmethod
    def __gt__(self, other: Any) -> bool:
        pass

    @abstractmethod
    def __floordiv__(self, other: Any) -> Any:  # TODO(posita): should be int
        pass

    @abstractmethod
    def __rfloordiv__(self, other: Any) -> Any:  # TODO(posita): should be int
        pass

    @abstractmethod
    def __mod__(self, other: Any) -> _T_co:
        pass

    @abstractmethod
    def __rmod__(self, other: Any) -> _T_co:
        pass


@runtime_checkable
class SupportsRealOps(
    _SupportsRealOps[_T_co],
    Protocol,
    Generic[_T_co],
    metaclass=CachingProtocolMeta,
):
    r"""
    A caching ABC defining the [``Real`` operator
    methods](https://docs.python.org/3/library/numbers.html#numbers.Real) with covariant
    return values.

    ([``_SupportsRealOps``][numerary.types._SupportsRealOps] is the raw, non-caching
    version that defines the actual methods.)

    ``` python
    >>> from typing import Any, Tuple, TypeVar
    >>> from numerary.types import SupportsRealOps
    >>> MyRealOpsT = TypeVar("MyRealOpsT", bound=SupportsRealOps)

    >>> def real_ops_my_thing(arg: MyRealOpsT) -> Any:
    ...   assert isinstance(arg, SupportsRealOps)
    ...   return arg // -2

    >>> real_ops_my_thing(3)
    -2

    >>> from decimal import Decimal
    >>> real_ops_my_thing(Decimal("2.5"))
    Decimal('-1')

    >>> import sympy
    >>> real_ops_my_thing(sympy.Float(3.5))
    -2
    >>> type(_)
    <class 'sympy.core.numbers.Integer'>

    >>> # error: Value of type variable "MyRealOpsT" of "real_ops_my_thing" cannot be "str"
    >>> real_ops_my_thing("not-a-number")  # type: ignore [type-var]
    Traceback (most recent call last):
      ...
    AssertionError

    ```
    """


# complex defines these methods, but only to raise exceptions
SupportsRealOps.excludes(complex)
_assert_isinstance(int, float, bool, Decimal, Fraction, target_t=SupportsRealOps)


@runtime_checkable
class _SupportsIntegralOps(
    _Protocol,
    Generic[_T_co],
):
    r"""
    The non-caching version of
    [``SupportsIntegralOps``][numerary.types.SupportsIntegralOps].
    """

    @abstractmethod
    def __lshift__(self, other: Any) -> _T_co:
        pass

    @abstractmethod
    def __rlshift__(self, other: Any) -> _T_co:
        pass

    @abstractmethod
    def __rshift__(self, other: Any) -> _T_co:
        pass

    @abstractmethod
    def __rrshift__(self, other: Any) -> _T_co:
        pass

    @abstractmethod
    def __and__(self, other: Any) -> _T_co:
        pass

    @abstractmethod
    def __rand__(self, other: Any) -> _T_co:
        pass

    @abstractmethod
    def __xor__(self, other: Any) -> _T_co:
        pass

    @abstractmethod
    def __rxor__(self, other: Any) -> _T_co:
        pass

    @abstractmethod
    def __or__(self, other: Any) -> _T_co:
        pass

    @abstractmethod
    def __ror__(self, other: Any) -> _T_co:
        pass

    @abstractmethod
    def __invert__(self) -> _T_co:
        pass


@runtime_checkable
class SupportsIntegralOps(
    _SupportsIntegralOps[_T_co],
    Protocol,
    Generic[_T_co],
    metaclass=CachingProtocolMeta,
):
    r"""
    A caching ABC defining the [``Integral`` operator
    methods](https://docs.python.org/3/library/numbers.html#numbers.Integral) with
    covariant return values.

    ([``_SupportsIntegralOps``][numerary.types._SupportsIntegralOps] is the raw,
    non-caching version that defines the actual methods.)

    ``` python
    >>> from typing import Any, Tuple, TypeVar
    >>> from numerary.types import SupportsIntegralOps
    >>> MyIntegralOpsT = TypeVar("MyIntegralOpsT", bound=SupportsIntegralOps)

    >>> def integral_ops_my_thing(arg: MyIntegralOpsT) -> MyIntegralOpsT:
    ...   assert isinstance(arg, SupportsIntegralOps)
    ...   return arg << 1

    >>> integral_ops_my_thing(3)
    6

    >>> import sympy
    >>> integral_ops_my_thing(sympy.Integer(3))
    6
    >>> type(_)
    <class 'sympy.core.numbers.Integer'>

    >>> # error: Value of type variable "MyIntegralOpsT" of "integral_ops_my_thing" cannot be "str"
    >>> integral_ops_my_thing("not-a-number")  # type: ignore [type-var]
    Traceback (most recent call last):
      ...
    AssertionError

    ```
    """


_assert_isinstance(int, bool, target_t=SupportsIntegralOps)


@runtime_checkable
class _SupportsIntegralPow(_Protocol):
    r"""
    The non-caching version of
    [``SupportsIntegralPow``][numerary.types.SupportsIntegralPow].
    """

    @abstractmethod
    def __pow__(self, exponent: Any, modulus: Optional[Any] = None) -> Any:
        pass

    @abstractmethod
    def __rpow__(self, exponent: Any, modulus: Optional[Any] = None) -> Any:
        pass


@runtime_checkable
class SupportsIntegralPow(
    _SupportsIntegralPow,
    Protocol,
    metaclass=CachingProtocolMeta,
):
    r"""
    A caching ABC defining the ``#!python Integral`` (i.e., modulo) versions of the
    [``__pow__``](https://docs.python.org/3/reference/datamodel.html#object.__pow__) and
    [``__rpow__``](https://docs.python.org/3/reference/datamodel.html#object.__rpow__)
    methods.

    ([``_SupportsIntegralPow``][numerary.types._SupportsIntegralPow] is the raw,
    non-caching version that defines the actual methods.)

    ``` python
    >>> from typing import Any, Tuple, TypeVar
    >>> from numerary.types import SupportsIntegralPow
    >>> MyIntegralPowT = TypeVar("MyIntegralPowT", bound=SupportsIntegralPow)

    >>> def integral_pow_my_thing(arg: MyIntegralPowT) -> MyIntegralPowT:
    ...   assert isinstance(arg, SupportsIntegralPow)
    ...   return pow(arg, 2, 2)

    >>> integral_pow_my_thing(3)
    1

    >>> import sympy
    >>> integral_pow_my_thing(sympy.Integer(3))
    1
    >>> type(_)
    <class 'int'>

    >>> # error: Value of type variable "MyIntegralPowT" of "integral_pow_my_thing" cannot be "str"
    >>> integral_pow_my_thing("not-a-number")  # type: ignore [type-var]
    Traceback (most recent call last):
      ...
    AssertionError

    ```
    """


_assert_isinstance(int, bool, target_t=SupportsIntegralPow)


@runtime_checkable
class RealLike(
    SupportsAbs[_T_co],
    SupportsFloat,
    SupportsRealOps[_T_co],
    SupportsComplexOps[_T_co],
    SupportsComplexPow,
    Protocol,
    Generic[_T_co],
    metaclass=CachingProtocolMeta,
):
    r"""
    A caching ABC that defines a core set of operations for interacting with reals. It
    is a composition of:

    * [``SupportsAbs``][numerary.types.SupportsAbs]
    * [``SupportsFloat``][numerary.types.SupportsFloat]
    * [``SupportsRealOps``][numerary.types.SupportsRealOps]
    * [``SupportsComplexOps``][numerary.types.SupportsComplexOps]
    * [``SupportsComplexPow``][numerary.types.SupportsComplexPow]
    * a ``__hash__`` method

    Basically:

    ``` python
    from typing import TypeVar, runtime_checkable
    from beartype.typing import Protocol
    from numerary.types import CachingProtocolMeta, Supports…
    T_co = TypeVar("T_co", covariant=True)

    @runtime_checkable
    class RealLike(
      SupportsAbs[T_co],
      SupportsFloat,
      SupportsRealOps[T_co],
      SupportsComplexOps[T_co],
      SupportsComplexPow[T_co],
      Protocol[T_co],
      metaclass=CachingProtocolMeta,
    ):
      @abstractmethod
      def __hash__(self) -> int:
        pass
    ```

    This is intended as a practically useful, but incomplete list. To enforce
    equivalence to ``#!python numbers.Real``, one would also need:

    * [``SupportsComplex``][numerary.types.SupportsComplex]
    * [``SupportsConjugate``][numerary.types.SupportsConjugate]
    * [``SupportsRealImag``][numerary.types.SupportsRealImag]
    * [``SupportsRound``][numerary.types.SupportsRound]
    * [``SupportsTrunc``][numerary.types.SupportsTrunc]
    * [``SupportsFloorCeil``][numerary.types.SupportsFloorCeil]
    * [``SupportsDivmod``][numerary.types.SupportsDivmod]
    """

    # Must be able to instantiate it
    @abstractmethod
    def __init__(self, *args: Any, **kw: Any):
        pass

    @abstractmethod
    def __hash__(self) -> int:
        pass


_assert_isinstance(int, float, bool, Decimal, Fraction, target_t=RealLike)


@runtime_checkable
class RationalLike(
    SupportsAbs[_T_co],
    SupportsFloat,
    SupportsNumeratorDenominator,
    SupportsRealOps[_T_co],
    SupportsComplexOps[_T_co],
    SupportsComplexPow,
    Protocol,
    Generic[_T_co],
    metaclass=CachingProtocolMeta,
):
    r"""
    A caching ABC that defines a core set of operations for interacting with rationals.
    It is a composition of:

    * [``SupportsAbs``][numerary.types.SupportsAbs]
    * [``SupportsFloat``][numerary.types.SupportsFloat]
    * [``SupportsNumeratorDenominator``][numerary.types.SupportsNumeratorDenominator]
    * [``SupportsRealOps``][numerary.types.SupportsRealOps]
    * [``SupportsComplexOps``][numerary.types.SupportsComplexOps]
    * [``SupportsComplexPow``][numerary.types.SupportsComplexPow]
    * a ``__hash__`` method

    Basically:

    ``` python
    from typing TypeVar, runtime_checkable
    from beartype.typing import Protocol
    from numerary.types import CachingProtocolMeta, Supports…
    T_co = TypeVar("T_co", covariant=True)

    @runtime_checkable
    class RationalLike(
      SupportsAbs[T_co],
      SupportsFloat,
      SupportsNumeratorDenominator,
      SupportsRealOps[T_co],
      SupportsComplexOps[T_co],
      SupportsComplexPow[T_co],
      Protocol[T_co],
      metaclass=CachingProtocolMeta,
    ):
      @abstractmethod
      def __hash__(self) -> int:
        pass
    ```

    This is intended as a practically useful, but incomplete list. To enforce
    equivalence to ``#!python numbers.Rational``, one would also need:

    * [``SupportsComplex``][numerary.types.SupportsComplex]
    * [``SupportsConjugate``][numerary.types.SupportsConjugate]
    * [``SupportsRealImag``][numerary.types.SupportsRealImag]
    * [``SupportsRound``][numerary.types.SupportsRound]
    * [``SupportsTrunc``][numerary.types.SupportsTrunc]
    * [``SupportsFloorCeil``][numerary.types.SupportsFloorCeil]
    * [``SupportsDivmod``][numerary.types.SupportsDivmod]
    """

    # Must be able to instantiate it
    @abstractmethod
    def __init__(self, *args: Any, **kw: Any):
        pass

    @abstractmethod
    def __hash__(self) -> int:
        pass


_assert_isinstance(int, bool, Fraction, target_t=RationalLike)


@runtime_checkable
class RationalLikeMethods(
    SupportsAbs[_T_co],
    SupportsFloat,
    SupportsNumeratorDenominatorMethods,
    SupportsRealOps[_T_co],
    SupportsComplexOps[_T_co],
    SupportsComplexPow,
    Protocol,
    Generic[_T_co],
    metaclass=CachingProtocolMeta,
):
    r"""
    A caching ABC that defines a core set of operations for interacting with rationals.
    It is identical to [``RationalLike``][numerary.types.RationalLike] with one
    important exception. Instead of
    [``SupportsNumeratorDenominator``][numerary.types.SupportsNumeratorDenominator],
    this protocol provides
    [``SupportsNumeratorDenominatorMethods``][numerary.types.SupportsNumeratorDenominatorMethods].

    Basically:

    ``` python
    from typing TypeVar, runtime_checkable
    from beartype.typing import Protocol
    from numerary.types import CachingProtocolMeta, Supports…
    T_co = TypeVar("T_co", covariant=True)

    @runtime_checkable
    class RationalLikeMethods(
      SupportsAbs[T_co],
      SupportsFloat,
      SupportsNumeratorDenominatorMethods,
      SupportsRealOps[T_co],
      SupportsComplexOps[T_co],
      SupportsComplexPow[T_co],
      Protocol[T_co],
      metaclass=CachingProtocolMeta,
    ):
      @abstractmethod
      def __hash__(self) -> int:
        pass
    ```

    This is probably not very useful on its own, but is important to the construction of
    [``RationalLikeMixedU``][numerary.types.RationalLikeMixedU] and
    [``RationalLikeMixedT``][numerary.types.RationalLikeMixedT].

    See also the [``numerator``][numerary.types.numerator] and
    [``denominator``][numerary.types.denominator] helper functions.
    """

    # Must be able to instantiate it
    @abstractmethod
    def __init__(self, *args: Any, **kw: Any):
        pass

    @abstractmethod
    def __hash__(self) -> int:
        pass


# See <https://github.com/mkdocstrings/mkdocstrings/issues/333>
RationalLikeMixedU = Union[RationalLike, RationalLikeMethods]
rf"""
{RationalLikeMixedU!r}
"""
RationalLikeMixedT = (RationalLike, RationalLikeMethods)
rf"""
{RationalLikeMixedT!r}
"""
assert RationalLikeMixedU.__args__ == RationalLikeMixedT  # type: ignore [attr-defined]
assert RationalLikeMethods.__doc__
RationalLikeMethods.__doc__ += rf"""

    ``` python
    RationalLikeMixedU = {RationalLikeMixedU!r}
    RationalLikeMixedT = ({", ".join(cls.__name__ for cls in  RationalLikeMixedT)})
    ```
"""


@runtime_checkable
class IntegralLike(
    SupportsAbs[_T_co],
    SupportsFloat,
    SupportsIndex,
    SupportsInt,
    SupportsIntegralOps[_T_co],
    SupportsIntegralPow,
    SupportsRealOps[_T_co],
    SupportsComplexOps[_T_co],
    Protocol,
    Generic[_T_co],
    metaclass=CachingProtocolMeta,
):
    r"""
    A caching ABC that defines a core set of operations for interacting with integrals.
    It is a composition of:

    * [``SupportsAbs``][numerary.types.SupportsAbs]
    * [``SupportsFloat``][numerary.types.SupportsFloat]
    * [``SupportsIndex``][numerary.types.SupportsIndex]
    * [``SupportsInt``][numerary.types.SupportsInt]
    * [``SupportsIntegralOps``][numerary.types.SupportsIntegralOps]
    * [``SupportsIntegralPow``][numerary.types.SupportsIntegralPow]
    * [``SupportsRealOps``][numerary.types.SupportsRealOps]
    * [``SupportsComplexOps``][numerary.types.SupportsComplexOps]
    * a ``__hash__`` method

    Basically:

    ``` python
    from typing TypeVar, runtime_checkable
    from beartype.typing import Protocol
    from numerary.types import CachingProtocolMeta, Supports…
    T_co = TypeVar("T_co", covariant=True)

    @runtime_checkable
    class IntegralLike(
      SupportsAbs[T_co],
      SupportsFloat,
      SupportsIndex,
      SupportsInt,
      SupportsIntegralOps[T_co],
      SupportsIntegralPow[T_co],
      SupportsRealOps[T_co],
      SupportsComplexOps[T_co],
      Protocol[T_co],
      metaclass=CachingProtocolMeta,
    ):
      @abstractmethod
      def __hash__(self) -> int:
        pass
    ```

    This is intended as a practically useful, but incomplete list. To enforce
    equivalence to ``#!python numbers.Integral``, one would also need:

    * [``SupportsComplex``][numerary.types.SupportsComplex]
    * [``SupportsConjugate``][numerary.types.SupportsConjugate]
    * [``SupportsRealImag``][numerary.types.SupportsRealImag]
    * [``SupportsRound``][numerary.types.SupportsRound]
    * [``SupportsTrunc``][numerary.types.SupportsTrunc]
    * [``SupportsFloorCeil``][numerary.types.SupportsFloorCeil]
    * [``SupportsDivmod``][numerary.types.SupportsDivmod]
    * [``SupportsNumeratorDenominator``][numerary.types.SupportsNumeratorDenominator]
    """

    # Must be able to instantiate it
    @abstractmethod
    def __init__(self, *args: Any, **kw: Any):
        pass

    @abstractmethod
    def __hash__(self) -> int:
        pass


_assert_isinstance(int, bool, target_t=IntegralLike)


# ---- Functions -----------------------------------------------------------------------


@beartype
def real(operand: SupportsRealImagMixedU):
    r"""
    Helper function that extracts the real part from *operand* including resolving
    non-compliant implementations that implement such extraction via a ``as_real_imag``
    method rather than as properties.

    ``` python
    >>> import sympy
    >>> from numerary.types import real
    >>> real(sympy.Float(3.5))
    3.5

    ```

    See
    [SupportsRealImag][numerary.types.SupportsRealImag]
    and
    [SupportsRealImagAsMethod][numerary.types.SupportsRealImagAsMethod].
    """
    if callable(getattr(operand, "as_real_imag", None)):
        real_part, _ = operand.as_real_imag()  # type: ignore [union-attr]

        return real_part
    elif hasattr(operand, "real"):
        return operand.real  # type: ignore [union-attr]
    else:
        raise TypeError(f"{operand!r} has no real or as_real_imag")


@beartype
def imag(operand: SupportsRealImagMixedU):
    r"""
    Helper function that extracts the imaginary part from *operand* including resolving
    non-compliant implementations that implement such extraction via a ``as_real_imag``
    method rather than as properties.

    ``` python
    >>> import sympy
    >>> from numerary.types import real
    >>> imag(sympy.Float(3.5))
    0

    ```

    See
    [SupportsRealImag][numerary.types.SupportsRealImag]
    and
    [SupportsRealImagAsMethod][numerary.types.SupportsRealImagAsMethod].
    """
    if callable(getattr(operand, "as_real_imag", None)):
        _, imag_part = operand.as_real_imag()  # type: ignore [union-attr]

        return imag_part
    elif hasattr(operand, "imag"):
        return operand.imag  # type: ignore [union-attr]
    else:
        raise TypeError(f"{operand!r} has no real or as_real_imag")


# TODO(posita): Are these sufficient? Could these be more specific? See:
# <https://github.com/python/typeshed/issues/6303#issuecomment-969392257>.
@overload
def __pow__(arg: Union[SupportsComplexPow, SupportsIntegralPow], exponent: Any) -> Any:
    ...


@overload
def __pow__(
    arg: Union[SupportsComplexPow, SupportsIntegralPow], exponent: Any, modulus: None
) -> Any:
    ...


@overload
def __pow__(arg: SupportsIntegralPow, exponent: Any, modulus: Any) -> Any:
    ...


@beartype
def __pow__(
    arg: Union[SupportsComplexPow, SupportsIntegralPow],
    exponent: Any,
    modulus: Optional[Any] = None,
) -> Any:
    r"""
    Helper function that wraps ``pow`` to work with
    [``SupportsComplexPow``][numerary.types.SupportsComplexPow],
    [``SupportsIntegralPow``][numerary.types.SupportsIntegralPow].

    ``` python
    >>> from numerary.types import SupportsComplexPow, SupportsIntegralPow, __pow__
    >>> my_complex_pow: SupportsComplexPow = complex(2)
    >>> __pow__(my_complex_pow, 1)
    (2+0j)
    >>> __pow__(my_complex_pow, 1, None)
    (2+0j)
    >>> __pow__(my_complex_pow, 1, 1)  # type: ignore [operator]  # properly caught by Mypy
    Traceback (most recent call last):
      ...
    ValueError: complex modulo

    >>> my_complex_pow = 1.2
    >>> __pow__(my_complex_pow, 1)
    1.2
    >>> __pow__(my_complex_pow, 1, None)
    1.2
    >>> __pow__(my_complex_pow, 1, 1)  # ugh; *not* caught by Mypy because it treats floats as equivalent to ints?
    Traceback (most recent call last):
      ...
    TypeError: pow() 3rd argument not allowed unless all arguments are integers
    >>> from fractions import Fraction

    >>> my_complex_pow = Fraction(1, 2)
    >>> __pow__(my_complex_pow, 1)
    Fraction(1, 2)
    >>> __pow__(my_complex_pow, 1, None)
    Fraction(1, 2)
    >>> __pow__(my_complex_pow, 1, 1)  # type: ignore [operator]  # properly caught by Mypy
    Traceback (most recent call last):
      ...
    TypeError: __pow__() takes 2 positional arguments but 3 were given

    >>> from decimal import Decimal
    >>> my_integral_pow: SupportsIntegralPow = Decimal("2")
    >>> __pow__(my_integral_pow, 1)
    Decimal('2')
    >>> __pow__(my_integral_pow, 1, None)
    Decimal('2')
    >>> __pow__(my_integral_pow, 1, 2)
    Decimal('0')

    >>> my_integral_pow = Decimal("1.2")  # ruh-roh
    >>> __pow__(my_integral_pow, 1)
    Decimal('1.2')
    >>> __pow__(my_integral_pow, 1, None)
    Decimal('1.2')
    >>> __pow__(my_integral_pow, 1, 2)  # not catchable by Mypy, since it works *some* of the time
    Traceback (most recent call last):
      ...
    decimal.InvalidOperation: [<class 'decimal.InvalidOperation'>]

    >>> my_integral_pow = 2
    >>> __pow__(my_integral_pow, 1)
    2
    >>> __pow__(my_integral_pow, 1, None)
    2
    >>> __pow__(my_integral_pow, 1, 2)
    0

    ```
    """
    return pow(arg, exponent, modulus)


@beartype
def __trunc__(operand: Union[SupportsFloat, SupportsTrunc]):
    r"""
    Helper function that wraps ``math.trunc``.

    ``` python
    >>> from numerary.types import SupportsFloat, SupportsTrunc, __trunc__
    >>> my_trunc: SupportsTrunc
    >>> my_trunc = 1
    >>> __trunc__(my_trunc)
    1
    >>> from fractions import Fraction
    >>> my_trunc = Fraction(1, 2)
    >>> __trunc__(my_trunc)
    0
    >>> my_trunc_float: SupportsFloat = 1.2
    >>> __trunc__(my_trunc_float)
    1

    ```
    """
    return math.trunc(operand)  # type: ignore [arg-type]


@beartype
def __floor__(operand: Union[SupportsFloat, SupportsFloorCeil]):
    r"""
    Helper function that wraps ``math.floor``.

    ``` python
    >>> from numerary.types import SupportsFloat, SupportsFloorCeil, __floor__
    >>> my_floor: SupportsFloorCeil
    >>> my_floor = 1
    >>> __floor__(my_floor)
    1
    >>> from fractions import Fraction
    >>> my_floor = Fraction(1, 2)
    >>> __floor__(my_floor)
    0
    >>> my_floor_float: SupportsFloat = 1.2
    >>> __floor__(my_floor_float)
    1

    ```
    """
    return math.floor(operand)  # type: ignore [arg-type]


@beartype
def __ceil__(operand: Union[SupportsFloat, SupportsFloorCeil]):
    r"""
    Helper function that wraps ``math.ceil``.

    ``` python
    >>> from numerary.types import SupportsFloat, SupportsFloorCeil, __ceil__
    >>> my_ceil: SupportsFloorCeil
    >>> my_ceil = 1
    >>> __ceil__(my_ceil)
    1
    >>> from fractions import Fraction
    >>> my_ceil = Fraction(1, 2)
    >>> __ceil__(my_ceil)
    1
    >>> my_ceil_float: SupportsFloat = 1.2
    >>> __ceil__(my_ceil_float)
    2

    ```
    """
    return math.ceil(operand)  # type: ignore [arg-type]


@beartype
def numerator(operand: SupportsNumeratorDenominatorMixedU):
    r"""
    Helper function that extracts the numerator from *operand* including resolving
    non-compliant rational implementations that implement ``numerator`` as a method
    rather than a property.

    ``` python
    >>> from fractions import Fraction
    >>> from numerary.types import numerator
    >>> numerator(Fraction(22, 7))
    22

    ```

    See
    [SupportsNumeratorDenominator][numerary.types.SupportsNumeratorDenominator]
    and
    [SupportsNumeratorDenominatorMethods][numerary.types.SupportsNumeratorDenominatorMethods].
    """
    if hasattr(operand, "numerator"):
        if callable(operand.numerator):
            return operand.numerator()
        else:
            return operand.numerator
    else:
        raise TypeError(f"{operand!r} has no numerator")


@beartype
def denominator(operand: SupportsNumeratorDenominatorMixedU):
    r"""
    Helper function that extracts the denominator from *operand* including resolving
    non-compliant rational implementations that implement ``denominator`` as a method
    rather than a property.

    ``` python
    >>> from fractions import Fraction
    >>> from numerary.types import denominator
    >>> denominator(Fraction(22, 7))
    7

    ```

    See
    [SupportsNumeratorDenominator][numerary.types.SupportsNumeratorDenominator]
    and
    [SupportsNumeratorDenominatorMethods][numerary.types.SupportsNumeratorDenominatorMethods].
    """
    if hasattr(operand, "denominator"):
        if callable(operand.denominator):
            return operand.denominator()
        else:
            return operand.denominator
    else:
        raise TypeError(f"{operand!r} has no denominator")


# ---- Initialization ------------------------------------------------------------------


try:
    # Register known numpy exceptions
    import numpy
except ImportError:
    pass
except Exception as exc:
    logging.getLogger(__name__).warning(
        f"unexpected error when attempting to load numpy ({exc})"
    )
    logging.getLogger(__name__).debug(traceback.format_exc())
else:
    t: Optional[Type]

    for t_name in (
        "uint8",
        "uint16",
        "uint32",
        "uint64",
        "int8",
        "int16",
        "int32",
        "int64",
    ):
        t = getattr(numpy, t_name, None)

        if t is not None:
            SupportsFloorCeil.includes(t)

    for t_name in (
        "float16",
        "float32",
        "float64",
        "float128",
    ):
        t = getattr(numpy, t_name, None)

        if t is not None:
            SupportsFloorCeil.includes(t)
            SupportsIntegralOps.excludes(t)
            SupportsIntegralPow.excludes(t)

    # numpy complex types define these methods, but only to raise exceptions
    for t_name in (
        "csingle",
        "cdouble",
        "clongdouble",
    ):
        t = getattr(numpy, t_name, None)

        if t is not None:
            SupportsDivmod.excludes(t)
            SupportsRealOps.excludes(t)
            SupportsIntegralOps.excludes(t)
            SupportsIntegralPow.excludes(t)


try:
    # Register known sympy exceptions
    import sympy
except ImportError:
    pass
except Exception as exc:
    logging.getLogger(__name__).warning(
        f"unexpected error when attempting to load sympy ({exc})"
    )
    logging.getLogger(__name__).debug(traceback.format_exc())
else:
    SupportsTrunc.excludes(sympy.Symbol)
    SupportsIntegralOps.excludes(sympy.Symbol)
    SupportsIntegralPow.excludes(sympy.Symbol)
