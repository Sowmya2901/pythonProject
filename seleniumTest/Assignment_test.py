import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from SeleniumHelpers.helpers import Helpers
from Pages.AssignmentPage import TestAssignmentPage
from seleniumValidations.Assignment_validations import AssignmentMethods


class AssignmentTest:
    # adding chrome options to block the alerts from browser
    chr_options = Options()
    chr_options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.media_stream_mic":  2})  # 1: Allow, 2: Block

    # initializing the Chrome browser
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chr_options)

    assignment_page = TestAssignmentPage(driver)
    assignment_methods = AssignmentMethods(driver, assignment_page)

    # navigating to the application
    assignment_page.navigate_to_URL(
        "https://apps.inindca.com/wem-learning-ui/#/assignments/5bba88c6-1377-441e-b7c5-1a927c139e1e")
    driver.implicitly_wait(3)

    # maximizing the widow
    driver.maximize_window()

    # waiting until the page loads
    helper_wait = Helpers(driver)
    helper_wait.wait_for_element((By.TAG_NAME, "body"))
    time.sleep(5)

    # entering login credentials
    assignment_page.login_page()
    time.sleep(15)

    # click on start module of the test assignment
    driver.find_element(*assignment_page.start_module_button).click()
    time.sleep(5)

    # able to see the content tab of the assignment page
    driver.find_element(*assignment_page.content_tab)

    # validating the progress bar functionality in the assignment feature
    assignment_methods.validate_test_assignment_page()

