import json
import pathlib

from flask import Flask, render_template

from pyhead import Head


def create_app():
    app = Flask(__name__)

    @app.route("/json")
    def json_method():
        json_file = pathlib.Path(__file__).parent / "head.json"

        head = Head(**json.loads(json_file.read_text()))

        return render_template("index.html", head=head)

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
