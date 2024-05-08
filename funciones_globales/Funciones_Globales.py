import logging
import os
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

class FuncionesGlobales:
    def __init__(self, driver, test_name):
        self.driver = driver
        self.logger = logging.getLogger(test_name)
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        # Crear la carpeta Reportes si no existe
        reportes_dir = os.path.join(os.path.dirname(__file__), 'Reportes')
        os.makedirs(reportes_dir, exist_ok=True)

        # Crear el manejador de archivo para el log del test actual
        file_handler = logging.FileHandler(os.path.join(reportes_dir, f'{test_name}.log'))
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def Navegar(self, url, timeout=10):
        self.driver.get(url)
        self.driver.maximize_window()
        self.logger.info("Navegando a {}".format(url))
        time.sleep(timeout)

    def Click_Mixto(self, tipo, locator, timeout=10):
        try:
            if tipo == "id":
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, locator)))
            elif tipo == "xpath":
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, locator)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val.click()
            self.logger.info("Click en el elemento %s", locator)
            time.sleep(timeout)
        except TimeoutException as ex:
            self.logger.error("Timeout al intentar encontrar el elemento %s", locator)

    def Tiempo(self, segundos):
        time.sleep(segundos)
        self.logger.info("Esperando {} segundos".format(segundos))

    def Log(self, mensaje):
        self.logger.info(mensaje)
        print(mensaje)

    def Colocar_Texto(self, tipo, locator, texto, timeout=10):
        try:
            if tipo == "id":
                val = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.ID, locator)))
            elif tipo == "xpath":
                val = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
            val.send_keys(texto)
            self.logger.info("Texto '{}' colocado en {}".format(texto, locator))
            time.sleep(timeout)
        except TimeoutException as ex:
            self.logger.error("Timeout al intentar encontrar el elemento %s", locator)

    def Select(self, tipo, locator, valor, timeout=10):
        try:
            if tipo == "id":
                select = Select(WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.ID, locator))))
            elif tipo == "xpath":
                select = Select(WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, locator))))
            select.select_by_value(valor)
            self.logger.info("Valor '{}' seleccionado en {}".format(valor, locator))
            time.sleep(timeout)
        except TimeoutException as ex:
            self.logger.error("Timeout al intentar encontrar el elemento %s", locator)

    def Upload(self, tipo, locator, archivo, timeout=10):
        try:
            if tipo == "id":
                val = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.ID, locator)))
            elif tipo == "xpath":
                val = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
            val.send_keys(archivo)
            self.logger.info("Archivo '{}' subido en {}".format(archivo, locator))
            time.sleep(timeout)
        except TimeoutException as ex:
            self.logger.error("Timeout al intentar encontrar el elemento %s", locator)

    def Check(self, tipo, locator, timeout=10):
        try:
            if tipo == "id":
                element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.ID, locator)))
            elif tipo == "xpath":
                element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
            if not element.is_selected():
                element.click()
                self.logger.info("Elemento %s chequeado", locator)
                time.sleep(timeout)
        except TimeoutException as ex:
            self.logger.error("Timeout al intentar encontrar el elemento %s", locator)
