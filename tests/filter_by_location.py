from playwright.sync_api import Page
from pages.homePage import HomePage

TEST_DATA = ["London", "Seoul", "NorthVirginia"]

def test_location_filter(page):
    # Given the Grafana home page is displayed
    homePage = HomePage(page)
    homePage.load()
    # When the user filters results by specific probes
    homePage.filter_probes(TEST_DATA)
    # Then the page only displays data matching those probes
    homePage.verify_results_location_consistency()


