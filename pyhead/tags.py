from typing import Optional, Literal

from markupsafe import Markup


class Charset:
    _charset: str = None

    def __init__(self, charset: str = 'utf-8'):
        self._charset = charset

    def __repr__(self):
        return f'<Charset charset="{self._charset}">'

    def __str__(self):
        return Markup(f'<meta charset="{self._charset}">')

    def replace(self, charset: str):
        self._charset = charset
        return self


class MetaTag:
    _name: str = None
    _content: str = None

    def __init__(self, name: str, content: str):
        self._name = name
        self._content = content

    def __repr__(self):
        return f'<MetaTag name="{self._name}" content="{self._content}">'

    def __str__(self):
        return Markup(f'<meta name="{self._name}" content="{self._content}">')

    def replace_content(self, content: str):
        self._content = content
        return self


class ContentSecurityPolicy:
    _content_security_policy: str = None

    def __init__(self, content_security_policy: str = "default-src 'self'"):
        self._content_security_policy = content_security_policy

    def __repr__(self):
        return f'<ContentSecurityPolicy content_security_policy="{self._content_security_policy}">'

    def __str__(self):
        return Markup(f'<meta http-equiv="Content-Security-Policy" content="{self._content_security_policy}">')

    def replace(self, content_security_policy: str):
        self._content_security_policy = content_security_policy
        return self


class Base:
    _base: str = None

    def __init__(self, base: str):
        self._base = base

    def __repr__(self):
        return f'<Base base="{self._base}">'

    def __str__(self):
        return Markup(f'<base href="{self._base}">')

    def replace(self, base: str):
        self._base = base
        return self


class Title:
    _title: str = None
    _exclude_title_tags: bool = False

    def __init__(self, page_title: str, _exclude_title_tags: bool = False):
        self._title = page_title
        self._exclude_title_tags = _exclude_title_tags

    def __repr__(self):
        return f'<Title page_title="{self._title}">'

    def __str__(self):
        if not self._exclude_title_tags:
            return Markup(f'<title>{self._title}</title>')
        else:
            return Markup(f'{self._title}')

    def replace(self, page_title: str):
        self._title = page_title
        return self

    def append(self, more_page_title: str, separator: str):
        self._title = self._title + separator + more_page_title
        return self

    def prepend(self, more_page_title: str, separator: str):
        self._title = more_page_title + separator + self._title
        return self


class Keywords:
    _keywords: list = None

    def __init__(self):
        pass

    def __repr__(self):
        return f'<Keywords page_keywords="{self._keywords}">'

    def __str__(self):
        return Markup(f'<meta name="keywords" content="{", ".join(self._keywords)}">')

    def set_from_string(self, keywords: str):
        self._keywords = keywords.replace(" ", "").split(',')
        return self

    def set_from_list(self, keywords: list):
        self._keywords = keywords
        return self

    def str_append(self, more_keywords: str):
        self._keywords.append(more_keywords.replace(" ", "").split(','))
        return self

    def list_append(self, more_keywords: list):
        self._keywords.append(more_keywords)
        return self


class Google:
    googlebot: Optional[MetaTag] = None
    sitelinks: Optional[MetaTag] = None
    no_translate: Optional[MetaTag] = None
    verification_token: Optional[MetaTag] = None

    _googlebot: list

    _order: list = [
        "googlebot",
        "sitelinks",
        "no_translate",
    ]

    def __init__(
            self,
            index: Optional[bool] = None,
            follow: Optional[bool] = None,
            no_sitelinks_search_box: bool = False,
            no_translate: bool = False,
    ):
        self._googlebot = []

        if index is not None:
            if index:
                self._googlebot.append('index')
            else:
                self._googlebot.append('noindex')

        if follow is not None:
            if follow:
                self._googlebot.append('follow')
            else:
                self._googlebot.append('nofollow')

        if len(self._googlebot) > 0:
            self.googlebot = MetaTag('googlebot', f'{", ".join(self._googlebot)}')

        if no_sitelinks_search_box:
            self.sitelinks = MetaTag('google', 'nositelinkssearchbox')

        if no_translate:
            self.no_translate = MetaTag('google', 'notranslate')

    def __repr__(self):
        return '<Google>'

    def __str__(self):
        _ = [str(getattr(self, o_tag)) for o_tag in self._order if getattr(self, o_tag) is not None]
        if _:
            return Markup("\n".join(_))
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
    ):
        if google is not None:
            self.google = MetaTag('google-site-verification', google)

        if yandex is not None:
            self.yandex = MetaTag('yandex-verification', yandex)

        if bing is not None:
            self.bing = MetaTag('msvalidate.01', bing)

        if alexa is not None:
            self.alexa = MetaTag('alexaVerifyID', alexa)

        if pinterest is not None:
            self.pinterest = MetaTag('p:domain_verify', pinterest)

        if norton is not None:
            self.norton = MetaTag('norton-safeweb-site-verification', norton)

    def __repr__(self):
        return '<Verification>'

    def __str__(self):
        _ = [str(getattr(self, o_tag)) for o_tag in self._order if getattr(self, o_tag) is not None]
        if _:
            return Markup("\n".join(_))
        return ""


class ReferrerPolicy:
    _policy: str = None
    _fallback: str = None

    def __init__(self, policy: str, fallback: Optional[str] = None):
        self._policy = policy
        self._fallback = fallback

    def __repr__(self):
        return f'<ReferrerPolicy content="{self._policy}" fallback="{self._fallback}">'

    def __str__(self):
        _ = []
        if self._fallback is not None:
            _.append(self._fallback)

        _.append(self._policy)

        return Markup(f'<meta name="referrer" content="{", ".join(_)}">')

    def replace_content(self, content: str, fallback: Optional[str] = None):
        self._policy = content
        self._fallback = fallback
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
            locale: str = 'en_US',
            title: Optional[str] = None,
            image: Optional[str] = None,
            image_alt: Optional[str] = None,
            description: Optional[str] = None,
            site_name: Optional[str] = None,
            url: Optional[str] = None,
    ):
        self.type = MetaTag('og:type', 'website')
        self.locale = MetaTag('og:locale', locale)

        if title is not None:
            self.title = MetaTag('og:title', title)

        if url is not None:
            self.url = MetaTag('og:url', url)

        if image is not None:
            self.image = MetaTag('og:image', image)

        if image_alt is not None:
            self.image_alt = MetaTag('og:image:alt', image_alt)

        if description is not None:
            self.description = MetaTag('og:description', description)

        if site_name is not None:
            self.site_name = MetaTag('og:site_name', site_name)

    def __repr__(self):
        return '<OpenGraph type="website">'

    def __str__(self):
        _ = [str(getattr(self, o_tag)) for o_tag in self._order if getattr(self, o_tag) is not None]
        if _:
            return Markup("\n".join(_))
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
            card: Literal['summary', 'summary_large_image'] = 'summary',
            site_account: Optional[str] = None,
            creator_account: Optional[str] = None,
            title: Optional[str] = None,
            description: Optional[str] = None,
            image: Optional[str] = None,
            image_alt: Optional[str] = None,
            url: Optional[str] = None,

    ):
        self.card = MetaTag('twitter:card', card)

        if site_account is not None:
            self.site_account = MetaTag('twitter:site', site_account)

        if creator_account is not None:
            self.creator_account = MetaTag('twitter:creator', creator_account)

        if title is not None:
            self.title = MetaTag('twitter:title', title)

        if description is not None:
            self.description = MetaTag('twitter:description', description)

        if image is not None:
            self.image = MetaTag('twitter:image', image)

        if image_alt is not None:
            self.image_alt = MetaTag('twitter:image:alt', image_alt)

        if url is not None:
            self.url = MetaTag('twitter:url', url)

    def __repr__(self):
        return '<TwitterCard>'

    def __str__(self):
        _ = [str(getattr(self, o_tag)) for o_tag in self._order if getattr(self, o_tag) is not None]
        if _:
            return Markup("\n".join(_))
        return ""
