
# Test Strategy

On each test presented, I first start with a deep manual check on the application frontend. The aim is understanding, as a user, what are the functionalities and the information at my disposal.

Then, I write a brief example on how I can perform the test in the Given-When-Then format, to help me visualize the steps to reproduce manually and later in automation

1. Filtering Checks by Location:
- Steps to apply a location filter.
- Expected outcome: Only checks from the selected location are displayed.

```bash
    Given the Grafana home page is displayed
    When the user filters results by specific probes
    Then the page only displays data matching those probes
```
In this scenario I decided to use probes as location reference, as it's more accurate and always displayed in the detail page of each check.

The manual steps become
- Click on the probe filter
- Select a subset of locations
- For each result:
    - Navigate to its detail page clicking on the link
    - Check in the detail page if there is any information relative to at least one of the selected probes

2. Viewing Check Details:
- Steps to access detailed information of a specific check.
- Expected outcome: Correct details are displayed corresponding to the selected check.

```bash
    Given the Grafana home page is displayed
    When I click on a specific check
    And the check detail page is shown
    Then the informations displayed are correct
```
This scenario can be developed in different ways depending on what the "Displayed correct details" means. In a real situation, it could be discussed with the product team to assure the expectations of the user are met.

My personal interpretation was: having on the home page some brief information on the checks, let's assure that the data displayed are coherent with what is displayed in the detail page of each check.

I also noticed that the platform displays dynamic data, that is continuously updated. Therefore sometimes data relative to a check can differ slightly between the home page and the detail page. I then decided to set up some thresholds to evaluate if the test is to be considered passed or failed. In a real situation the threshold can be set based on business reasons.

Manual steps:
- Choose a random check
- Save the values of the shown metrics (reachability and latency)
- Open the check details clicking on the link
- Check that the metrics displays a value within the defined threshold

3. Handling No Data Scenario:
- Steps to apply a filter that results in no matching checks.
- Expected outcome: Appropriate message indicating no data is displayed.

```bash
    Given the Grafana home page is displayed
    When I filter on a region
    And I filter on a probe not matching the reagion previously selected
    Then no results should be displayed
```
The scenario is straightforward as we have a clear constraint to verify the test case. It is sufficient to define combinations of region/probes that don't match, and thus producing no results

Manual steps:
- Click on the region filter
- Select a specific value
- Click on the probe filter
- Select one or more values not matching the region
- Check that the "No data" text is displayed in the home page



