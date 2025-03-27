from .basic import BasicFormatter
from .html import HTMLFormatter

__all__ = [
    "BasicFormatter",
    "HTMLFormatter",
]


FORMATTER_MAP = {
    "basic": BasicFormatter,
    "html": HTMLFormatter,
}
