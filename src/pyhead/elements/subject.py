from markupsafe import escape

from .._base import BaseElement


class Subject(BaseElement):
    key: str = "subject"

    _subject: str

    def __init__(self, subject: str) -> None:
        self._subject = subject

    def __repr__(self) -> str:
        return f"Subject(subject={self._subject!r})"

    def compile(self) -> str:
        return f'<meta name="subject" content="{escape(self._subject)}">'
