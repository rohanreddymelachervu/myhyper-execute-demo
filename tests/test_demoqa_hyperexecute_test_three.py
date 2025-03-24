# HyperTestPyUnit: DemoQA HyperExecute Test Three
import os
import pytest
import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException

# Fixture to initialize the WebDriver session with command-line options
@pytest.fixture(scope="session")
def driver(request):
    # Set up command-line arguments with default values for convenience
    parser = argparse.ArgumentParser()
    parser.add_argument("--OS", type=str, default="win10", help="Operating system for the test")
    parser.add_argument("--browser", type=str, default="chrome", help="Browser to run tests on")
    # Parse known args; ignore pytest-related ones
    args, _ = parser.parse_known_args()

    browser = args.browser.lower()
    platform_name = args.OS

    # Select the correct options based on the browser choice
    if browser == "firefox":
        from selenium.webdriver.firefox.options import Options as FirefoxOptions
        options = FirefoxOptions()
    else:
        from selenium.webdriver.chrome.options import Options as ChromeOptions
        options = ChromeOptions()

    # Set standard capabilities
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
        "name": f"HyperExecute DemoQA Check Box Test - {browser.capitalize()} on {platform_name}",
        "w3c": True,
        "plugin": "python-python"
    }
    options.set_capability("LT:Options", lt_options)

    # Connect to LambdaTest hub using environment credentials
    hub_url = f"http://{os.getenv('LT_USERNAME')}:{os.getenv('LT_ACCESS_KEY')}@hub.lambdatest.com/wd/hub"
    driver = webdriver.Remote(command_executor=hub_url, options=options)
    yield driver
    driver.quit()

# Third test case: Check Box test on DemoQA
def test_demoqa_check_box(driver):
    # Set timeouts
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(60)
    
    # Step 1: Navigate to DemoQA homepage
    driver.get("https://demoqa.com/")
    
    # Step 2: Click on the "Elements" card
    elements_card = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//h5[text()='Elements']"))
    )
    elements_card.click()
    
    # Step 3: Click on "Check Box" in the sidebar
    check_box_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Check Box']"))
    )
    check_box_option.click()
    
    # Step 4: Expand all nodes
    expand_all_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[title='Expand all']"))
    )
    expand_all_button.click()
    
    # Step 5: Select the "Downloads" checkbox
    downloads_checkbox = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@class='rct-title' and text()='Downloads']"))
    )
    # Scroll the element into view to help avoid overlay issues
    driver.execute_script("arguments[0].scrollIntoView(true);", downloads_checkbox)
    try:
        downloads_checkbox.click()
    except ElementClickInterceptedException:
        # Fallback to JavaScript click if normal click is intercepted
        driver.execute_script("arguments[0].click();", downloads_checkbox)
    
    # Step 6: Validate that the output contains "downloads"
    output_result = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "result"))
    )
    assert "downloads" in output_result.text.lower(), "Downloads not found in output."
    print("Check Box Output:", output_result.text)
    
    # Optionally, generate an artifact file containing the test output
    artifact_dir = "example_report"
    if not os.path.exists(artifact_dir):
        os.makedirs(artifact_dir)
    artifact_path = os.path.join(artifact_dir, "artifact_test_three.txt")
    with open(artifact_path, "w") as f:
        f.write("This is an automatically generated artifact from Test Three (Check Box Test).\n")
        f.write("Output:\n" + output_result.text)
    
    # Mark the test as passed on LambdaTest
    driver.execute_script("lambda-status=passed")

# Main block to allow running the test with python3 filename.py
if __name__ == '__main__':
    import sys
    sys.exit(pytest.main(["-v", __file__]))
