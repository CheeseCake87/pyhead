from typing import Optional, Literal

from .meta import Meta
from .open_graph_website import OpenGraphWebsite
from .twitter_card import TwitterCard


class SocialMediaCard:
    e: dict

    _type: Meta
    _locale: Optional[Meta] = None
    _site_name: Optional[Meta] = None
    _card: Meta
    _site_account: Optional[Meta] = None
    _creator_account: Optional[Meta] = None
    _title: Optional[Meta] = None
    _description: Optional[Meta] = None
    _image: Optional[Meta] = None
    _image_alt: Optional[Meta] = None
    _url: Optional[Meta] = None

    def __init__(
        self,
        card: Literal["summary", "summary_large_image"] = "summary_large_image",
        title: Optional[str] = None,
        description: Optional[str] = None,
        url: Optional[str] = None,
        image: Optional[str] = None,
        image_alt: Optional[str] = None,
        site_account: Optional[str] = None,
        creator_account: Optional[str] = None,
        site_name: Optional[str] = None,
        locale: str = "en_US",
    ) -> None:
        self.e = {}

        self.e["twitter_card"] = TwitterCard(
            card,
            title,
            description,
            url,
            image,
            image_alt,
            site_account,
            creator_account,
        )
        self.e["open_graph_website"] = OpenGraphWebsite(
            locale, site_name, title, description, url, image, image_alt
        )

    def __repr__(self) -> str:
        return "<SocialMediaCard ...>"
