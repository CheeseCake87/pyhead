from typing import Optional

from .._base import BaseElement
from .meta import Meta


class Verification(BaseElement):
    key: str = "verification"

    _google: Optional[Meta] = None
    _yandex: Optional[Meta] = None
    _bing: Optional[Meta] = None
    _pinterest: Optional[Meta] = None
    _norton: Optional[Meta] = None

    _order: list[str] = [
        "_google",
        "_yandex",
        "_bing",
        "_pinterest",
        "_norton",
    ]

    def __init__(
        self,
        google: Optional[str] = None,
        yandex: Optional[str] = None,
        bing: Optional[str] = None,
        pinterest: Optional[str] = None,
        norton: Optional[str] = None,
    ) -> None:
        if google is not None:
            self._google = Meta(name="google-site-verification", content=google)

        if yandex is not None:
            self._yandex = Meta(name="yandex-verification", content=yandex)

        if bing is not None:
            self._bing = Meta(name="msvalidate.01", content=bing)

        if pinterest is not None:
            self._pinterest = Meta(name="p:domain_verify", content=pinterest)

        if norton is not None:
            self._norton = Meta(name="norton-safeweb-site-verification", content=norton)

    def __repr__(self) -> str:
        return (
            f"Verification(google={self._google!r}, yandex={self._yandex!r}, "
            f"bing={self._bing!r}, pinterest={self._pinterest!r}, "
            f"norton={self._norton!r})"
        )

    def compile(self) -> str:
        rendered = [
            str(getattr(self, o_tag))
            for o_tag in self._order
            if getattr(self, o_tag) is not None
        ]
        return "\n".join(rendered) if rendered else ""
