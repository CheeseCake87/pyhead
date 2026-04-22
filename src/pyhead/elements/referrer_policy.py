from .._base import BaseElement
from .meta import Meta


class ReferrerPolicy(BaseElement):
    key: str = "referrer_policy"

    _content: str

    def __init__(self, content: str) -> None:
        self._content = content

    def __repr__(self) -> str:
        return f"ReferrerPolicy(content={self._content!r})"

    def compile(self) -> str:
        return str(Meta(name="referrer", content=self._content))
