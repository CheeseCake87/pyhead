from markupsafe import Markup


class BaseTag:
    href: str = None

    def __init__(self, href: str):
        self.href = href

    def __repr__(self):
        return f'<Base base="{self.href}">'

    def __str__(self):
        return Markup(self._compile())

    def __call__(self, *args, **kwargs):
        return Markup(self._compile())

    def _compile(self):
        return f'<base href="{self.href}">'

    def replace(self, href: str):
        self.href = href
        return self
