from time import sleep

from playwright.sync_api import sync_playwright

with sync_playwright() as abc:
    browser = abc.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://saucedemo.com/")

    page.locator("//input[@id='user-name']").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    sleep(3)
    page.locator("//input[@id='login-button']").click()
    page.screenshot(path="./screenshot.png")
    sleep(3)
    page.close()