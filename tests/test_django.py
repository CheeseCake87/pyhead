import pytest

django = pytest.importorskip("django")

from django.conf import settings  # noqa: E402


def _configure_django() -> None:
    if settings.configured:
        return
    settings.configure(
        DEBUG=False,
        ALLOWED_HOSTS=["*"],
        ROOT_URLCONF=__name__,
        STATIC_URL="/static/",
        INSTALLED_APPS=[
            "django.contrib.staticfiles",
            "pyhead.django",
        ],
        TEMPLATES=[
            {
                "BACKEND": "django.template.backends.django.DjangoTemplates",
                "DIRS": [],
                "APP_DIRS": False,
                "OPTIONS": {
                    "libraries": {
                        "pyhead": "pyhead.django.templatetags.pyhead",
                    },
                },
            }
        ],
    )
    django.setup()


_configure_django()


from django.http import HttpResponse  # noqa: E402
from django.template import Context, Template  # noqa: E402
from django.urls import path  # noqa: E402

from pyhead import Head  # noqa: E402
from pyhead.django import DjangoStatic, DjangoUrlFor  # noqa: E402
from pyhead.elements import Page, Script, Stylesheet  # noqa: E402


def _home(_request):  # pragma: no cover - only registered for reverse() to find
    return HttpResponse("ok")


urlpatterns = [
    path("", _home, name="home"),
    path("article/<int:pk>/", _home, name="article"),
]


# ---------- DjangoUrlFor ----------


def test_django_url_for_resolves_simple_route():
    assert DjangoUrlFor("home").compile() == "/"


def test_django_url_for_passes_kwargs():
    assert DjangoUrlFor("article", pk=42).compile() == "/article/42/"


def test_django_url_for_defers_until_compile():
    u = DjangoUrlFor("home")
    assert u.view_name == "home"
    assert u.compile() == "/"


# ---------- DjangoStatic ----------


def test_django_static_prefixes_static_url():
    assert DjangoStatic("main.css").compile() == "/static/main.css"


def test_django_static_nested_path():
    assert (
        DjangoStatic("favicons/favicon.ico").compile() == "/static/favicons/favicon.ico"
    )


# ---------- Elements compose with the deferred helpers ----------


def test_stylesheet_uses_django_static_at_compile_time():
    out = str(Stylesheet(DjangoStatic("main.css")))
    assert 'href="/static/main.css"' in out


def test_script_uses_django_url_for_at_compile_time():
    out = str(Script(src=DjangoUrlFor("home")))
    assert 'src="/"' in out


# ---------- Template tags ----------


def _render(source: str, head_obj: Head) -> str:
    return Template(source).render(Context({"head": head_obj}))


def test_head_templatetag_renders_full_head():
    out = _render(
        "{% load pyhead %}{% head head %}",
        Head([Page(title="Hi")]),
    )
    assert out.startswith("<head>")
    assert out.rstrip().endswith("</head>")
    assert "<title>Hi</title>" in out


def test_head_templatetag_can_omit_wrapping_head_and_title():
    out = _render(
        "{% load pyhead %}{% head head render_head_tag=False render_title_tag=False %}",
        Head([Page(title="Hi", description="D")]),
    )
    assert "<head>" not in out
    assert "</head>" not in out
    assert "<title>" not in out
    assert 'name="description" content="D"' in out


def test_head_title_templatetag_renders_only_title_text():
    out = _render(
        "{% load pyhead %}<title>{% head_title head %}</title>",
        Head([Page(title="Just Title")]),
    )
    assert out.strip() == "<title>Just Title</title>"


def test_head_title_templatetag_escapes_html():
    out = _render(
        "{% load pyhead %}{% head_title head %}",
        Head([Page(title="<script>alert(1)</script>")]),
    )
    assert "<script>" not in out
    assert "&lt;script&gt;alert(1)&lt;/script&gt;" in out


def test_head_title_templatetag_fallback_when_no_title():
    out = _render(
        "{% load pyhead %}<title>{% head_title head %}</title>",
        Head([]),
    )
    assert out.strip() == "<title>Title Not Set</title>"


def test_head_via_str_does_not_get_autoescaped():
    """Head.__html__ lets Django render {{ head }} without |safe."""
    out = _render("{{ head }}", Head([Page(title="Hi")]))
    assert "<title>Hi</title>" in out
    assert "&lt;" not in out
