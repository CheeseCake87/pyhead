import pytest
from markupsafe import Markup

from pyhead import Head, HeadClass
from pyhead.elements import Description, Page, Script, Stylesheet, Title


# ---------- Head basic wiring ----------


def test_head_page_compiles_all_fields():
    out = str(
        Head(
            [
                Page(
                    title="T",
                    description="D",
                    keywords="a, b",
                    subject="S",
                    rating="General",
                )
            ]
        ).compile()
    )
    for needle in [
        '<meta charset="utf-8">',
        "<title>T</title>",
        'name="description" content="D"',
        'name="keywords" content="a,  b"',
        'name="subject" content="S"',
        'name="rating" content="General"',
    ]:
        assert needle in out


def test_head_compile_is_markup():
    assert isinstance(Head([Page(title="T")]).compile(), Markup)


def test_head_title_attr_is_set():
    h = Head([Page(title="My Title")])
    assert h.title == "My Title"


def test_head_skip_title():
    h = Head([Page(title="T")])
    out = str(h.compile(skip_title=True))
    assert "<title>T</title>" not in out
    assert "charset" in out


# ---------- Charset before title ordering ----------


def test_head_emits_charset_before_title():
    out = str(Head([Page(title="T")]).compile())
    charset_idx = out.index('<meta charset="utf-8">')
    title_idx = out.index("<title>T</title>")
    assert charset_idx < title_idx


# ---------- extend ----------


def test_extend_preserves_existing_scripts():
    h = Head([Script("a.js"), Script("b.js")])
    h.extend([Script("c.js")])
    out = str(h.compile())
    assert "a.js" in out
    assert "b.js" in out
    assert "c.js" in out


def test_extend_updates_tracked_elements_for_copy():
    h = Head([Page(title="Orig")])
    h.extend([Description("Added")])
    out = str(h.copy().compile())
    assert "Added" in out
    assert "<title>Orig</title>" in out


# ---------- copy is deep ----------


def test_copy_is_deep():
    h1 = Head([Description("orig")])
    h2 = h1.copy()
    h1.e["description"]._description = "mutated"
    assert "orig" in str(h2.compile())
    assert "mutated" not in str(h2.compile())


def test_copy_and_extend_does_not_mutate_original():
    h1 = Head([Page(title="Original")])
    h2 = h1.copy().extend([Description("Only on h2")])
    assert "Only on h2" not in str(h1.compile())
    assert "Only on h2" in str(h2.compile())


# ---------- Page replaces earlier Page fields ----------


def test_second_page_overwrites_first():
    out = str(Head([Page(title="First"), Page(title="Second")]).compile())
    assert "<title>Second</title>" in out
    assert "<title>First</title>" not in out


# ---------- HeadClass ----------


def test_headclass_direct_instantiation_raises():
    with pytest.raises(TypeError, match="subclassed"):
        HeadClass()


def test_headclass_subclass_without_elements_raises():
    class _NoElems(HeadClass):
        pass

    with pytest.raises(TypeError, match="elements"):
        _NoElems()


def test_headclass_subclass_returns_head_instance():
    class _MyHead(HeadClass):
        elements = [Title("Sub")]

    instance = _MyHead()
    assert isinstance(instance, Head)
    assert "<title>Sub</title>" in str(instance.compile())


# ---------- Keyed vs index-fallback keying ----------


def test_explicit_id_wins_over_fallback():
    h = Head([Script("a.js"), Script("b.js", id_="mine")])
    assert "mine" in h.e
    assert "0" in h.e
    assert "1" not in h.e


def test_stylesheet_id_is_rendered():
    out = str(Stylesheet("/s.css", id_="main"))
    assert 'id="main"' in out
