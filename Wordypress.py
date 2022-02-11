from playwright.sync_api import sync_playwright
import json

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # login
    page.goto("https://wordpress.com/")
    page.click("text=Log In")
    page.fill('input[name="usernameOrEmail"]', "testinggoentri")
    page.click('text=Continue')
    page.fill('input[name="password"]', 'G0Entri!123!')
    page.click('button:has-text("Log In")')

    # wait for page to load
    page.locator('h1:has-text("My Home")').wait_for()

    # grab content
    # the page title here contains the title, tagline and domain, normally I'd access the domain based on the url
    title_line = page.title() 
    title, tag_domain = title_line.split('‹')
    tagline, domain = tag_domain.split('—')

    # write content to file to save for later
    with open('pressyInfo.json', 'w') as f:
        f.write(json.dumps({'title': title.strip(), 'tagline': tagline.strip(), 'domain': domain.strip()}))