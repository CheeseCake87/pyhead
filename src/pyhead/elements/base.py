from markupsafe import Markup


class Base:
    unique: bool = True
    key: str = "base"

    _href: str

    def __init__(self, href: str) -> None:
        self._href = href

    def __repr__(self) -> str:
        return f'<Base base="{self._href}">'

    def __str__(self) -> Markup:
        return Markup(self._compile())

    def __call__(self) -> Markup:
        return Markup(self._compile())

    def _compile(self) -> str:
        return f'<base href="{self._href}">'
