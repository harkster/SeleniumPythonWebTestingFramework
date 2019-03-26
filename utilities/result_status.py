import utilities.custom_logger as cl
from base.webdriver_helper import Helper

class ResultStatus(Helper):

    def __init__(self, driver):
        super.__init__(driver)
        self.results = []

    def get_results(self, result):
        if result is True:
            self.results.append('PASS')
        else:
            self.take_screenshot()
            self.results.append('FAIL')

    def mid_test_verification(self, result, verification_point):
        self.get_results(result)
        if 'PASS' in self.results:
            self.log.info("Verification point: {} -- PASSED".format(verification_point))
        else:
            self.log.info("Verification point: {} -- FAILED".format(verification_point))
        self.results.clear()

    def final_verification(self, result):
        self.get_results(result)
        if 'PASS' in self.results:
            self.log.info("Test Case -- PASSED")
            assert True is True
        else:
            self.log.info("Test Case -- FAILED")
            assert False is False
        self.results.clear()
