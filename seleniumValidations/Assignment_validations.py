import random
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin


class AssignmentMethods:
    def __init__(self, driver, assignment_page):
        self.driver = driver
        self.assignment_page = assignment_page

    def validate_rich_text(self):
        # click on the content title
        self.driver.find_element(*self.assignment_page.content_title).click()
        scrollable_content = self.driver.find_element(By.XPATH, "//div[@class='InvisibleElement']")
        delta_y = scrollable_content.rect['y']
        scroll_origin = ScrollOrigin.from_element(scrollable_content)
        ActionChains(self.driver).scroll_from_origin(scroll_origin, 0, int(delta_y)).perform()
        time.sleep(3)
        flag = self.assignment_page.validate_progress_perc()
        self.driver.find_element(*self.assignment_page.next_button).click()
        return flag

    def validate_the_url(self):
        time.sleep(3)
        # click on next
        self.driver.find_element(*self.assignment_page.next_button).click()
        time.sleep(3)
        flag = self.assignment_page.validate_progress_perc()
        return flag

    def validate_group1_ques(self, ans_option_list):
        # switch to the assessment frame
        self.driver.switch_to.frame('assessment-builder')
        # select the answers for the group 1 questions
        self.assignment_page.select_option_for_questions(ans_option_list)
        # switch back to default frame
        self.driver.switch_to.default_content()
        # click on next
        self.driver.find_element(By.XPATH, "//h2[text()=' 2. Group 2 ']").click()
        time.sleep(2)
        flag = self.assignment_page.validate_progress_perc()
        return flag

    def validate_group2_ques(self, g2_ans_opt_list):
        # switch to the assessment frame
        self.driver.switch_to.frame('assessment-builder')
        random_choice = random.choice(g2_ans_opt_list)
        self.driver.find_element(By.XPATH, random_choice).click()
        self.driver.switch_to.default_content()
        time.sleep(2)
        flag = self.assignment_page.validate_progress_perc()
        return flag

    def validate_scorm(self):
        flag = True
        bret = False
        while flag:
            self.driver.switch_to.default_content()
            element_displayed = self.driver.find_element(By.XPATH, "//h2[text()=' 2. Group 2 ']").is_displayed()
            if element_displayed:
                flag = False
                bret = True
            else:
                self.driver.find_element(*self.assignment_page.next_button).click()
                time.sleep(4)
                flag = self.assignment_page.validate_progress_perc()
        return bret

    def validate_regression_of_progress_bar(self):
        time.sleep(2)
        perc_before = self.assignment_page.progress_percentage_val()
        self.driver.switch_to.frame('assessment-builder')
        self.driver.find_element(*self.assignment_page.G2_clear_answer).click()
        self.driver.switch_to.default_content()
        time.sleep(3)
        perc_after = self.assignment_page.progress_percentage_val()
        if perc_after < perc_before:
            assert True
        else:
            assert False

    def validate_test_assignment_page(self):
        if self.assignment_page.progress_percentage_val() == 0:
            if self.validate_rich_text():
                if self.validate_the_url():
                    if self.validate_group1_ques(self.assignment_page.optionsList):
                        if self.validate_group2_ques(self.assignment_page.G2_Q1_options):
                            assert True
                        else:
                            assert True

        self.validate_regression_of_progress_bar()

    def validate_beta_feature_of_test_assignment_page(self):
        if self.validate_the_url():
            if self.validate_rich_text():
                if self.validate_scorm():
                    if self.validate_group1_ques(self.assignment_page.optionsList_Beta):
                        if self.validate_group2_ques(self.assignment_page.G2_Beta_Q1_options):
                            assert True
                        else:
                            assert False
        self.validate_regression_of_progress_bar()