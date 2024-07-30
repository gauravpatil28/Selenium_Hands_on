import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import pytest


class TestSample():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Firefox()
        driver.set_window_size(1920, 1080)
        driver.get("https://artoftesting.com/samplesiteforselenium")
        yield
        driver.close()
        driver.quit()
        print("Test Completed")

    def test_link(self,test_setup):
        element = driver.find_element(By.LINK_TEXT, "This is a link")
        text = element.get_attribute("href")
        print(text)
        element.click()

    def test_textbox(self,test_setup):
        driver.find_element(By.ID, "fname").send_keys("Gaurav")
        print("Text box successfully Checked")

    def test_button(self,test_setup):
        element = driver.find_element(By.ID, "idOfButton")
        old_element_colour = element.value_of_css_property("background-color")
        element.click()
        new_element_colour = element.value_of_css_property("backgorund-color")
        assert old_element_colour != new_element_colour
        print("Button successfully Checked")

    def test_double_click(self, test_setup):
        element = driver.find_element(By.ID, "dblClkBtn")

        action = ActionChains(driver)
        action.double_click(element).perform()
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        print(alert.text)
        alert.accept()
        print("Double click successfully Checked")

    def test_radio(self,test_setup):
        m_radio = driver.find_element(By.ID, "male")
        f_radio = driver.find_element(By.ID, "female")
        m_radio.click()
        assert m_radio.is_selected()
        assert not f_radio.is_selected()
        print("Radio Button successfully Checked")

    def test_checkbox(self,test_setup):
        driver.find_element(By.CLASS_NAME, "Automation").click()
        driver.find_element(By.CLASS_NAME, "Performance").click()
        print("Checkbox successfully Verified")

    def test_dropdown(self,test_setup):
        driver.find_element(By.ID, "testingDropdown").click()
        time.sleep(1)
        driver.find_element(By.ID, "automation").click()
        time.sleep(1)
        driver.find_element(By.ID, "testingDropdown").click()
        time.sleep(1)
        driver.find_element(By.ID, "performance").click()
        time.sleep(1)
        driver.find_element(By.ID, "testingDropdown").click()
        time.sleep(1)
        driver.find_element(By.ID, "manual").click()
        time.sleep(1)
        driver.find_element(By.ID, "testingDropdown").click()
        time.sleep(1)
        driver.find_element(By.ID, "database").click()
        time.sleep(1)
        print("DropDown successfully Checked")

    def test_alertbox(self,test_setup):
        driver.find_element(By.XPATH, "//button[@onclick='generateAlertBox()']").click()
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        print(alert.text)
        alert.accept()
        print("Alert Button successfully Checked")

    def test_confirmbutton(self,test_setup):
        driver.find_element(By.XPATH, "//button[@onclick='generateConfirmBox()']").click()
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        num = random.randint(0,1)
        if num == 1:
            alert.accept()
            element = driver.find_element(By.ID, "demo")
            response = element.text
            assert response == "You pressed OK!"
        else:
            alert.dismiss()
            element = driver.find_element(By.ID, "demo")
            response = element.text
            assert response == "You pressed Cancel!"

if __name__ == "main":
    pytest.main()