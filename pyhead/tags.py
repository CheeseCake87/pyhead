from typing import Optional, Literal

from markupsafe import Markup


class LinkTag:
    rel: str = None
    href: str = None
    sizes: str = None
    type: str = None
    hreflang: str = None

    _rel: str = None
    _href: str = None
    _sizes: str = None
    _type: str = None
    _hreflang: str = None

    def __init__(
        self,
        rel: str,
        href: Optional[str] = None,
        sizes: Optional[str] = None,
        type_: Optional[str] = None,
        hreflang: Optional[str] = None,
    ):
        self.rel = rel
        self.href = href
        self.sizes = sizes
        self.type = type_
        self.hreflang = hreflang

        self._rel = f'rel="{self.rel}" '
        self._href = f'href="{self.href}" ' if self.href is not None else ""
        self._sizes = f'sizes="{self.sizes}" ' if self.sizes is not None else ""
        self._type = f'type="{self.type}" ' if self.type is not None else ""
        self._hreflang = (
            f'hreflang="{self.hreflang}" ' if self.hreflang is not None else ""
        )

    def __repr__(self):
        return Markup(
            f"<LinkTag {self._rel}{self._href}{self._sizes}{self._type}{self._hreflang}>".replace(
                " >", ">"
            )
        )

    def __str__(self):
        return Markup(self._compile())

    def __call__(self, *args, **kwargs):
        return Markup(self._compile())

    def _compile(self):
        return f"<link {self._rel}{self._href}{self._sizes}{self._type}{self._hreflang}>".replace(
            " >", ">"
        )


class FavIcon:
    ico_icon_16_32_href: Optional[LinkTag] = None
    png_icon_16_href: Optional[LinkTag] = None
    png_icon_32_href: Optional[LinkTag] = None
    png_icon_128_href: Optional[LinkTag] = None
    png_icon_180_href: Optional[LinkTag] = None
    png_icon_192_href: Optional[LinkTag] = None
    png_icon_228_href: Optional[LinkTag] = None
    png_icon_512_href: Optional[LinkTag] = None
    apple_touch_icon: Optional[LinkTag] = None

    _order: list = [
        "ico_icon_16_32_href",
        "png_icon_16_href",
        "png_icon_32_href",
        "png_icon_128_href",
        "png_icon_180_href",
        "png_icon_192_href",
        "png_icon_228_href",
        "png_icon_512_href",
        "apple_touch_icon",
    ]

    def __init__(
        self,
        ico_icon_16_32_href: Optional[str] = None,
        png_icon_16_href: Optional[str] = None,
        png_icon_32_href: Optional[str] = None,
        png_icon_128_href: Optional[str] = None,
        png_icon_180_href: Optional[str] = None,
        png_icon_192_href: Optional[str] = None,
        png_icon_228_href: Optional[str] = None,
        png_icon_512_href: Optional[str] = None,
        set_icon_192_to_apple_touch_icon: bool = False,
        *args,
        **kwargs,
    ):
        if ico_icon_16_32_href is not None:
            self.ico_icon_16_32_href = LinkTag(
                "icon", ico_icon_16_32_href, "16x16 32x32", "image/x-icon"
            )

        if png_icon_16_href is not None:
            self.png_icon_16_href = LinkTag(
                "icon", png_icon_16_href, "16x16", "image/png"
            )

        if png_icon_32_href is not None:
            self.png_icon_32_href = LinkTag(
                "icon", png_icon_32_href, "32x32", "image/png"
            )

        if png_icon_128_href is not None:
            self.png_icon_128_href = LinkTag(
                "icon", png_icon_128_href, "128x128", "image/png"
            )

        if png_icon_180_href is not None:
            self.png_icon_180_href = LinkTag(
                "icon", png_icon_180_href, "180x180", "image/png"
            )

        if png_icon_192_href is not None:
            self.png_icon_192_href = LinkTag(
                "icon", png_icon_192_href, "192x192", "image/png"
            )
            if set_icon_192_to_apple_touch_icon:
                self.apple_touch_icon = LinkTag("apple-touch-icon", png_icon_192_href)

        if png_icon_228_href is not None:
            self.png_icon_228_href = LinkTag(
                "icon", png_icon_228_href, "228x228", "image/png"
            )

        if png_icon_512_href is not None:
            self.png_icon_228_href = LinkTag(
                "icon", png_icon_512_href, "512x512", "image/png"
            )

        _, __ = args, kwargs

    def __repr__(self):
        _ico_icon_16_32_href = (
            f'ico_icon_16_32_href="{self.ico_icon_16_32_href}" '
            if self.ico_icon_16_32_href is not None
            else ""
        )
        _png_icon_16_href = (
            f'png_icon_16_href="{self.png_icon_16_href}" '
            if self.png_icon_16_href is not None
            else ""
        )
        _png_icon_32_href = (
            f'png_icon_32_href="{self.png_icon_32_href}" '
            if self.png_icon_32_href is not None
            else ""
        )
        _png_icon_128_href = (
            f'png_icon_128_href="{self.png_icon_128_href}" '
            if self.png_icon_128_href is not None
            else ""
        )
        _png_icon_180_href = (
            f'png_icon_180_href="{self.png_icon_180_href}" '
            if self.png_icon_180_href is not None
            else ""
        )
        _png_icon_192_href = (
            f'png_icon_192_href="{self.png_icon_192_href}" '
            if self.png_icon_192_href is not None
            else ""
        )
        _png_icon_228_href = (
            f'png_icon_228_href="{self.png_icon_228_href}" '
            if self.png_icon_228_href is not None
            else ""
        )
        _png_icon_512_href = (
            f'png_icon_512_href="{self.png_icon_512_href}" '
            if self.png_icon_512_href is not None
            else ""
        )
        _apple_touch_icon = (
            f'apple_touch_icon="{self.apple_touch_icon}" '
            if self.apple_touch_icon is not None
            else ""
        )
        return (
            f"<FavIcon {_ico_icon_16_32_href}"
            f"{_png_icon_16_href}"
            f"{_png_icon_32_href}"
            f"{_png_icon_128_href}"
            f"{_png_icon_180_href}"
            f"{_png_icon_192_href}"
            f"{_png_icon_228_href}"
            f"{_png_icon_512_href}"
            f"{_apple_touch_icon}"
            ">".replace(" >", ">")
        )

    def __str__(self):
        return Markup(self._compile())

    def __call__(self, *args, **kwargs):
        return Markup(self._compile())

    def _compile(self):
        _ = [
            str(getattr(self, o_link))
            for o_link in self._order
            if getattr(self, o_link) is not None
        ]
        if _:
            return "\n".join(_)
        return ""


class MetaTag:
    name: str = None
    content: str = None
    is_http_equiv: bool = False

    def __init__(self, name: str, content: str, is_http_equiv: bool = False):
        self.name = name
        self.content = content
        self.is_http_equiv = is_http_equiv

    def __repr__(self):
        return (
            f'<MetaTag {"http-equiv" if self.is_http_equiv else "name"}'
            f'="{self.name}" content="{self.content}">'
        )

    def __str__(self):
        return Markup(self._compile())

    def __call__(self, *args, **kwargs):
        return Markup(self._compile())

    def _compile(self):
        return (
            f'<meta {"http-equiv" if self.is_http_equiv else "name"}'
            f'="{self.name}" content="{self.content}">'
        )

    def replace_content(self, content: str):
        self.content = content
        return self


class Charset:
    charset: str = None

    def __init__(self, charset: str = "utf-8"):
        self.charset = charset

    def __repr__(self):
        return f'<Charset charset="{self.charset}">'

    def __str__(self):
        return Markup(self._compile())

    def __call__(self, *args, **kwargs):
        return Markup(self._compile())

    def _compile(self):
        return f'<meta charset="{self.charset}">'

    def replace(self, charset: str):
        self.charset = charset
        return self


class Base:
    base: str = None

    def __init__(self, base: str):
        self.base = base

    def __repr__(self):
        return f'<Base base="{self.base}">'

    def __str__(self):
        return Markup(self._compile())

    def __call__(self, *args, **kwargs):
        return Markup(self._compile())

    def _compile(self):
        return f'<base href="{self.base}">'

    def replace(self, base: str):
        self.base = base
        return self


class Title:
    title: str = None
    _exclude_title_tags: bool = False

    def __init__(
        self,
        page_title: str,
        _exclude_title_tags: bool = False,
    ):
        self.title = page_title
        self._exclude_title_tags = _exclude_title_tags

    def __repr__(self):
        return f'<Title page_title="{self.title}">'

    def __str__(self):
        return Markup(f"{self._compile()}")

    def __call__(self, *args, **kwargs):
        return Markup(f"{self._compile()}")

    def _compile(self):
        if self._exclude_title_tags:
            return f"{self.title}"
        else:
            return f"<title>{self.title}</title>"

    def replace(self, page_title: str):
        self.title = page_title
        return self

    def append(self, more_page_title: str, separator: str):
        self.title = self.title + separator + more_page_title
        return self

    def prepend(self, more_page_title: str, separator: str):
        self.title = more_page_title + separator + self.title
        return self


class Keywords:
    keywords: list = None

    def __init__(self):
        pass

    def __repr__(self):
        return f'<Keywords page_keywords="{self.keywords}">'

    def __str__(self):
        return Markup(self._compile())

    def __call__(self, *args, **kwargs):
        return Markup(self._compile())

    def _compile(self):
        return f'<meta name="keywords" content="{", ".join(self.keywords)}">'

    def set_from_string(self, keywords: str):
        self.keywords = keywords.replace(" ", "").split(",")
        return self

    def set_from_list(self, keywords: list):
        self.keywords = keywords
        return self

    def str_append(self, more_keywords: str):
        self.keywords.append(more_keywords.replace(" ", "").split(","))
        return self

    def list_append(self, more_keywords: list):
        self.keywords.append(more_keywords)
        return self


class Google:
    googlebot: Optional[MetaTag] = None
    sitelinkssearchbox: Optional[MetaTag] = None
    no_translate: Optional[MetaTag] = None

    _googlebot: list

    _order: list = [
        "googlebot",
        "sitelinkssearchbox",
        "no_translate",
    ]

    def __init__(
        self,
        googlebot: Optional[str] = None,
        no_sitelinks_search_box: bool = False,
        no_translate: bool = False,
        *args,
        **kwargs,
    ):
        self._googlebot = []

        if googlebot is not None:
            self.googlebot = MetaTag("googlebot", googlebot)

        if no_sitelinks_search_box:
            self.sitelinks = MetaTag("google", "nositelinkssearchbox")

        if no_translate:
            self.no_translate = MetaTag("google", "notranslate")

        _, __ = args, kwargs

    def __repr__(self):
        return (
            f"<Google googlebot={self.googlebot} sitelinkssearchbox={self.sitelinkssearchbox} "
            f"no_translate={self.no_translate}>"
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


class Verification:
    google: Optional[MetaTag] = None
    yandex: Optional[MetaTag] = None
    bing: Optional[MetaTag] = None
    alexa: Optional[MetaTag] = None
    pinterest: Optional[MetaTag] = None
    norton: Optional[MetaTag] = None

    _order: list = [
        "google",
        "yandex",
        "bing",
        "alexa",
        "pinterest",
        "norton",
    ]

    def __init__(
        self,
        google: Optional[str] = None,
        yandex: Optional[str] = None,
        bing: Optional[str] = None,
        alexa: Optional[str] = None,
        pinterest: Optional[str] = None,
        norton: Optional[str] = None,
        *args,
        **kwargs,
    ):
        if google is not None:
            self.google = MetaTag("google-site-verification", google)

        if yandex is not None:
            self.yandex = MetaTag("yandex-verification", yandex)

        if bing is not None:
            self.bing = MetaTag("msvalidate.01", bing)

        if alexa is not None:
            self.alexa = MetaTag("alexaVerifyID", alexa)

        if pinterest is not None:
            self.pinterest = MetaTag("p:domain_verify", pinterest)

        if norton is not None:
            self.norton = MetaTag("norton-safeweb-site-verification", norton)

        _, __ = args, kwargs

    def __repr__(self):
        return (
            f"<Verification google={self.google} yandex={self.yandex} "
            f"bing={self.bing} alexa={self.alexa} pinterest={self.pinterest} "
            f"norton={self.norton}>"
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


class ReferrerPolicy:
    policy: str = None
    fallback: str = None

    def __init__(self, policy: str, fallback: Optional[str] = None, *args, **kwargs):
        self.policy = policy
        self.fallback = fallback

        _, __ = args, kwargs

    def __repr__(self):
        return f'<ReferrerPolicy content="{self.policy}" fallback="{self.fallback}">'

    def __str__(self):
        return Markup(self._compile())

    def __call__(self, *args, **kwargs):
        return Markup(self._compile())

    def _compile(self):
        _ = []
        if self.fallback is not None:
            _.append(self.fallback)

        _.append(self.policy)

        return f'<meta name="referrer" content="{", ".join(_)}">'

    def replace_content(self, content: str, fallback: Optional[str] = None):
        self.policy = content
        self.fallback = fallback
        return self


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
        self.type = MetaTag("og:type", "website")
        self.locale = MetaTag("og:locale", locale)

        if title is not None:
            self.title = MetaTag("og:title", title)

        if url is not None:
            self.url = MetaTag("og:url", url)

        if image is not None:
            self.image = MetaTag("og:image", image)

        if image_alt is not None:
            self.image_alt = MetaTag("og:image:alt", image_alt)

        if description is not None:
            self.description = MetaTag("og:description", description)

        if site_name is not None:
            self.site_name = MetaTag("og:site_name", site_name)

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
        self.card = MetaTag("twitter:card", card)

        if site_account is not None:
            self.site_account = MetaTag("twitter:site", site_account)

        if creator_account is not None:
            self.creator_account = MetaTag("twitter:creator", creator_account)

        if title is not None:
            self.title = MetaTag("twitter:title", title)

        if description is not None:
            self.description = MetaTag("twitter:description", description)

        if image is not None:
            self.image = MetaTag("twitter:image", image)

        if image_alt is not None:
            self.image_alt = MetaTag("twitter:image:alt", image_alt)

        if url is not None:
            self.url = MetaTag("twitter:url", url)

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


class GeoPosition:
    icbm: Optional[MetaTag] = None
    geo_position: Optional[MetaTag] = None
    geo_region: Optional[MetaTag] = None
    geo_placename: Optional[MetaTag] = None

    _order: list = [
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
        *args,
        **kwargs,
    ):
        if icbm is not None:
            self.icbm = MetaTag("ICBM", icbm)

        if geo_position is not None:
            self.geo_position = MetaTag("geo.position", geo_position)

        if geo_region is not None:
            self.geo_region = MetaTag("geo.region", geo_region)

        if geo_placename is not None:
            self.geo_placename = MetaTag("geo.placename", geo_placename)

        _, __ = args, kwargs

    def __repr__(self):
        return (
            f"<GeoPosition icbm={self.icbm} geo_position={self.geo_position} "
            f"geo_region={self.geo_region} geo_placename={self.geo_placename}>"
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
