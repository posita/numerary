# ======================================================================================
# Copyright and other protections apply. Please see the accompanying LICENSE file for
# rights and restrictions governing use of this software. All rights not expressly
# waived or licensed are reserved. If that file is missing or appears to be modified
# from its original, then please contact the author before viewing or using this
# software in any capacity.
# ======================================================================================

from __future__ import annotations

from collections import defaultdict
from typing import TYPE_CHECKING, Any, Dict, Set, Tuple, Type, TypeVar

from beartype.typing import Protocol as _BeartypeCachingProtocol

__all__ = ("CachingProtocolMeta",)


# ---- Types ---------------------------------------------------------------------------


_T_co = TypeVar("_T_co", covariant=True)
_TT = TypeVar("_TT", bound="CachingProtocolMeta")


if TYPE_CHECKING:
    # Warning: Deep typing voodoo ahead. See
    # <https://github.com/python/mypy/issues/11614>.
    from abc import ABCMeta as _BeartypeCachingProtocolMeta
else:
    _BeartypeCachingProtocolMeta = type(_BeartypeCachingProtocol)


class CachingProtocolMeta(_BeartypeCachingProtocolMeta):
    # TODO(posita): Add more precise link to beartype.typing.Protocol documentation once
    # it becomes available.
    r"""
    An extension of [``#!python
    beartype.typing.Protocol``](https://github.com/beartype/beartype) that allows
    overriding runtime checks.
    """

    _abc_inst_check_cache_overridden: Dict[Type, bool]
    _abc_inst_check_cache_listeners: Set[CachingProtocolMeta]

    # Defined in beartype.typing.Protocol from which we inherit
    _abc_inst_check_cache: Dict[type, bool]

    def __new__(
        mcls: Type[_TT],
        name: str,
        bases: Tuple[Type, ...],
        namespace: Dict[str, Any],
        **kw: Any,
    ) -> _TT:
        cls = super().__new__(mcls, name, bases, namespace, **kw)

        # Prefixing this class member with "_abc_" is necessary to prevent it from being
        # considered part of the Protocol. (See
        # <https://github.com/python/cpython/blob/main/Lib/typing.py>.)
        cls._abc_inst_check_cache_overridden = defaultdict(bool)  # defaults to False
        cls._abc_inst_check_cache_listeners = set()

        for base in bases:
            if hasattr(base, "_abc_inst_check_cache_listeners"):
                base._abc_inst_check_cache_listeners.add(cls)

        return cls

    def includes(cls, inst_t: Type) -> None:
        r"""
        Registers *inst_t* as supporting the interface in the runtime type-checking cache.
        This overrides any prior cached value.

        ``` python
        >>> from abc import abstractmethod
        >>> from numerary.types import CachingProtocolMeta, Protocol, runtime_checkable

        >>> @runtime_checkable
        ... class SupportsSpam(
        ...   Protocol,
        ...   metaclass=CachingProtocolMeta
        ... ):
        ...   @abstractmethod
        ...   def spam(self) -> str:
        ...     pass

        >>> class NoSpam:
        ...   pass

        >>> isinstance(NoSpam(), SupportsSpam)
        False
        >>> SupportsSpam.includes(NoSpam)
        >>> isinstance(NoSpam(), SupportsSpam)
        True

        ```

        !!! note

            This does not affect static type-checking.

            ``` python
            >>> my_spam: SupportsSpam = NoSpam()  # type: ignore [assignment]  # still generates a Mypy warning

            ```
        """
        cls._abc_inst_check_cache[inst_t] = True
        cls._abc_inst_check_cache_overridden[inst_t] = True
        cls._dirty_for(inst_t)

    def excludes(cls, inst_t: Type) -> None:
        r"""
        Registers *inst_t* as supporting the interface in the runtime type-checking cache.
        This overrides any prior cached value.

        ``` python
        >>> from abc import abstractmethod
        >>> from numerary.types import CachingProtocolMeta, Protocol, runtime_checkable

        >>> @runtime_checkable
        ... class SupportsHam(
        ...   Protocol,
        ...   metaclass=CachingProtocolMeta
        ... ):
        ...   @abstractmethod
        ...   def ham(self) -> str:
        ...     pass

        >>> class NoHam:
        ...   def ham(self) -> str:
        ...     raise NotImplementedError

        >>> isinstance(NoHam(), SupportsHam)
        True
        >>> SupportsHam.excludes(NoHam)
        >>> isinstance(NoHam(), SupportsHam)
        False

        ```

        !!! note

            This does not affect static type-checking.

            ``` python
            >>> my_ham: SupportsHam = NoHam()  # does *not* generate a Mypy warning

            ```
        """
        cls._abc_inst_check_cache[inst_t] = False
        cls._abc_inst_check_cache_overridden[inst_t] = True
        cls._dirty_for(inst_t)

    def reset_for(cls, inst_t: Type) -> None:
        r"""
        Clears any cached instance check for *inst_t*.
        """
        if inst_t in cls._abc_inst_check_cache:
            del cls._abc_inst_check_cache[inst_t]
            del cls._abc_inst_check_cache_overridden[inst_t]
            cls._dirty_for(inst_t)

    def _dirty_for(cls, inst_t: Type) -> None:
        for inheriting_cls in cls._abc_inst_check_cache_listeners:
            if (
                inst_t in inheriting_cls._abc_inst_check_cache
                and not inheriting_cls._abc_inst_check_cache_overridden[inst_t]
            ):
                del inheriting_cls._abc_inst_check_cache[inst_t]
                del inheriting_cls._abc_inst_check_cache_overridden[inst_t]
