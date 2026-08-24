from time import sleep

from playwright.sync_api import sync_playwright

with sync_playwright() as p1:
    browser = p1.firefox.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
    page.wait_for_load_state("networkidle", timeout=50)
    page.locator("#name").wait_for(state="enabled", timeout=50)
    page.locator("#name").fill("Naima")

    page.locator("//input[@id='gender']").click()

    page.locator("#hobbies").wait_for(state="clickable", timeout=50)
    page.locator("#hobbies").click()
    page.locator("#dob").fill("2010-10-10")
    sleep(2)
    page.locator("//input[@id='picture']").set_input_files("/home/jannat-mugdho/Pictures/Playwright Terminal Commands Cheat Sheet.jpeg")

    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    sleep(2)
    page.select_option("//select[@id='state']", index=2)
    page.select_option("//select[@id='state']", label="Rajasthan")
    sleep(2)

    page.select_option("//select[@id='city']", "Lucknow")
    sleep(2)

    browser.close()
