from playwright.sync_api import Page

def test_no_data_scenario(page):
    # Given the Grafana home page is displayed
    page.goto('https://play.grafana.org/a/grafana-synthetic-monitoring-app/home', wait_until='networkidle')