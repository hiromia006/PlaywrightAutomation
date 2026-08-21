from time import sleep

from playwright.sync_api import sync_playwright

with sync_playwright() as abc:
    browser = abc.firefox.launch(headless=False)
    # browser = abc.firefox.launch()
    page = browser.new_page()
    page.goto("https://playwright.dev/")
    sleep(3)
    print(page.title())

    browser.close()
