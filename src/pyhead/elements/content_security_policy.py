from markupsafe import Markup

from .meta import Meta


class ContentSecurityPolicy:
    unique: bool = True
    key: str = "content_security_policy"

    _content: str

    def __init__(self, content: str = "default-src 'self'") -> None:
        self._content = content

    def __repr__(self) -> str:
        return f'<ContentSecurityPolicy content="{self._content}">'

    def __str__(self) -> Markup:
        return Markup(self._compile())

    def __call__(self) -> Markup:
        return Markup(self._compile())

    def _compile(self) -> str:
        meta = Meta(http_equiv="Content-Security-Policy", content=self._content)
        return str(meta)
