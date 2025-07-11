
# Playwright Testing - Grafana Synthetic Monitoring

The aim of this project is providing a brief overview of Playwright capabilities on a multi-functional platform.




## Setup

Clone the repository in your local machine and open the terminal on the project main directory.

To run the tests all together:

```bash
  python -m pytest tests --slowmo 1000
```

To run the tests in parallel:

```bash
  python -m pytest tests -n 3 --slowmo 1000
```

To check any single test in headed mode:

```bash
  python -m pytest .\tests\test_filter_by_location.py --headed --slowmo 1000
  python -m pytest .\tests\test_check_details.py --headed --slowmo 1000
  python -m pytest .\tests\test_no_data.py --headed --slowmo 1000
```


## Support

For support, email federico.sergio17@gmail.com.


    
