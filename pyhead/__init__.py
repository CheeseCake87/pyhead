"""A simple python package to generate HTML head tags."""

import hashlib

from typing import Optional, Union, Literal, List

from markupsafe import Markup

from .presets import (
    Favicon,
    Charset,
    Keywords,
    Google,
    Verification,
    OpenGraphWebsite,
    TwitterCard,
    GeoPosition,
)
from .tags import (
    LinkTag,
    MetaTag,
    TitleTag,
    BaseTag,
    ScriptTag,
)

__version__ = "3.0"


class Head:
    _exclude_title_tags: bool

    # Preset tags
    _t__charset: Charset
    _t__title: Optional[TitleTag] = None
    _t__base: Optional[BaseTag] = None
    _t__keywords: Optional[Keywords] = None
    _t__google: Optional[Google] = None
    _t__verification: Optional[Verification] = None
    _t__opengraph_website: Optional[OpenGraphWebsite] = None
    _t__twitter_card: Optional[TwitterCard] = None
    _t__geo_position: Optional[GeoPosition] = None

    # Build on run tags
    _t__viewport: MetaTag
    _t__content_security_policy: Optional[MetaTag] = None
    _t__application_name: Optional[MetaTag] = None
    _t__generator: Optional[MetaTag] = None
    _t__theme_color: Optional[MetaTag] = None
    _t__description: Optional[MetaTag] = None
    _t__subject: Optional[MetaTag] = None
    _t__rating: Optional[MetaTag] = None
    _t__robots: Optional[MetaTag] = None
    _t__referrer_policy: Optional[MetaTag] = None
    _t__detect_telephone_numbers: Optional[MetaTag] = None

    _set_meta_tags: dict
    _set_link_tags: dict
    _set_script_tags: dict

    _title_tag_appends: List[tuple] = None
    _title_tag_prepends: List[tuple] = None
    _keywords: List[str] = None

    _top_level_tags = [
        "_t__charset",
        "_t__viewport",
        "_t__base",
    ]
    _order = [
        "_t__content_security_policy",
        "_t__application_name",
        "_t__generator",
        "_t__theme_color",
        "_t__description",
        "_t__keywords",
        "_t__subject",
        "_t__rating",
        "_t__robots",
        "_t__referrer_policy",
        "_t__google",
        "_t__verification",
        "_t__opengraph_website",
        "_t__twitter_card",
        "_t__geo_position",
        "_t__detect_telephone_numbers",
    ]

    def __init__(
        self,
        charset: str = "utf-8",
        viewport: Optional[str] = None,
        content_security_policy: Optional[str] = None,
        application_name: Optional[str] = None,
        generator: Optional[str] = None,
        theme_color: Optional[str] = None,
        title: Optional[str] = None,
        base: Optional[str] = None,
        description: Optional[str] = None,
        keywords: Optional[Union[str, list]] = None,
        subject: Optional[str] = None,
        rating: Optional[str] = None,
        robots: Optional[str] = None,
        referrer_policy: Optional[str] = None,
        google: Optional[dict] = None,
        verification: Optional[dict] = None,
        opengraph_website: Optional[dict] = None,
        twitter_card: Optional[dict] = None,
        geo_position: Optional[dict] = None,
        disable_detection_of_telephone_numbers: bool = False,
        exclude_title_tags: bool = False,
        exclude_viewport: bool = False,
        favicon: Optional[dict] = None,
    ):
        """
        viewport is set to "width=device-width, initial-scale=1" by default.
        Set exclude_viewport to True to exclude the tag.

        content_security_policy is set to "default-src 'self'" by default.
        Set exclude_content_security_policy to True to exclude the tag.

        detect_telephone_numbers is set to "telephone=no" by default.
        Set exclude_detect_telephone_numbers to True to exclude the tag.

        .. code-block::

            google: {
                'googlebot': 'index, follow',
                'no_sitelinks_search_box': False,
                'no_translate': False,
            }

        .. code-block::

            verification: {
                'google': '1234567890',
                'yandex': '1234567890',
                'bing': '1234567890',
                'alexa': '1234567890',
                'pinterest': '1234567890',
                'norton': '1234567890',
            }

        .. code-block::

            opengraph_website: {
                'site_name': 'Example',
                'title': 'Example',
                'description': 'Example',
                'url': 'https://example.com',
                'image': 'https://example.com/image.png',
                'image_alt': 'Example',
                'locale': 'en_US',
            }

        .. code-block::

            twitter_card: {
                'card': 'summary',
                'site_account': '@example',
                'creator_account': '@example',
                'title': 'Example',
                'description': 'Example',
                'image': 'https://example.com/image.png',
                'image_alt': 'Example',
            }

        .. code-block::

            geo_position: {
                'icbm': '55.86013028402754, -4.252019430273945',
                'geo_position': '55.86013028402754;-4.252019430273945',
                'geo_region': 'en_GB',
                'geo_placename': 'Duke of Wellington',
            }

        """

        self._exclude_title_tags = exclude_title_tags
        self._set_meta_tags = {}
        self._set_link_tags = {}
        self._set_script_tags = {}

        self._t__charset = Charset(charset)

        self._title_tag_appends = []
        self._title_tag_prepends = []

        # Preset tags

        if base is not None:
            self._t__base = BaseTag(base)

        if title is not None:
            self._t__title = TitleTag(title, self._exclude_title_tags)

        if google:
            self._t__google = Google(**google)

        if verification:
            self._t__verification = Verification(**verification)

        if opengraph_website:
            self._t__opengraph_website = OpenGraphWebsite(**opengraph_website)

        if twitter_card:
            self._t__twitter_card = TwitterCard(**twitter_card)

        if geo_position:
            self._t__geo_position = GeoPosition(**geo_position)

        if favicon:
            self._set_link_tags["favicon"] = Favicon(**favicon)

        # Build on run tags

        if viewport:
            self._t__viewport = MetaTag(name="viewport", content=viewport)
        else:
            if not exclude_viewport:
                self._t__viewport = MetaTag(
                    name="viewport", content="width=device-width, initial-scale=1"
                )

        if content_security_policy:
            self._t__content_security_policy = MetaTag(
                http_equiv="Content-Security-Policy", content=content_security_policy
            )

        if application_name:
            self._t__application_name = MetaTag(
                name="application_name", content=application_name
            )

        if generator:
            self._t__generator = MetaTag(name="generator", content=generator)

        if theme_color:
            self._t__theme_color = MetaTag(name="theme-color", content=theme_color)

        if description:
            self._t__description = MetaTag(name="description", content=description)

        if keywords:
            self._t__keywords = Keywords()
            if isinstance(keywords, str):
                self._t__keywords.set_from_string(keywords)
            if isinstance(keywords, list):
                self._t__keywords.set_from_list(keywords)

        if subject:
            self._t__subject = MetaTag(name="subject", content=subject)

        if rating:
            self._t__rating = MetaTag(name="rating", content=rating)

        if robots:
            self._t__robots = MetaTag(name="robots", content=robots)

        if referrer_policy:
            self._t__referrer_policy = MetaTag(name="referrer", content=referrer_policy)

        if disable_detection_of_telephone_numbers:
            self._t__detect_telephone_numbers = MetaTag(
                name="format-detection", content="telephone=no"
            )

    @property
    def instance(self):
        return self

    def __repr__(self):
        return f'<Head page_title="{self._t__title}">'

    def __str__(self):
        return Markup(self._compile_all())

    def __call__(self, *args, **kwargs):
        return Markup(self._compile_all())

    def set_charset(
        self, charset: str, _from_template: bool = False
    ) -> Union[str, "Head"]:
        self._t__charset.replace(charset)
        return self if not _from_template else ""

    def set_viewport(
        self, viewport: str, _from_template: bool = False
    ) -> Union[str, "Head"]:
        self._t__viewport.replace_content(viewport)
        return self if not _from_template else ""

    def set_content_security_policy(
        self, content_security_policy: str, _from_template: bool = False
    ) -> Union[str, "Head"]:
        if self._t__content_security_policy:
            self._t__content_security_policy.replace_content(content_security_policy)
            return self if not _from_template else ""

        self._t__content_security_policy = MetaTag(
            http_equiv="Content-Security-Policy", content=content_security_policy
        )
        return self if not _from_template else ""

    def set_default_content_security_policy(
        self, _from_template: bool = False
    ) -> Union[str, "Head"]:
        MetaTag(http_equiv="Content-Security-Policy", content="default-src 'self'")
        return self if not _from_template else ""

    def set_application_name(
        self, application_name: str, _from_template: bool = False
    ) -> Union[str, "Head"]:
        if self._t__application_name is not None:
            self._t__application_name.replace_content(application_name)
            return self if not _from_template else ""

        self._t__application_name = MetaTag(
            name="application_name", content=application_name
        )
        return self if not _from_template else ""

    def set_generator(
        self, generator: str, _from_template: bool = False
    ) -> Union[str, "Head"]:
        if self._t__generator is not None:
            self._t__generator.replace_content(generator)
            return self if not _from_template else ""

        self._t__generator = MetaTag(name="generator", content=generator)
        return self if not _from_template else ""

    def set_theme_color(
        self, theme_color: str, _from_template: bool = False
    ) -> Union[str, "Head"]:
        if self._t__theme_color is not None:
            self._t__theme_color.replace_content(theme_color)
            return self if not _from_template else ""

        self._t__theme_color = MetaTag(name="theme-color", content=theme_color)
        return self if not _from_template else ""

    def set_title(self, title: str, _from_template: bool = False) -> Union[str, "Head"]:
        self._t__title = TitleTag(title, self._exclude_title_tags)
        return self if not _from_template else ""

    def reset_title_appends(self, _from_template: bool = False) -> Union[str, "Head"]:
        self._title_tag_appends = []
        if isinstance(self._t__title, TitleTag):
            self._t__title.set_appends(self._title_tag_appends)

        return self if not _from_template else ""

    def reset_title_prepends(self, _from_template: bool = False) -> Union[str, "Head"]:
        self._title_tag_prepends = []
        if isinstance(self._t__title, TitleTag):
            self._t__title.set_prepends(self._title_tag_prepends)

        return self if not _from_template else ""

    def append_title(
        self, append: str, separator: str = " ", _from_template: bool = False
    ) -> Union[str, "Head"]:
        self._title_tag_appends.append((append, separator))
        if isinstance(self._t__title, TitleTag):
            print(self._title_tag_appends)
            self._t__title.set_appends(self._title_tag_appends)

        return self if not _from_template else ""

    def prepend_title(
        self, prepend: str, separator: str = " ", _from_template: bool = False
    ) -> Union[str, "Head"]:
        self._title_tag_prepends.append((prepend, separator))
        if isinstance(self._t__title, TitleTag):
            print(self._title_tag_prepends)
            self._t__title.set_prepends(self._title_tag_prepends)

        return self if not _from_template else ""

    def set_base(self, href: str, _from_template: bool = False) -> Union[str, "Head"]:
        self._t__base = BaseTag(href)
        return self if not _from_template else ""

    def set_description(
        self, description: str, _from_template: bool = False
    ) -> Union[str, "Head"]:
        if self._t__description is not None:
            self._t__description.replace_content(description)
            return self if not _from_template else ""

        self._t__description = MetaTag(name="description", content=description)
        return self if not _from_template else ""

    def set_subject(
        self, subject: str, _from_template: bool = False
    ) -> Union[str, "Head"]:
        if self._t__subject is not None:
            self._t__subject.replace_content(subject)
            return self if not _from_template else ""

        self._t__subject = MetaTag(name="subject", content=subject)
        return self if not _from_template else ""

    def set_rating(
        self, rating: str = "General", _from_template: bool = False
    ) -> Union[str, "Head"]:
        if self._t__rating is not None:
            self._t__rating.replace_content(rating)
            return self if not _from_template else ""

        self._t__rating = MetaTag(name="rating", content=rating)
        return self if not _from_template else ""

    def set_referrer_policy(
        self, policy: str = "no-referrer", _from_template: bool = False
    ) -> Union[str, "Head"]:
        if self._t__referrer_policy is not None:
            self._t__referrer_policy.replace_content(policy)
            return self if not _from_template else ""

        self._t__referrer_policy = MetaTag(name="referrer", content=policy)
        return self if not _from_template else ""

    def set_keywords(
        self, keywords: Union[str, list], _from_template: bool = False
    ) -> Union[str, "Head"]:
        self._t__keywords = Keywords()
        if isinstance(keywords, str):
            self._t__keywords.set_from_string(keywords)
            return self if not _from_template else ""
        if isinstance(keywords, list):
            self._t__keywords.set_from_list(keywords)
            return self if not _from_template else ""

        return self if not _from_template else ""

    def set_google(
        self,
        googlebot: Optional[str] = "index, follow",
        no_sitelinks_search_box: bool = False,
        no_translate: bool = False,
        _from_template: bool = False,
    ):
        google_meta = Google(
            googlebot=googlebot,
            no_sitelinks_search_box=no_sitelinks_search_box,
            no_translate=no_translate,
        )
        if str(google_meta) != "":
            self._t__google = google_meta
        else:
            self._t__google = None

        return self if not _from_template else ""

    def set_robots(
        self,
        instructions: Optional[str] = "index, follow",
        _from_template: bool = False,
    ):
        self._t__robots = MetaTag(name="robots", content=instructions)
        return self if not _from_template else ""

    def set_verification(
        self,
        google: Optional[str] = None,
        yandex: Optional[str] = None,
        bing: Optional[str] = None,
        alexa: Optional[str] = None,
        pinterest: Optional[str] = None,
        norton: Optional[str] = None,
        _from_template: bool = False,
    ):
        self._t__verification = Verification(
            google=google,
            yandex=yandex,
            bing=bing,
            alexa=alexa,
            pinterest=pinterest,
            norton=norton,
        )
        return self if not _from_template else ""

    def set_opengraph_website(
        self,
        site_name: Optional[str] = None,
        title: Optional[str] = None,
        description: Optional[str] = None,
        url: Optional[str] = None,
        image: Optional[str] = None,
        image_alt: Optional[str] = None,
        locale: Optional[str] = None,
        _from_template: bool = False,
    ):
        self._t__opengraph_website = OpenGraphWebsite(
            site_name=site_name,
            title=title,
            description=description,
            url=url,
            image=image,
            image_alt=image_alt,
            locale=locale,
        )
        return self if not _from_template else ""

    def set_twitter_card(
        self,
        card: Literal["summary", "summary_large_image"] = "summary",
        site_account: Optional[str] = None,
        creator_account: Optional[str] = None,
        title: Optional[str] = None,
        description: Optional[str] = None,
        image: Optional[str] = None,
        image_alt: Optional[str] = None,
        url: Optional[str] = None,
        _from_template: bool = False,
    ):
        self._t__twitter_card = TwitterCard(
            card=card,
            site_account=site_account,
            creator_account=creator_account,
            title=title,
            description=description,
            image=image,
            image_alt=image_alt,
            url=url,
        )
        return self if not _from_template else ""

    def set_geo_position(
        self,
        icbm: Optional[str] = None,
        geo_position: Optional[str] = None,
        geo_region: Optional[str] = None,
        geo_placename: Optional[str] = None,
        _from_template: bool = False,
    ):
        self._t__geo_position = GeoPosition(
            icbm=icbm,
            geo_position=geo_position,
            geo_region=geo_region,
            geo_placename=geo_placename,
        )
        return self if not _from_template else ""

    def set_disable_detection_of_telephone_numbers(
        self, _from_template: bool = False
    ) -> Union[str, "Head"]:
        self._t__detect_telephone_numbers = MetaTag(
            name="format-detection", content="telephone=no"
        )
        return self if not _from_template else ""

    def set_favicon(
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
        _from_template: bool = False,
    ):
        """
        Set favicon links.

        :return:
        """
        self._set_link_tags["favicon"] = Favicon(
            ico_icon_href=ico_icon_href,
            png_icon_16_href=png_icon_16_href,
            png_icon_32_href=png_icon_32_href,
            png_icon_64_href=png_icon_64_href,
            png_icon_96_href=png_icon_96_href,
            png_icon_180_href=png_icon_180_href,
            png_icon_196_href=png_icon_196_href,
            png_apple_touch_icon_57_href=png_apple_touch_icon_57_href,
            png_apple_touch_icon_60_href=png_apple_touch_icon_60_href,
            png_apple_touch_icon_72_href=png_apple_touch_icon_72_href,
            png_apple_touch_icon_76_href=png_apple_touch_icon_76_href,
            png_apple_touch_icon_114_href=png_apple_touch_icon_114_href,
            png_apple_touch_icon_120_href=png_apple_touch_icon_120_href,
            png_apple_touch_icon_144_href=png_apple_touch_icon_144_href,
            png_apple_touch_icon_152_href=png_apple_touch_icon_152_href,
            png_apple_touch_icon_167_href=png_apple_touch_icon_167_href,
            png_apple_touch_icon_180_href=png_apple_touch_icon_180_href,
            png_mstile_70_href=png_mstile_70_href,
            png_mstile_270_href=png_mstile_270_href,
            png_mstile_310x150_href=png_mstile_310x150_href,
            png_mstile_310_href=png_mstile_310_href,
        )
        return self if not _from_template else ""

    def set_meta_tag(
        self,
        name: str = None,
        http_equiv: str = None,
        property_: str = None,
        content: str = None,
        lookup_id: Optional[str] = None,
        _from_template: bool = False,
    ):
        """
        Set a meta tag.

        The lookup_id is used to remove the tag later. One is generated if not provided.

        :param name:
        :param http_equiv:
        :param property_:
        :param content:
        :param lookup_id:
        :param _from_template:
        :return:
        """
        if not lookup_id:
            lookup_id = hashlib.md5(
                f"{''.join([x for x in [name, http_equiv, property_, content] if x])}".encode()
            ).hexdigest()
        self._set_meta_tags[lookup_id] = MetaTag(
            name, http_equiv, property_, content, id_=lookup_id
        )
        return self if not _from_template else ""

    def remove_meta_tag(
        self, lookup_id: str, _from_template: bool = False
    ) -> Union[str, "Head"]:
        """
        Remove a meta tag by lookup_id.

        :param lookup_id:
        :param _from_template:
        :return:
        """
        if lookup_id in self._set_meta_tags:
            del self._set_meta_tags[lookup_id]
        return self if not _from_template else ""

    def set_link_tag(
        self,
        rel: str,
        href: str,
        sizes: Optional[str] = None,
        type_: Optional[str] = None,
        hreflang: Optional[str] = None,
        lookup_id: Optional[str] = None,
        _from_template: bool = False,
    ):
        """
        Set a link tag.

        The lookup_id is used to remove the tag later. One is generated if not provided.

        :param rel:
        :param href:
        :param sizes:
        :param type_:
        :param hreflang:
        :param lookup_id:
        :param _from_template:
        :return:
        """
        if not lookup_id:
            lookup_id = hashlib.md5(
                f"{''.join([x for x in [rel, href, sizes, type_, hreflang] if x])}".encode()
            ).hexdigest()
        self._set_link_tags[lookup_id] = LinkTag(
            rel, href, sizes, type_, hreflang, id_=lookup_id
        )
        return self if not _from_template else ""

    def remove_link_tag(
        self, lookup_id: str, _from_template: bool = False
    ) -> Union[str, "Head"]:
        """
        Remove a link tag by lookup_id.

        :param lookup_id:
        :param _from_template:
        :return:
        """
        if lookup_id in self._set_link_tags:
            del self._set_link_tags[lookup_id]
        return self if not _from_template else ""

    def set_script_tag(
        self,
        src: str,
        type_: Optional[str] = None,
        async_: bool = False,
        defer: bool = False,
        crossorigin: Optional[str] = None,
        integrity: Optional[str] = None,
        lookup_id: Optional[str] = None,
        _from_template: bool = False,
    ):
        if not lookup_id:
            lookup_id = hashlib.md5(
                f"{''.join([x for x in [src, type_, async_, defer, crossorigin, integrity] if x])}".encode()
            ).hexdigest()
        self._set_script_tags[src] = ScriptTag(
            src, type_, async_, defer, crossorigin, integrity, id_=lookup_id
        )
        return self if not _from_template else ""

    def remove_script_tag(
        self, lookup_id: str, _from_template: bool = False
    ) -> Union[str, "Head"]:
        if lookup_id in self._set_script_tags:
            del self._set_script_tags[lookup_id]
        return self if not _from_template else ""

    def as_dict(self):
        return {
            **{
                o_tag.replace("_t__", ""): getattr(self, o_tag)
                for o_tag in self._top_level_tags
                if getattr(self, o_tag) is not None
            },
            **{
                o_tag.replace("_t__", ""): getattr(self, o_tag)
                for o_tag in self._order
                if getattr(self, o_tag) is not None
            },
            **self._set_meta_tags,
            **self._set_link_tags,
        }

    @property
    def title(self):
        return Markup(str(self._t__title))

    @property
    def top_level_tags(self):
        return Markup(
            "\n".join(
                [
                    *[
                        str(getattr(self, o_tag))
                        for o_tag in self._top_level_tags
                        if getattr(self, o_tag) is not None
                    ]
                ]
            )
        )

    @property
    def meta_tags(self):
        return Markup(
            "\n".join(
                [
                    *[
                        str(getattr(self, o_tag))
                        for o_tag in self._order
                        if getattr(self, o_tag) is not None
                    ],
                    *[
                        str(c_tag)
                        for c_tag in self._set_meta_tags.values()
                        if c_tag is not None
                    ],
                ]
            )
        )

    @property
    def link_tags(self):
        return Markup(
            "\n".join(
                [
                    *[
                        str(c_tag)
                        for c_tag in self._set_link_tags.values()
                        if c_tag is not None
                    ]
                ]
            )
        )

    @property
    def script_tags(self):
        return Markup(
            "\n".join(
                [
                    *[
                        str(c_tag)
                        for c_tag in self._set_script_tags.values()
                        if c_tag is not None
                    ]
                ]
            )
        )

    def _compile_all(self):
        compiled_tags = [
            *[
                str(getattr(self, o_tag))
                for o_tag in self._top_level_tags
                if getattr(self, o_tag) is not None
            ],
        ]

        if not self._exclude_title_tags:
            if self._t__title is not None:
                compiled_tags.append(str(self._t__title))

        compiled_tags = compiled_tags + [
            *[
                str(getattr(self, o_tag))
                for o_tag in self._order
                if getattr(self, o_tag) is not None
            ],
            *[
                str(c_tag)
                for c_tag in self._set_meta_tags.values()
                if c_tag is not None
            ],
            *[
                str(c_tag)
                for c_tag in self._set_link_tags.values()
                if c_tag is not None
            ],
            *[
                str(c_tag)
                for c_tag in self._set_script_tags.values()
                if c_tag is not None
            ],
        ]
        return "\n".join([tag for tag in compiled_tags if tag is not None])
