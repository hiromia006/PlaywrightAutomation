from time import sleep

from playwright.sync_api import sync_playwright

with sync_playwright() as p1:
    browser = p1.firefox.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
    page.locator("#name").fill("Naima")
    page.locator("#dob").fill("2026-08-24")
    page.locator("//input[@id='gender']").click()

    page.locator("#hobbies").click()
    sleep(2)
    page.locator("//input[@id='picture']").set_input_files("/home/jannat-mugdho/Pictures/Playwright Terminal Commands Cheat Sheet.jpeg")
    page.select_option("//select[@id='state']", index=2)
    page.select_option("//select[@id='state']", label="Rajasthan")
    sleep(2)

    page.select_option("//select[@id='city']", "Lucknow")
    sleep(2)

    browser.close()
