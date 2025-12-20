import requests, re

# * Requests (STATIC)
# ! contras: 
    # - Cannot bypass paywalls or captchas
    # - Cannot navigate
    # - Very manual
    # - It does not work with SPAs
# ? pros: 
    # + Very fast
    # + Very easy to implement

url = 'https://davidoar15.github.io/Portfolio/'
response = requests.get(url)
if response.status_code == 200:
    print("REQUEST SUCCESSFUL")
    html = response.text
    if html: 
        title_pattern = r'<title>(.*?)</title>'
        match = re.search(title_pattern, html)
        if match: print(f"{ match.group(1)}")
    else: print("ERROR")
