from .basic import BasicFormatter
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
}
