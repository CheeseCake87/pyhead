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
