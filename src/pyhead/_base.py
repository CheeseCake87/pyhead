from typing import Optional

from markupsafe import Markup


class BaseElement:
    """
    Shared behaviour for simple (leaf) head elements.

    Subclasses must implement ``compile()`` returning a string of HTML. The
    mixin provides the boilerplate ``__str__`` and ``__call__`` wrappers that
    every element needs — both return a ``Markup`` of the compiled output so
    the result is usable directly inside a Jinja template.

    Subclasses may set a ``key`` attribute to opt into deduplication /
    ordering inside ``Head.e``.
    """

    key: Optional[str] = None

    def compile(self) -> str:
        raise NotImplementedError

    def __str__(self) -> Markup:
        return Markup(self.compile())

    def __call__(self) -> Markup:
        return Markup(self.compile())
