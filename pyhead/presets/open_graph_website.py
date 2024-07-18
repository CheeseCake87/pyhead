from typing import Optional

from markupsafe import Markup

from ..tags import MetaTag


class OpenGraphWebsite:
    type: MetaTag
    locale: Optional[MetaTag] = None
    title: Optional[MetaTag] = None
    url: Optional[MetaTag] = None
    image: Optional[MetaTag] = None
    image_alt: Optional[MetaTag] = None
    description: Optional[MetaTag] = None
    site_name: Optional[MetaTag] = None

    _order: list = [
        "type",
        "locale",
        "site_name",
        "title",
        "description",
        "image",
        "image_alt",
        "url",
    ]

    def __init__(
        self,
        locale: str = "en_US",
        title: Optional[str] = None,
        image: Optional[str] = None,
        image_alt: Optional[str] = None,
        description: Optional[str] = None,
        site_name: Optional[str] = None,
        url: Optional[str] = None,
        *args,
        **kwargs,
    ):
        self.type = MetaTag(property_="og:type", content="website")
        self.locale = MetaTag(property_="og:locale", content=locale)

        if title is not None:
            self.title = MetaTag(property_="og:title", content=title)

        if url is not None:
            self.url = MetaTag(property_="og:url", content=url)

        if image is not None:
            self.image = MetaTag(property_="og:image", content=image)

        if image_alt is not None:
            self.image_alt = MetaTag(property_="og:image:alt", content=image_alt)

        if description is not None:
            self.description = MetaTag(property_="og:description", content=description)

        if site_name is not None:
            self.site_name = MetaTag(property_="og:site_name", content=site_name)

        _, __ = args, kwargs

    def __repr__(self):
        return (
            f"<OpenGraphWebsite type={self.type} locale={self.locale} "
            f"title={self.title} url={self.url} image={self.image} "
            f"image_alt={self.image_alt} description={self.description} "
            f"site_name={self.site_name}>"
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
