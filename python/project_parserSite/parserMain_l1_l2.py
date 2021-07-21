import requests
#import fake_useragent
from bs4 import BeautifulSoup

link = 'https://browser-info.ru/'
#user = fake_useragent.UserAgent().random
#header = {'user-agent': user}
responce = requests.get(link, headers = header).text

#JS
soup = BeautifulSoup(responce, 'lxml')
block = soup.find('div', id ="tool_padding")
check_js = block.find('div', id = 'javascript_check')
status_js = check_js.find_all('span')[1].text
result_js = f'jacascript: {status_js}'

#Flash
check_flash = block.find('div', id = 'flash_version')
status_flash = check_flash.find_all('span')[1].text
result_flash = f'flash: {status_flash}'

#User-agent
check_ua = block.find('div', id = 'user_agent').text

print(result_js, result_flash, check_ua)
