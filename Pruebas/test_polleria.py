
import unittest
import time
import uuid

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = "https://versionamiento-diaz-daniel.onrender.com"


class PruebasPolleria(unittest.TestCase):

    def setUp(self):
        opciones = webdriver.ChromeOptions()
        opciones.add_argument("--headless")
        opciones.add_argument("--no-sandbox")

        self.driver = webdriver.Chrome(options=opciones)
        self.driver.get(URL)
        self.wait = WebDriverWait(self.driver, 45)

    def tearDown(self):
        self.driver.quit()

    # PRUEBA 1: Registrar un producto
    def test_registrar_producto(self):

        nombre = "Producto Selenium " + uuid.uuid4().hex[:6]
        precio = "150"

        self.wait.until(
            EC.presence_of_element_located((By.ID, "name"))
        )

        self.driver.find_element(By.ID, "name").send_keys(nombre)
        self.driver.find_element(By.ID, "price").send_keys(precio)

        self.driver.find_element(By.ID, "addProduct").click()

        self.wait.until(
            lambda d: nombre in d.find_element(
                By.CSS_SELECTOR, "#productsTable tbody"
            ).text
        )

        tabla = self.driver.find_element(
            By.CSS_SELECTOR, "#productsTable tbody"
        )

        self.assertIn(nombre, tabla.text)

        print("PRUEBA 1 APROBADA: Producto registrado correctamente.")

    # PRUEBA 2: Validar campos vacíos
    def test_validar_campos_vacios(self):

        self.wait.until(
            EC.presence_of_element_located((By.ID, "addProduct"))
        )

        tabla = self.driver.find_element(
            By.CSS_SELECTOR, "#productsTable tbody"
        )

        registros_antes = len(
            tabla.find_elements(By.TAG_NAME, "tr")
        )

        self.driver.find_element(By.ID, "addProduct").click()

        alerta = self.wait.until(EC.alert_is_present())

        mensaje = alerta.text

        self.assertEqual(
            mensaje,
            "Ingresa un nombre y un precio válidos."
        )

        alerta.accept()

        tabla = self.driver.find_element(
            By.CSS_SELECTOR, "#productsTable tbody"
        )

        registros_despues = len(
            tabla.find_elements(By.TAG_NAME, "tr")
        )

        self.assertEqual(registros_antes, registros_despues)

        print("PRUEBA 2 APROBADA: Se rechazaron los campos vacíos.")


if __name__ == "__main__":
    unittest.main(verbosity=2)
