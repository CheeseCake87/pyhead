from typing import Optional

from .._base import BaseElement
from .meta import Meta


class Google(BaseElement):
    key: str = "google"

    _googlebot: Optional[Meta] = None
    _sitelinkssearchbox: Optional[Meta] = None
    _no_translate: Optional[Meta] = None

    _order: list[str] = [
        "_googlebot",
        "_sitelinkssearchbox",
        "_no_translate",
    ]

    def __init__(
        self,
        googlebot: Optional[str] = None,
        no_sitelinks_search_box: bool = False,
        no_translate: bool = False,
    ) -> None:
        if googlebot is not None:
            self._googlebot = Meta(name="googlebot", content=googlebot)

        if no_sitelinks_search_box:
            self._sitelinkssearchbox = Meta(
                name="google", content="nositelinkssearchbox"
            )

        if no_translate:
            self._no_translate = Meta(name="google", content="notranslate")

    def __repr__(self) -> str:
        return (
            f"Google(googlebot={self._googlebot!r}, "
            f"sitelinkssearchbox={self._sitelinkssearchbox!r}, "
            f"no_translate={self._no_translate!r})"
        )

    def compile(self) -> str:
        rendered = [
            str(getattr(self, o_tag))
            for o_tag in self._order
            if getattr(self, o_tag) is not None
        ]
        return "\n".join(rendered) if rendered else ""
