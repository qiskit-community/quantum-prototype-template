"""Template project."""

from .template_module import TemplateClass


def __get_version():
    import os
    with open(
        os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "VERSION.txt",
        ),
        "r",
    ) as f:
        return f.read().strip()

__version__ = __get_version()
