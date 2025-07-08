from playwright.sync_api import Page
from region import Region

class HomePage:

    URL = 'https://play.grafana.org/a/grafana-synthetic-monitoring-app/home'

    def __init__(self, page: Page) -> None:
        self.page = page
        self.region_filter_dropdown = page.locator('#f6d1c462-62b0-447f-af15-9ee2f018c8e3')
        self.selected_region = page.locator(".css-8nwx1l-singleValue.css-0")
        self.probe_filter_dropdown = page.locator('#e41417e3-e555-4685-a9d1-0dba9c38c169')
    
    def load(self) -> None:
        self.page.goto(self.URL)
    
    def filter_region(self, region_code: Region) -> None:
        self.region_filter_dropdown.click()
        self.page.get_by_label(region_code).click()

    def check_results_location() -> None:
        # controllare che selected_region combaci con i risultati
        assert(true)