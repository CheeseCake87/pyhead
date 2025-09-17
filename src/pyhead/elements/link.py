from typing import Optional, Union, Literal

from markupsafe import Markup

from ..protocols import CompileDelayed


class Link:
    unique: bool = False
    key: str = None

    _rel: str
    _href: Union[str, CompileDelayed]
    _sizes: str
    _type: str
    _hreflang: str
    _crossorigin: Optional[Literal["anonymous", "use-credentials"]]
    _id: str

    def __init__(
        self,
        rel: str,
        href: Optional[Union[str, CompileDelayed]] = None,
        sizes: Optional[str] = None,
        type_: Optional[str] = None,
        hreflang: Optional[str] = None,
        crossorigin: Optional[Literal["anonymous", "use-credentials"]] = None,
        id_: Optional[str] = None,
    ) -> None:
        self._rel = rel
        self._href = href
        self._sizes = sizes
        self._type = type_
        self._hreflang = hreflang
        self._crossorigin = crossorigin
        self._id = id_

        if self._id:
            self.key = self._id

    def __repr__(self) -> str:
        return self.compile(_repr=True).replace("link", "Link")

    def __str__(self) -> Markup:
        return Markup(self.compile())

    def __call__(self) -> Markup:
        return Markup(self.compile())

    def compile(self, _repr: bool = False) -> str:
        __items = []

        if self._rel:
            __items.append(f'rel="{self._rel}"')

        if self._href:
            if _repr:
                __items.append(f'href="{self._href}"')
            else:
                __items.append(
                    f'href="{self._href.compile() if isinstance(self._href, CompileDelayed) else self._href}"'
                )

        if self._sizes:
            __items.append(f'sizes="{self._sizes}"')

        if self._type:
            __items.append(f'type="{self._type}"')

        if self._hreflang:
            __items.append(f'hreflang="{self._hreflang}"')

        if self._crossorigin:
            __items.append(f'crossorigin="{self._crossorigin}"')

        return f"<link {' '.join(__items)}>"
