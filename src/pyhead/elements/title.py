from markupsafe import Markup, escape


class Title:
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
        return Markup(f"{self.compile()}")

    def __call__(self) -> Markup:
        return Markup(f"{self.compile()}")

    def compile(self) -> str:
        return f"<title>{escape(self._title)}</title>"
