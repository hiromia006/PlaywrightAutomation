from time import sleep

from playwright.sync_api import sync_playwright

with sync_playwright() as page2:
    page = page2.firefox.launch(headless=False).new_page()
    page.goto("https://www.tutorialspoint.com/selenium/practice/alerts.php")
    print("Alert page opened")
    page.locator("//button[normalize-space()='Alert']").wait_for(5).click()
    sleep(2)
    page.on("dialog", lambda dialog: dialog.accept())
    print("Alert accepted")
    sleep(2)

    page.locator("//button[@onclick='myDesk()']").click()
    print("Alert page opened")
    sleep(2)
    page.on("dialog", lambda dialog: dialog.dismiss)
    print("Alert dismissed")
    sleep(2)

    page.locator("button[onclick='myPromp()']").click()
    print("Alert page opened")
    print("Alert text is : ", page.on("dialog", lambda dialog: dialog.message))
    page.on("dialog", lambda dialog: dialog.accept("Naima"))
    print("Alert accepted with input")



    page.close()
