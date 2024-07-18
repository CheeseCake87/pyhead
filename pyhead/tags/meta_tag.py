from markupsafe import Markup


class MetaTag:
    # ta = Tag Attribute
    _ta_name: str = None
    _ta_http_equiv: str = None
    _ta_property: str = None
    _ta_content: str = None
    _ta_id: str = None

    def __init__(
        self,
        name: str = None,
        http_equiv: str = None,
        property_: str = None,
        content: str = None,
        id_: str = None,
    ):
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

    def __repr__(self):
        return (
            f"<MetaTag "
            f"{self._ta_name}"
            f"{self._ta_http_equiv}"
            f"{self._ta_property}"
            f"{self._ta_content}"
            f"{self._ta_id}"
            f">"
        )

    def __str__(self):
        return Markup(self._compile())

    def __call__(self, *args, **kwargs):
        return Markup(self._compile())

    def _compile(self):
        return (
            f"<meta "
            f"{self._ta_name}"
            f"{self._ta_http_equiv}"
            f"{self._ta_property}"
            f"{self._ta_content}"
            f"{self._ta_id}"
            f">"
        )

    def replace_content(self, content: str):
        self.content = content
        return self
