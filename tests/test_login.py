import pytest
from pages.login_page import LoginPage
from data.users import STANDARD_USER, LOCKED_OUT_USER
from conftest import load_json_data


def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.login(STANDARD_USER["username"], STANDARD_USER["password"])

    assert "inventory" in driver.current_url


def test_locked_out_user(driver):
    login_page = LoginPage(driver)
    login_page.login(LOCKED_OUT_USER["username"], LOCKED_OUT_USER["password"])

    error_text = login_page.get_error_message()
    assert "locked out" in error_text.lower()


invalid_login_cases = load_json_data("invalid_logins.json")


@pytest.mark.parametrize("case", invalid_login_cases)
def test_invalid_login_combinations(driver, case):
    login_page = LoginPage(driver)
    login_page.login(case["username"], case["password"])

    error_text = login_page.get_error_message()
    assert case["expected_error"] in error_text.lower()