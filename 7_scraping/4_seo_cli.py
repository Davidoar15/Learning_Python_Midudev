import requests
import argparse
from bs4 import BeautifulSoup

argparse_description = "Web scraping to check SEO for a given URL"
parser_help = "The URL of the site you want to scrape and check"

parser = argparse.ArgumentParser(description=argparse_description)
parser.add_argument('url', type=str, help=parser_help)

args = parser.parse_args()
url = args.url

response = requests.get(url)
if response.status_code == 200:
    print("REQUEST SUCCESSFUL")
    soup = BeautifulSoup(response.text, 'html.parser')
    #print(soup.prettify)
    print(f"Checking URL: { url }")
    print("\n Basic SEO")

    web_title = soup.title.string
    if web_title:
        print(f"Website title: { web_title }")
        if len(web_title) < 70:
            print("The website title is of an appropriate length")
        else: print("The website title is too long")

    titles = [title.string for title in soup.find_all('h2')]
    if not titles:
        print("No 'h1' headings were found on the page X")
    elif len(titles) > 1:
        print("There are more of one title 'h1' on the page X")
        for title in titles:
            print(title)
    else: print(f"There are ONE title 'h1' on the page! { titles }")

#def scrape_url(url: str):
