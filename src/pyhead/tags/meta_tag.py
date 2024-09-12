from markupsafe import Markup
from typing import Optional


class MetaTag:
    # ta = Tag Attribute
    _ta_name: str
    _ta_http_equiv: str
    _ta_property: str
    _ta_content: str
    _ta_id: str

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

        self._ta_name = f'name="{name}" ' if name is not None else ""
        self._ta_http_equiv = (
            f'http-equiv="{http_equiv}" ' if http_equiv is not None else ""
        )
        self._ta_property = f'property="{property_}" ' if property_ is not None else ""
        self._ta_content = f'content="{content}" ' if content is not None else ""
        self._ta_id = f'id="{id_}" ' if id_ is not None else ""

    def __repr__(self) -> str:
        return (
            f"<MetaTag "
            f"{self._ta_name}"
            f"{self._ta_http_equiv}"
            f"{self._ta_property}"
            f"{self._ta_content}"
            f"{self._ta_id}"
            f">"
        )

    def __str__(self) -> Markup:
        return Markup(self._compile())

    def __call__(self) -> Markup:
        return Markup(self._compile())

    def _compile(self) -> str:
        return (
            f"<meta "
            f"{self._ta_name}"
            f"{self._ta_http_equiv}"
            f"{self._ta_property}"
            f"{self._ta_content}"
            f"{self._ta_id}"
            f">"
        )

    def replace_content(self, content: str) -> "MetaTag":
        self.content = content
        return self
