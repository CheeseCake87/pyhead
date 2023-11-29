# pyhead

[![PyPI version](https://badge.fury.io/py/pyhead.svg)](https://badge.fury.io/py/pyhead)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/alexandrevicenzi/pyhead/master/LICENSE)

The Python HTML `<head>` filler.

```python
from pyhead import Head

head = Head(page_title="My Page")
head.set_page_description("My Page Description")
head.set_page_keywords(["keyword1", "keyword2"])
```

```jinja
{# using jinja to output #}
<head>
    {{ head }}
</head>
```

```html
<!-- output -->
<head>
    <title>My Page</title>
    <meta name="description" content="My Page Description">
    <meta name="keywords" content="keyword1, keyword2">
</head>
```