"""
sunraster
=========

Does stuff.
"""
import os
import sys
import logging

from .raster import Raster, RasterSequence

try:
    from .version import __version__
except ImportError:
    __version__ = "unknown"

# Enforce Python version check during package import.
__minimum_python_version__ = "3.7"

__all__ = ['Raster', 'RasterSequence']


class UnsupportedPythonError(Exception):
    pass


if sys.version_info < tuple(int(val) for val in __minimum_python_version__.split('.')):
    # This has to be .format to keep backwards compatibly.
    raise UnsupportedPythonError(
        f"sunraster does not support Python < {__minimum_python_version__}")
