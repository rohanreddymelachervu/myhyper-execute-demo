# # HyperTestPyUnit: DemoQA HyperExecute Test
# import os
# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options as ChromeOptions
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# # Fetch LambdaTest credentials from environment variables
# LT_USERNAME = os.getenv("LT_USERNAME")
# LT_ACCESS_KEY = os.getenv("LT_ACCESS_KEY")

# @pytest.fixture(scope="session")
# def driver():
#     # Set up Chrome capabilities
#     options = ChromeOptions()
#     options.browser_version = "latest"
#     options.platform_name = "Windows 10"

#     # HyperExecute / SmartUI options
#     lt_options = {
#         "username": LT_USERNAME,
#         "accessKey": LT_ACCESS_KEY,
#         "network": True,
#         "build": "HyperExecute DemoQA Test Build",
#         "smartUI.project": "HyperExecute DemoQA Testing",
#         "name": "HyperExecute DemoQA Text Box Test - Pytest",
#         "w3c": True,
#         "plugin": "python-python"
#     }
#     options.set_capability("LT:Options", lt_options)

#     # Use the HyperExecute (SmartUI) hub URL
#     hub_url = f"http://{LT_USERNAME}:{LT_ACCESS_KEY}@hub.lambdatest.com/wd/hub"

#     # Create the Remote WebDriver session
#     driver = webdriver.Remote(
#         command_executor=hub_url,
#         options=options,
#     )
#     driver.maximize_window()

#     yield driver
#     # Teardown
#     driver.quit()

# def test_demoqa_text_box(driver):
#     driver.implicitly_wait(10)
#     driver.set_page_load_timeout(30)

#     # Step 1: Navigate to DemoQA
#     driver.get("https://demoqa.com/")

#     # Step 2: Click on the "Elements" card
#     elements_card = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, "//h5[text()='Elements']"))
#     )
#     elements_card.click()

#     # Step 3: Click on "Text Box" in the sidebar
#     text_box_option = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, "//span[text()='Text Box']"))
#     )
#     text_box_option.click()

#     # Step 4: Fill out the form
#     full_name_field = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "userName"))
#     )
#     email_field = driver.find_element(By.ID, "userEmail")
#     current_address_field = driver.find_element(By.ID, "currentAddress")
#     permanent_address_field = driver.find_element(By.ID, "permanentAddress")
#     submit_button = driver.find_element(By.ID, "submit")

#     full_name_field.send_keys("John Doe")
#     email_field.send_keys("john.doe@example.com")
#     current_address_field.send_keys("123 Main St, City, Country")
#     permanent_address_field.send_keys("456 Secondary St, City, Country")

#     # Scroll and submit
#     driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
#     submit_button.click()

#     # Step 5: Validate the output
#     output_section = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "output"))
#     )
#     assert output_section.is_displayed(), "Output section not displayed."

#     output_text = output_section.text
#     print("Output text:", output_text)

#     # Mark the test as passed on LambdaTest
#     driver.execute_script("lambda-status=passed")
# if __name__ == '__main__':
#     import sys
#     sys.exit(pytest.main(["-v", __file__]))

# HyperTestPyUnit: DemoQA HyperExecute Test
import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Fetch LambdaTest credentials from environment variables
LT_USERNAME = os.getenv("LT_USERNAME")
LT_ACCESS_KEY = os.getenv("LT_ACCESS_KEY")

@pytest.fixture(scope="session")
def driver():
    # Set up Chrome capabilities
    options = ChromeOptions()
    options.browser_version = "latest"
    options.platform_name = "Windows 10"

    # HyperExecute / SmartUI options
    lt_options = {
        "username": LT_USERNAME,
        "accessKey": LT_ACCESS_KEY,
        "network": True,
        "build": "HyperExecute DemoQA Test Build",
        "smartUI.project": "HyperExecute DemoQA Testing",
        "name": "HyperExecute DemoQA Text Box Test - Pytest",
        "w3c": True,
        "plugin": "python-python"
    }
    options.set_capability("LT:Options", lt_options)

    # Use the standard LambdaTest hub URL (change to beta-smartui-hub.lambdatest.com if needed)
    hub_url = f"http://{LT_USERNAME}:{LT_ACCESS_KEY}@hub.lambdatest.com/wd/hub"

    # Create the Remote WebDriver session
    driver = webdriver.Remote(
        command_executor=hub_url,
        options=options,
    )
    driver.maximize_window()

    yield driver
    # Teardown
    driver.quit()

def test_demoqa_text_box(driver):
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(30)

    # Step 1: Navigate to DemoQA
    driver.get("https://demoqa.com/")

    # Step 2: Click on the "Elements" card
    elements_card = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//h5[text()='Elements']"))
    )
    elements_card.click()

    # Step 3: Click on "Text Box" in the sidebar
    text_box_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Text Box']"))
    )
    text_box_option.click()

    # Step 4: Fill out the form
    full_name_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "userName"))
    )
    email_field = driver.find_element(By.ID, "userEmail")
    current_address_field = driver.find_element(By.ID, "currentAddress")
    permanent_address_field = driver.find_element(By.ID, "permanentAddress")
    submit_button = driver.find_element(By.ID, "submit")

    full_name_field.send_keys("John Doe")
    email_field.send_keys("john.doe@example.com")
    current_address_field.send_keys("123 Main St, City, Country")
    permanent_address_field.send_keys("456 Secondary St, City, Country")

    # Scroll and submit the form
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    submit_button.click()

    # Step 5: Validate the output
    output_section = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "output"))
    )
    assert output_section.is_displayed(), "Output section not displayed."

    output_text = output_section.text
    print("Output text:", output_text)

    # Generate a simple artifact file containing the test output
    artifact_dir = "example_report"
    if not os.path.exists(artifact_dir):
        os.makedirs(artifact_dir)
    artifact_path = os.path.join(artifact_dir, "artifact.txt")
    with open(artifact_path, "w") as f:
        f.write("This is an automatically generated artifact file.\n")
        f.write("Test Output:\n")
        f.write(output_text)

    # Mark the test as passed on LambdaTest
    driver.execute_script("lambda-status=passed")

if __name__ == '__main__':
    import sys
    sys.exit(pytest.main(["-v", __file__]))

