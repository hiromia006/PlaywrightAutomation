from time import sleep

from playwright.sync_api import sync_playwright

with sync_playwright() as abc:
    brower = abc.firefox.launch(headless=False)
    page = brower.new_page()
    page.goto("https://google.com")
    sleep(3)
    page.goto("https://yahoo.com")
    sleep(3)
    page.go_back()
    sleep(3)
    page.go_forward()
    sleep(3)
    page.reload()
    sleep(3)
    print("Current Page URL: ", page.url)
    page.close()
