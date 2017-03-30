from selenium import webdriver
from selenium.webdriver.common.keys import Keys

desired_cap = {'os': 'Windows',
               'os_version': 'xp',
               'browser': 'Chrome',
               'browser_version': '47.0'
               }


def test_browser_stack():
    desired_cap['project'] = "Lviv meetup"
    desired_cap['build'] = "build 1.0.1"
    desired_cap['browserstack.debug'] = True
    desired_cap['browserstack.video'] = False

    # driver = webdriver.Remote(
    #     command_executor='http://meetup1:cFWMJhFtUEyVxQYqLLMp@hub.browserstack.com:80/wd/hub',
    #     desired_capabilities=desired_cap)
    #
    # driver.save_screenshot('screenshots.png')
    driver = webdriver.Firefox()
    driver.maximize_window()

    driver.get("http://www.python.org")
    if "Python" not in driver.title:
        raise Exception("Unable to load python.org page!")
    elem = driver.find_element_by_name("q")
    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    print driver.title
    driver.quit()

