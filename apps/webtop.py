from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.alert import Alert

import utils

def webtop_main(**kw):
  username, password = kw.values()

  options = Options()
  options.headless = True

  try:
    settings = utils.get_settings("webtop")
    driver = webdriver.Firefox(executable_path=settings.get('geckdriverPath', 'geckodriver'), options=options)

    driver.get('https://www.webtop.co.il/v2/default.aspx')
    utils.wait(3)

    driver.find_element_by_id('identityNumber').send_keys(username)
    utils.wait(1)

    driver.find_element_by_id('password').send_keys(password)
    utils.wait(2)

    driver.find_element_by_id('loginLogoutButton').click()
    utils.wait(4)

    driver.get('https://www.webtop.co.il/corona.aspx')
    utils.wait(1)

    driver.find_element_by_id('saveButton').click()
    Alert(driver).accept()

    driver.close()

    utils.log(f'The clearance was successfully signed', src="webtop")
  except Exception as exc:
    utils.log(f'Signature the clearance failed', src="webtop")

    raise exc

