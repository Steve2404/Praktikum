from selenium.webdriver.firefox.service import Service
from selenium import webdriver

servicee = Service(executable_path="/home/ljatsa/Downloads/geckodriver-v0.28.0-linux64")
driver = webdriver.Firefox(service=servicee)


"""
url = "https://www.google.com/search?q=twitter&sxsrf=ALiCzsZkG1MgR7tTuwLUADmd_cmWer-" \
      "jhQ%3A1669117654230&source=hp&ei=1rZ8Y_2RC7KOxc8P7vKjoAc&iflsig=AJiK0e8AAAAAY3zE5" \
      "vkMoxKIJYjmcB3nELJ1IYKG5tpw&oq=twii&gs_lcp=Cgdnd3Mtd2l6EAMYADIHCCMQsQIQJzIMCC4QxwEQ0QMQChBDMg" \
      "YIABAKEEMyBwgAEIAEEAoyBwgAEIAEEAoyBwgAEIAEEAoyBwgAEIAEEAoyBwgAEIAEEAoyBwgAEIAEEAoyBwgAEIAEEAo6BAg" \
      "jECc6CgguEMcBENEDEEM6BAgAEEM6BQgAEIAEOggILhCABBDUAlAAWLwKYIcnaABwAHgAgAGRAYgBhgOSA" \
      "QMzLjGYAQCgAQE&sclient=gws-wiz"
      """
"""

driver.get(url)
link = driver.find_element(By.CLASS_NAME, "iUh30 qLRx3b tjvcx")
print(link.text)
"""
driver.get('http://google.com')
print(driver.title)
driver.quit()
