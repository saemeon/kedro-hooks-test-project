import kedro_hooks_test


def test_import():
    assert kedro_hooks_test.__version__ != "unknown"
