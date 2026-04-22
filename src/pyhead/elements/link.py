from typing import Optional, Union, Literal

from markupsafe import escape

from .._base import BaseElement
from ..protocols import CompileDelayed


class Link(BaseElement):
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
        parts = [f"rel={self._rel!r}"]
        if self._href is not None:
            parts.append(f"href={self._href!r}")
        if self._sizes is not None:
            parts.append(f"sizes={self._sizes!r}")
        if self._type is not None:
            parts.append(f"type={self._type!r}")
        if self._hreflang is not None:
            parts.append(f"hreflang={self._hreflang!r}")
        if self._crossorigin is not None:
            parts.append(f"crossorigin={self._crossorigin!r}")
        if self._id is not None:
            parts.append(f"id={self._id!r}")
        return f"Link({', '.join(parts)})"

    def compile(self) -> str:
        __items = [f'rel="{escape(self._rel)}"']

        if self._href:
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
