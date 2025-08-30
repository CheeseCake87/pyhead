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

    _elements: list

    def __init__(
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
        This is the main class that controls the rendering of elements.

        Here's a simple example.

        .. highlight:: python
        .. code-block:: python

            from pyhead import Head
            from pyhead.elements import Page

            head = Head([Page(title="My Website")])

        :param elements_:
            A list of objects that can include any of the following types:
            ApplicationName, Base, Charset, ContentSecurityPolicy, Description,
            Favicon, FormatDetection, GeoPosition, Google, Keywords, Link, Meta,
            OpenGraphWebsite, Page, ReferrerPolicy, Robots, Script,
            SocialMediaCard, Stylesheet, ThemeColor, Title, TwitterCard,
            Verification.
        :type elements_: list[ApplicationName | Base | Charset |
            ContentSecurityPolicy | Description | Favicon | FormatDetection |
            GeoPosition | Google | Keywords | Link | Meta | OpenGraphWebsite |
            Page | ReferrerPolicy | Robots | Script | SocialMediaCard |
            Stylesheet | ThemeColor | Title | TwitterCard | Verification]
        """
        self.e = {}

        self._elements = elements_
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
        :return: None
        :rtype: None
        """
        for index, element in enumerate(elements_):
            if isinstance(element, Page):
                if self.e.get("title"):
                    del self.e["title"]

                if self.e.get("description"):
                    del self.e["description"]

                if self.e.get("keywords"):
                    del self.e["keywords"]

                if self.e.get("subject"):
                    del self.e["subject"]

                if self.e.get("rating"):
                    del self.e["rating"]

                for key, value in element.e.items():
                    self.e[key] = value
                continue

            if isinstance(element, SocialMediaCard):
                if self.e.get("twitter_card"):
                    del self.e["twitter_card"]

                if self.e.get("open_graph_website"):
                    del self.e["open_graph_website"]

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

        .. highlight:: python
        .. code-block:: python

            from pyhead import Head
            from pyhead.elements import Page, Description

            head = Head([Page(title="My Website")])

            head.extend([Description("This is my website.")])


        See head.copy if you want to create a deep copy to then extend.

        :param elements_:
        :return: The extended Head object.
        :rtype: Head
        """
        self._loop_elements(elements_)
        return self

    def copy(self) -> "Head":
        """
        Creates and returns a copy of the current object.

        The method generates a new instance of the same type by creating a deep
        copy of its underlying attributes.

        :return: A new instance of the same type as the original object with
                 copied data.
        :rtype: Head
        """
        return Head(self._elements)

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


__all__ = [
    "__version__",
    "Head",
    "ApplicationName",
    "Base",
    "Charset",
    "ContentSecurityPolicy",
    "Description",
    "Favicon",
    "FormatDetection",
    "GeoPosition",
    "Google",
    "Keywords",
    "Link",
    "Meta",
    "OpenGraphWebsite",
    "Page",
    "ReferrerPolicy",
    "Robots",
    "Script",
    "SocialMediaCard",
    "Stylesheet",
    "ThemeColor",
    "Title",
    "TwitterCard",
    "Verification",
]
