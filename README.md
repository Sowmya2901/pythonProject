# AssessmentProject



# Learning Module Automation

The objective of this automation documentation is to outline the process and steps involved in verifying the functionality of the progress bar in the learning feature of 'XXX' company.



## Installation

- Install pycharm from https://www.jetbrains.com/pycharm/download/?section=windows

- Install latest version of python from https://www.python.org/downloads/
 
- Once completed open the terminal of pycharm and install pip using command- 'python get-pip.py.'

- Install selenium using command - ' pip install -U selenium '


## SetUp
- Download python project from github to the local machine and open the project in python

Github link - https://github.com/Sowmya2901/pythonProject

    
## Execution

- Run Assignment_test.py file by run button on the top or right click on the Assignment_test.py file and click on run option for test module Assignment_test

- For running beta feature run Beta_test.py file by clicking run button on the top


## Tech Stack 

programming language used : Python

Automation tool :  Selenium

IDE : Pycharm

## Note:

-Please execute the test files after resetting the status of the assigment modules to 'planned'.
The code works perfectly only when progress bar is at 0%.

- Please use the login credentials for Test User3  by sending email as a string in send keys method of email and password as a string in sendkeys method of pasword respectively.
please refer below example to do modification in AssignmentPage.py file line number 46 and 47.

eg:  
self.driver.find_element(By.ID, 'email').send_keys('abc@gmail.com')
self.driver.find_element(By.ID, 'password').send_keys('abc@123')







 
