from playwright.sync_api import Page
from pages.homePage import HomePage
import pytest

TEST_LOCATIONS = [
    ["SaoPaulo"],
    ["Hyderabad", "Paris"],
    ["London", "Seoul", "NorthVirginia"],
    ["Singapore", "Seoul", "NorthVirginia", "Frankfurt"],
    ["Tokyo", "Singapore", "CapeTown", "Frankfurt", "Seoul"]
]

@pytest.mark.parametrize('locations', TEST_LOCATIONS)
def test_location_filter(page, locations: list[str]):
    # Given the Grafana home page is displayed
    homePage = HomePage(page)
    homePage.load()
    # When the user filters results by specific probes
    homePage.filter_probes(locations)
    # Then the page only displays data matching those probes
    homePage.verify_results_location_consistency()


