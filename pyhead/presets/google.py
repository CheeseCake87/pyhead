from typing import Optional

from markupsafe import Markup

from ..tags import MetaTag


class Google:
    googlebot: Optional[MetaTag] = None
    sitelinkssearchbox: Optional[MetaTag] = None
    no_translate: Optional[MetaTag] = None

    _googlebot: list

    _order: list = [
        "googlebot",
        "sitelinkssearchbox",
        "no_translate",
    ]

    def __init__(
        self,
        googlebot: Optional[str] = None,
        no_sitelinks_search_box: bool = False,
        no_translate: bool = False,
        *args,
        **kwargs,
    ):
        self._googlebot = []

        if googlebot is not None:
            self.googlebot = MetaTag(name="googlebot", content=googlebot)

        if no_sitelinks_search_box:
            self.sitelinks = MetaTag(name="google", content="nositelinkssearchbox")

        if no_translate:
            self.no_translate = MetaTag(name="google", content="notranslate")

        _, __ = args, kwargs

    def __repr__(self):
        return (
            f"<Google googlebot={self.googlebot} sitelinkssearchbox={self.sitelinkssearchbox} "
            f"no_translate={self.no_translate}>"
        )

    def __str__(self):
        return Markup(self._compile())

    def __call__(self, *args, **kwargs):
        return Markup(self._compile())

    def _compile(self):
        _ = [
            str(getattr(self, o_tag))
            for o_tag in self._order
            if getattr(self, o_tag) is not None
        ]
        if _:
            return "\n".join(_)
        return ""
