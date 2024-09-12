from typing import Optional, Any

from markupsafe import Markup

from ..tags import MetaTag


class GeoPosition:
    icbm: Optional[MetaTag] = None
    geo_position: Optional[MetaTag] = None
    geo_region: Optional[MetaTag] = None
    geo_placename: Optional[MetaTag] = None

    _order: list[str] = [
        "icbm",
        "geo_position",
        "geo_region",
        "geo_placename",
    ]

    def __init__(
        self,
        icbm: Optional[str] = None,
        geo_position: Optional[str] = None,
        geo_region: Optional[str] = None,
        geo_placename: Optional[str] = None,
            *args: list[Any],
            **kwargs: dict[str, Any],
    ) -> None:
        if icbm is not None:
            self.icbm = MetaTag(name="ICBM", content=icbm)

        if geo_position is not None:
            self.geo_position = MetaTag(name="geo.position", content=geo_position)

        if geo_region is not None:
            self.geo_region = MetaTag(name="geo.region", content=geo_region)

        if geo_placename is not None:
            self.geo_placename = MetaTag(name="geo.placename", content=geo_placename)

        _, __ = args, kwargs

    def __repr__(self) -> str:
        return (
            f"<GeoPosition icbm={self.icbm} geo_position={self.geo_position} "
            f"geo_region={self.geo_region} geo_placename={self.geo_placename}>"
        )

    def __str__(self) -> Markup:
        return Markup(self._compile())

    def __call__(self) -> Markup:
        return Markup(self._compile())

    def _compile(self) -> str:
        _ = [
            str(getattr(self, o_tag))
            for o_tag in self._order
            if getattr(self, o_tag) is not None
        ]
        if _:
            return "\n".join(_)
        return ""
