from typing import Optional, Union, Literal

from markupsafe import Markup, escape

from ..protocols import CompileDelayed


class Link:
    key: Optional[str] = None

    _rel: str
    _href: Optional[Union[str, CompileDelayed]]
    _sizes: Optional[str]
    _type: Optional[str]
    _hreflang: Optional[str]
    _crossorigin: Optional[Literal["anonymous", "use-credentials"]]
    _id: Optional[str]

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
            __items.append(f'rel="{escape(self._rel)}"')

        if self._href:
            if _repr:
                __items.append(f'href="{self._href}"')
            else:
                href = (
                    self._href.compile()
                    if isinstance(self._href, CompileDelayed)
                    else self._href
                )
                __items.append(f'href="{escape(href)}"')

        if self._sizes:
            __items.append(f'sizes="{escape(self._sizes)}"')

        if self._type:
            __items.append(f'type="{escape(self._type)}"')

        if self._hreflang:
            __items.append(f'hreflang="{escape(self._hreflang)}"')

        if self._crossorigin:
            __items.append(f'crossorigin="{escape(self._crossorigin)}"')

        if self._id:
            __items.append(f'id="{escape(self._id)}"')

        return f"<link {' '.join(__items)}>"
