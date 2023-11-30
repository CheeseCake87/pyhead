# pyhead

[![PyPI version](https://badge.fury.io/py/pyhead.svg)](https://badge.fury.io/py/pyhead)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/CheeseCake87/pyhead/master/LICENSE)

The Python HTML `<head>` filler.

```python
from flask import Flask

from pyhead import Head


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def method_chain():
        head = Head()
        verification = {
            'google': '1234567890',
            'bing': '1234567890',
        }
        head.set_verification(**verification)
        head.set_base('https://example.com')
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
        head.set_referrer_policy('no-referrer', 'origin')
        head.set_default_content_security_policy()
        head.set_title('Hello World')
        head.set_description('This is a test')
        head.set_keywords('test, hello, world')
        head.set_description('This is a test')
        head.set_google(index=True, follow=False)
        head.set_rating('General')
        head.append_title('Hello World1', ' - ')
        head.prepend_title('Hello World2', ' - ')

        return f"""\
        <html>
            <head>
                {head}
            </head>
            <body>
                <h1>Flask App</h1>
            </body>
        </html>
        """

    @app.route('/class')
    def class_only():
        head2 = Head(
            title='Hello World',
            description='This is a test',
            keywords='test, hello, world',
            base='https://example.com',
            google={
                'index': True,
                'follow': False,
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
            referrer_policy={
                'policy': 'no-referrer',
                'fallback': 'origin',
            },
            rating='General',
        )
        head2.append_title('Hello World1', ' - ')
        head2.prepend_title('Hello World2', ' - ')

        return f"""\
            <html>
                <head>
                    {head2}
                </head>
                <body>
                    <h1>Flask App</h1>
                </body>
            </html>
            """

    return app
```

view-source:

```text
        <html>
            <head>
                <meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="Content-Security-Policy" content="default-src 'self'">
<title>Hello World2 - Hello World - Hello World1</title>
<base href="https://example.com">
<meta name="description" content="This is a test">
<meta name="keywords" content="test, hello, world">
<meta name="rating" content="General">
<meta name="referrer" content="origin, no-referrer">
<meta name="googlebot" content="index, nofollow">
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
            </head>
            <body>
                <h1>Flask App</h1>
            </body>
        </html>
```