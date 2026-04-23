from typing import Optional

from .charset import Charset
from .description import Description
from .keywords import Keywords
from .meta import Meta
from .rating import Rating
from .subject import Subject
from .title import Title
from .viewport import Viewport


class Page:
    e: dict

    _description: Optional[Meta] = None
    _keywords: Optional[Keywords] = None
    _subject: Optional[Meta] = None
    _rating: Optional[Meta] = None

    def __init__(
        self,
        title: str | Title,
        description: Optional[str | Description] = None,
        keywords: Optional[str | list | Keywords] = None,
        subject: Optional[str | Subject] = None,
        rating: Optional[str | Rating] = None,
        charset: str = "utf-8",
        viewport: Viewport | str = "width=device-width, initial-scale=1",
    ) -> None:
        if isinstance(viewport, Viewport):
            viewport_element: Meta | Viewport = viewport
        else:
            viewport_element = Meta(name="viewport", content=viewport)

        title_element = title if isinstance(title, Title) else Title(title)

        self.e = {
            "charset": Charset(charset),
            "title": title_element,
            "viewport": viewport_element,
        }

        if description is not None:
            if isinstance(description, Description):
                self.e["description"] = description
            else:
                self.e["description"] = Meta(name="description", content=description)

        if keywords is not None:
            if isinstance(keywords, Keywords):
                self.e["keywords"] = keywords
            elif isinstance(keywords, str):
                self.e["keywords"] = Keywords(from_string=keywords)
            elif isinstance(keywords, list):
                self.e["keywords"] = Keywords(from_list=keywords)

        if subject is not None:
            if isinstance(subject, Subject):
                self.e["subject"] = subject
            else:
                self.e["subject"] = Meta(name="subject", content=subject)

        if rating is not None:
            if isinstance(rating, Rating):
                self.e["rating"] = rating
            else:
                self.e["rating"] = Meta(name="rating", content=rating)

    def __repr__(self) -> str:
        return "<Page ...>"
