from markupsafe import Markup


class Title:
    unique: bool = True
    disabled: bool = False
    key: str = "title"

    _title: str

    def __init__(
        self,
        title: str,
    ) -> None:
        self._title = title

    def __repr__(self) -> str:
        return f'<Title title="{self._title}">'

    def __str__(self) -> Markup:
        return Markup(f"{self._compile()}")

    def __call__(self) -> Markup:
        return Markup(f"{self._compile()}")

    def _compile(self) -> str:
        return f"<title>" f"{self._title}" f"</title>"
