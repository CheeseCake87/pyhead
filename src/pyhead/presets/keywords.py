from markupsafe import Markup


class Keywords:
    keywords: list = None

    def __init__(self):
        pass

    def __repr__(self):
        return f'<Keywords page_keywords="{self.keywords}">'

    def __str__(self):
        return Markup(self._compile())

    def __call__(self, *args, **kwargs):
        return Markup(self._compile())

    def _compile(self):
        return f'<meta name="keywords" content="{", ".join(self.keywords)}">'

    def set_from_string(self, keywords: str):
        self.keywords = keywords.replace(" ", "").split(",")
        return self

    def set_from_list(self, keywords: list):
        self.keywords = keywords
        return self
