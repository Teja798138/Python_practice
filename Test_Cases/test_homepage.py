import pytest

@pytest.mark.sanity
def test_homepage_title(setup_browser):
    driver = setup_browser
    assert "Cleartrip" in driver.title
