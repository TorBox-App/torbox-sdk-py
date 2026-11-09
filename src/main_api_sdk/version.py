from importlib import metadata

try:
    __version__ = metadata.version("main_api_sdk")
except metadata.PackageNotFoundError:
    # Not installed as a distribution: a source checkout, or a vendored copy. Reading the version
    # off the package metadata is what makes a patched or forked install report its real version,
    # so the generated one is only the fallback.
    __version__ = "1.0.1"
