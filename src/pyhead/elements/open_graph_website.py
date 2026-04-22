from typing import Optional, Union

from .._base import BaseElement
from .meta import Meta
from ..protocols import CompileDelayed


class OpenGraphWebsite(BaseElement):
    key: str = "open_graph_website"

    _type: Meta
    _locale: Optional[Meta] = None
    _title: Optional[Meta] = None
    _url: Optional[Meta] = None
    _image: Optional[Meta] = None
    _image_alt: Optional[Meta] = None
    _description: Optional[Meta] = None
    _site_name: Optional[Meta] = None

    _order: list[str] = [
        "_type",
        "_locale",
        "_site_name",
        "_title",
        "_description",
        "_image",
        "_image_alt",
        "_url",
    ]

    def __init__(
        self,
        locale: str = "en_US",
        site_name: Optional[str] = None,
        title: Optional[str] = None,
        description: Optional[str] = None,
        url: Optional[Union[str, CompileDelayed]] = None,
        image: Optional[Union[str, CompileDelayed]] = None,
        image_alt: Optional[str] = None,
    ) -> None:
        self._type = Meta(property_="og:type", content="website")
        self._locale = Meta(property_="og:locale", content=locale)

        if title is not None:
            self._title = Meta(property_="og:title", content=title)

        if url is not None:
            self._url = Meta(property_="og:url", content=url)

        if image is not None:
            self._image = Meta(property_="og:image", content=image)

        if image_alt is not None:
            self._image_alt = Meta(property_="og:image:alt", content=image_alt)

        if description is not None:
            self._description = Meta(property_="og:description", content=description)

        if site_name is not None:
            self._site_name = Meta(property_="og:site_name", content=site_name)

    def __repr__(self) -> str:
        return (
            f"OpenGraphWebsite(type={self._type!r}, locale={self._locale!r}, "
            f"title={self._title!r}, url={self._url!r}, image={self._image!r}, "
            f"image_alt={self._image_alt!r}, description={self._description!r}, "
            f"site_name={self._site_name!r})"
        )

    def compile(self) -> str:
        rendered = [
            str(getattr(self, o_tag))
            for o_tag in self._order
            if getattr(self, o_tag) is not None
        ]
        return "\n".join(rendered) if rendered else ""
