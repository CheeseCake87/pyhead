from typing import Protocol, runtime_checkable


@runtime_checkable
class CompileDelayed(Protocol):
    """
    A value whose final string form is produced lazily by calling ``compile()``.

    Used for things like ``FlaskUrlFor`` that need to defer resolution until
    the surrounding ``Head`` is rendered (e.g. to acquire a request context).

    Note on ``@runtime_checkable``: ``isinstance(x, CompileDelayed)`` only
    verifies that ``x`` has a ``compile`` attribute — it does not check that
    the attribute is callable or returns a ``str``. Callers that rely on
    isinstance to branch should trust the duck-type contract; if you hand
    pyhead an object with a non-callable ``compile`` attribute, rendering
    will fail at compile time, not at dispatch time.
    """

    def compile(self) -> str: ...
