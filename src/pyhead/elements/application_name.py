from markupsafe import Markup

from .meta import Meta


class ApplicationName:
    unique: bool = True
    key: str = "application_name"

    _content: str

    def __init__(self, content: str) -> None:
        self._content = content

    def __repr__(self) -> str:
        return f'<ApplicationName content="{self._content}">'

    def __str__(self) -> Markup:
        return Markup(self._compile())

    def __call__(self) -> Markup:
        return Markup(self._compile())

    def _compile(self) -> str:
        meta = Meta(name="application_name", content=self._content)
        return str(meta)
