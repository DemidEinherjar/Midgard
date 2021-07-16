import multiprocessing

import requests
from multiprocessing import Pool

def handler(proxy):
    link = 'http://icanhazip.com/'
    proxies = {
        'http': f'http://{proxy}',
        'https': f'http://{proxy}'
    }
    try:
        responce = requests.get(link, proxies=proxies, timeout=2).text
        print(f'IP:{responce.strip()}')
    except:
        print('Proxy is not valid!')


with open('proxy') as file:
    proxy_base = ''.join(file.readlines()).strip().split('\n')
if __name__ == '__main__':
    with multiprocessing.Pool(multiprocessing.cpu_count()) as process:
        process.map(handler, proxy_base)



