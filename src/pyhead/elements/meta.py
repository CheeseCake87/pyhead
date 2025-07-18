from typing import Optional

from markupsafe import Markup


class Meta:
    unique: bool = False
    key: str = None

    _name: str
    _http_equiv: str
    _property: str
    _content: str
    _id: str

    def __init__(
        self,
        name: Optional[str] = None,
        http_equiv: Optional[str] = None,
        property_: Optional[str] = None,
        content: Optional[str] = None,
        id_: Optional[str] = None,
    ) -> None:
        one_only = [name, http_equiv, property_]
        if one_only.count(None) != 2:
            raise ValueError(
                "You can only specify one of name, http_equiv, or property_."
            )

        self._name = f'name="{name}" ' if name is not None else ""
        self._http_equiv = (
            f'http-equiv="{http_equiv}" ' if http_equiv is not None else ""
        )
        self._property = f'property="{property_}" ' if property_ is not None else ""
        self._content = f'content="{content}" ' if content is not None else ""
        self._id = f'id="{id_}" ' if id_ is not None else ""

        if self._id:
            self.key = self._id

    def __repr__(self) -> str:
        return (
            f"<Meta "
            f"{self._name}"
            f"{self._http_equiv}"
            f"{self._property}"
            f"{self._content}"
            f"{self._id}"
            f">"
        )

    def __str__(self) -> Markup:
        return Markup(self._compile())

    def __call__(self) -> Markup:
        return Markup(self._compile())

    def _compile(self) -> str:
        return (
            f"<meta "
            f"{self._name}"
            f"{self._http_equiv}"
            f"{self._property}"
            f"{self._content}"
            f"{self._id}"
            f">"
        )
