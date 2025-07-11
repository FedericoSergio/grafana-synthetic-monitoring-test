from playwright.sync_api import Page
from pages.homePage import HomePage
from pages.checkDetailPage import CheckDetailPage, HttpDetailPage, PingDetailPage, DnsDetailPage, ScriptedDetailPage, MultiHttpDetailPage, TracerouteDetailPage
import pytest

TEST_CASES = [
    [2.0, 5.0],
    [1.0, 10.0],
    [0.0, 20.0],
    [5.0, 30.0]
]

@pytest.mark.parametrize('thresholds', TEST_CASES)
def test_data_consistency(page, thresholds: list[float]):
    # Given the Grafana home page is displayed
    homePage = HomePage(page)
    homePage.load()
    # When I click on a specific check
    check = homePage.click_on_random_check()
    # And the check detail page is shown
    match(check.checkType):
        case "http":
            detailPage = HttpDetailPage(page)
        case "dns":
            detailPage = DnsDetailPage(page)
        case "ping":
            detailPage = PingDetailPage(page)
        case "scripted":
            detailPage = ScriptedDetailPage(page)
        case "multihttp":
            detailPage = MultiHttpDetailPage(page)
        case "traceroute":
            detailPage = TracerouteDetailPage(page)
        case _:
            raise ValueError(f"Unknown check type: {check.checkType}")
    detailPage.verify_page(check.job)
    # Then the informations displayed are correct
    detailPage.verify_data_consistency(check, reachability_threshold=thresholds[0], latency_threshold=thresholds[1])