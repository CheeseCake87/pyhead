from markupsafe import Markup


class Charset:
    charset: str = None

    def __init__(self, charset: str = "utf-8"):
        self.charset = charset

    def __repr__(self):
        return f'<Charset charset="{self.charset}">'

    def __str__(self):
        return Markup(self._compile())

    def __call__(self, *args, **kwargs):
        return Markup(self._compile())

    def _compile(self):
        return f'<meta charset="{self.charset}">'

    def replace(self, charset: str):
        self.charset = charset
        return self
