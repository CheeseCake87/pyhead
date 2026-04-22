from typing import Optional, Union

from markupsafe import escape

from .._base import BaseElement
from ..protocols import CompileDelayed


class Meta(BaseElement):
    _name: Optional[str]
    _http_equiv: Optional[str]
    _property: Optional[str]
    _content: Optional[Union[str, CompileDelayed]]
    _id: Optional[str]

    def __init__(
        self,
        name: Optional[str] = None,
        http_equiv: Optional[str] = None,
        property_: Optional[str] = None,
        content: Optional[Union[str, CompileDelayed]] = None,
        id_: Optional[str] = None,
    ) -> None:
        provided = [x for x in (name, http_equiv, property_) if x is not None]
        if len(provided) == 0:
            raise ValueError(
                "Meta requires exactly one of name, http_equiv, or property_."
            )
        if len(provided) > 1:
            raise ValueError(
                "Meta accepts only one of name, http_equiv, or property_ "
                "(not multiple)."
            )

        self._name = name
        self._http_equiv = http_equiv
        self._property = property_
        self._content = content
        self._id = id_

    def __repr__(self) -> str:
        parts = []
        if self._name is not None:
            parts.append(f"name={self._name!r}")
        if self._http_equiv is not None:
            parts.append(f"http_equiv={self._http_equiv!r}")
        if self._property is not None:
            parts.append(f"property={self._property!r}")
        if self._content is not None:
            parts.append(f"content={self._content!r}")
        if self._id is not None:
            parts.append(f"id={self._id!r}")
        return f"Meta({', '.join(parts)})"

    def compile(self) -> str:
        __items = []

        if self._name:
            __items.append(f'name="{escape(self._name)}"')

        if self._http_equiv:
            __items.append(f'http-equiv="{escape(self._http_equiv)}"')

        if self._property:
            __items.append(f'property="{escape(self._property)}"')

        if self._content:
            if isinstance(self._content, CompileDelayed):
                __items.append(f'content="{escape(self._content.compile())}"')
            else:
                __items.append(f'content="{escape(self._content)}"')

        if self._id:
            __items.append(f'id="{escape(self._id)}"')

        return f"<meta {' '.join(__items)}>"
