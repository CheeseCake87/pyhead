"""A simple python package to generate HTML head tags."""

from typing import Optional, Union, Literal

from markupsafe import Markup

from exceptions import *
from tags import (
    Charset,
    ContentSecurityPolicy,
    Title,
    Base,
    Keywords,
    MetaTag,
    Google,
    Verification,
    ReferrerPolicy,
    OpenGraphWebsite,
    TwitterCard,
)

__version__ = "0.3"


class Head:
    _exclude_title_tags: bool

    t__charset: Charset
    t__viewport: MetaTag
    t__content_security_policy: Optional[ContentSecurityPolicy] = None
    t__application_name: Optional[MetaTag] = None
    t__generator: Optional[MetaTag] = None
    t__theme_color: Optional[MetaTag] = None
    t__title: Optional[Title] = None
    t__base: Optional[Base] = None
    t__description: Optional[MetaTag] = None
    t__subject: Optional[MetaTag] = None
    t__rating: Optional[MetaTag] = None
    t__referrer_policy: Optional[ReferrerPolicy] = None
    t__keywords: Optional[Keywords] = None
    t__google: Optional[Google] = None
    t__verification: Optional[Verification] = None
    t__open_graph_website: Optional[OpenGraphWebsite] = None
    t__twitter_card: Optional[TwitterCard] = None

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
        't__subject',
        't__rating',
        't__referrer_policy',
        't__keywords',
        't__google',
        't__verification',
        't__open_graph_website',
        't__twitter_card',
    ]

    def __init__(
            self,
            charset: str = 'utf-8',
            viewport: str = 'width=device-width, initial-scale=1.0',
            content_security_policy: str = None,
            title: str = None,
            base: str = None,
            description: str = None,
            keywords: Union[str, list] = None,
            _exclude_title_tags: bool = False,
    ):
        self._exclude_title_tags = _exclude_title_tags

        self.t__charset = Charset(charset)
        self.t__viewport = MetaTag('viewport', viewport)

        if content_security_policy is not None:
            self.t__content_security_policy = ContentSecurityPolicy(content_security_policy)

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

    def set_charset(self, charset: str):
        self.t__charset.replace(charset)
        return self

    def set_viewport(self, viewport: str):
        self.t__viewport.replace_content(viewport)
        return self

    def set_content_security_policy(self, content_security_policy: str):
        self.t__content_security_policy = ContentSecurityPolicy(content_security_policy)
        return self

    def set_default_content_security_policy(self):
        self.t__content_security_policy = ContentSecurityPolicy("default-src 'self'")
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

    def set_referrer_policy(self, referrer_policy: str = 'no-referrer', fallback: Optional[str] = None):
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

    def set_open_graph_website(
            self,
            site_name: Optional[str] = None,
            title: Optional[str] = None,
            description: Optional[str] = None,
            url: Optional[str] = None,
            image: Optional[str] = None,
            image_alt: Optional[str] = None,
            locale: Optional[str] = None,
    ):
        self.t__open_graph_website = OpenGraphWebsite(
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

    def as_dict(self):
        return {o_tag.replace("t__", ""): getattr(self, o_tag) for o_tag in self._order
                if getattr(self, o_tag) is not None}

    def __str__(self):
        return Markup("\n".join(
            [str(getattr(self, o_tag)) for o_tag in self._order
             if getattr(self, o_tag) is not None]
        ))


if __name__ == '__main__':
    head = Head(base='https://example.com')
    head.set_title('Hello World')
    head.set_referrer_policy('no-referrer', 'origin')
    ver = {
        'google': '1234567890',
        'bing': '1234567890',
    }
    head.set_verification(**ver)
    head.set_open_graph_website(
        site_name='Example',
        title='Example',
        description='Example',
        url='https://example.com',
        image='https://example.com/image.png',
        image_alt='Example',
        locale='en_US',
    )
    head.set_twitter_card(
        card='summary_large_image',
        site_account='@example',
        creator_account='@example',
        title='Example',
        description='Example',
        image='https://example.com/image.png',
        image_alt='Example',
    )
    # head.set_default_content_security_policy()
    # head.set_title('Hello World')
    # head.set_description('This is a test')
    # head.set_keywords('test, hello, world')
    # head.set_description('This is a test')
    # head.set_google(index=True, follow=False)
    # head.set_verification(google='1234567890')
    # head.set_rating('General')
    # head.append_title('Hello World1', ' - ')

    print(head)

    # for k, v in head.as_dict().items():
    #     print(k, "=", v)
