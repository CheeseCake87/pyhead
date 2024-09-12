from typing import List

from markupsafe import Markup


class TitleTag:
    title: str = None
    _exclude_title_tags: bool = False

    _appends: List[tuple] = None
    _prepends: List[tuple] = None

    def __init__(
        self,
        page_title: str,
        _exclude_title_tags: bool = False,
    ):
        self._appends = []
        self._prepends = []

        self.title = page_title
        self._exclude_title_tags = _exclude_title_tags

    def __repr__(self):
        return f'<Title page_title="{self.title}">'

    def __str__(self):
        return Markup(f"{self._compile()}")

    def __call__(self, *args, **kwargs):
        return Markup(f"{self._compile()}")

    def set_appends(self, appends: List[tuple]):
        """
        appends = [(text, separator), ...]
        :param appends:
        :return:
        """
        self._appends = appends
        return self

    def set_prepends(self, prepends: List[tuple]):
        """
        prepends = [(text, separator), ...]
        :param prepends:
        :return:
        """
        self._prepends = prepends
        return self

    def _compile(self):
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
