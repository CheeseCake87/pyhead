from markupsafe import Markup


class BaseTag:
    href: str

    def __init__(self, href: str) -> None:
        self.href = href

    def __repr__(self)  -> str:
        return f'<Base base="{self.href}">'

    def __str__(self) -> Markup:
        return Markup(self._compile())

    def __call__(self) -> Markup:
        return Markup(self._compile())

    def _compile(self) -> str:
        return f'<base href="{self.href}">'

    def replace(self, href: str) -> "BaseTag":
        self.href = href
        return self
