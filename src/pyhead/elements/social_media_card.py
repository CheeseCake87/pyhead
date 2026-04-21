from typing import Optional, Literal, Union

from .open_graph_website import OpenGraphWebsite
from .twitter_card import TwitterCard
from ..protocols import CompileDelayed


class SocialMediaCard:
    e: dict

    def __init__(
        self,
        card: Literal["summary", "summary_large_image"] = "summary_large_image",
        title: Optional[str] = None,
        description: Optional[str] = None,
        url: Optional[Union[str, CompileDelayed]] = None,
        image: Optional[Union[str, CompileDelayed]] = None,
        image_alt: Optional[str] = None,
        site_account: Optional[str] = None,
        creator_account: Optional[str] = None,
        site_name: Optional[str] = None,
        locale: str = "en_US",
    ) -> None:
        self.e = {
            "twitter_card": TwitterCard(
                card,
                title,
                description,
                url,
                image,
                image_alt,
                site_account,
                creator_account,
            ),
            "open_graph_website": OpenGraphWebsite(
                locale, site_name, title, description, url, image, image_alt
            ),
        }

    def __repr__(self) -> str:
        return "<SocialMediaCard ...>"
