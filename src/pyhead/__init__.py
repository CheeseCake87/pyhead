from typing import Optional

from markupsafe import Markup

from .__version__ import __version__
from ._helpers import has_key
from .elements import (
    ApplicationName,
    Base,
    Charset,
    ContentSecurityPolicy,
    Description,
    Favicon,
    FormatDetection,
    GeoPosition,
    Google,
    Keywords,
    Link,
    Meta,
    OpenGraphWebsite,
    Page,
    ReferrerPolicy,
    Robots,
    Script,
    SocialMediaCard,
    Stylesheet,
    ThemeColor,
    Title,
    TwitterCard,
    Verification,
)


class Head:
    e: dict  # Element ID: Element Class

    title: Optional[str] = None

    def __init__(
        self,
        elements_: list[  #
            ApplicationName
            | Base
            | Charset
            | ContentSecurityPolicy
            | Description
            | Favicon
            | FormatDetection
            | GeoPosition
            | Google
            | Keywords
            | Link
            | Meta
            | OpenGraphWebsite
            | Page
            | ReferrerPolicy
            | Robots
            | Script
            | SocialMediaCard
            | Stylesheet
            | ThemeColor
            | Title
            | TwitterCard
            | Verification
        ],
    ) -> None:
        """
        This is the main class that controls the rendering of elements.

        Here's a simple example.

        .. code-block::

            from pyhead import Head
            from pyhead.elements import Page

            head = Head([Page(title="My Website")])


        :param elements_:
        """
        self.e = {}

        self._loop_elements(elements_)

    def _loop_elements(
        self,
        elements_: list[
            ApplicationName
            | Base
            | Charset
            | ContentSecurityPolicy
            | Description
            | Favicon
            | FormatDetection
            | GeoPosition
            | Google
            | Keywords
            | Link
            | Meta
            | OpenGraphWebsite
            | Page
            | ReferrerPolicy
            | Robots
            | Script
            | SocialMediaCard
            | Stylesheet
            | ThemeColor
            | Title
            | TwitterCard
            | Verification
        ],
    ) -> None:
        """
        A private method that loops through elements and adds them to head.e dict.

        :param elements_:
        :return:
        """
        for index, element in enumerate(elements_):
            if isinstance(element, Page):
                for key, value in element.e.items():
                    self.e[key] = value
                continue

            if isinstance(element, SocialMediaCard):
                for key, value in element.e.items():
                    self.e[key] = value
                continue

            key = has_key(element)

            self.e[str(key if key else index)] = element

        if self.e.get("title"):
            self.title = self.e["title"]._title

    def extend(
        self,
        elements_: list[
            ApplicationName
            | Base
            | Charset
            | ContentSecurityPolicy
            | Description
            | Favicon
            | FormatDetection
            | GeoPosition
            | Google
            | Keywords
            | Link
            | Meta
            | OpenGraphWebsite
            | Page
            | ReferrerPolicy
            | Robots
            | Script
            | Stylesheet
            | ThemeColor
            | Title
            | TwitterCard
            | Verification
        ],
    ) -> "Head":
        """
        Used to extend an already initialized Head object.

        .. code-block::

            from pyhead import Head
            from pyhead.elements import Page, Description

            head = Head([Page(title="My Website")])

            head.extend([Description("This is my website.")])

        :param elements_:
        :return:
        """
        self._loop_elements(elements_)
        return self

    def compile(self, skip_title: bool = False) -> Markup:
        """
        Used to compile the elements in head.e dict.

        .. code-block::

            <head>
                {{ head.compile() }}
            </head>

        If you prefer to have the title rendered separately, you can use the skip_title parameter.

        .. code-block::

            <head>
                <title>{{ head.title }}</title>
                {{ head.compile(skip_title=True) }}
            </head>

        :param skip_title:
        :return:
        """
        render = []

        for key, element in self.e.items():
            if key == "title" and skip_title:
                continue

            render.append(str(element))

        return Markup("\n".join(render))


__all__ = ["__version__", "Head"]
