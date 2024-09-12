from typing import List

from markupsafe import Markup


class TitleTag:
    title: str
    _exclude_title_tags: bool

    _appends: List[tuple[str, str]]
    _prepends: List[tuple[str, str]]

    def __init__(
        self,
        page_title: str,
        _exclude_title_tags: bool = False,
    ) -> None:
        self._appends = []
        self._prepends = []

        self.title = page_title
        self._exclude_title_tags = _exclude_title_tags

    def __repr__(self) -> str:
        return f'<Title page_title="{self.title}">'

    def __str__(self) -> Markup:
        return Markup(f"{self._compile()}")

    def __call__(self) -> Markup:
        return Markup(f"{self._compile()}")

    def set_appends(self, appends: List[tuple[str, str]]) -> "TitleTag":
        """
        appends = [(text, separator), ...]
        :param appends:
        :return:
        """
        self._appends = appends
        return self

    def set_prepends(self, prepends: List[tuple[str, str]]) -> "TitleTag":
        """
        prepends = [(text, separator), ...]
        :param prepends:
        :return:
        """
        self._prepends = prepends
        return self

    def _compile(self) -> str:
        if self._exclude_title_tags:
            return (
                f"{''.join([f'{x[0]}{x[1]}' for x in self._prepends])}"
                f"{self.title}"
                f"{''.join([f'{x[1]}{x[0]}' for x in self._appends])}"
            )
        else:
            return (
                f"<title>"
                f"{''.join([f'{x[0]}{x[1]}' for x in self._prepends])}"
                f"{self.title}"
                f"{''.join([f'{x[1]}{x[0]}' for x in self._appends])}"
                f"</title>"
            )
