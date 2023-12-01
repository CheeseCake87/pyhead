# pyhead 🐍🤯

[![PyPI version](https://badge.fury.io/py/pyhead.svg)](https://badge.fury.io/py/pyhead)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/CheeseCake87/pyhead/master/LICENSE)

The Python HTML `<head>` filler.

`pip install pyhead`

```python
from flask import Flask

from pyhead import Head


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def dicts_as_args():
        head = Head(
            charset='utf-8',
            viewport='width=device-width, initial-scale=1.0',
            title='Hello World',
            base='https://example.com',
            description='This is a test',
            keywords='test, hello, world',
            subject='Hello World',
            rating='General',
            robots='index, follow',
            referrer_policy={
                'policy': 'no-referrer',
                'fallback': 'origin',
            },
            google={
                'googlebot': 'index, follow',
                'no_sitelinks_search_box': False,
                'no_translate': False,
            },
            verification={
                'google': '1234567890',
                'bing': '1234567890',
            },
            opengraph_website={
                'site_name': 'Example',
                'title': 'Example',
                'description': 'Example',
                'url': 'https://example.com',
                'image': 'https://example.com/image.png',
                'image_alt': 'Example',
                'locale': 'en_US',
            },
            twitter_card={
                'card': 'summary',
                'site_account': '@example',
                'creator_account': '@example',
                'title': 'Example',
                'description': 'Example',
                'image': 'https://example.com/image.png',
                'image_alt': 'Example',
            },
            geo_position={
                'icbm': '55.86013028402754, -4.252019430273945',
                'geo_position': '55.86013028402754;-4.252019430273945',
                'geo_region': 'en_GB',
                'geo_placename': 'Duke of Wellington',
            }
        )
        head.append_title('Hello World1', ' - ')
        head.prepend_title('Hello World2', ' - ')
        
        head.set_tag(name='tag', content='tag-content')
        head.set_tag(name='another-tag', content='another-tag-content', is_http_equiv=True)

        return f"""\
            <html>
                <head>
                    {head}
                </head>
                <body>
                    <h1>Flask App</h1>
                    <p>Right-Click view source</p>
                </body>
            </html>
            """

    @app.route('/args')
    def using_args():
        head = Head(
            charset='utf-8',
            viewport='width=device-width, initial-scale=1.0',
            title='Hello World',
            base='https://example.com',
            description='This is a test',
            keywords='test, hello, world',
            subject='Hello World',
            rating='General',
            robots='index, follow',
        )
        head.set_referrer_policy(
            policy='no-referrer',
            fallback='origin',
        )
        head.set_google(
            googlebot='index, follow',
            no_sitelinks_search_box=False,
            no_translate=False,
        )
        head.set_verification(
            google='1234567890',
            bing='1234567890',
        )
        head.set_opengraph_website(
            site_name='Example',
            title='Example',
            description='Example',
            url='https://example.com',
            image='https://example.com/image.png',
            image_alt='Example',
            locale='en_US',
        )
        head.set_twitter_card(
            card='summary',
            site_account='@example',
            creator_account='@example',
            title='Example',
            description='Example',
            image='https://example.com/image.png',
            image_alt='Example',
        )
        head.set_geo_position(
            icbm='55.86013028402754, -4.252019430273945',
            geo_position='55.86013028402754;-4.252019430273945',
            geo_region='en_GB',
            geo_placename='Duke of Wellington',
        )

        head.append_title('Hello World1', ' - ')
        head.prepend_title('Hello World2', ' - ')
        
        head.set_tag(name='tag', content='tag-content')
        head.set_tag(name='another-tag', content='another-tag-content', is_http_equiv=True)

        return f"""\
            <html>
                <head>
                    {head}
                </head>
                <body>
                    <h1>Flask App</h1>
                    <p>Right-Click view source</p>
                </body>
            </html>
            """

    return app
```

view-source:

```text
<meta charset="utf-8">
<meta name="viewport" content="'width=device-width, initial-scale=1.0'">
<meta http-equiv="Content-Security-Policy" content="default-src 'self'">
<title>Hello World2 - Hello World - Hello World1</title>
<base href="https://example.com">
<meta name="description" content="This is a test">
<meta name="keywords" content="test, hello, world">
<meta name="subject" content="Hello World">
<meta name="rating" content="General">
<meta name="robots" content="index, follow">
<meta name="referrer" content="origin, no-referrer">
<meta name="googlebot" content="index, follow">
<meta name="google-site-verification" content="1234567890">
<meta name="msvalidate.01" content="1234567890">
<meta name="og:type" content="website">
<meta name="og:locale" content="en_US">
<meta name="og:site_name" content="Example">
<meta name="og:title" content="Example">
<meta name="og:description" content="Example">
<meta name="og:image" content="https://example.com/image.png">
<meta name="og:image:alt" content="Example">
<meta name="og:url" content="https://example.com">
<meta name="twitter:card" content="summary">
<meta name="twitter:site" content="@example">
<meta name="twitter:creator" content="@example">
<meta name="twitter:title" content="Example">
<meta name="twitter:description" content="Example">
<meta name="twitter:image" content="https://example.com/image.png">
<meta name="twitter:image:alt" content="Example">
<meta name="ICBM" content="55.86013028402754, -4.252019430273945">
<meta name="geo.position" content="55.86013028402754;-4.252019430273945">
<meta name="geo.region" content="en_GB">
<meta name="geo.placename" content="Duke of Wellington">
<meta name="format-detection" content="telephone=no">
<meta name="tag" content="tag-content">
<meta http-equiv="another-tag" content="another-tag-content">
```