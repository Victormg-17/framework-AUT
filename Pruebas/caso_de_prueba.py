import logging
import unittest
from selenium import webdriver

import Curso_selenium
from Curso_selenium.PruebaBase.Configuraciones.config import Configuracion
from Curso_selenium.PruebaBase.funciones_globales.Funciones_Globales import FuncionesGlobales

# Configuración básica del logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Configuración específica para los logs de selenium
logging.getLogger('selenium').setLevel(logging.WARNING)


class CasoDePrueba(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()

    def setUp(self):
        test_name = self._testMethodName  # Obtener el nombre del test
        self.funciones_globales = FuncionesGlobales(self.driver, test_name)

    def test_navegacion_y_login(self):


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
