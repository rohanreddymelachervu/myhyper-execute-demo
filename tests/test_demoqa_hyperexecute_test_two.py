# HyperTestPyUnit: DemoQA HyperExecute Test Two
import os
import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
    # Parse command-line options (e.g., --OS and --browser)
    parser = argparse.ArgumentParser()
    parser.add_argument("--OS", type=str, required=True, help="Operating system for the test (e.g., 'win 10' or 'linux')")
    parser.add_argument("--browser", type=str, required=True, help="Browser to run tests on (e.g., 'chrome' or 'firefox')")
    args = parser.parse_args()

    # Retrieve values from arguments
    browser = args.browser.lower()
    platform_name = args.OS  # Use the OS value passed from the command line

    # Choose the correct Selenium Options based on the browser
    if browser == "firefox":
        from selenium.webdriver.firefox.options import Options as FirefoxOptions
        options = FirefoxOptions()
    else:
        from selenium.webdriver.chrome.options import Options as ChromeOptions
        options = ChromeOptions()

    # Set Selenium capabilities using the command-line parameters
    options.set_capability("browserName", browser.capitalize())
    options.set_capability("browser_version", "latest")
    options.set_capability("platform_name", platform_name)

    # Set LambdaTest-specific options
    lt_options = {
        "username": os.getenv("LT_USERNAME"),
        "accessKey": os.getenv("LT_ACCESS_KEY"),
        "network": True,
        "build": "HyperExecute DemoQA Test Build",
        "smartUI.project": "HyperExecute DemoQA Testing",
        "name": f"HyperExecute DemoQA Test Two - {browser.capitalize()} on {platform_name}",
        "w3c": True,
        "plugin": "python-python"
    }
    options.set_capability("LT:Options", lt_options)

    # Connect to the LambdaTest hub using credentials from environment variables
    hub_url = f"http://{os.getenv('LT_USERNAME')}:{os.getenv('LT_ACCESS_KEY')}@hub.lambdatest.com/wd/hub"
    driver = webdriver.Remote(command_executor=hub_url, options=options)

    try:
        # Navigate to LambdaTest homepage as a sample test
        driver.implicitly_wait(10)
        driver.set_page_load_timeout(60)
        driver.get("https://www.lambdatest.com/")

        # Wait for a header element (assume the homepage has an <h1> header)
        header = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        )
        assert header.is_displayed(), "Header is not displayed on LambdaTest homepage."

        # Capture and print the page title
        title = driver.title
        print("LambdaTest homepage title is:", title)

        # Generate an artifact file containing the test output
        artifact_dir = "example_report"
        if not os.path.exists(artifact_dir):
            os.makedirs(artifact_dir)
        artifact_path = os.path.join(artifact_dir, "artifact_test_two.txt")
        with open(artifact_path, "w") as f:
            f.write("This is an automatically generated artifact from Test Two.\n")
            f.write("Page Title: " + title + "\n")

        # Mark the test as passed on LambdaTest
        driver.execute_script("lambda-status=passed")
    finally:
        driver.quit()

if __name__ == '__main__':
    main()
