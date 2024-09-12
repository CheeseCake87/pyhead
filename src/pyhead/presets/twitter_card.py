from typing import Optional, Literal

from markupsafe import Markup

from ..tags import MetaTag


class TwitterCard:
    card: MetaTag
    site_account: Optional[MetaTag] = None
    creator_account: Optional[MetaTag] = None
    title: Optional[MetaTag] = None
    description: Optional[MetaTag] = None
    image: Optional[MetaTag] = None
    image_alt: Optional[MetaTag] = None
    url: Optional[MetaTag] = None

    _order: list = [
        "card",
        "site_account",
        "creator_account",
        "title",
        "description",
        "image",
        "image_alt",
        "url",
    ]

    def __init__(
        self,
        card: Literal["summary", "summary_large_image"] = "summary",
        site_account: Optional[str] = None,
        creator_account: Optional[str] = None,
        title: Optional[str] = None,
        description: Optional[str] = None,
        image: Optional[str] = None,
        image_alt: Optional[str] = None,
        url: Optional[str] = None,
        *args,
        **kwargs,
    ):
        self.card = MetaTag(name="twitter:card", content=card)

        if site_account is not None:
            self.site_account = MetaTag(name="twitter:site", content=site_account)

        if creator_account is not None:
            self.creator_account = MetaTag(
                name="twitter:creator", content=creator_account
            )

        if title is not None:
            self.title = MetaTag(name="twitter:title", content=title)

        if description is not None:
            self.description = MetaTag(name="twitter:description", content=description)

        if image is not None:
            self.image = MetaTag(name="twitter:image", content=image)

        if image_alt is not None:
            self.image_alt = MetaTag(name="twitter:image:alt", content=image_alt)

        if url is not None:
            self.url = MetaTag(name="twitter:url", content=url)

        _, __ = args, kwargs

    def __repr__(self):
        return (
            f"<TwitterCard card={self.card} site_account={self.site_account} "
            f"creator_account={self.creator_account} title={self.title} "
            f"description={self.description} image={self.image} "
            f"image_alt={self.image_alt} url={self.url}>"
        )

    def __str__(self):
        return Markup(self._compile())

    def __call__(self, *args, **kwargs):
        return Markup(self._compile())

    def _compile(self):
        _ = [
            str(getattr(self, o_tag))
            for o_tag in self._order
            if getattr(self, o_tag) is not None
        ]
        if _:
            return "\n".join(_)
        return ""
