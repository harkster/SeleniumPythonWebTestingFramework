from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import *
import selenium.webdriver.support.expected_conditions as ec
import utilities.custom_logger as cl
import datetime
import os


class Helper:

    log = cl.custom_logger()

    def __init__(self, driver):
        self.driver = driver

    def get_page_title(self):
        return self.driver.title

    def get_by_type(self, locator_type='id'):
        locator_type = locator_type.lower()
        if locator_type == 'id':
            return By.ID
        elif locator_type == 'xpath':
            return By.XPATH
        elif locator_type == 'css':
            return By.CSS_SELECTOR
        elif locator_type == 'class':
            return By.CLASS_NAME
        elif locator_type == 'link':
            return By.LINK_TEXT
        else:
            self.log.info('Invalid locator type entered, defaulting to ID')
            return By.ID

    def get_element(self, locator_type='id', locator=''):
        element = None
        try:
            self.log.info("Finding element using locator_type: {} and locator: {}".format(locator_type, locator))
            element = self.driver.find_element(self.get_by_type(locator_type), locator)
            self.log.info("Element Found")
        except Exception as e:
            self.log.error("Following exception occurred while getting element:\n{}".format(e))
        return element

    def wait_for_element(self,  locator, locator_type='id', timeout=5, freq=0.5):
        element = None
        try:
            self.log.info("Finding element using locator_type: {} and locator: {}".format(locator_type, locator))
            self.log.info("Waiting for element for {} secs".format(str(timeout)))
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=freq,
                                 ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
            element = wait.until(ec.visibility_of_element_located((self.get_by_type(locator_type), locator)))
            if element is not None:
                self.log.info("Element found")
            else:
                self.log.info("Element not found")
        except Exception as e:
            self.log.error("Following exception occurred while waiting for element:\n{}".format(e))
        return element

    def click_on_element(self, locator, locator_type='id'):
        self.wait_for_element(locator, locator_type).click()
        self.log.info('Clicked on element')

    def clear_element(self, locator, locator_type='id'):
        self.wait_for_element(locator, locator_type).clear()
        self.log.info('Cleared element')

    def send_data_to_element(self, data, locator, locator_type='id'):
        self.wait_for_element(locator, locator_type).send_keys(data)
        self.log.info('Sent data to element: {}'.format(str(data)))

    def get_element_attribute_value(self, attribute_name, locator, locator_type='id'):
        value = ''
        element = self.wait_for_element(locator, locator_type)
        try:
            value = element.get_attribute(attribute_name)
        except Exception as e:
            self.log.error("Following exception occurred while getting attribute value of element:\n{}".format(e))
        return value

    def is_element_present(self, locator, locator_type):
        element = self.wait_for_element(locator, locator_type)
        if element is not None:
            return True
        else:
            return False

    def is_element_displayed(self, locator, locator_type):
        displayed = False
        element = self.wait_for_element(locator, locator_type)
        try:
            displayed = element.is_displayed()
        except Exception as e:
            self.log.error("Following exception occurred while checking if element is displayed:\n{}".format(e))
        if displayed is True:
            self.log.info("Element is displyed")
        else:
            self.log.info("Element is not displyed")
        return displayed

    def is_element_enabled(self, atrname, locator, locator_type):
        # this method will work only when attribute name is either enabled or disabled
        # atrname is the name of attribute - enabled or disabled
        enabled = False
        value = self.get_element_attribute_value(atrname, locator, locator_type)
        atrname = atrname.lower()
        if value is True and atrname == 'enabled':
            self.log.info("Element is enabled")
            enabled = True
        elif value is False and atrname == 'disabled':
            self.log.info("Element is enabled")
            enabled = True
        else:
            self.log.info("Element is disabled")
        return enabled

    def scroll_window(self, direction='down', scroll_by=1000):
        direction = direction.lower()
        if direction == 'down':
            self.driver.execute_script("window.scrollBy(0,{});".format(str(scroll_by)))
            self.log.info("Scrolled down by {} points".format(str(scroll_by)))
        elif direction == 'up':
            self.driver.execute_script("window.scrollBy(0,-{});".format(str(scroll_by)))
            self.log.info("Scrolled up by {} points".format(str(scroll_by)))

    def switch_to_frame(self, frame_name=None, frame_index=None, frame_tag_name=None, frame_tag_index=None):
        # use either frame_name or frame_index or combination of frame_tag_name and frame_tag_index
        self.log.info("Switching to frame")
        try:
            if frame_name is not None and frame_index is None and frame_tag_name is None and frame_tag_index is None:
                self.driver.switch_to.frame(frame_name)
            elif frame_index is not None and frame_name is None and frame_tag_name is None and frame_tag_index is None:
                self.driver.switch_to.frame(frame_index)
            elif frame_tag_name is not None and frame_tag_index is not None and frame_index is None and frame_name is None:
                self.driver.switch_to.frame(self.driver.find_elements_by_tag_name(frame_tag_name)[frame_tag_index])
            else:
                self.log.info("Invalid input")
        except Exception as e:
            self.log.error("Following exception occurred while switching frame:\n{}".format(e))

    def switch_back_to_default_window(self):
        self.driver.switch_to.default_content()
        self.log.info("Switched back to default content")

    def take_screenshot(self):
        current_time = datetime.datetime.strftime(datetime.datetime.now(), '%m-%d-%Y_%H-%M-%S')
        file_name = 'screenshot_{}.png'.format(current_time)
        relative_screenshot_folder = '../screenshots/'
        relative_screenshot_file = relative_screenshot_folder + file_name

        self.driver.save_screenshot(relative_screenshot_file)
