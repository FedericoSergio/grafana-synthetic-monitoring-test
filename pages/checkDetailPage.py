from playwright.sync_api import Page, expect

class CheckDetailPage:

    URL = 'https://play.grafana.org/a/grafana-synthetic-monitoring-app/checks/'

    def __init__(self, page: Page) -> None:
        self.page = page
        self.reachability = page.get_by_test_id("data-testid Panel header Reachability").get_by_test_id("data-testid panel content").locator("//span")

    def verify_page(self, check_name: str) -> None:
        """Verify that the check detail page is displayed for the given check name."""
        assert self.page.url.startswith(self.URL)
        expect(self.page.locator("h1")).to_have_text(check_name)

    def verify_probes(self, probes: list[str]) -> bool:
        """Verify that the detail page matches at least one of filtered probes."""
        for probe in probes:
            if self.page.get_by_text(probe).nth(0).is_visible():
                return True
        return False
    
    def verify_data_consistency(self, result) -> None:
        """Verify that the data displayed in the detail page matches the correspondent homePage result."""
        expect(self.reachability).to_have_text(result.reachability)