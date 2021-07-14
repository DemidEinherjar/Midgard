import requests
from bs4 import BeautifulSoup
session = requests.Session()

link = 'https://airsoftsamara.ru/ucp.php?mode=login'

header = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36'
}

data = {
    'username': 'demid',
    'password': 'Qwe12345'
}

responce = session.post(link, data=data, headers=header).text

profile_info = 'https://airsoftsamara.ru/memberlist.php?mode=viewprofile&u=3910'
profile_responce = session.get(profile_info, headers=header).text

cookies_dict = [
    {'domain': key.domain, 'name':  key.name, 'path': key.path, 'value': key.value}
    for key in session.cookies
]

session2 = requests.Session()

for cookies in cookies_dict:
    session2.cookies.set(**cookies)

resp = session2.get(profile_info, headers=header)
print(resp.text)