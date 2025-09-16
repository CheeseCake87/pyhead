from typing import Optional, Literal, Union

from markupsafe import Markup

from .meta import Meta
from ..protocols import CompileDelayed


class TwitterCard:
    unique: bool = True
    key: str = "twitter_card"

    _card: Meta
    _site_account: Optional[Meta] = None
    _creator_account: Optional[Meta] = None
    _title: Optional[Meta] = None
    _description: Optional[Meta] = None
    _image: Optional[Meta] = None
    _image_alt: Optional[Meta] = None
    _url: Optional[Meta] = None

    _order: list[str] = [
        "_card",
        "_site_account",
        "_creator_account",
        "_title",
        "_description",
        "_image",
        "_image_alt",
        "_url",
    ]

    def __init__(
        self,
        card: Literal["summary", "summary_large_image"] = "summary",
        title: Optional[str] = None,
        description: Optional[str] = None,
        url: Optional[Union[str, CompileDelayed]] = None,
        image: Optional[Union[str, CompileDelayed]] = None,
        image_alt: Optional[str] = None,
        site_account: Optional[str] = None,
        creator_account: Optional[str] = None,
    ) -> None:
        self._card = Meta(name="twitter:card", content=card)

        if site_account is not None:
            self._site_account = Meta(name="twitter:site", content=site_account)

        if creator_account is not None:
            self._creator_account = Meta(
                name="twitter:creator", content=creator_account
            )

        if title is not None:
            self._title = Meta(name="twitter:title", content=title)

        if description is not None:
            self._description = Meta(name="twitter:description", content=description)

        if image is not None:
            self._image = Meta(name="twitter:image", content=image)

        if image_alt is not None:
            self._image_alt = Meta(name="twitter:image:alt", content=image_alt)

        if url is not None:
            self._url = Meta(name="twitter:url", content=url)

    def __repr__(self) -> str:
        return (
            f"<TwitterCard card={self._card} site_account={self._site_account} "
            f"creator_account={self._creator_account} title={self._title} "
            f"description={self._description} image={self._image} "
            f"image_alt={self._image_alt} url={self._url}>"
        )

    def __str__(self) -> Markup:
        return Markup(self.compile())

    def __call__(self) -> Markup:
        return Markup(self.compile())

    def compile(self) -> str:
        _ = [
            str(getattr(self, o_tag))
            for o_tag in self._order
            if getattr(self, o_tag) is not None
        ]
        if _:
            return "\n".join(_)
        return ""
