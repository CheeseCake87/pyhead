from typing import Optional, Union

from markupsafe import Markup, escape

from ..protocols import CompileDelayed


class Meta:
    key: Optional[str] = None

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
        one_only = [name, http_equiv, property_]
        if one_only.count(None) != 2:
            raise ValueError(
                "You can only specify one of name, http_equiv, or property_."
            )

        self._name = name
        self._http_equiv = http_equiv
        self._property = property_
        self._content = content
        self._id = id_

    def __repr__(self) -> str:
        return self.compile().replace("meta", "Meta")

    def __str__(self) -> Markup:
        return Markup(self.compile())

    def __call__(self) -> Markup:
        return Markup(self.compile())

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
