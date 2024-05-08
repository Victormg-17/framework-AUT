import unittest
from selenium import webdriver

class TestNavegacion(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()

    def test_buscar_pagina(self):
        self.driver.get("https://www.google.com")
        self.assertIn("Google", self.driver.title)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()