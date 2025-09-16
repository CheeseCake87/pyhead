from typing import Any

try:
    from flask import url_for
except ImportError:
    raise ImportError(
        "You are trying to use something from the Flask library, "
        "but Flask is not installed. Install Flask with 'pip install flask'."
    )


class FlaskUrlFor:
    """
    Flask-specific URL generation.

    This will allow the use of Flask's url_for function.

    Flask's url_for function will be called when the head is compiled.
    """

    endpoint: str

    _anchor: str | None = None
    _method: str | None = None
    _scheme: str | None = None
    _external: str | None = None

    values: dict[str, Any]

    def __init__(
        self,
        endpoint: str,
        *,
        _anchor: str | None = None,
        _method: str | None = None,
        _scheme: str | None = None,
        _external: str | None = None,
        **values: Any,
    ) -> None:
        self.endpoint = endpoint
        self._anchor = _anchor
        self._method = _method
        self._scheme = _scheme
        self._external = _external
        self.values = values

    def compile(self) -> str:
        return url_for(
            self.endpoint,
            _anchor=self._anchor,
            _method=self._method,
            _scheme=self._scheme,
            _external=self._external,
            **self.values,
        )
