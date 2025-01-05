"""Tests over the full package."""


def test_version_is_exported_from_package() -> None:
    """Tests that a valid version is exported from the package."""
    from sacra import __version__, __version_tuple__

    assert __version__ != "0.0.0"
    assert __version_tuple__ > (1, 0, 0)
