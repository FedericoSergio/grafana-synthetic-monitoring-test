from playwright.sync_api import Page
from pages.homePage import HomePage

def test_no_data_scenario(page):
    # Given the Grafana home page is displayed
    homePage = HomePage(page)
    homePage.load()
    # When I filter on a region
    homePage.filter_region("EMEA")
    # And I filter on a probe not matching the reagion previously selected
    homePage.filter_probes(["NorthVirginia", "Seoul"])
    # Then no results should be displayed
    homePage.verify_no_results()