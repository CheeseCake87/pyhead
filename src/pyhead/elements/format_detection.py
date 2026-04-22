from .._base import BaseElement
from .meta import Meta


class FormatDetection(BaseElement):
    key: str = "format_detection"

    _telephone: bool
    _date: bool
    _address: bool
    _email: bool
    _url: bool

    def __init__(
        self,
        telephone: bool = True,
        date: bool = True,
        address: bool = True,
        email: bool = True,
        url: bool = True,
    ) -> None:
        self._telephone = telephone
        self._date = date
        self._address = address
        self._email = email
        self._url = url

    def __repr__(self) -> str:
        return (
            f"FormatDetection(telephone={self._telephone!r}, date={self._date!r}, "
            f"address={self._address!r}, email={self._email!r}, url={self._url!r})"
        )

    def compile(self) -> str:
        __items = []

        if not self._telephone:
            __items.append("telephone=no")
        if not self._date:
            __items.append("date=no")
        if not self._address:
            __items.append("address=no")
        if not self._email:
            __items.append("email=no")
        if not self._url:
            __items.append("url=no")

        if not __items:
            return ""

        return Meta(name="format-detection", content=",".join(__items)).compile()
