import pytest
import time
import allure
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class")
def chrome_driver_init(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    driver.maximize_window()
    yield
    driver.quit()


@allure.description("Validation Website with Valid Login")
@allure.severity(severity_level='CRITICAL')
def test_ValidLogin(chrome_driver_init):
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    Username = driver.find_element(By.NAME, "username").send_keys("Admin")
    Password = driver.find_element(By.NAME, "password").send_keys("admin123")
    btn_login = driver.find_element(By.XPATH, "//button[@type='submit']").click()
    btn_profil = driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']").click()
    time.sleep(5)
    btn_logout = driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()

    logo = driver.find_element(By.XPATH, "//img[@alt='company-branding']")
    if logo.is_displayed():
        print("Passed")

    else:
        print("Not Passed")


@allure.description("Validation Website with Invalid Login")
@allure.severity(severity_level='NORMAL')
def test_InvalidLogin_Passed(chrome_driver_init):
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    Username = driver.find_element(By.NAME, "username").send_keys("hjasgdhj")
    Password = driver.find_element(By.NAME, "password").send_keys("kjsah8475")
    btn_login = driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)
    alert_invalid = driver.find_element(By.XPATH, "//div[@class='oxd-alert-content oxd-alert-content--error']")
    driver.save_screenshot('Invalid Credentials.png')
    if alert_invalid.is_displayed():
        print("Invalid credentials")
    else:
        print("Return")

@allure.description("Verify user Profil")
@allure.severity(severity_level='NORMAL')
def test_Verify_Profil_UserName (chrome_driver_init):
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    Username = driver.find_element(By.NAME, "username").send_keys("Admin")
    Password = driver.find_element(By.NAME, "password").send_keys("admin123")
    btn_login = driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)

    Menu_MyInfo = driver.find_element(By.XPATH,"//span[normalize-space()='My Info']").click()
    time.sleep(5)
    profil_username = driver.find_element(By.XPATH, "//h6[@class='oxd-text oxd-text--h6 --strong']")
    if profil_username.is_displayed():
        print("Displayed")
    else:
        print("Not Displayed")

