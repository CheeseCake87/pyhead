from copy import deepcopy
from glob import escape
from typing import Optional, TypeAlias

from markupsafe import Markup

from .__version__ import __version__
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
    Rating,
    ReferrerPolicy,
    Robots,
    Script,
    SocialMediaCard,
    Stylesheet,
    Subject,
    ThemeColor,
    Title,
    TwitterCard,
    Verification,
    Viewport,
)

HeadElement: TypeAlias = (
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
    | Rating
    | ReferrerPolicy
    | Robots
    | Script
    | SocialMediaCard
    | Stylesheet
    | Subject
    | ThemeColor
    | Title
    | TwitterCard
    | Verification
    | Viewport
)


class Head:
    e: dict  # Element ID: Element Class

    render_head_tag: bool = True
    render_title_tag: Optional[str] = None

    _elements: list[HeadElement]

    def __init__(self, elements_: list[HeadElement]) -> None:
        """
        This is the main class that controls the rendering of elements.

        Here's a simple example.

        .. highlight:: python
        .. code-block:: python

            from pyhead import Head
            from pyhead.elements import Page

            head = Head([Page(title="My Website")])

        :param elements_:
            A list of head elements. See ``HeadElement`` for the accepted types.
        :type elements_: list[HeadElement]
        """
        self.e = {}

        self._elements = elements_
        self._loop_elements(elements_)

    def _loop_elements(self, elements_: list[HeadElement]) -> None:
        """
        A private method that loops through elements and adds them to head.e dict.

        :param elements_:
        :return: None
        :rtype: None
        """
        for element in elements_:
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

            key = getattr(element, "key", None)
            if key:
                self.e[str(key)] = element
            else:
                fallback = str(len(self.e))
                while fallback in self.e:
                    fallback = str(int(fallback) + 1)
                self.e[fallback] = element

        if self.e.get("title"):
            self.render_title_tag = self.e["title"].title_

    def extend(self, elements_: list[HeadElement]) -> "Head":
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
        self._elements = [*self._elements, *elements_]
        self._loop_elements(elements_)
        return self

    def copy(self) -> "Head":
        """
        Creates and returns a deep copy of the current Head.

        Element instances are duplicated so that mutations on the copy do not
        affect the original.

        :return: A new Head whose elements are independent of the original's.
        :rtype: Head
        """
        return Head(deepcopy(self._elements))

    def copy_extend(self, elements_: list[HeadElement]) -> "Head":
        """
        Used to copy and extend an already initialized Head object.

        .. highlight:: python
        .. code-block:: python

            from pyhead import Head
            from pyhead.elements import Page, Description

            head = Head([Page(title="My Website")])

            head = head.copy_extend([Description("This is my website.")])

        :param elements_:
        :return: The copied and extended Head object.
        :rtype: Head
        """
        self._elements = [*self._elements, *elements_]
        return Head(deepcopy(self._elements))

    def cp(self) -> "Head":
        """
        Shortcut for copy.

        Creates and returns a deep copy of the current Head.

        Element instances are duplicated so that mutations on the copy do not
        affect the original.

        :return: A new Head whose elements are independent of the original's.
        :rtype: Head
        """
        return self.copy()

    def cpe(self, elements_: list[HeadElement]) -> "Head":
        """
        Shortcut for copy_extend.

        Used to copy and extend an already initialized Head object.

        .. highlight:: python
        .. code-block:: python

            from pyhead import Head
            from pyhead.elements import Page, Description

            head = Head([Page(title="My Website")])

            head = head.cpe([Description("This is my website.")])

        :param elements_:
        :return: The copied and extended Head object.
        :rtype: Head
        """
        return self.copy_extend(elements_)

    def compile(
        self, render_head_tag: bool = True, render_title_tag: bool = True
    ) -> Markup:
        """
        Used to compile the elements in head.e dict.

        .. code-block::

            <html>
            {{ head.compile() }}
            <body>
            ...
            </body>
            </html>

        If you prefer to have the head and the title tag rendered separately,
        you can use the render_head_tag and render_title_tag parameters.

        .. code-block::

            <head>
                <title>{{ head.title }}</title>
                {{ head.compile(render_head_tag = False, render_title_tag = False) }}
            </head>

        :param render_head_tag: If False, the head tag will not be rendered.
        :param render_title_tag: If False, the title tag will not be rendered.
        :return:
        """
        render = ["<head>" if render_head_tag else ""]

        for key, element in self.e.items():
            if key == "title" and not render_title_tag:
                continue

            render.append(str(element))

        if render_head_tag:
            render.append("</head>")

        return Markup("\n".join(render))

    def title(self) -> str:
        if self.e.get("title"):
            return escape(self.e["title"].title_)
        return ""

    def __str__(self) -> Markup:
        return self.compile()

    def __html__(self) -> Markup:
        return self.compile()


class HeadClass:
    elements: list[HeadElement]

    def __new__(cls):
        if cls is HeadClass:
            raise TypeError(
                "HeadClass is meant to be subclassed. "
                "Define a subclass with `elements = [...]` and instantiate that."
            )
        if not hasattr(cls, "elements"):
            raise TypeError(
                f"{cls.__name__} must define an `elements` class attribute "
                f"(a list of head elements)."
            )
        return Head(cls.elements)


__all__ = [
    "__version__",
    "Head",
    "HeadClass",
    "HeadElement",
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
    "Rating",
    "ReferrerPolicy",
    "Robots",
    "Script",
    "SocialMediaCard",
    "Stylesheet",
    "Subject",
    "ThemeColor",
    "Title",
    "TwitterCard",
    "Verification",
    "Viewport",
]
