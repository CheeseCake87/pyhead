from markupsafe import escape

from .._base import BaseElement


class Rating(BaseElement):
    key: str = "rating"

    _rating: str

    def __init__(self, rating: str) -> None:
        self._rating = rating

    def __repr__(self) -> str:
        return f"Rating(rating={self._rating!r})"

    def compile(self) -> str:
        return f'<meta name="rating" content="{escape(self._rating)}">'
