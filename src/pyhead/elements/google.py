from typing import Optional

from markupsafe import Markup

from .meta import Meta


class Google:
    unique: bool = True
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
            self.sitelinks = Meta(name="google", content="nositelinkssearchbox")

        if no_translate:
            self._no_translate = Meta(name="google", content="notranslate")

    def __repr__(self) -> str:
        return (
            f"<Google googlebot={self._googlebot} sitelinkssearchbox={self._sitelinkssearchbox} "
            f"no_translate={self._no_translate}>"
        )

    def __str__(self) -> Markup:
        return Markup(self.compile())

    def __call__(self) -> Markup:
        return Markup(self.compile())

    def compile(self) -> str:
        _ = [
            str(getattr(self, o_tag))
            for o_tag in self._order
            if getattr(self, o_tag) is not None
        ]
        if _:
            return "\n".join(_)
        return ""
