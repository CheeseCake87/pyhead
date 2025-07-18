from typing import Optional

from markupsafe import Markup


class Script:
    unique: bool = False
    key: str = None

    _src: str
    _type: str
    _async: str
    _defer: str
    _crossorigin: str
    _integrity: str
    _nomodule: str
    _referrerpolicy: str
    _id: str

    def __init__(
        self,
        src: str,
        type_: Optional[str] = None,
        async_: bool = False,
        defer: bool = False,
        crossorigin: Optional[str] = None,
        integrity: Optional[str] = None,
        nomodule: bool = False,
        referrerpolicy: Optional[str] = None,
        id_: Optional[str] = None,
    ) -> None:
        self._src = f'src="{src}" '
        self._type = f'type="{type_}" ' if type_ is not None else ""
        self._async = f'async="{str(async_).lower()}" ' if async_ else ""
        self._defer = "defer " if defer else ""
        self._crossorigin = (
            f'crossorigin="{crossorigin}" ' if crossorigin is not None else ""
        )
        self._integrity = f'integrity="{integrity}" ' if integrity is not None else ""
        self._nomodule = "nomodule " if nomodule else ""
        self._referrerpolicy = (
            f'referrerpolicy="{referrerpolicy}" ' if referrerpolicy is not None else ""
        )
        self._id = f'id="{id_}" ' if id_ is not None else ""

        if self._id:
            self.key = self._id

    def __repr__(self) -> Markup:
        return Markup(
            (
                f"<ScriptTag "
                f"{self._src}"
                f"{self._type}"
                f"{self._async}"
                f"{self._defer}"
                f"{self._crossorigin}"
                f"{self._integrity}"
                f"{self._nomodule}"
                f"{self._referrerpolicy}"
                f"{self._id}"
                f">"
            ).replace(" >", ">")
        )

    def __str__(self) -> Markup:
        return Markup(self._compile())

    def __call__(self) -> Markup:
        return Markup(self._compile())

    def _compile(self) -> str:
        return (
            f"<script "
            f"{self._src}"
            f"{self._type}"
            f"{self._async}"
            f"{self._defer}"
            f"{self._crossorigin}"
            f"{self._integrity}"
            f"{self._nomodule}"
            f"{self._referrerpolicy}"
            f"{self._id}"
            f"></script>"
        ).replace(" >", ">")
