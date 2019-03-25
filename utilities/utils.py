import string
import random
import time
import utilities.custom_logger as cl


class Utils(object):

    log = cl.custom_logger()

    def sleep_driver(self, duration=3, reason=None):
        time.sleep(duration)
        if reason is not None:
            self.log.info("Driver sleeping for {} secs due to: {}".format(str(duration), reason))

    def generate_random_value(self, length=10, value_type='letters'):
        value_type = value_type.lower()
        value = ''
        if value_type == 'lower':
            val = string.ascii_lowercase
        elif value_type == 'upper':
            val = string.ascii_uppercase
        elif value_type == 'digits':
            val = string.digits
        elif value_type == 'mix':
            val = string.ascii_letters + string.digits
        else:
            val = string.ascii_letters
        for i in range(length):
            value += random.choice(val)
        self.log.info('Random value generated: {}'.format(value))
        return value

    def generate_random_name(self, length=10):
        return self.generate_random_value(length=length, value_type='letters')

    def generate_random_names_list(self, number_of_names=5, length_if_all_names_same_length=None,
                                   list_of_length_of_all_names=None):
        # use either number_of_names together with length_if_all_names_same_length or list_of_length_of_all_names alone
        # when using list_of_length_of_all_names parameter be sure to enter a list

        names_list = []
        try:
            if len(list_of_length_of_all_names) > 1 and length_if_all_names_same_length is None:
                number_of_names = len(list_of_length_of_all_names)
                for i in range(number_of_names):
                    names_list.append(self.generate_random_name(list_of_length_of_all_names[i]))
            elif len(list_of_length_of_all_names) == 0 and length_if_all_names_same_length is not None:
                for i in range(number_of_names):
                    names_list.append(self.generate_random_name(length_if_all_names_same_length))
            else:
                self.log.info('Invalid input')
        except Exception as e:
            self.log.error('Following exception occurred while generating a random names list:\n{}'.format(e))
        return names_list

    def verify_text_contain(self, actual_text, expected_text):
        if expected_text in actual_text:
            self.log.info("Actual text contains Expected text")
            return True
        else:
            self.log.info("Actual text does not contain Expected text")
            return False

    def verify_text_match(self, actual_text, expected_text):
        if expected_text == actual_text:
            self.log.info("Actual text matched Expected text")
            return True
        else:
            self.log.info("Actual text does not match Expected text")
            return False

    def verify_list_contain(self, actual_list, expected_list):
        actual_list_len = len(actual_list)
        expected_list_len = len(expected_list)
        result = False
        for i in range(expected_list_len):
            for j in range(actual_list_len):
                if expected_list[i] == actual_list[j]:
                    result = True
        if result is True:
            self.log.info("Actual list contains Expected list")
        else:
            self.log.info("Actual list does not contain Expected list")
        return result

    def verify_list_match(self, actual_list, expected_list):
        result = actual_list == expected_list
        if result is True:
            self.log.info("Actual list matches Expected list")
        else:
            self.log.info("Actual list does not match Expected list")
        return result


print(Utils.verify_text_contain('Hi', 'Hi'))