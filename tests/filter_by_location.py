from playwright.sync_api import Page
from ..pages.homePage import HomePage
from region import Region

def test_location_filter(page):
    # Given the Grafana home page is displayed
    homePage = HomePage(page)
    homePage.load()

    # When the user filters by a specific region
    homePage.filter_region(Region.AMER)
    # Then the page should display data for that region


