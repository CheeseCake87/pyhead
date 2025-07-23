# pyhead 🐍🤯

[![PyPI version](https://badge.fury.io/py/pyhead.svg)](https://badge.fury.io/py/pyhead)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/CheeseCake87/pyhead/master/LICENSE)

The Python HTML `<head>` filler.

`pip install pyhead`

<!-- TOC -->
* [pyhead 🐍🤯](#pyhead-)
  * [What is Pyhead?](#what-is-pyhead)
  * [Flask example](#flask-example)
  * [Usage Examples](#usage-examples)
    * [Route by Route](#route-by-route)
    * [Copy and Extend](#copy-and-extend)
  * [CLI Commands](#cli-commands)
    * [Generating favicons](#generating-favicons)
<!-- TOC -->

## What is Pyhead?

Pyhead is a Python package that helps you generate the `<head>` tag for your HTML pages.

## Flask example

```python
from flask import Flask, render_template

from pyhead import Head
from pyhead import elements as e


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        head = Head([
            e.Page(
                title="Hello World",
                description="This is a test",
                keywords="test, hello, world",
                subject="Hello World",
                rating="General",
            ),
            e.Base("http://127.0.0.1:5000"),
            e.Robots("index, follow"),
            e.ContentSecurityPolicy(),
            e.ReferrerPolicy("no-referrer"),
            e.Google(
                googlebot="index, follow",
                no_sitelinks_search_box=True,
                no_translate=True,
            ),
            e.Verification(
                google="1234567890",
                yandex="1234567890",
                bing="1234567890",
                alexa="1234567890",
            ),
            e.GeoPosition(
                icbm="55.86013028402754, -4.252019430273945",
                geo_position="55.86013028402754;-4.252019430273945",
                geo_region="en_GB",
                geo_placename="Duke of Wellington",
            ),
            e.SocialMediaCard(
                site_account="@example",
                creator_account="@example",
                title="Example",
                description="Example",
                image="https://example.com/image.png",
                image_alt="Example",
                site_name="Example",
                url="https://example.com",
                locale="en_US",
            ),
            e.Favicon(
                ico_icon_href="/static/favicons/favicon.ico",
                png_icon_16_href="/static/favicons/favicon-16x16.png",
                png_icon_32_href="/static/favicons/favicon-32x32.png",
                png_icon_64_href="/static/favicons/favicon-64x64.png",
                png_icon_96_href="/static/favicons/favicon-96x96.png",
                png_icon_180_href="/static/favicons/favicon-180x180.png",
                png_icon_196_href="/static/favicons/favicon-196x196.png",
                png_apple_touch_icon_57_href="/static/favicons/apple-touch-icon-57x57.png",
                png_apple_touch_icon_60_href="/static/favicons/apple-touch-icon-60x60.png",
                png_apple_touch_icon_72_href="/static/favicons/apple-touch-icon-72x72.png",
                png_apple_touch_icon_76_href="/static/favicons/apple-touch-icon-76x76.png",
                png_apple_touch_icon_114_href="/static/favicons/apple-touch-icon-114x114.png",
                png_apple_touch_icon_120_href="/static/favicons/apple-touch-icon-120x120.png",
                png_apple_touch_icon_144_href="/static/favicons/apple-touch-icon-144x144.png",
                png_apple_touch_icon_152_href="/static/favicons/apple-touch-icon-152x152.png",
                png_apple_touch_icon_167_href="/static/favicons/apple-touch-icon-167x167.png",
                png_apple_touch_icon_180_href="/static/favicons/apple-touch-icon-180x180.png",
                png_mstile_70_href="/static/favicons/mstile-70x70.png",
                png_mstile_270_href="/static/favicons/mstile-270x270.png",
                png_mstile_310x150_href="/static/favicons/mstile-310x150.png",
                png_mstile_310_href="/static/favicons/mstile-310x150.png",
            ),
            e.Link(rel="canonical", href="https://example.com"),
            e.Link(rel="canonical", href="https://example.co.uk"),
            e.Script(type_="module", src="/static/example.js"),
            e.Stylesheet("/static/main.css"),
        ])

        return render_template("index.html", head=head)

    return app
```

`index.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
<title>{{ head.title }}</title>
{{ head.compile(skip_title=True) }}
</head>

<body>
{% block content %}

{% endblock %}
</body>
</html>
```

or

```html
<!DOCTYPE html>
<html lang="en">
<head>
{{ head.compile() }}
</head>

<body>
{% block content %}

{% endblock %}
</body>
</html>
```

Results in:

```html
<html lang="en">
<head>
<title>Hello World</title>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1" >
<meta name="description" content="This is a test" >
<meta name="keywords" content="test,  hello,  world">
<meta name="subject" content="Hello World" >
<meta name="rating" content="General" >
<base href="http://127.0.0.1:5000">
<meta name="robots" content="index, follow" >
<meta http-equiv="Content-Security-Policy" content="default-src 'self'" >
<meta name="referrer" content="no-referrer" >
<meta name="googlebot" content="index, follow" >
<meta name="google" content="notranslate" >
<meta name="google-site-verification" content="1234567890" >
<meta name="yandex-verification" content="1234567890" >
<meta name="msvalidate.01" content="1234567890" >
<meta name="alexaVerifyID" content="1234567890" >
<meta name="ICBM" content="55.86013028402754, -4.252019430273945" >
<meta name="geo.position" content="55.86013028402754;-4.252019430273945" >
<meta name="geo.region" content="en_GB" >
<meta name="geo.placename" content="Duke of Wellington" >
<meta name="twitter:card" content="summary_large_image" >
<meta name="twitter:site" content="@example" >
<meta name="twitter:creator" content="@example" >
<meta name="twitter:title" content="Example" >
<meta name="twitter:description" content="Example" >
<meta name="twitter:image" content="https://example.com/image.png" >
<meta name="twitter:image:alt" content="Example" >
<meta name="twitter:url" content="https://example.com" >
<meta property="og:type" content="website" >
<meta property="og:locale" content="en_US" >
<meta property="og:site_name" content="Example" >
<meta property="og:title" content="Example" >
<meta property="og:description" content="Example" >
<meta property="og:image" content="https://example.com/image.png" >
<meta property="og:image:alt" content="Example" >
<meta property="og:url" content="https://example.com" >
<link rel="icon" href="/static/favicons/favicon.ico" sizes="16x16 32x32" type="image/x-icon">
<link rel="icon" href="/static/favicons/favicon-16x16.png" sizes="16x16" type="image/png">
<link rel="icon" href="/static/favicons/favicon-32x32.png" sizes="32x32" type="image/png">
<link rel="icon" href="/static/favicons/favicon-64x64.png" sizes="64x64" type="image/png">
<link rel="icon" href="/static/favicons/favicon-96x96.png" sizes="96x96" type="image/png">
<link rel="icon" href="/static/favicons/favicon-180x180.png" sizes="180x180" type="image/png">
<link rel="icon" href="/static/favicons/favicon-196x196.png" sizes="196x196" type="image/png">
<link rel="apple-touch-icon" href="/static/favicons/apple-touch-icon-57x57.png" sizes="57x57" type="image/png">
<link rel="apple-touch-icon" href="/static/favicons/apple-touch-icon-60x60.png" sizes="60x60" type="image/png">
<link rel="apple-touch-icon" href="/static/favicons/apple-touch-icon-72x72.png" sizes="72x72" type="image/png">
<link rel="apple-touch-icon" href="/static/favicons/apple-touch-icon-76x76.png" sizes="76x76" type="image/png">
<link rel="apple-touch-icon" href="/static/favicons/apple-touch-icon-114x114.png" sizes="114x114" type="image/png">
<link rel="apple-touch-icon" href="/static/favicons/apple-touch-icon-120x120.png" sizes="120x120" type="image/png">
<link rel="apple-touch-icon" href="/static/favicons/apple-touch-icon-144x144.png" sizes="144x144" type="image/png">
<link rel="apple-touch-icon" href="/static/favicons/apple-touch-icon-152x152.png" sizes="152x152" type="image/png">
<link rel="apple-touch-icon" href="/static/favicons/apple-touch-icon-167x167.png" sizes="167x167" type="image/png">
<link rel="apple-touch-icon" href="/static/favicons/apple-touch-icon-180x180.png" sizes="180x180" type="image/png">
<link rel="msapplication-square70x70logo" href="/static/favicons/mstile-70x70.png">
<link rel="msapplication-square270x270logo" href="/static/favicons/mstile-270x270.png">
<link rel="msapplication-wide310x150logo" href="/static/favicons/mstile-310x150.png">
<link rel="msapplication-wide310x150logo" href="/static/favicons/mstile-310x150.png">
<link rel="canonical" href="https://example.com">
<link rel="canonical" href="https://example.co.uk">
<script src="/static/example.js" type="module"></script>
<link rel="stylesheet" href="/static/main.css">
</head>
<body>
<h1>Flask App</h1>
<p>Right-Click view source</p>
</body>
</html>

```

## Usage Examples

### Route by Route

```python
...
from pyhead import Head
from pyhead import elements as e
...

@app.get("/")
def index():
    head = Head([
        e.Page(
            title="Hello World",
            description="This is a test",
            keywords="test, hello, world",
            subject="Hello World",
            rating="General",
        )
    ])
    return render_template("index.html", head=head)
```

### Copy and Extend

`app/page_head.py`
```python
...
from pyhead import Head
from pyhead import elements as e
...

head = Head([
    e.Page(
        title="Hello World",
        description="This is a test",
        keywords="test, hello, world",
        subject="Hello World",
        rating="General",
    )
])
```
`app/__init__.py`

```python
...
from app.page_head import head
from pyhead import elements as e
...


@app.get("/my-cool-page")
def my_cool_page():
  my_cool_page_head = head.copy().extend([
    e.Page(
      title="This is my cool page",
      description="This is a test",
      keywords="test, hello, world",
      subject="Hello World",
      rating="General",
    ),
    e.Robots(
      "index, follow"
    )
  ])
  return render_template("my_cool_page.html", head=my_cool_page_head)
```

## CLI Commands

### Generating favicons

You can generate favicons from a source image using the cli command `pyhead favicons -s favicon-gen-test.png`

This uses the python package `favicons` to generate the favicons.

You need to install the `favicons` package to use this command.

```bash
pip install favicons
```

All paths in the cli command are relative to the current working directory.

Only the following source formats are supported:

png, jpg, jpeg, gif, svg, tiff

`-s, --source` This will look for the image file to use

`-o, --output` This will be the output directory for the favicons

`-hp, --href-prefix` This will prefix the href tag in the output html

The following command:

```bash
pyhead favicons -s favicon-gen-test.png -o favicons -hp https://example.com
```

Will create a folder called `favicons` with the following files:

```text
apple-touch-icon-57x57.png
apple-touch-icon-60x60.png
apple-touch-icon-72x72.png
apple-touch-icon-76x76.png
apple-touch-icon-114x114.png
apple-touch-icon-120x120.png
apple-touch-icon-144x144.png
apple-touch-icon-152x152.png
apple-touch-icon-167x167.png
apple-touch-icon-180x180.png
favicon-16x16.png
favicon-32x32.png
favicon-64x64.png
favicon-96x96.png
favicon-180x180.png
favicon-196x196.png
favicon-delete_me_after_use.html
favicon-delete_me_after_use.py
mstile-70x70.png
mstile-270x270.png
mstile-310x150.png
mstile-310x310.png
```

The `favicon-delete_me_after_use.html` file will contain the following:

```html

<link rel="icon" href="https://example.com/favicon.ico" sizes="16x16 32x32">
<link rel="icon" href="https://example.com/favicon-16x16.png" sizes="16x16">
<link rel="icon" href="https://example.com/favicon-32x32.png" sizes="32x32">
<link rel="icon" href="https://example.com/favicon-64x64.png" sizes="64x64">
<link rel="icon" href="https://example.com/favicon-96x96.png" sizes="96x96">
<link rel="icon" href="https://example.com/favicon-180x180.png" sizes="180x180">
<link rel="icon" href="https://example.com/favicon-196x196.png" sizes="196x196">
<link rel="apple-touch-icon" href="https://example.com/apple-touch-icon-57x57.png" sizes="57x57">
<link rel="apple-touch-icon" href="https://example.com/apple-touch-icon-60x60.png" sizes="60x60">
<link rel="apple-touch-icon" href="https://example.com/apple-touch-icon-72x72.png" sizes="72x72">
<link rel="apple-touch-icon" href="https://example.com/apple-touch-icon-76x76.png" sizes="76x76">
<link rel="apple-touch-icon" href="https://example.com/apple-touch-icon-114x114.png" sizes="114x114">
<link rel="apple-touch-icon" href="https://example.com/apple-touch-icon-120x120.png" sizes="120x120">
<link rel="apple-touch-icon" href="https://example.com/apple-touch-icon-144x144.png" sizes="144x144">
<link rel="apple-touch-icon" href="https://example.com/apple-touch-icon-152x152.png" sizes="152x152">
<link rel="apple-touch-icon" href="https://example.com/apple-touch-icon-167x167.png" sizes="167x167">
<link rel="apple-touch-icon" href="https://example.com/apple-touch-icon-180x180.png" sizes="180x180">
<link rel="msapplication-square70x70logo" href="https://example.com/mstile-70x70.png">
<link rel="msapplication-square270x270logo" href="https://example.com/mstile-270x270.png">
<link rel="msapplication-wide310x150logo" href="https://example.com/mstile-310x150.png">
<link rel="msapplication-wide310x150logo" href="https://example.com/mstile-310x150.png">
```

The `favicon-delete_me_after_use.py` file will contain the following:

```python
from pyhead.elements import Favicon

Favicon(
    ico_icon_href="https://example.com/favicon.ico",
    png_icon_16_href="https://example.com/favicon-16x16.png",
    png_icon_32_href="https://example.com/favicon-32x32.png",
    png_icon_64_href="https://example.com/favicon-64x64.png",
    png_icon_96_href="https://example.com/favicon-96x96.png",
    png_icon_180_href="https://example.com/favicon-180x180.png",
    png_icon_196_href="https://example.com/favicon-196x196.png",
    png_apple_touch_icon_57_href="https://example.com/apple-touch-icon-57x57.png",
    png_apple_touch_icon_60_href="https://example.com/apple-touch-icon-60x60.png",
    png_apple_touch_icon_72_href="https://example.com/apple-touch-icon-72x72.png",
    png_apple_touch_icon_76_href="https://example.com/apple-touch-icon-76x76.png",
    png_apple_touch_icon_114_href="https://example.com/apple-touch-icon-114x114.png",
    png_apple_touch_icon_120_href="https://example.com/apple-touch-icon-120x120.png",
    png_apple_touch_icon_144_href="https://example.com/apple-touch-icon-144x144.png",
    png_apple_touch_icon_152_href="https://example.com/apple-touch-icon-152x152.png",
    png_apple_touch_icon_167_href="https://example.com/apple-touch-icon-167x167.png",
    png_apple_touch_icon_180_href="https://example.com/apple-touch-icon-180x180.png",
    png_mstile_70_href="https://example.com/mstile-70x70.png",
    png_mstile_270_href="https://example.com/mstile-270x270.png",
    png_mstile_310x150_href="https://example.com/mstile-310x150.png",
    png_mstile_310_href="https://example.com/mstile-310x150.png",
)
```

Remember to delete the `favicon-delete_me_after_use.html` and `favicon-delete_me_after_use.py` files after use.
