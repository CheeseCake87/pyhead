import pytest
from markupsafe import Markup

from pyhead.elements import (
    ApplicationName,
    Base,
    Charset,
    ContentSecurityPolicy,
    Description,
    Favicon,
    FormatDetection,
    GeoPosition,
    Google,
    Keywords,
    Link,
    Meta,
    OpenGraphWebsite,
    ReferrerPolicy,
    Robots,
    Script,
    Stylesheet,
    ThemeColor,
    Title,
    TwitterCard,
    Verification,
)
from pyhead.protocols import CompileDelayed


class _Delayed:
    """Minimal CompileDelayed stand-in for tests — no Flask needed."""

    def __init__(self, value: str) -> None:
        self._value = value

    def compile(self) -> str:
        return self._value


def test_compile_delayed_is_isinstance():
    assert isinstance(_Delayed("/x"), CompileDelayed)


# ---------- Title ----------


def test_title_basic():
    assert str(Title("Hello")) == "<title>Hello</title>"


def test_title_escapes_angle_brackets():
    out = str(Title("<script>alert(1)</script>"))
    assert "<script>" not in out
    assert "&lt;script&gt;" in out


# ---------- Charset ----------


def test_charset_default():
    assert str(Charset()) == '<meta charset="utf-8">'


def test_charset_custom():
    assert str(Charset("latin-1")) == '<meta charset="latin-1">'


# ---------- Meta ----------


def test_meta_name_content():
    assert str(Meta(name="foo", content="bar")) == '<meta name="foo" content="bar">'


def test_meta_http_equiv():
    assert (
        str(Meta(http_equiv="refresh", content="30"))
        == '<meta http-equiv="refresh" content="30">'
    )


def test_meta_property():
    assert (
        str(Meta(property_="og:type", content="website"))
        == '<meta property="og:type" content="website">'
    )


def test_meta_escapes_quotes_in_content():
    out = str(Meta(name="desc", content='a"b'))
    assert '"a"b"' not in out
    assert "&#34;" in out


def test_meta_requires_one_of_name_http_equiv_property():
    with pytest.raises(ValueError, match="requires exactly one"):
        Meta(content="x")


def test_meta_rejects_multiple_of_name_http_equiv_property():
    with pytest.raises(ValueError, match="not multiple"):
        Meta(name="a", http_equiv="b", content="x")


def test_meta_compile_delayed_content():
    out = str(Meta(name="url", content=_Delayed("/page")))
    assert 'content="/page"' in out


def test_meta_escapes_compile_delayed_output():
    out = str(Meta(name="url", content=_Delayed("a&b")))
    assert "a&amp;b" in out


# ---------- Description / Keywords ----------


def test_description():
    assert (
        str(Description("hello world"))
        == '<meta name="description" content="hello world">'
    )


def test_description_escapes():
    assert "&#34;" in str(Description('say "hi"'))


def test_keywords_from_list():
    assert (
        str(Keywords(from_list=["a", "b"])) == '<meta name="keywords" content="a, b">'
    )


def test_keywords_from_string():
    assert str(Keywords(from_string="a,b")) == '<meta name="keywords" content="a, b">'


def test_keywords_escapes():
    assert "&lt;x&gt;" in str(Keywords(from_list=["<x>"]))


# ---------- Link ----------


def test_link_minimal():
    assert str(Link(rel="canonical", href="/")) == '<link rel="canonical" href="/">'


def test_link_with_all_attrs():
    out = str(
        Link(
            rel="preload",
            href="/f.woff2",
            type_="font/woff2",
            crossorigin="anonymous",
            id_="font-1",
        )
    )
    assert 'rel="preload"' in out
    assert 'href="/f.woff2"' in out
    assert 'type="font/woff2"' in out
    assert 'crossorigin="anonymous"' in out
    assert 'id="font-1"' in out


def test_link_escapes_href():
    out = str(Link(rel="canonical", href="/?a=1&b=2"))
    assert "&amp;" in out


def test_link_compile_delayed_href():
    assert (
        str(Link(rel="stylesheet", href=_Delayed("/s.css")))
        == '<link rel="stylesheet" href="/s.css">'
    )


# ---------- Script ----------


def test_script_minimal():
    assert str(Script(src="/a.js")) == '<script src="/a.js"></script>'


def test_script_type_module_async():
    out = str(Script(src="/a.js", type_="module", async_=True))
    assert 'type="module"' in out
    assert 'async="true"' in out


def test_script_compile_delayed_src():
    assert str(Script(src=_Delayed("/a.js"))) == '<script src="/a.js"></script>'


def test_script_escapes_src():
    assert "&amp;" in str(Script(src="/a.js?x=1&y=2"))


# ---------- Base / Stylesheet / ApplicationName / CSP / ThemeColor / ReferrerPolicy / Robots ----------


def test_base():
    assert str(Base("https://example.com/")) == '<base href="https://example.com/">'


def test_base_compile_delayed():
    assert str(Base(_Delayed("/"))) == '<base href="/">'


def test_stylesheet_minimal():
    assert str(Stylesheet("/app.css")) == '<link rel="stylesheet" href="/app.css">'


def test_stylesheet_with_id():
    assert (
        str(Stylesheet("/app.css", id_="main"))
        == '<link rel="stylesheet" href="/app.css" id="main">'
    )


def test_application_name():
    assert (
        str(ApplicationName("MyApp"))
        == '<meta name="application_name" content="MyApp">'
    )


def test_content_security_policy_default():
    out = str(ContentSecurityPolicy())
    assert 'http-equiv="Content-Security-Policy"' in out
    assert "default-src &#39;self&#39;" in out


def test_theme_color():
    assert str(ThemeColor("#ff0000")) == '<meta name="theme-color" content="#ff0000">'


def test_referrer_policy():
    assert (
        str(ReferrerPolicy("no-referrer"))
        == '<meta name="referrer" content="no-referrer">'
    )


def test_robots():
    assert (
        str(Robots("index, follow")) == '<meta name="robots" content="index, follow">'
    )


# ---------- Google ----------


def test_google_no_sitelinks_search_box_is_emitted():
    out = str(Google(no_sitelinks_search_box=True))
    assert 'content="nositelinkssearchbox"' in out


def test_google_combined():
    out = str(
        Google(
            googlebot="index, follow",
            no_sitelinks_search_box=True,
            no_translate=True,
        )
    )
    assert 'name="googlebot"' in out
    assert "nositelinkssearchbox" in out
    assert "notranslate" in out


# ---------- GeoPosition ----------


def test_geo_position_icbm():
    out = str(GeoPosition(icbm="1,2"))
    assert 'name="ICBM"' in out


def test_geo_position_all():
    out = str(
        GeoPosition(
            icbm="1,2",
            geo_position="1;2",
            geo_region="en_GB",
            geo_placename="Somewhere",
        )
    )
    for needle in ["ICBM", "geo.position", "geo.region", "geo.placename"]:
        assert needle in out


# ---------- FormatDetection ----------


def test_format_detection_default_empty():
    assert str(FormatDetection()) == ""


def test_format_detection_disabled():
    out = str(FormatDetection(telephone=False, email=False))
    assert 'content="telephone=no,email=no"' in out


# ---------- Verification ----------


def test_verification_google():
    out = str(Verification(google="abc"))
    assert 'name="google-site-verification"' in out
    assert 'content="abc"' in out


def test_verification_no_alexa_param():
    with pytest.raises(TypeError):
        Verification(alexa="x")  # type: ignore[call-arg]


# ---------- TwitterCard / OpenGraphWebsite ----------


def test_twitter_card_default():
    out = str(TwitterCard(title="T"))
    assert 'name="twitter:card" content="summary"' in out
    assert 'name="twitter:title" content="T"' in out


def test_open_graph_website():
    out = str(OpenGraphWebsite(title="T", url="/", site_name="S"))
    assert 'property="og:type" content="website"' in out
    assert 'property="og:title"' in out
    assert 'property="og:url"' in out
    assert 'property="og:site_name"' in out


# ---------- Favicon ----------


def test_favicon_repr_does_not_crash():
    f = Favicon(ico_icon_href="/f.ico", png_mstile_70_href="/m.png")
    assert "Favicon(" in repr(f)


def test_favicon_mstile_emits_type_attribute():
    out = str(Favicon(png_mstile_70_href="/m.png"))
    assert 'type="image/png"' in out


# ---------- Markup return type ----------


def test_str_returns_markup():
    assert isinstance(str.__call__(Title("x")), str)
    assert isinstance(Title("x").__str__(), Markup)


def test_call_returns_markup():
    assert isinstance(Title("x")(), Markup)
