import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from Pages.AssignmentPage import TestAssignmentPage
from SeleniumHelpers.helpers import Helpers
from seleniumValidations.Assignment_validations import AssignmentMethods


class BetaTest:
    # adding chrome options to block the alerts from browser
    chr_options = Options()
    chr_options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.media_stream_mic": 2})  # 1: Allow, 2: Block

    # initializing the Chrome browser
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chr_options)

    # initializing the assignment page, assignment methods class
    assignment_page = TestAssignmentPage(driver)
    assignment_methods = AssignmentMethods(driver, assignment_page)

    # navigating to the application and adding implicit wait
    assignment_page.navigate_to_URL(
        "https://apps.inindca.com/wem-learning-ui/#/assignments/a66c044d-0d52-4a43-9ec3-5af39f4986e3")
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

    # validating the progress bar functionality in the beta feature
    assignment_methods.validate_beta_feature_of_test_assignment_page()
