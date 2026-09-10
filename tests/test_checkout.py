from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_complete_checkout(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    inventory_page.add_backpack_to_cart()

    cart_icon = logged_in_driver.find_element("css selector", "[data-test='shopping-cart-link']")
    cart_icon.click()

    cart_page = CartPage(logged_in_driver)
    cart_page.click_checkout()

    checkout_page = CheckoutPage(logged_in_driver)
    checkout_page.fill_checkout_info("Sneha", "Devi", "65189")
    checkout_page.click_finish()

    confirmation = checkout_page.get_confirmation_message()
    assert confirmation == "Thank you for your order!"