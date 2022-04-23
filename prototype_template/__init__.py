"""Template project."""

from importlib_metadata import version as metadata_version, PackageNotFoundError

from .template_module import TemplateClass


try:
    __version__ = metadata_version("prototype_template")
except PackageNotFoundError:  # pragma: no cover
    # package is not installed
    pass
