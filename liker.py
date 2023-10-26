from selenium_func import *
from time_util import *
import sys

from xpath import read_xpath


def explore_liker(likes):
    # To prevent being busted to use a bot, random sleep between a time interval
    sleep_for_rand_between(6, 8)

    # Click the first available post on the section
    try:
        timeout = 20
        element_locator = By.XPATH, read_xpath("explore_section", "first_explore_post")
        explore_post = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(element_locator)
        )
        explore_post.click()
    except Exception as e:
        print("Can't find a post to click")
        print(e)
        raise

    i = 0
    while i in range(likes):

        # Check if post is already liked, if yes skip post, except find like button and like post
        try:
            # Check for already liked post
            timeout = 3
            element_locator = By.XPATH, read_xpath("get_comments_on_post", "unlike_button_full_XPath")
            WebDriverWait(driver, timeout).until(
                EC.visibility_of_element_located(element_locator)
            )

            # Skip the already liked post
            try:
                timeout = 5
                element_locator = By.XPATH, read_xpath("explore_section", "next_button")
                next_button = WebDriverWait(driver, timeout).until(
                    EC.visibility_of_element_located(element_locator)
                )
                next_button.click()
            except Exception as e:
                print("Can't find next post button")
                print(e)

        # If Not already liked
        except Exception as e:

            # Find the like button and click it
            try:
                timeout = 5
                element_locator = By.XPATH, read_xpath("get_comments_on_post", "like_button_full_XPath")
                like_button = WebDriverWait(driver, timeout).until(
                    EC.visibility_of_element_located(element_locator)
                )
                like_button.click()
                sys.stdout.write(f"Like number: {str(i)}   \r")
                sys.stdout.flush()
                try:
                    timeout = 5
                    element_locator = By.XPATH, read_xpath("explore_section", "next_button")
                    next_button = WebDriverWait(driver, timeout).until(
                        EC.visibility_of_element_located(element_locator)
                    )
                    next_button.click()
                    i += 1
                except Exception as e:
                    print("Can't find next post button")
                    print(e)
            except Exception as e:
                print("Can't find next post button")
                print(e)
