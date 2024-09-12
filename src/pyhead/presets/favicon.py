from typing import Optional, Any

from markupsafe import Markup

from ..tags import LinkTag


class Favicon:
    ico_icon_href: Optional[LinkTag] = None
    png_icon_16_href: Optional[LinkTag] = None
    png_icon_32_href: Optional[LinkTag] = None
    png_icon_64_href: Optional[LinkTag] = None
    png_icon_96_href: Optional[LinkTag] = None
    png_icon_180_href: Optional[LinkTag] = None
    png_icon_196_href: Optional[LinkTag] = None
    png_apple_touch_icon_57_href: Optional[LinkTag] = None
    png_apple_touch_icon_60_href: Optional[LinkTag] = None
    png_apple_touch_icon_72_href: Optional[LinkTag] = None
    png_apple_touch_icon_76_href: Optional[LinkTag] = None
    png_apple_touch_icon_114_href: Optional[LinkTag] = None
    png_apple_touch_icon_120_href: Optional[LinkTag] = None
    png_apple_touch_icon_144_href: Optional[LinkTag] = None
    png_apple_touch_icon_152_href: Optional[LinkTag] = None
    png_apple_touch_icon_167_href: Optional[LinkTag] = None
    png_apple_touch_icon_180_href: Optional[LinkTag] = None
    png_mstile_70_href: Optional[LinkTag] = None
    png_mstile_270_href: Optional[LinkTag] = None
    png_mstile_310x150_href: Optional[LinkTag] = None
    png_mstile_310_href: Optional[LinkTag] = None

    icon_reference: dict[str, dict[str, str]] = {
        "ico_icon_href": {
            "rel": "icon",
            "sizes": "16x16 32x32",
            "type_": "image/x-icon",
            "generated_filename": "favicon.ico",
        },
        "png_icon_16_href": {
            "rel": "icon",
            "sizes": "16x16",
            "type_": "image/png",
            "generated_filename": "favicon-16x16.png",
        },
        "png_icon_32_href": {
            "rel": "icon",
            "sizes": "32x32",
            "type_": "image/png",
            "generated_filename": "favicon-32x32.png",
        },
        "png_icon_64_href": {
            "rel": "icon",
            "sizes": "64x64",
            "type_": "image/png",
            "generated_filename": "favicon-64x64.png",
        },
        "png_icon_96_href": {
            "rel": "icon",
            "sizes": "96x96",
            "type_": "image/png",
            "generated_filename": "favicon-96x96.png",
        },
        "png_icon_180_href": {
            "rel": "icon",
            "sizes": "180x180",
            "type_": "image/png",
            "generated_filename": "favicon-180x180.png",
        },
        "png_icon_196_href": {
            "rel": "icon",
            "sizes": "196x196",
            "type_": "image/png",
            "generated_filename": "favicon-196x196.png",
        },
        "png_apple_touch_icon_57_href": {
            "rel": "apple-touch-icon",
            "sizes": "57x57",
            "type_": "image/png",
            "generated_filename": "apple-touch-icon-57x57.png",
        },
        "png_apple_touch_icon_60_href": {
            "rel": "apple-touch-icon",
            "sizes": "60x60",
            "type_": "image/png",
            "generated_filename": "apple-touch-icon-60x60.png",
        },
        "png_apple_touch_icon_72_href": {
            "rel": "apple-touch-icon",
            "sizes": "72x72",
            "type_": "image/png",
            "generated_filename": "apple-touch-icon-72x72.png",
        },
        "png_apple_touch_icon_76_href": {
            "rel": "apple-touch-icon",
            "sizes": "76x76",
            "type_": "image/png",
            "generated_filename": "apple-touch-icon-76x76.png",
        },
        "png_apple_touch_icon_114_href": {
            "rel": "apple-touch-icon",
            "sizes": "114x114",
            "type_": "image/png",
            "generated_filename": "apple-touch-icon-114x114.png",
        },
        "png_apple_touch_icon_120_href": {
            "rel": "apple-touch-icon",
            "sizes": "120x120",
            "type_": "image/png",
            "generated_filename": "apple-touch-icon-120x120.png",
        },
        "png_apple_touch_icon_144_href": {
            "rel": "apple-touch-icon",
            "sizes": "144x144",
            "type_": "image/png",
            "generated_filename": "apple-touch-icon-144x144.png",
        },
        "png_apple_touch_icon_152_href": {
            "rel": "apple-touch-icon",
            "sizes": "152x152",
            "type_": "image/png",
            "generated_filename": "apple-touch-icon-152x152.png",
        },
        "png_apple_touch_icon_167_href": {
            "rel": "apple-touch-icon",
            "sizes": "167x167",
            "type_": "image/png",
            "generated_filename": "apple-touch-icon-167x167.png",
        },
        "png_apple_touch_icon_180_href": {
            "rel": "apple-touch-icon",
            "sizes": "180x180",
            "type_": "image/png",
            "generated_filename": "apple-touch-icon-180x180.png",
        },
        "png_mstile_70_href": {
            "rel": "msapplication-square70x70logo",
            "content": "image/png",
            "generated_filename": "mstile-70x70.png",
        },
        "png_mstile_270_href": {
            "rel": "msapplication-square270x270logo",
            "content": "image/png",
            "generated_filename": "mstile-270x270.png",
        },
        "png_mstile_310x150_href": {
            "rel": "msapplication-wide310x150logo",
            "content": "image/png",
            "generated_filename": "mstile-310x150.png",
        },
        "png_mstile_310_href": {
            "rel": "msapplication-wide310x150logo",
            "content": "image/png",
            "generated_filename": "mstile-310x150.png",
        },
    }

    def __init__(
        self,
        ico_icon_href: Optional[str] = None,
        png_icon_16_href: Optional[str] = None,
        png_icon_32_href: Optional[str] = None,
        png_icon_64_href: Optional[str] = None,
        png_icon_96_href: Optional[str] = None,
        png_icon_180_href: Optional[str] = None,
        png_icon_196_href: Optional[str] = None,
        png_apple_touch_icon_57_href: Optional[str] = None,
        png_apple_touch_icon_60_href: Optional[str] = None,
        png_apple_touch_icon_72_href: Optional[str] = None,
        png_apple_touch_icon_76_href: Optional[str] = None,
        png_apple_touch_icon_114_href: Optional[str] = None,
        png_apple_touch_icon_120_href: Optional[str] = None,
        png_apple_touch_icon_144_href: Optional[str] = None,
        png_apple_touch_icon_152_href: Optional[str] = None,
        png_apple_touch_icon_167_href: Optional[str] = None,
        png_apple_touch_icon_180_href: Optional[str] = None,
        png_mstile_70_href: Optional[str] = None,
        png_mstile_270_href: Optional[str] = None,
        png_mstile_310x150_href: Optional[str] = None,
        png_mstile_310_href: Optional[str] = None,
        *args: list[Any],
        **kwargs: dict[str, Any],
    ) -> None:
        set_kwargs = {
            "ico_icon_href": ico_icon_href,
            "png_icon_16_href": png_icon_16_href,
            "png_icon_32_href": png_icon_32_href,
            "png_icon_64_href": png_icon_64_href,
            "png_icon_96_href": png_icon_96_href,
            "png_icon_180_href": png_icon_180_href,
            "png_icon_196_href": png_icon_196_href,
            "png_apple_touch_icon_57_href": png_apple_touch_icon_57_href,
            "png_apple_touch_icon_60_href": png_apple_touch_icon_60_href,
            "png_apple_touch_icon_72_href": png_apple_touch_icon_72_href,
            "png_apple_touch_icon_76_href": png_apple_touch_icon_76_href,
            "png_apple_touch_icon_114_href": png_apple_touch_icon_114_href,
            "png_apple_touch_icon_120_href": png_apple_touch_icon_120_href,
            "png_apple_touch_icon_144_href": png_apple_touch_icon_144_href,
            "png_apple_touch_icon_152_href": png_apple_touch_icon_152_href,
            "png_apple_touch_icon_167_href": png_apple_touch_icon_167_href,
            "png_apple_touch_icon_180_href": png_apple_touch_icon_180_href,
            "png_mstile_70_href": png_mstile_70_href,
            "png_mstile_270_href": png_mstile_270_href,
            "png_mstile_310x150_href": png_mstile_310x150_href,
            "png_mstile_310_href": png_mstile_310_href,
        }

        for name, value in set_kwargs.items():
            if value:
                setattr(
                    self,
                    name,
                    LinkTag(
                        **{
                            k: v
                            for k, v in self.icon_reference[name].items()
                            if k not in ["generated_filename", "content"]
                        },
                        href=value,
                    ),
                )

        _, __ = args, kwargs

    def __repr__(self) -> str:
        attrs = " ".join(
            [
                str(getattr(self, o_link).href)
                for o_link in self.icon_reference
                if getattr(self, o_link) is not None
            ]
        )
        return f"<FavIcon {attrs}>".replace(" >", ">")

    def __str__(self) -> str:
        return Markup(self._compile())

    def __call__(self) -> str:
        return Markup(self._compile())

    def _compile(self) -> str:
        _ = [
            str(getattr(self, o_link))
            for o_link in self.icon_reference
            if getattr(self, o_link) is not None
        ]
        if _:
            return "\n".join(_)
        return ""
