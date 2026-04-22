from typing import Optional, Union

from markupsafe import escape

from .._base import BaseElement
from ..protocols import CompileDelayed


class Script(BaseElement):
    _src: Union[str, CompileDelayed]
    _type: Optional[str]
    _async: bool
    _defer: bool
    _crossorigin: Optional[str]
    _integrity: Optional[str]
    _nomodule: bool
    _referrerpolicy: Optional[str]
    _id: Optional[str]

    def __init__(
        self,
        src: Union[str, CompileDelayed],
        type_: Optional[str] = None,
        async_: bool = False,
        defer: bool = False,
        crossorigin: Optional[str] = None,
        integrity: Optional[str] = None,
        nomodule: bool = False,
        referrerpolicy: Optional[str] = None,
        id_: Optional[str] = None,
    ) -> None:
        self._src = src
        self._type = type_
        self._async = async_
        self._defer = defer
        self._crossorigin = crossorigin
        self._integrity = integrity
        self._nomodule = nomodule
        self._referrerpolicy = referrerpolicy
        self._id = id_

        if self._id:
            self.key = self._id

    def __repr__(self) -> str:
        parts = [f"src={self._src!r}"]
        if self._type is not None:
            parts.append(f"type={self._type!r}")
        if self._async:
            parts.append(f"async_={self._async!r}")
        if self._defer:
            parts.append(f"defer={self._defer!r}")
        if self._crossorigin is not None:
            parts.append(f"crossorigin={self._crossorigin!r}")
        if self._integrity is not None:
            parts.append(f"integrity={self._integrity!r}")
        if self._nomodule:
            parts.append(f"nomodule={self._nomodule!r}")
        if self._referrerpolicy is not None:
            parts.append(f"referrerpolicy={self._referrerpolicy!r}")
        if self._id is not None:
            parts.append(f"id={self._id!r}")
        return f"Script({', '.join(parts)})"

    def compile(self) -> str:
        __items = []

        if self._src:
            src = (
                self._src.compile()
                if isinstance(self._src, CompileDelayed)
                else self._src
            )
            __items.append(f'src="{escape(src)}"')
        if self._type:
            __items.append(f'type="{escape(self._type)}"')
        if self._async:
            __items.append(f'async="{str(self._async).lower()}"')
        if self._defer:
            __items.append(f'defer="{str(self._defer).lower()}"')
        if self._crossorigin:
            __items.append(f'crossorigin="{escape(self._crossorigin)}"')
        if self._integrity:
            __items.append(f'integrity="{escape(self._integrity)}"')
        if self._nomodule:
            __items.append(f'nomodule="{str(self._nomodule).lower()}"')
        if self._referrerpolicy:
            __items.append(f'referrerpolicy="{escape(self._referrerpolicy)}"')
        if self._id:
            __items.append(f'id="{escape(self._id)}"')

        return f"<script {' '.join(__items)}></script>"
