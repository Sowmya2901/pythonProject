import random
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from SeleniumHelpers.helpers import Helpers
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from Pages.BetaPage import BetaPage


# adding chrome options to block the alerts from browser
chr_options = Options()
chr_options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 2})  # 1: Allow, 2: Block

# initializing the Chrome browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chr_options)

# initializing the beta page class
beta_page = BetaPage(driver)

# navigating to the application
beta_page.navigate_to_URL(
    "https://apps.inindca.com/wem-learning-ui/#/assignments/a66c044d-0d52-4a43-9ec3-5af39f4986e3")
driver.implicitly_wait(3)

# maximizing the widow
driver.maximize_window()

# waiting until the page loads
helper_wait = Helpers(driver)
helper_wait.wait_for_element((By.TAG_NAME, "body"))
time.sleep(5)

# entering login credentials
beta_page.login_page()
time.sleep(15)

# click on start module of the test assignment
driver.find_element(*beta_page.start_module_button).click()
time.sleep(5)

# able to see the content tab of the assignment page
driver.find_element(*beta_page.content_tab)


def validate_rich_text():
    time.sleep(3)
    scrollable_content = driver.find_element(By.XPATH, "//div[@class='InvisibleElement']")
    delta_y = scrollable_content.rect['y']
    scroll_origin = ScrollOrigin.from_element(scrollable_content)
    ActionChains(driver).scroll_from_origin(scroll_origin, 0, int(delta_y)).perform()
    time.sleep(3)
    flag = beta_page.validate_progress_perc()
    driver.find_element(*beta_page.next_button).click()
    return flag


def validate_the_url():
    time.sleep(3)
    # click on next
    driver.find_element(*beta_page.next_button).click()
    time.sleep(3)
    flag = beta_page.validate_progress_perc()
    return flag


def validate_group1_ques():
    # switch to the assessment frame
    driver.switch_to.frame('assessment-builder')
    # select the answers for the group 1 questions
    beta_page.select_option_for_questions()
    # switch back to default frame
    driver.switch_to.default_content()
    # click on next
    driver.find_element(By.XPATH, "//h2[text()=' 2. Group 2 ']").click()
    time.sleep(2)
    flag = beta_page.validate_progress_perc()
    return flag


def validate_group2_ques():
    # switch to the assessment frame
    driver.switch_to.frame('assessment-builder')
    random_choice = random.choice(beta_page.G2_Q1_options)
    driver.find_element(By.XPATH, random_choice).click()
    driver.switch_to.default_content()
    time.sleep(2)
    flag = beta_page.validate_progress_perc()
    return flag


def validate_scorm():
    flag = True
    bret = False
    while flag:
        driver.switch_to.default_content()
        element_displayed = driver.find_element(By.XPATH, "//h2[text()=' 2. Group 2 ']").is_displayed()
        if element_displayed:
            flag = False
            bret = True
        else:
            driver.find_element(*beta_page.next_button).click()
            time.sleep(4)
            flag = beta_page.validate_progress_perc()
    return bret


if validate_the_url():
    if validate_rich_text():
        if validate_scorm():
            if validate_group1_ques():
                if validate_group2_ques():
                    assert True
                else:
                    assert False


def validate_regression_of_progress_bar():
    time.sleep(2)
    perc_before = beta_page.progress_percentage_val()
    driver.switch_to.frame('assessment-builder')
    driver.find_element(*beta_page.G2_clear_answer).click()
    driver.switch_to.default_content()
    time.sleep(3)
    perc_after = beta_page.progress_percentage_val()
    if perc_after < perc_before:
        assert True
    else:
        assert False


validate_regression_of_progress_bar()
