import random
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from SeleniumHelpers.helpers import Helpers
from seleniumTest.AssignmentPage import TestAssignmentPage
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

chr_options = Options()

# adding chrome options to block the aslerts from browser
chr_options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 2  # 1: Allow, 2: Block
})

# initializing the Chrome browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chr_options)

assignment_page = TestAssignmentPage(driver)

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


def validate_rich_text():
    # click on the content title
    driver.find_element(*assignment_page.content_title).click()
    scrollable_content = driver.find_element(By.XPATH, "//div[@class='InvisibleElement']")
    delta_y = scrollable_content.rect['y']
    scroll_origin = ScrollOrigin.from_element(scrollable_content)
    ActionChains(driver).scroll_from_origin(scroll_origin, 0, int(delta_y)).perform()
    time.sleep(3)
    flag = assignment_page.validate_progress_perc()
    driver.find_element(*assignment_page.next_button).click()
    print(flag)
    return flag


def validate_the_url():
    time.sleep(3)
    # click on the launch content link in the url section and will be navigated to another tab
    driver.find_element(*assignment_page.new_window_launch_link).click()
    # switch to the parent frame
    driver.switch_to.window(driver.window_handles[0])
    # click on next
    driver.find_element(*assignment_page.next_button).click()
    time.sleep(3)
    flag = assignment_page.validate_progress_perc()
    print(flag)
    return flag


def validate_group1_ques():
    # switch to the assessment frame
    driver.switch_to.frame('assessment-builder')
    # select the answers for the group 1 questions
    assignment_page.select_option_for_questions()
    # switch back to default frame
    driver.switch_to.default_content()
    # click on next
    driver.find_element(By.XPATH, "//h2[text()=' 2. Group 2 ']").click()
    time.sleep(2)
    flag = assignment_page.validate_progress_perc()
    print(flag)
    return flag


def validate_group2_ques():
    # switch to the assessment frame
    driver.switch_to.frame('assessment-builder')
    random_choice = random.choice(assignment_page.G2_Q1_options)
    driver.find_element(By.XPATH, random_choice).click()
    driver.switch_to.default_content()
    time.sleep(2)
    flag = assignment_page.validate_progress_perc()
    print(flag)
    return flag


if assignment_page.progress_percentage_val() == 0:
    if validate_rich_text():
        if validate_the_url():
            if validate_group1_ques():
                if validate_group2_ques():
                    assert True


def validate_regression_of_progress_bar():
    time.sleep(2)
    perc_before = assignment_page.progress_percentage_val()
    driver.switch_to.frame('assessment-builder')
    driver.find_element(*assignment_page.G2_clear_answer).click()
    driver.switch_to.default_content()
    time.sleep(3)
    perc_after = assignment_page.progress_percentage_val()
    if perc_after < perc_before:
        assert True


validate_regression_of_progress_bar()
