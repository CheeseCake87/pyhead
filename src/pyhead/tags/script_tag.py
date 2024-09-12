from typing import Optional

from markupsafe import Markup


class ScriptTag:
    # ta = Tag Attribute
    _ta_src: str = None
    _ta_type: str = None
    _ta_async: str = None
    _ta_defer: str = None
    _ta_crossorigin: str = None
    _ta_integrity: str = None
    _ta_nomodule: str = None
    _ta_referrerpolicy: str = None
    _ta_id: str = None

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
    ):
        self._ta_src = f'src="{src}" '
        self._ta_type = f'type="{type_}" ' if type_ is not None else ""
        self._ta_async = f'async="{str(async_).lower()}" ' if async_ else ""
        self._ta_defer = "defer " if defer else ""
        self._ta_crossorigin = (
            f'crossorigin="{crossorigin}" ' if crossorigin is not None else ""
        )
        self._ta_integrity = (
            f'integrity="{integrity}" ' if integrity is not None else ""
        )
        self._ta_nomodule = "nomodule " if nomodule else ""
        self._ta_referrerpolicy = (
            f'referrerpolicy="{referrerpolicy}" ' if referrerpolicy is not None else ""
        )
        self._ta_id = f'id="{id_}" ' if id_ is not None else ""

    def __repr__(self):
        return Markup(
            (
                f"<ScriptTag "
                f"{self._ta_src}"
                f"{self._ta_type}"
                f"{self._ta_async}"
                f"{self._ta_defer}"
                f"{self._ta_crossorigin}"
                f"{self._ta_integrity}"
                f"{self._ta_nomodule}"
                f"{self._ta_referrerpolicy}"
                f"{self._ta_id}"
                f">"
            ).replace(" >", ">")
        )

    def __str__(self):
        return Markup(self._compile())

    def __call__(self, *args, **kwargs):
        return Markup(self._compile())

    def _compile(self):
        return (
            f"<script "
            f"{self._ta_src}"
            f"{self._ta_type}"
            f"{self._ta_async}"
            f"{self._ta_defer}"
            f"{self._ta_crossorigin}"
            f"{self._ta_integrity}"
            f"{self._ta_nomodule}"
            f"{self._ta_referrerpolicy}"
            f"{self._ta_id}"
            f"></script>"
        ).replace(" >", ">")
