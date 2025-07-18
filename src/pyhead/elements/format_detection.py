from markupsafe import Markup

from .meta import Meta


class FormatDetection:
    unique: bool = True
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
            "<FormatDetection "
            f'telephone="{self._telephone}" '
            f'date="{self._date}" '
            f'address="{self._address}" '
            f'email="{self._email}" '
            f'url="{self._url}">'
        )

    def __str__(self) -> Markup:
        return Markup(self._compile())

    def __call__(self) -> Markup:
        return Markup(self._compile())

    def _compile(self) -> str:
        content = []

        if not self._telephone:
            content.append("telephone=no")
        if not self._date:
            content.append("date=no")
        if not self._address:
            content.append("address=no")
        if not self._email:
            content.append("email=no")
        if not self._url:
            content.append("url=no")

        if not content:
            return ""

        meta = Meta(name="format-detection", content=",".join(content))
        return str(meta)
