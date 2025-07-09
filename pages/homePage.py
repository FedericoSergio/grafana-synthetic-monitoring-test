from playwright.sync_api import Page, expect
from region import Region

class HomePage:

    URL = 'https://play.grafana.org/a/grafana-synthetic-monitoring-app/home'

    def __init__(self, page: Page) -> None:
        self.page = page
        self.region_filter_dropdown = page.get_by_test_id("data-testid template variable").nth(0)
        self.probe_filter_dropdown = page.get_by_test_id("data-testid template variable").nth(1)
        self.refresh_button = page.get_by_test_id("data-testid RefreshPicker run button")

        self.results = page.locator(".css-z0f43i-row")
    
    def load(self) -> None:
        self.page.goto(self.URL)
    
    def filter_region(self, region_code: str) -> None:
        self.region_filter_dropdown.click()
        self.page.get_by_text(region_code).click()
        self.refresh_button.click()

    def filter_probes(self, probe_names: list[str]) -> None:
        self.probe_filter_dropdown.click()
        for probe in probe_names:        
            self.page.get_by_text(probe).click()
        # self.page.get_by_text("probe").click()
        # self.page.locator("css=css-1d3xu67-Icon").click()
        self.page.keyboard.press("Escape")
        self.refresh_button.click()

    def check_results_location() -> None:
        # controllare che selected_region combaci con i risultati
        expect(true)

    def verify_no_results(self) -> None:
        no_data_text = self.page.get_by_text("No data")
        for no_data in no_data_text.all():
            expect(no_data).to_be_visible()
    