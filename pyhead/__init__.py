"""A simple python package to generate HTML head tags."""

from typing import Optional, Union

from markupsafe import Markup

__version__ = "0.2"


class PageTitle:
    _page_title: str = None

    def __init__(self, page_title: str):
        self._page_title = page_title

    def __repr__(self):
        return f'<PageTitle page_title="{self._page_title}">'

    def __str__(self):
        return Markup(f'<title>{self._page_title}</title>')

    def replace(self, page_title: str):
        self._page_title = page_title
        return self

    def append(self, more_page_title: str, separator: str):
        self._page_title = self._page_title + separator + more_page_title
        return self

    def prepend(self, more_page_title: str, separator: str):
        self._page_title = more_page_title + separator + self._page_title
        return self


class PageDescription:
    _page_description: str = None

    def __init__(self, page_description: str):
        self._page_description = page_description

    def __repr__(self):
        return f'<PageDescription page_description="{self._page_description}">'

    def __str__(self):
        return Markup(f'<meta name="description" content="{self._page_description}">')

    def replace(self, page_description: str):
        self._page_description = page_description
        return self


class PageKeywords:
    _page_keywords: list = None

    def __init__(self):
        pass

    def __repr__(self):
        return f'<PageKeywords page_keywords="{self._page_keywords}">'

    def __str__(self):
        return Markup(f'<meta name="keywords" content="{", ".join(self._page_keywords)}">')

    def set_from_string(self, keywords: str):
        self._page_keywords = keywords.replace(" ", "").split(',')
        return self

    def set_from_list(self, keywords: list):
        self._page_keywords = keywords
        return self


class Head:
    page_title: PageTitle
    page_description: Optional[PageDescription] = None
    page_keywords: Optional[PageKeywords] = None

    def __init__(
            self,
            page_title: str,
    ):
        self.page_title = PageTitle(page_title)

    def set_page_title(self, page_title: str):
        self.page_title.replace(page_title)
        return self

    def set_page_description(self, page_description: str):
        self.page_description = PageDescription(page_description)
        return self

    def set_page_keywords(self, keywords: Union[str, list]):
        self.page_keywords = PageKeywords()
        if isinstance(keywords, str):
            self.page_keywords.set_from_string(keywords)
            return self
        if isinstance(keywords, list):
            self.page_keywords.set_from_list(keywords)
            return self

        return self

    def __repr__(self):
        return f'<Head page_title="{self.page_title}">'

    def as_dict(self):
        return {
            'page_title': self.page_title,
            'page_description': self.page_description,
            'page_keywords': self.page_keywords
        }

    def __str__(self):
        build = [
            f"{self.page_title}",
            f"{self.page_description}" if self.page_description else None,
            f"{self.page_keywords}" if self.page_keywords else None
        ]
        return Markup("\n".join([x for x in build if x is not None]))


if __name__ == '__main__':
    head = Head('Hello World')
    head.set_page_description('This is a test')
    head.set_page_keywords('test, hello, world')
    head.set_page_description('This is a test')
    head.page_title.append('Hello World1', ' - ')

    print(head)

    # for k, v in head.as_dict().items():
    #     print(k, "=", v)
