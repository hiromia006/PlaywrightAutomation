from playwright.sync_api import sync_playwright

with sync_playwright() as playwright1:
    br=playwright1.firefox.launch(headless=False)
    page=br.new_page()
    page.goto("https://parabank.parasoft.com/parabank/")
    text=page.locator("a[href='lookup.htm']").text_content()
    print("text_content : ", text)

    page.goto("https://saucedemo.com/")
    att= page.locator("#login-button").get_attribute("class")
    print("attribute : ", att)
    page.close()


