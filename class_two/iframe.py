from asyncio import sleep

from playwright.sync_api import sync_playwright

with sync_playwright() as p1:
    browser = p1.firefox.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.tutorialspoint.com/selenium/practice/frames.php")

    print(page.title())

    framTxt = page.frame_locator("iframe[src='new-tab-sample.php']").first.locator(
        "a[class='external-link']").text_content()
    print(framTxt)

    browser.close()

