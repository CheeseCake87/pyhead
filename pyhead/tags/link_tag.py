from typing import Optional

from markupsafe import Markup


class LinkTag:
    # ta = Tag Attribute
    _ta_rel: str = None
    _ta_href: str = None
    _ta_sizes: str = None
    _ta_type: str = None
    _ta_hreflang: str = None
    _ta_id: str = None

    def __init__(
        self,
        rel: str,
        href: Optional[str] = None,
        sizes: Optional[str] = None,
        type_: Optional[str] = None,
        hreflang: Optional[str] = None,
        id_: Optional[str] = None,
    ):
        self._ta_rel = f'rel="{rel}" '
        self._ta_href = f'href="{href}" ' if href is not None else ""
        self._ta_sizes = f'sizes="{sizes}" ' if sizes is not None else ""
        self._ta_type = f'type="{type_}" ' if type_ is not None else ""
        self._ta_hreflang = f'hreflang="{hreflang}" ' if hreflang is not None else ""
        self._ta_id = f'id="{id_}" ' if id_ is not None else ""

    def __repr__(self):
        return Markup(
            (
                f"<LinkTag "
                f"{self._ta_rel}"
                f"{self._ta_href}"
                f"{self._ta_sizes}"
                f"{self._ta_type}"
                f"{self._ta_hreflang}"
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
            f"<link "
            f"{self._ta_rel}"
            f"{self._ta_href}"
            f"{self._ta_sizes}"
            f"{self._ta_type}"
            f"{self._ta_hreflang}"
            f"{self._ta_id}"
            f">"
        ).replace(" >", ">")
