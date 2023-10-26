from selenium_func import *
from time_util import *
import pickle

from xpath import read_xpath


def login(username, password):
    get_page("https://www.instagram.com/")

    cookie_uploaded = False
    cookie_filename = 'cookies.pkl'

    # Try check for cookie presence
    try:
        with open(cookie_filename, 'rb') as cookie_file:
            cookies = pickle.load(cookie_file)
            for cookie in cookies:
                driver.add_cookie(cookie)
            print("Cookies loaded successfully!")
            cookie_uploaded = True
            driver.refresh()

            # Click on explore button
            timeout = 300
            element_locator = By.XPATH, read_xpath("login_user", "explore")
            explore = WebDriverWait(driver, timeout).until(
                EC.visibility_of_element_located(element_locator)
            )

            try:
                timeout = 7
                element_locator = (By.XPATH, read_xpath("dismiss_notification_offer", "dismiss_elem_loc"))
                accept_cookie_field = WebDriverWait(driver, timeout).until(
                    EC.visibility_of_element_located(element_locator)
                )
                accept_cookie_field.click()
            except Exception as e:
                print("There is an error finding notification dismiss button")
                print(e)
                raise

            explore.click()
    except FileNotFoundError:
        print("No cookie file found. Continuing without loading cookies...")

    if not cookie_uploaded:

        # Accept cookie action
        try:
            timeout = 30
            element_locator = (By.XPATH, read_xpath("accept_igcookie_dialogue", "accept_button"))
            accept_cookie_field = WebDriverWait(driver, timeout).until(
                EC.visibility_of_element_located(element_locator)
            )
            accept_cookie_field.click()
        except Exception as e:
            print("There is an error finding the accept cookie button ")
            print(e)
            raise
        sleep_for_sec(5)

        # Insert username in the field
        try:
            timeout = 30
            element_locator = (By.XPATH, read_xpath("login_user", "input_username_XP"))
            username_field = WebDriverWait(driver, timeout).until(
                EC.visibility_of_element_located(element_locator)
            )
            username_field.send_keys(username)
        except Exception as e:
            print("There is an error during username finding step ")
            print(e)
            raise

        # Insert password in the field
        try:
            timeout = 30
            element_locator = By.XPATH, read_xpath("login_user", "input_password")
            password_field = WebDriverWait(driver, timeout).until(
                EC.visibility_of_element_located(element_locator)
            )
            password_field.send_keys(password)
        except Exception as e:
            print("There is an error during password finding step ")
            print(e)
            raise

        # Click the login button
        try:
            timeout = 30
            element_locator = By.XPATH, read_xpath("login_user", "login_elem_no_such_exception_2")
            submit_field = WebDriverWait(driver, timeout).until(
                EC.visibility_of_element_located(element_locator)
            )

            submit_field.click()
        except Exception as e:
            print("There is an error during password finding step ")
            print(e)
            raise

        # Wait for suspect login verification
        try:
            submit_field = By.XPATH, read_xpath("login_user", "login_elem_no_such_exception_3")
            submit_field.click()
        except Exception as e:
            print("There is an error during submit finding step ")
            print(e)
            pass

        # Wait for suspicious login verify and dump the cookie
        try:
            timeout = 300
            element_locator = By.XPATH, read_xpath("login_user", "explore")
            explore = WebDriverWait(driver, timeout).until(
                EC.visibility_of_element_located(element_locator)
            )

            explore.click()
            pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
        except Exception as e:
            print("There is an error during submit button finding step ")
            print(e)
            raise
