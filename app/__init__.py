from flask import Flask, render_template

from pyhead import Head, HeadClass
from pyhead import elements as e
from pyhead.flask import FlaskUrlFor

head = Head(
    [
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
            image=FlaskUrlFor("static", filename="favicons/favicon-196x196.png"),
            image_alt="Example",
            site_name="Example",
            url="https://example.com",
            locale="en_US",
        ),
        e.Favicon(
            ico_icon_href=FlaskUrlFor("static", filename="favicons/favicon.ico"),
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
        e.Stylesheet(FlaskUrlFor("static", filename="main.css")),
    ]
)


class StandardHeadClass(HeadClass):
    elements = [
        e.Page(
            title="Head Class",
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
            image=FlaskUrlFor("static", filename="favicons/favicon-196x196.png"),
            image_alt="Example",
            site_name="Example",
            url="https://example.com",
            locale="en_US",
        ),
        e.Favicon(
            ico_icon_href=FlaskUrlFor("static", filename="favicons/favicon.ico"),
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
        e.Stylesheet(FlaskUrlFor("static", filename="main.css")),
    ]


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return render_template("index.html", head=head)

    @app.route("/extend")
    def extend():
        copy_head = head.copy().extend([e.Page(title="Extended")])
        return render_template("index.html", head=copy_head)

    @app.route("/class-based")
    def class_based():
        return render_template("index.html", head=StandardHeadClass())

    return app
