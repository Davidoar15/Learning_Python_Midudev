from playwright.sync_api import sync_playwright
from urllib.parse import urljoin

url = "https://davidoar15.github.io/Portfolio/"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(url)

    first_details_anchor = page.locator('details summary').first
    print(first_details_anchor.text_content())
    first_details_anchor.click()

    # page.wait_for_load_state()
    page.wait_for_selector('details[open]')

    first_image = page.locator('details[open] img').first
    image_src = first_image.get_attribute('src')
    print(f"The first details image is: { image_src }")

    browser.close()

