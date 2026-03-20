# Copyright (c) Simon Niederberger.
# Distributed under the terms of the MIT License.


from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("kedro-hooks-test")
except PackageNotFoundError:
    __version__ = "unknown"
