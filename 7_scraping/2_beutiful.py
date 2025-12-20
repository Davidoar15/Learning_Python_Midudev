from bs4 import BeautifulSoup
import requests

# * Beautiful Soup (STATIC)
# ! contras: 
    # - Cannot bypass paywalls or captchas
    # - Very difficult to navigate
    # - It does not work with SPAs
# ? pros: 
    # + Fast
    # + Very easy to implement
    # + Easy find and filter elems, atributtes

url = 'https://davidoar15.github.io/Portfolio/'
response = requests.get(url)
if response.status_code == 200:
    print("REQUEST SUCCESSFUL")
    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup.prettify)
    
    title_tag = soup.title
    if title_tag:
        # print(f"Web Title is: { title_tag.string }")
        print(f"Web Title is: { title_tag.text }")
    
    metas = soup.title.parent.find_all('link')
    print(metas)

    icon_link = soup.find('link', rel="icon")
    if icon_link:
        print(f"Icon: { icon_link }")
else: print("ERROR")