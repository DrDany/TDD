from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time


class NewVisitorTest(unittest.TestCase):
    ''' тест нового поситетеля'''

    def setUp(self):
        '''Установка'''
        self.browser = webdriver.Firefox()

    def tearDown(self):
        '''Демонтаж'''
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        '''тест: можно начать список и получить его позже11'''
        self.browser.get('http://localhost:8000')

        # Она видит, что заголовок и шапка страницы говорят о
        # списках неотложных дел
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('hl').text
        self.assertIn('To-Do', header_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        inputbox.send_keys('Купить павлиньи перья')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Купить павлиньи перья' for row in rows),
            "Новый элемент списка не появился в таблице"
        )

        self.fail('Закончить тест!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
