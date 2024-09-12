from typing import Optional

from markupsafe import Markup

from ..tags import MetaTag


class Verification:
    google: Optional[MetaTag] = None
    yandex: Optional[MetaTag] = None
    bing: Optional[MetaTag] = None
    alexa: Optional[MetaTag] = None
    pinterest: Optional[MetaTag] = None
    norton: Optional[MetaTag] = None

    _order: list = [
        "google",
        "yandex",
        "bing",
        "alexa",
        "pinterest",
        "norton",
    ]

    def __init__(
        self,
        google: Optional[str] = None,
        yandex: Optional[str] = None,
        bing: Optional[str] = None,
        alexa: Optional[str] = None,
        pinterest: Optional[str] = None,
        norton: Optional[str] = None,
        *args,
        **kwargs,
    ):
        if google is not None:
            self.google = MetaTag(name="google-site-verification", content=google)

        if yandex is not None:
            self.yandex = MetaTag(name="yandex-verification", content=yandex)

        if bing is not None:
            self.bing = MetaTag(name="msvalidate.01", content=bing)

        if alexa is not None:
            self.alexa = MetaTag(name="alexaVerifyID", content=alexa)

        if pinterest is not None:
            self.pinterest = MetaTag(name="p:domain_verify", content=pinterest)

        if norton is not None:
            self.norton = MetaTag(
                name="norton-safeweb-site-verification", content=norton
            )

        _, __ = args, kwargs

    def __repr__(self):
        return (
            f"<Verification google={self.google} yandex={self.yandex} "
            f"bing={self.bing} alexa={self.alexa} pinterest={self.pinterest} "
            f"norton={self.norton}>"
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
