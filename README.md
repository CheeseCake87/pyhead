# pyhead 🐍🤯

[![PyPI version](https://badge.fury.io/py/pyhead.svg)](https://badge.fury.io/py/pyhead)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/CheeseCake87/pyhead/master/LICENSE)

The Python HTML `<head>` filler.

`pip install pyhead`

TOC:

- [What is Pyhead?](#what-is-pyhead)
- [Flask example](#flask-example)
- [Advanced use cases](#advanced-use-cases)
- [dict as args, and JSON](#dict-as-args-and-json)
- [Working with extended templates](#working-with-extended-templates)
- [Generating favicons](#generating-favicons)

## What is Pyhead?

Pyhead is a Python package that helps you generate the `<head>` tag for your HTML pages.

## Flask example:

```python
from flask import Flask, render_template

from pyhead import Head


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        head = Head(
            base="https://example.com",
            title="Hello World",
            exclude_title_tags=True,
            description="This is a test",
            keywords="test, hello, world",
            subject="Hello World",
            rating="General",
            robots="index, follow",
        )
        head.set_default_content_security_policy()
        head.set_referrer_policy(
            policy="no-referrer",
            fallback="origin",
        )
        head.set_google(
            googlebot="index, follow",
            no_sitelinks_search_box=True,
            no_translate=True,
        )
        head.set_verification(
            google="1234567890",
            yandex="1234567890",
            bing="1234567890",
            alexa="1234567890",
            pinterest="1234567890",
            norton="1234567890",
        )
        head.set_geo_position(
            icbm="55.86013028402754, -4.252019430273945",
            geo_position="55.86013028402754;-4.252019430273945",
            geo_region="en_GB",
            geo_placename="Duke of Wellington",
        )
        head.set_twitter_card(
            card="summary",
            site_account="@example",
            creator_account="@example",
            title="Example",
            description="Example",
            image="https://example.com/image.png",
            image_alt="Example",
        )
        head.set_opengraph_website(
            site_name="Example",
            title="Example",
            description="Example",
            url="https://example.com",
            image="https://example.com/image.png",
            image_alt="Example",
            locale="en_US",
        )
        head.set_favicon(
            ico_icon_16_32_href="https://example.com/favicon.ico",
            png_icon_16_href="https://example.com/favicon-16x16.png",
            png_icon_32_href="https://example.com/favicon-32x32.png",
            png_icon_128_href="https://example.com/favicon-128x128.png",
            png_icon_180_href="https://example.com/favicon-180x180.png",
            png_icon_192_href="https://example.com/favicon-192x192.png",
            png_icon_228_href="https://example.com/favicon-228x228.png",
            png_icon_512_href="https://example.com/favicon-512x512.png",
            set_icon_192_to_apple_touch_icon=True,
        )

        head.set_link_tag("canonical", "https://example.com")

        return render_template("index.html", head=head)

    return app
```

`index.html`:

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

Results in:

```html

<html lang="en">
<head>
    <!-- Top Level Tags - charset and viewport are set by default -->
    <meta charset="utf-8">
    <meta name="viewport" content="'width=device-width, initial-scale=1.0'">
    <base href="https://example.com">
    <!-- Title Tag -->
    <title>Hello World</title>
    <!-- Meta Tags -->
    <meta name="description" content="This is a test">
    <meta name="keywords" content="test, hello, world">
    <meta name="subject" content="Hello World">
    <meta name="rating" content="General">
    <meta name="robots" content="index, follow">
    <meta name="referrer" content="origin, no-referrer">
    <meta name="googlebot" content="index, follow">
    <meta name="google" content="notranslate">
    <meta name="google-site-verification" content="1234567890">
    <meta name="yandex-verification" content="1234567890">
    <meta name="msvalidate.01" content="1234567890">
    <meta name="alexaVerifyID" content="1234567890">
    <meta name="p:domain_verify" content="1234567890">
    <meta name="norton-safeweb-site-verification" content="1234567890">
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
    <!-- Link Tags -->
    <link rel="icon" href="https://example.com/favicon.ico" sizes="16x16 32x32" type="image/x-icon">
    <link rel="icon" href="https://example.com/favicon-16x16.png" sizes="16x16" type="image/png">
    <link rel="icon" href="https://example.com/favicon-32x32.png" sizes="32x32" type="image/png">
    <link rel="icon" href="https://example.com/favicon-128x128.png" sizes="128x128" type="image/png">
    <link rel="icon" href="https://example.com/favicon-180x180.png" sizes="180x180" type="image/png">
    <link rel="icon" href="https://example.com/favicon-192x192.png" sizes="192x192" type="image/png">
    <link rel="icon" href="https://example.com/favicon-512x512.png" sizes="512x512" type="image/png">
    <link rel="apple-touch-icon" href="https://example.com/favicon-192x192.png">
    <link rel="canonical" href="https://example.com">
</head>
<body>
<h1>Flask App</h1>
<p>Right-Click view source</p>
</body>
</html>

```

The following will result in the same output as above but with less template control over the title tag, **Note** You
must remove the `exclude_title_tags=True`, from the Head() constructor.

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

## Advanced use cases:

### dict as args, and JSON

You can pass a dict to the Head() constructor to set the values of the tags.
The keys must match the arguments of the set method.

```python
head = Head(
    ...,
    twitter_card={
        "card": "summary",
        "site_account": "@example",
        "creator_account": "@example",
        "title": "Example",
        "description": "Example",
        "image": "https://example.com/image.png",
        "image_alt": "Example",
    },
)
```

This is replacing the `set_twitter_card()` method.

With this, you can store the values in a database as JSON objects then pass them to the Head() constructor.

```python
page = model.get_page_by_name("index")

head = Head(
    ...,
    twitter=page.twitter_card,
)
```

A really efficient way would be to store the entire head object as JSON and pass it to the Head() constructor.

```python
page = model.get_page_by_name("index")

head = Head(**page.head)
```

the stored JSON data in this case would look something like:

```json
{
  "base": "https://example.com",
  "title": "Hello World",
  "exclude_title_tags": true,
  "description": "This is a test",
  "keywords": "test, hello, world",
  "subject": "Hello World",
  "rating": "General",
  "robots": "index, follow",
  "referrer_policy": {
    "policy": "no-referrer",
    "fallback": "origin"
  },
  "google": {
    "googlebot": "index, follow",
    "no_sitelinks_search_box": true,
    "no_translate": true
  },
  "twitter_card": {
    "card": "summary",
    "site_account": "@example",
    "creator_account": "@example",
    "title": "Example",
    "description": "Example",
    "image": "https://example.com/image.png",
    "image_alt": "Example"
  },
  "favicon": {
    "ico_icon_16_32_href": "https://example.com/favicon.ico"
  }
}
```

### Working with extended templates

The head object can be modified in templates that extend other templates. Here's an example:

`extends.html`

```html

<!DOCTYPE html>

<html lang="en">
<head>
    {%- block head -%}
    {{ head() }}
    {% endblock %}
</head>
<body>
{% block content %}

{% endblock %}
</body>
</html>

```

`index.hml`

```html

{% extends "extends.html" %}

{% block head %}
{% set _ = head.append_title('Flask App', ' - ') %}
{% set _ = head.remove_link_tag('canonical') %}
{{ super() }}
{% endblock %}

{% block content %}
<h1>Flask App</h1>
<p>Right-Click view source</p>
{% endblock %}

```

In this example the `<link rel="canonical" href="https://example.com">`
tag is removed, and the title is appended, resulting in:

```html
...

<meta charset="utf-8">
<meta name="viewport" content="'width=device-width, initial-scale=1.0'">
<base href="https://example.com">
<title>Hello World - Flask App</title>
...
<link rel="apple-touch-icon" href="https://example.com/favicon-192x192.png">

<!-- /\ No canonical link tag -->
</head>

...
```

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
favicon.html
favicon.ico
favicon-16x16.png
favicon-32x32.png
favicon-64x64.png
favicon-96x96.png
favicon-180x180.png
favicon-196x196.png
mstile-70x70.png
mstile-270x270.png
mstile-310x150.png
mstile-310x310.png
```

The `favicon.html` file will contain the following:

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

You can then copy the contents of the `favicon.html` file into the `<head>` tag of your HTML file.