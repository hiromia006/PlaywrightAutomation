from time import sleep

from playwright.sync_api import sync_playwright

with sync_playwright() as p1:
    browser = p1.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.tutorialspoint.com/selenium/practice/browser-windows.php")
    sleep(3)

    with context.expect_page() as new_page_info:
        page.locator("//button[@title='New Tab']").click()

    new_tab = new_page_info.value
    new_tab.wait_for_load_state()
    print(new_tab.title())
    print(new_tab.url)
    allUrl = new_tab.locator("a").all()
    for url in allUrl:
        print(url.get_attribute("href"))
    sleep(3)

    browser.close()
