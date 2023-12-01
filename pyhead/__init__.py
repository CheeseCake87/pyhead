"""A simple python package to generate HTML head tags."""

from typing import Optional, Union, Literal

from markupsafe import Markup

from .exceptions import *
from .tags import (
    Charset,
    Title,
    Base,
    Keywords,
    MetaTag,
    Google,
    Verification,
    ReferrerPolicy,
    OpenGraphWebsite,
    TwitterCard,
    GeoPosition,
)

__version__ = "0.5"


class Head:
    _exclude_title_tags: bool

    t__charset: Charset
    t__viewport: MetaTag
    t__content_security_policy: Optional[MetaTag] = None
    t__application_name: Optional[MetaTag] = None
    t__generator: Optional[MetaTag] = None
    t__theme_color: Optional[MetaTag] = None
    t__title: Optional[Title] = None
    t__base: Optional[Base] = None
    t__description: Optional[MetaTag] = None
    t__keywords: Optional[Keywords] = None
    t__subject: Optional[MetaTag] = None
    t__rating: Optional[MetaTag] = None
    t__referrer_policy: Optional[ReferrerPolicy] = None
    t__google: Optional[Google] = None
    t__verification: Optional[Verification] = None
    t__opengraph_website: Optional[OpenGraphWebsite] = None
    t__twitter_card: Optional[TwitterCard] = None
    t__geo_position: Optional[GeoPosition] = None
    t__detect_telephone_numbers: Optional[MetaTag] = None

    _custom_tags: dict

    _order = [
        't__charset',
        't__viewport',
        't__content_security_policy',
        't__application_name',
        't__generator',
        't__theme_color',
        't__title',
        't__base',
        't__description',
        't__keywords',
        't__subject',
        't__rating',
        't__referrer_policy',
        't__google',
        't__verification',
        't__opengraph_website',
        't__twitter_card',
        't__geo_position',
        't__detect_telephone_numbers',
    ]

    def __init__(
            self,
            charset: str = 'utf-8',
            viewport: Optional[str] = None,
            content_security_policy: Optional[str] = None,
            title: Optional[str] = None,
            base: Optional[str] = None,
            description: Optional[str] = None,
            keywords: Optional[Union[str, list]] = None,
            subject: Optional[str] = None,
            rating: Optional[str] = None,
            referrer_policy: Optional[dict] = None,
            google: Optional[dict] = None,
            verification: Optional[dict] = None,
            opengraph_website: Optional[dict] = None,
            twitter_card: Optional[dict] = None,
            geo_position: Optional[dict] = None,
            detect_telephone_numbers: bool = False,
            exclude_title_tags: bool = False,
            exclude_viewport: bool = False,
            exclude_content_security_policy: bool = False,
            exclude_detect_telephone_numbers: bool = False,
    ):
        """
        viewport is set to "'width=device-width, initial-scale=1.0'" by default.
        Set exclude_viewport to True to exclude the tag.

        content_security_policy is set to "default-src 'self'" by default.
        Set exclude_content_security_policy to True to exclude the tag.

        detect_telephone_numbers is set to "telephone=no" by default.
        Set exclude_detect_telephone_numbers to True to exclude the tag.

        .. code-block::

            referrer_policy: {
                'policy': 'no-referrer',
                'fallback': 'origin',
            }

        .. code-block::

            google: {
                'index': True,
                'follow': False,
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
                'icbm': '12.345, 12.345',
                'geo_position': '12.345;12.345',
                'geo_region': 'en_US',
                'geo_placename': 'Example',
            }

        """

        self._exclude_title_tags = exclude_title_tags
        self._custom_tags = {}

        self.t__charset = Charset(charset)

        if content_security_policy is not None:
            self.t__viewport = MetaTag('viewport', viewport)
        else:
            if not exclude_viewport:
                self.t__viewport = MetaTag(
                    'viewport',
                    "'width=device-width, initial-scale=1.0'")

        if content_security_policy is not None:
            self.t__content_security_policy = MetaTag(
                'Content-Security-Policy', content_security_policy, is_http_equiv=True)
        else:
            if not exclude_content_security_policy:
                self.t__content_security_policy = MetaTag(
                    'Content-Security-Policy',
                    "default-src 'self'", is_http_equiv=True)

        if title is not None:
            self.t__title = Title(title)

        if base is not None:
            self.t__base = Base(base)

        if description is not None:
            self.t__description = MetaTag('description', description)

        if keywords is not None:
            self.t__keywords = Keywords()
            if isinstance(keywords, str):
                self.t__keywords.set_from_string(keywords)
            if isinstance(keywords, list):
                self.t__keywords.set_from_list(keywords)

        if subject is not None:
            self.t__subject = MetaTag('subject', subject)

        if rating is not None:
            self.t__rating = MetaTag('rating', rating)

        if referrer_policy is not None:
            self.t__referrer_policy = ReferrerPolicy(**referrer_policy)

        if google is not None:
            self.t__google = Google(**google)

        if verification is not None:
            self.t__verification = Verification(**verification)

        if opengraph_website is not None:
            self.t__opengraph_website = OpenGraphWebsite(**opengraph_website)

        if twitter_card is not None:
            self.t__twitter_card = TwitterCard(**twitter_card)

        if geo_position is not None:
            self.t__geo_position = GeoPosition(**geo_position)

        if detect_telephone_numbers:
            self.t__detect_telephone_numbers = MetaTag(
                'format-detection', 'telephone=yes')
        else:
            if not exclude_detect_telephone_numbers:
                self.t__detect_telephone_numbers = MetaTag(
                    'format-detection', 'telephone=no')

    def set_charset(self, charset: str):
        self.t__charset.replace(charset)
        return self

    def set_viewport(self, viewport: str):
        self.t__viewport.replace_content(viewport)
        return self

    def set_content_security_policy(self, content_security_policy: str):
        if self.t__content_security_policy is not None:
            self.t__content_security_policy.replace_content(content_security_policy)
            return self

        self.t__content_security_policy = MetaTag(
            'Content-Security-Policy', content_security_policy, is_http_equiv=True)
        return self

    def set_default_content_security_policy(self):
        MetaTag('Content-Security-Policy',
                "default-src 'self'", is_http_equiv=True)
        return self

    def set_application_name(self, application_name: str):
        if self.t__application_name is not None:
            self.t__application_name.replace_content(application_name)
            return self

        self.t__application_name = MetaTag('application_name', application_name)
        return self

    def set_generator(self, generator: str):
        if self.t__generator is not None:
            self.t__generator.replace_content(generator)
            return self

        self.t__generator = MetaTag('generator', generator)
        return self

    def set_title(self, title: str):
        self.t__title = Title(title, self._exclude_title_tags)
        return self

    def append_title(self, title: str, separator: str = ' '):
        if self.t__title is not None:
            self.t__title.append(title, separator)
            return self

        raise PageTitleNotSet('Page title not set')

    def prepend_title(self, title: str, separator: str = ' '):
        if self.t__title is not None:
            self.t__title.prepend(title, separator)
            return self

        raise PageTitleNotSet('Page title not set')

    def set_base(self, base: str):
        self.t__base = Base(base)
        return self

    def set_description(self, description: str):
        if self.t__description is not None:
            self.t__description.replace_content(description)
            return self

        self.t__description = MetaTag('description', description)
        return self

    def set_subject(self, subject: str):
        if self.t__subject is not None:
            self.t__subject.replace_content(subject)
            return self

        self.t__subject = MetaTag('subject', subject)
        return self

    def set_rating(self, rating: str = 'General'):
        if self.t__rating is not None:
            self.t__rating.replace_content(rating)
            return self

        self.t__rating = MetaTag('rating', rating)
        return self

    def set_referrer_policy(
            self,
            referrer_policy: str = 'no-referrer',
            fallback: Optional[str] = None
    ):
        if self.t__referrer_policy is not None:
            self.t__referrer_policy.replace_content(referrer_policy, fallback)
            return self

        self.t__referrer_policy = ReferrerPolicy(referrer_policy, fallback)
        return self

    def set_keywords(self, keywords: Union[str, list]):
        self.t__keywords = Keywords()
        if isinstance(keywords, str):
            self.t__keywords.set_from_string(keywords)
            return self
        if isinstance(keywords, list):
            self.t__keywords.set_from_list(keywords)
            return self

        return self

    def append_keywords(self, keywords: Union[str, list]):
        if self.t__keywords is not None:
            if isinstance(keywords, str):
                self.t__keywords.str_append(keywords)
                return self
            if isinstance(keywords, list):
                self.t__keywords.list_append(keywords)
                return self

        raise KeywordsNotSet('Keywords not set')

    def __repr__(self):
        return f'<Head page_title="{self.t__title}">'

    def set_google(
            self,
            index: Optional[bool] = None,
            follow: Optional[bool] = None,
            no_sitelinks_search_box: bool = False,
            no_translate: bool = False
    ):
        google_meta = Google(
            index=index,
            follow=follow,
            no_sitelinks_search_box=no_sitelinks_search_box,
            no_translate=no_translate
        )
        if str(google_meta) != '':
            self.t__google = google_meta
        else:
            self.t__google = None

        return self

    def set_verification(
            self,
            google: Optional[str] = None,
            yandex: Optional[str] = None,
            bing: Optional[str] = None,
            alexa: Optional[str] = None,
            pinterest: Optional[str] = None,
            norton: Optional[str] = None,
    ):
        self.t__verification = Verification(
            google=google,
            yandex=yandex,
            bing=bing,
            alexa=alexa,
            pinterest=pinterest,
            norton=norton,
        )
        return self

    def set_opengraph_website(
            self,
            site_name: Optional[str] = None,
            title: Optional[str] = None,
            description: Optional[str] = None,
            url: Optional[str] = None,
            image: Optional[str] = None,
            image_alt: Optional[str] = None,
            locale: Optional[str] = None,
    ):
        self.t__opengraph_website = OpenGraphWebsite(
            site_name=site_name,
            title=title,
            description=description,
            url=url,
            image=image,
            image_alt=image_alt,
            locale=locale,
        )
        return self

    def set_twitter_card(
            self,
            card: Literal['summary', 'summary_large_image'] = 'summary',
            site_account: Optional[str] = None,
            creator_account: Optional[str] = None,
            title: Optional[str] = None,
            description: Optional[str] = None,
            image: Optional[str] = None,
            image_alt: Optional[str] = None,
    ):
        self.t__twitter_card = TwitterCard(
            card=card,
            site_account=site_account,
            creator_account=creator_account,
            title=title,
            description=description,
            image=image,
            image_alt=image_alt,
        )
        return self

    def set_geo_position(
            self,
            icbm: Optional[str] = None,
            geo_position: Optional[str] = None,
            geo_region: Optional[str] = None,
            geo_placename: Optional[str] = None,
    ):
        self.t__geo_position = GeoPosition(
            icbm=icbm,
            geo_position=geo_position,
            geo_region=geo_region,
            geo_placename=geo_placename,
        )
        return self

    def set_detect_telephone_numbers(self, detect_telephone_numbers: bool = False):
        if detect_telephone_numbers:
            self.t__detect_telephone_numbers = MetaTag(
                'format-detection', 'telephone=yes')
            return self

        self.t__detect_telephone_numbers = MetaTag(
            'format-detection', 'telephone=no')
        return self

    def set_tag(
            self,
            name: str,
            content: str,
            is_http_equiv: bool = False
    ):
        self._custom_tags[name] = MetaTag(name, content, is_http_equiv)
        return self

    def remove_tag(self, name: str):
        if name in self._custom_tags:
            del self._custom_tags[name]
        return self

    def as_dict(self):
        return {
            **{o_tag.replace("t__", ""): getattr(self, o_tag) for o_tag in self._order
               if getattr(self, o_tag) is not None},
            **self._custom_tags
        }

    def __str__(self):
        return Markup("\n".join(
            [
                *[str(getattr(self, o_tag)) for o_tag in self._order
                  if getattr(self, o_tag) is not None],
                *[str(c_tag) for c_tag in self._custom_tags.values() if c_tag is not None]
            ]
        ))
