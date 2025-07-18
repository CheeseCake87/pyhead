from docutils.nodes import title
from flask import Flask, render_template

from pyhead import Head
from pyhead.elements import Page, Title, Keywords, Description


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        head = Head([Page(title="Hello World", description="This is a test")])

        return render_template("index.html", head=head)

    return app


# head = Head(
#     base="http://127.0.0.1:5000",
#     title="Hello World",
#     exclude_title_tags=True,
#     description="This is a test",
#     keywords="test, hello, world",
#     subject="Hello World",
#     rating="General",
#     robots="index, follow",
# )
# head.set_default_content_security_policy()
# head.set_referrer_policy("no-referrer")
# head.set_google(
#     googlebot="index, follow",
#     no_sitelinks_search_box=True,
#     no_translate=True,
# )
# head.set_verification(
#     google="1234567890",
#     yandex="1234567890",
#     bing="1234567890",
#     alexa="1234567890",
#     pinterest="1234567890",
#     norton="1234567890",
# )
# head.set_geo_position(
#     icbm="55.86013028402754, -4.252019430273945",
#     geo_position="55.86013028402754;-4.252019430273945",
#     geo_region="en_GB",
#     geo_placename="Duke of Wellington",
# )
# head.set_twitter_card(
#     card="summary",
#     site_account="@example",
#     creator_account="@example",
#     title="Example",
#     description="Example",
#     image="https://example.com/image.png",
#     image_alt="Example",
# )
# head.set_opengraph_website(
#     site_name="Example",
#     title="Example",
#     description="Example",
#     url="https://example.com",
#     image="https://example.com/image.png",
#     image_alt="Example",
#     locale="en_US",
# )
# head.set_favicon(
#     ico_icon_href="/static/favicons/favicon.ico",
#     png_icon_16_href="/static/favicons/favicon-16x16.png",
#     png_icon_32_href="/static/favicons/favicon-32x32.png",
#     png_icon_64_href="/static/favicons/favicon-64x64.png",
#     png_icon_96_href="/static/favicons/favicon-96x96.png",
#     png_icon_180_href="/static/favicons/favicon-180x180.png",
#     png_icon_196_href="/static/favicons/favicon-196x196.png",
#     png_apple_touch_icon_57_href="/static/favicons/apple-touch-icon-57x57.png",
#     png_apple_touch_icon_60_href="/static/favicons/apple-touch-icon-60x60.png",
#     png_apple_touch_icon_72_href="/static/favicons/apple-touch-icon-72x72.png",
#     png_apple_touch_icon_76_href="/static/favicons/apple-touch-icon-76x76.png",
#     png_apple_touch_icon_114_href="/static/favicons/apple-touch-icon-114x114.png",
#     png_apple_touch_icon_120_href="/static/favicons/apple-touch-icon-120x120.png",
#     png_apple_touch_icon_144_href="/static/favicons/apple-touch-icon-144x144.png",
#     png_apple_touch_icon_152_href="/static/favicons/apple-touch-icon-152x152.png",
#     png_apple_touch_icon_167_href="/static/favicons/apple-touch-icon-167x167.png",
#     png_apple_touch_icon_180_href="/static/favicons/apple-touch-icon-180x180.png",
#     png_mstile_70_href="/static/favicons/mstile-70x70.png",
#     png_mstile_270_href="/static/favicons/mstile-270x270.png",
#     png_mstile_310x150_href="/static/favicons/mstile-310x150.png",
#     png_mstile_310_href="/static/favicons/mstile-310x150.png",
# )
#
# head.set_link_tag("canonical", "https://example.com")
# head.set_link_tag("canonical", "https://example.co.uk")
#
# head.set_script_tag("/static/example.js", type_="module")
# head.set_stylesheet("/static/main.css")
#
# head.reset_title_appends()
# head.reset_title_prepends()
#
# head.append_title("Append", " - ")
# head.append_title("Append", " - ")
# head.prepend_title("Prepend", " - ")
