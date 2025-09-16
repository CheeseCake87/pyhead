from typing import Optional

from markupsafe import Markup

from .meta import Meta


class GeoPosition:
    unique: bool = True
    key: str = "geo_position"

    _icbm: Optional[Meta] = None
    _geo_position: Optional[Meta] = None
    _geo_region: Optional[Meta] = None
    _geo_placename: Optional[Meta] = None

    _order: list[str] = [
        "_icbm",
        "_geo_position",
        "_geo_region",
        "_geo_placename",
    ]

    def __init__(
        self,
        icbm: Optional[str] = None,
        geo_position: Optional[str] = None,
        geo_region: Optional[str] = None,
        geo_placename: Optional[str] = None,
    ) -> None:
        if icbm is not None:
            self._icbm = Meta(name="ICBM", content=icbm)

        if geo_position is not None:
            self._geo_position = Meta(name="geo.position", content=geo_position)

        if geo_region is not None:
            self._geo_region = Meta(name="geo.region", content=geo_region)

        if geo_placename is not None:
            self._geo_placename = Meta(name="geo.placename", content=geo_placename)

    def __repr__(self) -> str:
        return (
            f"<GeoPosition icbm={self._icbm} geo_position={self._geo_position} "
            f"geo_region={self._geo_region} geo_placename={self._geo_placename}>"
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
