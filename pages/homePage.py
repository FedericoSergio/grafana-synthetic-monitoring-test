from playwright.sync_api import Page, Locator, expect
from pages.checkDetailPage import CheckDetailPage
import random

class Result:

    def __init__(self, locator: Locator) -> None:
        self.instance = locator.get_by_role("cell").nth(0).inner_text()
        self.job = locator.get_by_role("cell").nth(1).inner_text()
        self.checkType = locator.get_by_role("cell").nth(2).inner_text()
        self.state = locator.get_by_role("cell").nth(3).inner_text()
        self.reachability = locator.get_by_role("cell").nth(4).inner_text()
        self.latency = locator.get_by_role("cell").nth(5).inner_text()
        # The link to navigate to the check detail page
        self.detail_link = locator.get_by_role("cell").nth(0).get_by_role("link")

    def inspect_check(self) -> None:
        """Click on the check link to navigate to the detail page."""
        self.detail_link.click()

class HomePage:

    URL = 'https://play.grafana.org/a/grafana-synthetic-monitoring-app/home'

    def __init__(self, page: Page) -> None:
        self.page = page
        self.region_filter_dropdown = page.get_by_test_id("data-testid template variable").nth(0)
        self.probe_filter_dropdown = page.get_by_test_id("data-testid template variable").nth(1)
        self.selected_probes = page.locator("//div[contains(@class, 'css-1o4wo1x')]")
        self.refresh_button = page.get_by_test_id("data-testid RefreshPicker run button")

        # This locator identifies all the rows in "All checks" section
        # self.results_locator = page.get_by_test_id("data-testid table body").get_by_role("row")
        # self.results = [Result(result) for result in self.results_locator.all()]

    
    def load(self) -> None:
        """Load the Grafana home page."""
        self.page.goto(self.URL)
        expect(self.page.get_by_test_id("data-testid table body").get_by_role("row").nth(0)).to_be_visible()
    
    def filter_region(self, region_code: str) -> None:
        """Set a specific value in region dropdown."""
        self.region_filter_dropdown.click()
        self.page.get_by_text(region_code).click()
        self.refresh_button.click()

    def filter_probes(self, probe_names: list[str]) -> None:
        """Set a specific value in probes dropdown."""
        self.probe_filter_dropdown.click()
        for probe in probe_names:        
            self.page.get_by_text(probe).click()
        self.page.keyboard.press("Escape")
        self.refresh_button.click()

    def verify_results_location_consistency(self) -> None:
        """Verify that the results displayed match the filtered probes."""
        probes = self.selected_probes.all_inner_texts()
        self.results_locator = self.page.get_by_test_id("data-testid table body").get_by_role("row")
        self.results = [Result(result) for result in self.results_locator.all()]
        for result in self.results:
            result.inspect_check()
            detailPage = CheckDetailPage(self.page)
            detailPage.verify_page(result.job)
            assert detailPage.verify_probes(probes) == True
            self.page.go_back()

    # def verify_results_data_consistency(self, results: list[Result]) -> None:
    #     """Verify that the results parametes in home page match the detail page."""
    #     self.results_locator = self.page.get_by_test_id("data-testid table body").get_by_role("row")
    #     self.results = [Result(result) for result in self.results_locator.all()]
    #     for result in results:
    #         detailPage = CheckDetailPage(self.page)
    #         expect(result.reachability).to_have_text(detailPage.reachability.inner_text()) 

    def verify_no_results(self) -> None:
        """Verify that the page displays 'No data' when no results are available."""
        no_data_text = self.page.get_by_text("No data")
        for no_data in no_data_text.all():
            expect(no_data).to_be_visible()
        print("\nNo data is displayed as expected.")

    def click_on_random_check(self) -> Result:
        """Click on the first check in the results."""
        self.results_locator = self.page.get_by_test_id("data-testid table body").get_by_role("row")
        self.results = [Result(result) for result in self.results_locator.all()]
        if self.results:
            selected_result = random.choice(self.results)
            selected_result.inspect_check()
            return selected_result
        else:
            raise Exception("No results available to click on.")
