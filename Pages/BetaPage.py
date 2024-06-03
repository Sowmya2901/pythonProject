import random
import time
from selenium.webdriver.common.by import By


class BetaPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_textbox = (By.ID, 'email')
        self.password_textbox = (By.ID, 'password')
        self.login_button = (By.XPATH, "//button[@type='submit']")
        self.progress_percentage = (By.XPATH, "//div[@id='gux-tab-inform-panel']//div[@class='progress-bar-info']")
        self.start_module_button = (By.XPATH, "//gux-button[@class='module-start-button cover-art']")
        self.content_tab = (By.XPATH, "//button[@class='gux-tab gux-active']")
        self.content_title = (By.XPATH, "//span[text()='Lorem Ipsum']")
        self.next_button = (By.XPATH, "//div[@id='gux-tab-inform-panel']//gux-button[@title='Next']")
        self.contentParagraph = (By.XPATH, "// span[ @ id = 'assignment-rich-text'] / p[26]")
        self.new_window_launch_link = (By.XPATH, "//label[@class='button-label']")
        self.G2_clear_answer = (By.XPATH, "//button[@class='clear-answer-button Clickable']")
        self.G1_clear_answer = (By.XPATH, "//button[@class='clear-answer-button ']")
        self.Ques1_options = ["//input[@id='e589dda2-67bb-4211-add3-03233fe48b07']",
                              "//input[@id='4b2109c0-1fdb-4dc9-a641-8a8a5e932d27']",
                              "//input[@id='50d3652c-3018-499a-bf1d-dba86a439b93']"]
        self.Ques2_option = (By.XPATH,
                             "//li[@class='ScorableQuestionListEntry']//div[@class='FreeTextQuestionOption']//textarea")
        self.Ques3_options = ["//input[@id='2ae10166-84ac-4022-b1f3-20bbf1d2c085']",
                              "//input[@id='d566fc2a-cf32-4a5f-b862-61199b09d097']",]
        self.G2_Q1_options = ["//input[@id='75e697ab-a105-4529-ac3d-c29f8c017897']",
                              "//input[@id='26d296d3-d004-40e5-9a1e-5570e024caa8']",
                              "//input[@id='f7688ab3-4167-4f0a-b888-141ec59f7a96']"]
        self.optionsList = [self.Ques1_options, self.Ques2_option, self.Ques3_options]

    def navigate_to_URL(self, url):
        self.driver.get(url)

    def login_page(self):
        self.driver.find_element(By.ID, 'email').send_keys('test.user3@genesys-interview.com')
        self.driver.find_element(By.ID, 'password').send_keys('oR7]bajo')
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

    def progress_percentage_val(self):
        time.sleep(2)
        progress_eel = self.driver.find_element(By.XPATH,
                                                "//div[@id='gux-tab-inform-panel']//div[@class='progress-bar-info']")
        value_property = progress_eel.get_attribute("textContent")
        Val = value_property.split()
        numeric_val = Val[0].strip('%')
        return int(numeric_val)

    global temp_perc
    temp_perc = [0]

    def validate_progress_perc(self):
        expected_percentage = 100
        initial_percentage = 0
        val = self.progress_percentage_val()
        if initial_percentage < val <= expected_percentage:
            temp_perc.append(val)
            for i in range(len(temp_perc)):
                for j in range(i + 1, len(temp_perc)):
                    if temp_perc[i] < temp_perc[j]:
                        return True
                    else:
                        return False
        else:
            return False

    def select_option_for_questions(self):
        i = 0
        G1_list_of_questions = self.driver.find_elements(By.XPATH,
                                                         "//ol[@class='ScorableQuestionList']//div[@class='ScorableQuestion']//div[@class='QuestionName']")
        for question in G1_list_of_questions:
            if type(self.optionsList[i]) == list:
                random_element = random.choice(self.optionsList[i])
                self.driver.find_element(By.XPATH, random_element).click()
            else:
                self.driver.find_element(*self.optionsList[i]).send_keys("World Health Organisation")
            i += 1