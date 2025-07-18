from typing import Optional

from markupsafe import Markup


class Link:
    unique: bool = False
    key: str = None

    _rel: str
    _href: str
    _sizes: str
    _type: str
    _hreflang: str
    _id: str

    def __init__(
        self,
        rel: str,
        href: Optional[str] = None,
        sizes: Optional[str] = None,
        type_: Optional[str] = None,
        hreflang: Optional[str] = None,
        id_: Optional[str] = None,
    ) -> None:
        self._rel = f'rel="{rel}" '
        self._href = f'href="{href}" ' if href is not None else ""
        self._sizes = f'sizes="{sizes}" ' if sizes is not None else ""
        self._type = f'type="{type_}" ' if type_ is not None else ""
        self._hreflang = f'hreflang="{hreflang}" ' if hreflang is not None else ""
        self._id = f'id="{id_}" ' if id_ is not None else ""

        if self._id:
            self.key = self._id

    def __repr__(self) -> Markup:
        return Markup(
            (
                f"<Link "
                f"{self._rel}"
                f"{self._href}"
                f"{self._sizes}"
                f"{self._type}"
                f"{self._hreflang}"
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
            f"<link "
            f"{self._rel}"
            f"{self._href}"
            f"{self._sizes}"
            f"{self._type}"
            f"{self._hreflang}"
            f"{self._id}"
            f">"
        ).replace(" >", ">")
