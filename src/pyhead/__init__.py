from pprint import pprint
from typing import Optional

from markupsafe import Markup

from .__version__ import __version__
from ._helpers import has_key
from .elements import (
    Page,
    Link,
    Meta,
    Title,
    Description,
    Base,
    Script,
    Favicon,
    Charset,
    Keywords,
    Google,
    Verification,
    OpenGraphWebsite,
    Stylesheet,
    TwitterCard,
    GeoPosition,
)


class Head:
    e: dict  # Element ID: Element Class

    title: Optional[str] = None

    def __init__(
        self,
        elements: list[
            Page
            | Link
            | Meta
            | Title
            | Description
            | Base
            | Script
            | Favicon
            | Charset
            | Keywords
            | Google
            | Verification
            | OpenGraphWebsite
            | Stylesheet
            | TwitterCard
            | GeoPosition
        ],
    ) -> None:
        self.e = {}

        self._loop_elements(elements)

    def _loop_elements(
        self,
        elements: list[
            Page
            | Link
            | Meta
            | Title
            | Description
            | Base
            | Script
            | Favicon
            | Charset
            | Keywords
            | Google
            | Verification
            | OpenGraphWebsite
            | Stylesheet
            | TwitterCard
            | GeoPosition
        ],
    ) -> None:
        for index, element in enumerate(elements):
            if isinstance(element, Page):
                for key, value in element.e.items():
                    self.e[key] = value
                continue

            key = has_key(element)

            self.e[str(key if key else index)] = element

        if self.e.get("title"):
            self.title = self.e["title"]._title

    def extend(
        self,
        elements: list[
            Page
            | Link
            | Meta
            | Title
            | Description
            | Base
            | Script
            | Favicon
            | Charset
            | Keywords
            | Google
            | Verification
            | OpenGraphWebsite
            | Stylesheet
            | TwitterCard
            | GeoPosition
        ],
    ) -> "Head":
        self._loop_elements(elements)
        return self

    def compile(self, skip_title: bool = False) -> Markup:
        render = []

        pprint(self.e)

        for key, element in self.e.items():
            if key == "title" and skip_title:
                continue

            render.append(str(element))

        return Markup("\n".join(render))


__all__ = ["__version__", "Head"]
