import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@pytest.mark.saucedemo
def test_saucedemo():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # El usuario se loguea al sitio como usuario standard user
        driver.get("https://saucedemo.com")
        driver.find_element(By.CSS_SELECTOR, '[data-test="username"]').send_keys("standard_user")
        driver.find_element(By.CSS_SELECTOR, '[data-test="password"]').send_keys("secret_sauce")
        driver.find_element(By.CSS_SELECTOR, '[data-test="login-button"]').click()

        # Ordenar los elementos por “price (low to high)”
        select = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
        select.select_by_visible_text("Price (low to high)")
        time.sleep(2)

        # Verificar que los elementos estén ordenados
        precios = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        valores = [float(p.text.replace("$", "")) for p in precios]
        assert valores == sorted(valores)

        # Incorporar al carrito todos los elementos
        add_to_cart_buttons = driver.find_elements(By.XPATH, "//button[text()='Add to cart']")
        for button in add_to_cart_buttons:
            button.click()
            time.sleep(0.5)

        # Ir al carrito
        driver.find_element(By.CSS_SELECTOR, '[data-test="shopping-cart-link"]').click()
        wait = WebDriverWait(driver, 10)

        # Verificar que todos los elementos estén en el carrito
        cart_items = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "cart_item")))
        assert len(cart_items) == len(add_to_cart_buttons)

        # Ir al Checkout 
        driver.find_element(By.ID, "checkout").click()

        # Ingresar nombre y clickear "Continue"
        driver.find_element(By.ID, "first-name").send_keys("Camila")
        driver.find_element(By.ID, "continue").click()

        # Verificar que aparece el error “Error: Last Name is required”
        error1 = driver.find_element(By.CLASS_NAME, "error-message-container").text
        assert "Last Name is required" in error1

        # Ingresar un apellido y clickear “Continue”
        driver.find_element(By.ID, "last-name").send_keys("Cale")
        driver.find_element(By.ID, "continue").click()

        # Verificar que aparece el error “Error: Postal Code is required”
        error2 = driver.find_element(By.CLASS_NAME, "error-message-container").text
        assert "Postal Code is required" in error2

        # Vaciar carrito
        driver.find_element(By.CSS_SELECTOR, '[data-test="shopping-cart-link"]').click()
        remove_buttons = driver.find_elements(By.XPATH, "//button[text()='Remove']")
        for b in remove_buttons:
            b.click()
            time.sleep(0.3)
        driver.find_element(By.ID, "continue-shopping").click()

        # Agregar 2 elementos
        driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()
        driver.find_element(By.CSS_SELECTOR, '[data-test="add-to-cart-sauce-labs-bike-light"]').click()
        
        # Ir al carrito
        driver.find_element(By.CSS_SELECTOR, '[data-test="shopping-cart-link"]').click()

        # Verificar que los elementos existan
        assert len(driver.find_elements(By.CLASS_NAME, "cart_item")) == 2

        # Hacer el checkout
        driver.find_element(By.ID, "checkout").click()
        driver.find_element(By.ID, "first-name").send_keys("Camila")
        driver.find_element(By.ID, "last-name").send_keys("Cale")
        driver.find_element(By.ID, "postal-code").send_keys("1234")
        driver.find_element(By.ID, "continue").click()

        # Finalizar la compra
        driver.find_element(By.ID, "finish").click()

        # Verificar que la compra fue realizada
        mensaje = driver.find_element(By.CLASS_NAME, "complete-header").text
        assert mensaje == "Thank you for your order!"

    finally:
        driver.quit()
