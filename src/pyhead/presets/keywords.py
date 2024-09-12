from markupsafe import Markup


class Keywords:
    keywords: list[str]

    def __init__(self) -> None:
        self.keywords = []
        pass

    def __repr__(self) -> str:
        return f'<Keywords page_keywords="{self.keywords}">'

    def __str__(self) -> Markup:
        return Markup(self._compile())

    def __call__(self) -> Markup:
        return Markup(self._compile())

    def _compile(self) -> str:
        return f'<meta name="keywords" content="{", ".join(self.keywords)}">'

    def set_from_string(self, keywords: str) -> "Keywords":
        self.keywords = keywords.replace(" ", "").split(",")
        return self

    def set_from_list(self, keywords: list[str]) -> "Keywords":
        self.keywords = keywords
        return self
