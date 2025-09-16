from typing import Optional

from .charset import Charset
from .keywords import Keywords
from .meta import Meta
from .title import Title


class Page:
    e: dict

    _description: Optional[Meta] = None
    _keywords: Optional[Keywords] = None
    _subject: Optional[Meta] = None
    _rating: Optional[Meta] = None

    def __init__(
        self,
        title: str,
        description: Optional[str] = None,
        keywords: Optional[str | list] = None,
        subject: Optional[str] = None,
        rating: Optional[str] = None,
        charset: str = "utf-8",
        viewport: str = "width=device-width, initial-scale=1",
    ) -> None:
        self.e = {
            "title": Title(title),
            "charset": Charset(charset),
            "viewport": Meta(name="viewport", content=viewport),
        }

        if description is not None:
            self.e["description"] = Meta(name="description", content=description)

        if keywords is not None:
            if isinstance(keywords, str):
                self.e["keywords"] = Keywords(from_string=keywords)
            if isinstance(keywords, list):
                self.e["keywords"] = Keywords(from_list=keywords)

        if subject is not None:
            self.e["subject"] = Meta(name="subject", content=subject)

        if rating is not None:
            self.e["rating"] = Meta(name="rating", content=rating)

    def __repr__(self) -> str:
        return "<Page ...>"
