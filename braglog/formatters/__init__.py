from .basic import BasicFormatter
from .foldable_html import FodableHTMLFormatter
from .html import HTMLFormatter
from .json import JSONFormatter
from .markdown import MarkdownFormatter

__all__ = [
    "BasicFormatter",
    "HTMLFormatter",
    "JSONFormatter",
    "FodableHTMLFormatter",
    "MarkdownFormatter",
]


FORMATTER_MAP = {
    "basic": BasicFormatter,
    "html": HTMLFormatter,
    "json": JSONFormatter,
    "fhtml": FodableHTMLFormatter,
    "md": MarkdownFormatter,
}
