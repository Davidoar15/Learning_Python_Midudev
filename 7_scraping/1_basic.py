import requests, re

# * Requests
# ! contras: 
    # - Cannot bypass paywalls or captchas
    # - Cannot navegate
    # - Very manual
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


# * 
