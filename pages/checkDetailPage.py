from playwright.sync_api import Page, expect
from utility.operations import Operations

class CheckDetailPage:

    URL = 'https://play.grafana.org/a/grafana-synthetic-monitoring-app/checks/'

    def __init__(self, page: Page) -> None:
        self.page = page

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
    
        
class HttpDetailPage(CheckDetailPage):
    """
    Class for handling HTTP check detail page specific operations.
    """
    def __init__(self, page: Page) -> None:
        #super().__init__(page)
        self.page = page
        self.reachability = self.page.get_by_test_id("data-testid Panel header Reachability"). \
                                    get_by_test_id("data-testid panel content"). \
                                    locator("//span").nth(0). \
                                    inner_text()
        self.latency = self.page.get_by_test_id("data-testid Panel header Average latency"). \
                                    get_by_test_id("data-testid panel content"). \
                                    locator("//span").nth(0). \
                                    inner_text()
        
    def verify_data_consistency(self, result, reachability_threshold, latency_threshold) -> None:
        """
        Verify that the data displayed in the detail page matches the correspondent homePage result, within a threshold.
        Reachability unit is a percentage, while latency is in milliseconds.
        """
        reachability_detailPage = Operations.parse_metric_string(self.reachability)
        reachability_homePage = Operations.parse_metric_string(result.reachability)
        latency_detailsPage = Operations.parse_metric_string(self.latency)
        latency_homePage = Operations.parse_metric_string(result.latency)

        print("\n\nVerifying metrics consistency of check: ", result.job)
        print("\nReachability threshold: ", reachability_threshold, "%")
        print("Latency threshold: ", latency_threshold, "ms")
        print("Check's reachability in home page/detail page: ", reachability_homePage, "/", reachability_detailPage)
        print("Check's latency in home page/detail page: ", latency_homePage, "/", latency_detailsPage)

        assert abs(reachability_detailPage - reachability_homePage) <= reachability_threshold, "Reachability metrics are inconsistent."
        assert abs(latency_detailsPage - latency_homePage) <= latency_threshold, "Latency metrics are inconsistent."

        print("Metrics are consistent within the defined thresholds.")

class DnsDetailPage(CheckDetailPage):
    """
    Class for handling DNS check detail page specific operations.
    """
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.reachability = self.page.get_by_test_id("data-testid Panel header Reachability"). \
                                    get_by_test_id("data-testid panel content"). \
                                    locator("//span").nth(0). \
                                    inner_text()
        self.latency = self.page.get_by_test_id("data-testid Panel header Average latency"). \
                                    get_by_test_id("data-testid panel content"). \
                                    locator("//span").nth(0). \
                                    inner_text()
        
    def verify_data_consistency(self, result, reachability_threshold, latency_threshold) -> None:
        """
        Verify that the data displayed in the detail page matches the correspondent homePage result, within a threshold.
        Reachability unit is a percentage, while latency is in milliseconds.
        """
        reachability_detailPage = Operations.parse_metric_string(self.reachability)
        reachability_homePage = Operations.parse_metric_string(result.reachability)
        latency_detailsPage = Operations.parse_metric_string(self.latency)
        latency_homePage = Operations.parse_metric_string(result.latency)

        print("\n\nVerifying metrics consistency of check: ", result.job)
        print("\nReachability threshold: ", reachability_threshold, "%")
        print("Latency threshold: ", latency_threshold, "ms")
        print("Check's reachability in home page/detail page: ", reachability_homePage, "/", reachability_detailPage)
        print("Check's latency in home page/detail page: ", latency_homePage, "/", latency_detailsPage)

        assert abs(reachability_detailPage - reachability_homePage) <= reachability_threshold, "Reachability metrics are inconsistent."
        assert abs(latency_detailsPage - latency_homePage) <= latency_threshold, "Latency metrics are inconsistent."

        print("Metrics are consistent within the defined thresholds.")
        
class PingDetailPage(CheckDetailPage):
    """
    Class for handling Ping check detail page specific operations.
    """
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.reachability = self.page.get_by_test_id("data-testid Panel header Reachability"). \
                                    get_by_test_id("data-testid panel content"). \
                                    locator("//span").nth(0). \
                                    inner_text()
        self.latency = self.page.get_by_test_id("data-testid Panel header Average latency"). \
                                    get_by_test_id("data-testid panel content"). \
                                    locator("//span").nth(0). \
                                    inner_text()
        
    def verify_data_consistency(self, result, reachability_threshold, latency_threshold) -> None:
        """
        Verify that the data displayed in the detail page matches the correspondent homePage result, within a threshold.
        Reachability unit is a percentage, while latency is in milliseconds.
        """
        reachability_detailPage = Operations.parse_metric_string(self.reachability)
        reachability_homePage = Operations.parse_metric_string(result.reachability)
        latency_detailsPage = Operations.parse_metric_string(self.latency)
        latency_homePage = Operations.parse_metric_string(result.latency)

        print("\n\nVerifying metrics consistency of check: ", result.job)
        print("\nReachability threshold: ", reachability_threshold, "%")
        print("Latency threshold: ", latency_threshold, "ms")
        print("Check's reachability in home page/detail page: ", reachability_homePage, "/", reachability_detailPage)
        print("Check's latency in home page/detail page: ", latency_homePage, "/", latency_detailsPage)

        assert abs(reachability_detailPage - reachability_homePage) <= reachability_threshold, "Reachability metrics are inconsistent."
        assert abs(latency_detailsPage - latency_homePage) <= latency_threshold, "Latency metrics are inconsistent."

        print("Metrics are consistent within the defined thresholds.")
        
class ScriptedDetailPage(CheckDetailPage):
    """
    Class for handling MultiHTTP check detail page specific operations.
    """
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.reachability = self.page.get_by_test_id("data-testid Panel header Reachability"). \
                                    get_by_test_id("data-testid panel content"). \
                                    locator("//span").nth(0). \
                                    inner_text()
        
    def verify_data_consistency(self, result, reachability_threshold, latency_threshold) -> None:
        """
        Verify that the data displayed in the detail page matches the correspondent homePage result, within a threshold.
        Reachability unit is a percentage, while latency is in milliseconds.
        """
        reachability_detailPage = Operations.parse_metric_string(self.reachability)
        reachability_homePage = Operations.parse_metric_string(result.reachability)

        print("\n\nVerifying metrics consistency of check: ", result.job)
        print("\nReachability threshold: ", reachability_threshold, "%")
        print("Check's reachability in home page/detail page: ", reachability_homePage, "/", reachability_detailPage)

        assert abs(reachability_detailPage - reachability_homePage) <= reachability_threshold, "Reachability metrics are inconsistent."
        
        print("Metrics are consistent within the defined thresholds.")
        
class MultiHttpDetailPage(CheckDetailPage):
    """
    Class for handling MultiHTTP check detail page specific operations.
    """
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.reachability = self.page.get_by_test_id("data-testid Panel header Reachability"). \
                                    get_by_test_id("data-testid panel content"). \
                                    locator("//span").nth(0). \
                                    inner_text()
        
    def verify_data_consistency(self, result, reachability_threshold, latency_threshold) -> None:
        """
        Verify that the data displayed in the detail page matches the correspondent homePage result, within a threshold.
        Reachability unit is a percentage, while latency is in milliseconds.
        """
        reachability_detailPage = Operations.parse_metric_string(self.reachability)
        reachability_homePage = Operations.parse_metric_string(result.reachability)

        print("\n\nVerifying metrics consistency of check: ", result.job)
        print("\nReachability threshold: ", reachability_threshold, "%")
        print("Check's reachability in home page/detail page: ", reachability_homePage, "/", reachability_detailPage)

        assert abs(reachability_detailPage - reachability_homePage) <= reachability_threshold, "Reachability metrics are inconsistent."

        print("Metrics are consistent within the defined thresholds.")
        
class TracerouteDetailPage(CheckDetailPage):
    """
    Class for handling Traceroute check detail page specific operations.
    """
    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def verify_data_consistency(self, result, reachability_threshold, latency_threshold) -> None:
        """
        Verify that the data displayed in the detail page matches the correspondent homePage result, within a threshold.
        Reachability unit is a percentage, while latency is in milliseconds.
        """