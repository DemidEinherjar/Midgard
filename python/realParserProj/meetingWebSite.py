import requests
from bs4 import BeautifulSoup

storage_number = 0

link = 'https://beboo.ru/znakomstva/moscow?iaS=0&status=all&countryId=104&regionId=-1&townId=-1&lookFor=1&reason=0&endAge=30&startAge=18'

header = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36'
}

#try:
for storage in range(1, 5):
    responce = requests.get(f'{link}&page={storage}/', headers=header).text
    soup = BeautifulSoup(responce, 'lxml')
    block = soup.find('div', class_='box-wrap')
    devushki = block.find_all('div', class_='user-profile').text
    for i in devushki:
        print(i)
#except:
#    print('Страницы закончились!')