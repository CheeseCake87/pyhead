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
        head.set_referrer_policy('no-referrer', 'origin')
        head.set_default_content_security_policy()
        head.set_title('Hello World')
        head.set_description('This is a test')
        head.set_keywords('test, hello, world')
        head.set_description('This is a test')
        head.set_rating('General')
        head.set_robots('index, follow')
        head.set_google(googlebot='index, follow')
        head.set_geo_position(
            icbm='55.86013028402754, -4.252019430273945',
            geo_position='55.86013028402754;-4.252019430273945',
            geo_region='en_GB',
            geo_placename='Duke of Wellington',
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
        head.append_title('Hello World1', ' - ')
        head.prepend_title('Hello World2', ' - ')

        head.set_link_tag('canonical', 'https://example.com')

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

        print(head.as_dict())

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

    @app.route('/class')
    def class_only():
        head2 = Head(
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
            }
        )
        head2.append_title('Hello World1', ' - ')
        head2.prepend_title('Hello World2', ' - ')

        head2.set_meta_tag(name='test', content='test', is_http_equiv=True)

        head2.set_link_tag('canonical', 'https://example.com')

        print(head2.as_dict())

        return f"""\
            <html>
                <head>
                    {head2}
                </head>
                <body>
                    <h1>Flask App</h1>
                    <p>Right-Click view source</p>
                </body>
            </html>
            """

    return app
