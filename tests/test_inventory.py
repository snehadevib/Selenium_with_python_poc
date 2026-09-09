from pages.inventory_page import InventoryPage


def test_add_item_to_cart(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    inventory_page.add_backpack_to_cart()

    assert inventory_page.get_cart_count() == "1"