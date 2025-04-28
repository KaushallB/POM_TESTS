# Selenium POM Test Automation

This repository contains test scripts written using Selenium and the Page Object Model (POM) for automating the testing of a stock market web application. The tests utilize Python, Selenium WebDriver, and the `selenium-page-factory` library for a structured and scalable approach to web automation.

## Prerequisites

To run the tests in this repository, you'll need to have Python installed on your system. If you don’t have Python installed, you can download it from [here](https://www.python.org/downloads/).

## Installation Steps

Follow the steps below to set up the environment and install the necessary dependencies:

1. **Clone the repository**:
    ```bash
    git clone <your-repo-url>
    cd <your-repo-directory>
    ```

2. **Install the required Python packages**:
    Run the following command to install all the dependencies listed in this repository:
    ```bash
    pip install selenium pytest selenium-page-factory
    ```

## Running the Tests

After installing the dependencies, you can run the tests using the following command:

```bash
pytest tests/test_buy_stocks.py -s
