from typing import Any


class DjangoUrlFor:
    """
    Django-specific URL generation.

    This will allow the use of Django's :func:`django.urls.reverse` function
    through the same deferred-compile pattern used elsewhere in pyhead. The
    view name is resolved when the head is compiled, which means the current
    URL configuration is used.

    Example::

        from pyhead.django import DjangoUrlFor
        from pyhead.elements import Link

        Link(rel="canonical", href=DjangoUrlFor("home"))
    """

    view_name: str

    args: tuple[Any, ...]
    kwargs: dict[str, Any]

    _urlconf: Any | None = None
    _current_app: str | None = None

    def __init__(
        self,
        view_name: str,
        *args: Any,
        _urlconf: Any | None = None,
        _current_app: str | None = None,
        **kwargs: Any,
    ) -> None:
        self.view_name = view_name
        self.args = args
        self.kwargs = kwargs
        self._urlconf = _urlconf
        self._current_app = _current_app

    def compile(self) -> str:
        try:
            from django.urls import reverse
        except ImportError as e:
            raise ImportError(
                "You are trying to use DjangoUrlFor, but Django is not installed. "
                "Install Django with 'pip install django'."
            ) from e

        return reverse(
            self.view_name,
            urlconf=self._urlconf,
            args=self.args or None,
            kwargs=self.kwargs or None,
            current_app=self._current_app,
        )


class DjangoStatic:
    """
    Django-specific static file URL generation.

    Wraps :func:`django.templatetags.static.static` (which honours
    ``STATIC_URL`` and any configured staticfiles storage) behind the same
    deferred-compile pattern. The path is resolved when the head is compiled.

    Example::

        from pyhead.django import DjangoStatic
        from pyhead.elements import Stylesheet

        Stylesheet(DjangoStatic("main.css"))
    """

    path: str

    def __init__(self, path: str) -> None:
        self.path = path

    def compile(self) -> str:
        try:
            from django.templatetags.static import static
        except ImportError as e:
            raise ImportError(
                "You are trying to use DjangoStatic, but Django is not installed. "
                "Install Django with 'pip install django'."
            ) from e

        return static(self.path)
