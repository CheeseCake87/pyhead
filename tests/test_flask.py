import pytest

flask = pytest.importorskip("flask")

from flask import Flask  # noqa: E402

from pyhead.elements import Script, Stylesheet  # noqa: E402
from pyhead.flask import FlaskUrlFor  # noqa: E402


@pytest.fixture
def app():
    app = Flask(__name__, static_url_path="/static")

    @app.route("/", endpoint="home")
    def home():
        return "ok"

    @app.route("/article/<int:pk>/", endpoint="article")
    def article(pk):
        return "ok"

    return app


# ---------- FlaskUrlFor ----------


def test_flask_url_for_resolves_static(app):
    with app.test_request_context():
        assert (
            FlaskUrlFor("static", filename="main.css").compile() == "/static/main.css"
        )


def test_flask_url_for_resolves_named_endpoint(app):
    with app.test_request_context():
        assert FlaskUrlFor("home").compile() == "/"


def test_flask_url_for_passes_values(app):
    with app.test_request_context():
        assert FlaskUrlFor("article", pk=42).compile() == "/article/42/"


def test_flask_url_for_anchor(app):
    with app.test_request_context():
        assert FlaskUrlFor("home", _anchor="section").compile() == "/#section"


def test_flask_url_for_external_uses_scheme(app):
    with app.test_request_context():
        out = FlaskUrlFor("home", _external=True, _scheme="https").compile()
        assert out.startswith("https://")
        assert out.endswith("/")


def test_flask_url_for_defers_until_compile(app):
    u = FlaskUrlFor("static", filename="main.css")
    assert u.endpoint == "static"
    assert u.values == {"filename": "main.css"}

    with app.test_request_context():
        assert u.compile() == "/static/main.css"


def test_flask_url_for_raises_outside_context(app):
    with pytest.raises(RuntimeError):
        FlaskUrlFor("home").compile()


# ---------- Elements compose with FlaskUrlFor ----------


def test_stylesheet_uses_flask_url_for_at_compile_time(app):
    with app.test_request_context():
        out = str(Stylesheet(FlaskUrlFor("static", filename="main.css")))
        assert 'href="/static/main.css"' in out


def test_script_uses_flask_url_for_at_compile_time(app):
    with app.test_request_context():
        out = str(Script(src=FlaskUrlFor("static", filename="example.js")))
        assert 'src="/static/example.js"' in out


# ---------- End-to-end: Head rendered inside a Flask route ----------


def test_head_renders_inside_flask_route(app):
    from pyhead import Head
    from pyhead.elements import Page

    head = Head(
        [
            Page(title="Hi"),
            Stylesheet(FlaskUrlFor("static", filename="main.css")),
        ]
    )

    @app.route("/render")
    def render():
        return str(head)

    client = app.test_client()
    body = client.get("/render").get_data(as_text=True)

    assert "<title>Hi</title>" in body
    assert 'href="/static/main.css"' in body
