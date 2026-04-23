from typing import Literal, Optional, Union

from markupsafe import escape

from .._base import BaseElement

WidthValue = Union[int, Literal["device-width"]]
HeightValue = Union[int, Literal["device-height"]]
UserScalable = Literal["yes", "no"]
InteractiveWidget = Literal["resizes-visual", "resizes-content", "overlays-content"]
ViewportFit = Literal["auto", "contain", "cover"]


class Viewport(BaseElement):
    """
    Renders ``<meta name="viewport" content="...">``.

    Each keyword argument maps to one of the directives documented at
    https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/viewport

    Only directives that are not ``None`` are emitted, so passing just the
    ones you care about keeps the output minimal.

    Can be used two ways:

    1. As a standalone head element::

        Head([Viewport(width="device-width", initial_scale=1.0, viewport_fit="cover")])

    2. As the ``viewport`` argument on :class:`Page`::

        Page(
            title="Hi",
            viewport=Viewport(width="device-width", initial_scale=1.0),
        )
    """

    key: str = "viewport"

    width: Optional[WidthValue]
    initial_scale: Optional[float]
    height: Optional[HeightValue]
    minimum_scale: Optional[float]
    maximum_scale: Optional[float]
    user_scalable: Optional[UserScalable]
    interactive_widget: Optional[InteractiveWidget]
    viewport_fit: Optional[ViewportFit]

    def __init__(
        self,
        width: Optional[WidthValue] = "device-width",
        initial_scale: Optional[float] = 1.0,
        *,
        height: Optional[HeightValue] = None,
        minimum_scale: Optional[float] = None,
        maximum_scale: Optional[float] = None,
        user_scalable: Optional[UserScalable] = None,
        interactive_widget: Optional[InteractiveWidget] = None,
        viewport_fit: Optional[ViewportFit] = None,
    ) -> None:
        self.width = width
        self.initial_scale = initial_scale
        self.height = height
        self.minimum_scale = minimum_scale
        self.maximum_scale = maximum_scale
        self.user_scalable = user_scalable
        self.interactive_widget = interactive_widget
        self.viewport_fit = viewport_fit
        self._validate()

    def _validate(self) -> None:
        if isinstance(self.width, int) and not 1 <= self.width <= 10000:
            raise ValueError(
                "width must be an integer between 1 and 10000, "
                "or the string 'device-width'"
            )
        if isinstance(self.height, int) and not 1 <= self.height <= 10000:
            raise ValueError(
                "height must be an integer between 1 and 10000, "
                "or the string 'device-height'"
            )
        for name, val in (
            ("initial_scale", self.initial_scale),
            ("minimum_scale", self.minimum_scale),
            ("maximum_scale", self.maximum_scale),
        ):
            if val is not None and not 0.0 <= float(val) <= 10.0:
                raise ValueError(f"{name} must be between 0.0 and 10.0")
        if (
            self.minimum_scale is not None
            and self.maximum_scale is not None
            and self.minimum_scale > self.maximum_scale
        ):
            raise ValueError("minimum_scale must be <= maximum_scale")

    def content_string(self) -> str:
        """The ``content="..."`` value, without the surrounding ``<meta>``."""
        parts: list[str] = []
        if self.width is not None:
            parts.append(f"width={self.width}")
        if self.height is not None:
            parts.append(f"height={self.height}")
        if self.initial_scale is not None:
            parts.append(f"initial-scale={_fmt_scale(self.initial_scale)}")
        if self.minimum_scale is not None:
            parts.append(f"minimum-scale={_fmt_scale(self.minimum_scale)}")
        if self.maximum_scale is not None:
            parts.append(f"maximum-scale={_fmt_scale(self.maximum_scale)}")
        if self.user_scalable is not None:
            parts.append(f"user-scalable={self.user_scalable}")
        if self.interactive_widget is not None:
            parts.append(f"interactive-widget={self.interactive_widget}")
        if self.viewport_fit is not None:
            parts.append(f"viewport-fit={self.viewport_fit}")
        return ", ".join(parts)

    def compile(self) -> str:
        return f'<meta name="viewport" content="{escape(self.content_string())}">'

    def __repr__(self) -> str:
        kwargs = []
        for name in (
            "width",
            "initial_scale",
            "height",
            "minimum_scale",
            "maximum_scale",
            "user_scalable",
            "interactive_widget",
            "viewport_fit",
        ):
            value = getattr(self, name)
            if value is not None:
                kwargs.append(f"{name}={value!r}")
        return f"Viewport({', '.join(kwargs)})"


def _fmt_scale(value: float) -> str:
    # "1" reads nicer than "1.0" and matches the conventional shape.
    if float(value).is_integer():
        return str(int(value))
    return str(value)
