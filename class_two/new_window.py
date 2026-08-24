from time import sleep

from playwright.sync_api import sync_playwright

with sync_playwright() as p1:
    browser = p1.firefox.launch(headless=False)
    context = browser.new_context()

    page1 = context.new_page()
    page1.goto("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
    page1.locator("#name").fill("Naima")

    page1.locator("//input[@id='gender']").click()

    page1.locator("#hobbies").click()
    sleep(3)
    page2=context.new_page()
    page2.goto("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
    allUrls=page2.locator("a").all()
    for url in allUrls:
        print(url.get_attribute("href"))
    # page2.close()
    # sleep(3)
    # page1.close()
    browser.close()