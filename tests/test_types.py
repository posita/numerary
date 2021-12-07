# ======================================================================================
# Copyright and other protections apply. Please see the accompanying LICENSE file for
# rights and restrictions governing use of this software. All rights not expressly
# waived or licensed are reserved. If that file is missing or appears to be modified
# from its original, then please contact the author before viewing or using this
# software in any capacity.
# ======================================================================================

from __future__ import annotations

from abc import abstractmethod
from typing import Iterable, Tuple, Union

import pytest

from numerary import IntegralLikeSCU, RealLikeSCU
from numerary.bt import beartype
from numerary.types import CachingProtocolMeta, Protocol, runtime_checkable

__all__ = ()


# ---- Types ---------------------------------------------------------------------------


@runtime_checkable
class SupportsOne(
    Protocol,
    metaclass=CachingProtocolMeta,
):
    __slots__: Union[str, Iterable[str]] = ()

    @abstractmethod
    def one(self) -> int:
        pass


# ---- Classes -------------------------------------------------------------------------


class One:
    def one(self) -> int:
        return 1


class Two:
    def two(self) -> int:
        return 2


# ---- Tests ---------------------------------------------------------------------------


def test_beartype_detection() -> None:
    roar = pytest.importorskip("beartype.roar", reason="requires beartype")

    @beartype
    def _real_like_identity(arg: RealLikeSCU) -> RealLikeSCU:
        return arg

    with pytest.raises(roar.BeartypeException):
        _real_like_identity("-273")  # type: ignore [arg-type]

    @beartype
    def _lies_all_lies(arg: RealLikeSCU) -> Tuple[str]:
        return (arg,)  # type: ignore [return-value]

    with pytest.raises(roar.BeartypeException):
        _lies_all_lies(-273)


def test_beartype_validators() -> None:
    roar = pytest.importorskip("beartype.roar", reason="requires beartype")
    from beartype.vale import Is

    from numerary.types import Annotated

    NonZero = Annotated[IntegralLikeSCU, Is[lambda x: x != 0]]

    @beartype
    def _divide_it(n: IntegralLikeSCU, d: NonZero) -> RealLikeSCU:
        return n / d

    with pytest.raises(roar.BeartypeException):
        _divide_it(0, 0)

    with pytest.raises(roar.BeartypeException):
        _divide_it(0, "1")  # type: ignore [arg-type]

    If = Annotated[
        Tuple[str, ...],
        Is[
            lambda x: x
            == (
                "If you can dream—and not make dreams your master;",
                "If you can think—and not make thoughts your aim;",
            )
        ],
    ]

    @beartype
    def _if(lines: If) -> Tuple[str, ...]:
        return (
            "If you can meet with Triumph and Disaster",
            "And treat those two impostors just the same;",
        )

    with pytest.raises(roar.BeartypeException):
        _if(())


def test_caching_protocol_meta_cache_overrides() -> None:
    one: SupportsOne = One()
    assert isinstance(one, SupportsOne)

    SupportsOne.excludes(One)
    assert not isinstance(one, SupportsOne)

    SupportsOne.reset_for(One)
    assert isinstance(one, SupportsOne)

    two = Two()
    assert not isinstance(two, SupportsOne)

    SupportsOne.includes(Two)
    assert isinstance(two, SupportsOne)

    SupportsOne.reset_for(Two)
    assert not isinstance(two, SupportsOne)