from .._base import BaseElement
from .meta import Meta


class ContentSecurityPolicy(BaseElement):
    key: str = "content_security_policy"

    _content: str

    def __init__(self, content: str = "default-src 'self'") -> None:
        self._content = content

    def __repr__(self) -> str:
        return f"ContentSecurityPolicy(content={self._content!r})"

    def compile(self) -> str:
        return str(Meta(http_equiv="Content-Security-Policy", content=self._content))
