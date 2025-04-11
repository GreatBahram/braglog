from .basic import BasicFormatter
from .foldable_html import FodableHTMLFormatter
from .html import HTMLFormatter
from .json import JSONFormatter

__all__ = [
    "BasicFormatter",
    "HTMLFormatter",
]


FORMATTER_MAP = {
    "basic": BasicFormatter,
    "html": HTMLFormatter,
    "json": JSONFormatter,
    "fhtml": FodableHTMLFormatter,
}
