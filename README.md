# pyhead 🐍🤯

[![PyPI version](https://badge.fury.io/py/pyhead.svg)](https://badge.fury.io/py/pyhead)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/CheeseCake87/pyhead/master/LICENSE)

The Python HTML `<head>` filler.

`pip install pyhead`

```python
from flask import Flask, render_template

from pyhead import Head


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def dicts_as_args():
        """
        Using __init__ args, with jinja
        """
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
            },
            favicon={
                'ico_icon_16_32_href': 'https://example.com/favicon.ico',
                'png_icon_16_href': 'https://example.com/favicon-16x16.png',
                'png_icon_32_href': 'https://example.com/favicon-32x32.png',
                'png_icon_128_href': 'https://example.com/favicon-128x128.png',
                'png_icon_180_href': 'https://example.com/favicon-180x180.png',
                'png_icon_192_href': 'https://example.com/favicon-192x192.png',
                'png_icon_228_href': 'https://example.com/favicon-228x228.png',
                'png_icon_512_href': 'https://example.com/favicon-512x512.png',
                'set_icon_192_to_apple_touch_icon': True,
            },
            exclude_title_tags=True,
        )
        head.append_title('Hello World1', ' - ')
        head.prepend_title('Hello World2', ' - ')

        head.set_meta_tag(name='tag', content='tag-content')
        head.set_meta_tag(name='another-tag', content='another-tag-content', is_http_equiv=True)

        head.set_link_tag('canonical', 'https://example.com')

        return render_template(
            'index.html',
            head=head
        )

    @app.route('/args')
    def using_args():
        """
        Using set functions, no jinja
        """
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
        head.set_favicon(
            ico_icon_16_32_href='https://example.com/favicon.ico',
            png_icon_16_href='https://example.com/favicon-16x16.png',
            png_icon_32_href='https://example.com/favicon-32x32.png',
            png_icon_128_href='https://example.com/favicon-128x128.png',
            png_icon_180_href='https://example.com/favicon-180x180.png',
            png_icon_192_href='https://example.com/favicon-192x192.png',
            png_icon_228_href='https://example.com/favicon-228x228.png',
            png_icon_512_href='https://example.com/favicon-512x512.png',
            set_icon_192_to_apple_touch_icon=True,
        )

        head.append_title('Hello World1', ' - ')
        head.prepend_title('Hello World2', ' - ')

        head.set_meta_tag(name='tag', content='tag-content')
        head.set_meta_tag(name='another-tag', content='another-tag-content', is_http_equiv=True)

        head.set_link_tag('canonical', 'https://example.com')

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

Jinja usage:

```html

<html lang="en">
<head>
    {{ head.top_level_tags }}
    <title>{{ head.title }}</title>
    {{ head.meta_tags }}
    {{ head.link_tags }}
</head>
<body>
<h1>Flask App</h1>
<p>Right-Click view source</p>
</body>
</html>
```

`{{ head.top_level_tags }}` are:

```html

<meta charset="utf-8">
<meta name="viewport" content="'width=device-width, initial-scale=1.0'">
<base href="https://example.com">
```

This will output all the tags in the correct order:

```html

<html lang="en">
<head>
    {{ head() }}
</head>
<body>
<h1>Flask App</h1>
<p>Right-Click view source</p>
</body>
</html>
```

view-source (Using set functions, no jinja):

```html

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
<link rel="icon" href="https://example.com/favicon.ico" sizes="16x16 32x32" type="image/x-icon">
<link rel="icon" href="https://example.com/favicon-16x16.png" sizes="16x16" type="image/png">
<link rel="icon" href="https://example.com/favicon-32x32.png" sizes="32x32" type="image/png">
<link rel="icon" href="https://example.com/favicon-128x128.png" sizes="128x128" type="image/png">
<link rel="icon" href="https://example.com/favicon-180x180.png" sizes="180x180" type="image/png">
<link rel="icon" href="https://example.com/favicon-192x192.png" sizes="192x192" type="image/png">
<link rel="icon" href="https://example.com/favicon-512x512.png" sizes="512x512" type="image/png">
<link rel="apple-touch-icon" href="https://example.com/favicon-192x192.png">
<link rel="canonical" href="https://example.com">
```