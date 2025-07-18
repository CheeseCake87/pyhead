from markupsafe import Markup


class Description:
    unique: bool = True
    key: str = "description"

    _description: str

    def __init__(self, description: str) -> None:
        self._description = description

    def __repr__(self) -> str:
        return f'<Description content="{self._description}">'

    def __str__(self) -> Markup:
        return Markup(self._compile())

    def __call__(self) -> Markup:
        return Markup(self._compile())

    def _compile(self) -> str:
        return f'<meta name="description" content="{self._description}">'
