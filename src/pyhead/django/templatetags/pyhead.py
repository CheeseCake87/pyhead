from django import template
from django.utils.html import escape
from django.utils.safestring import SafeString, mark_safe

from pyhead import Head

register = template.Library()


@register.simple_tag
def head(
    head_obj: Head,
    *,
    render_head_tag: bool = True,
    render_title_tag: bool = True,
) -> SafeString:
    """
    Render a pyhead ``Head`` inside a Django template.

    Default usage renders the full ``<head>...</head>`` block::

        {% load pyhead %}
        <html>
        {% head head %}
        <body>...</body>
        </html>

    To render the ``<title>`` and the rest separately (for example when you
    want to author the outer ``<head>`` tag yourself)::

        <head>
            <title>{% head_title head %}</title>
            {% head head render_head_tag=False render_title_tag=False %}
        </head>
    """
    return mark_safe(
        head_obj.compile(
            render_head_tag=render_head_tag,
            render_title_tag=render_title_tag,
        )
    )


@register.simple_tag
def head_title(head_obj: Head) -> SafeString:
    """
    Render just the title text (no wrapping ``<title>`` tag).

    The caller is expected to author the ``<title>`` tag themselves; the
    returned value is HTML-escaped so it is safe to drop straight into the
    template.

    Usage::

        {% load pyhead %}
        <head>
            <title>{% head_title head %}</title>
            {% head head render_head_tag=False render_title_tag=False %}
        </head>
    """
    title_element = head_obj.e.get("title")
    if title_element is None:
        return mark_safe("Title Not Set")
    return mark_safe(escape(title_element.title_))
