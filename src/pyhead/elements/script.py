from typing import Optional, Union

from markupsafe import Markup

from ..protocols import CompileDelayed


class Script:
    unique: bool = False
    key: str = None

    _src: str
    _type: str
    _async: bool
    _defer: bool
    _crossorigin: str
    _integrity: str
    _nomodule: bool
    _referrerpolicy: str
    _id: str

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
        return self.compile().replace("script", "Script")

    def __str__(self) -> Markup:
        return Markup(self.compile())

    def __call__(self) -> Markup:
        return Markup(self.compile())

    def compile(self) -> str:
        __items = []

        if self._src:
            __items.append(f'src="{self._src}"')
        if self._type:
            __items.append(f'type="{self._type}"')
        if self._async:
            __items.append(f'async="{str(self._async).lower()}"')
        if self._defer:
            __items.append(f'defer="{str(self._defer).lower()}"')
        if self._crossorigin:
            __items.append(f'crossorigin="{self._crossorigin}"')
        if self._integrity:
            __items.append(f'integrity="{self._integrity}"')
        if self._nomodule:
            __items.append(f'nomodule="{str(self._nomodule).lower()}"')
        if self._referrerpolicy:
            __items.append(f'referrerpolicy="{self._referrerpolicy}"')
        if self._id:
            __items.append(f'id="{self._id}"')

        return f"<script {' '.join(__items)}></script>"
