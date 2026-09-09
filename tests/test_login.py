from pages.login_page import LoginPage


def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    assert "inventory" in driver.current_url

def test_locked_out_user(driver):
    login_page = LoginPage(driver)
    login_page.login("locked_out_user", "secret_sauce")

    error_text = login_page.get_error_message()
    assert "locked out" in error_text.lower()