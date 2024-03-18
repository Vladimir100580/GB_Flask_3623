import time
import urllib.request

# Использовал свой домен, предварительно загрузив на сервер несколько фоток
urls = ['https://u4help.ru/photo/photo1.jpg',
        'https://u4help.ru/photo/photo_2.jpg',
        'https://u4help.ru/photo/photo_3.jpg',
        'https://u4help.ru/photo/photo_4.jpg',
        'https://u4help.ru/photo/photo_5.jpg',
        ]

print(" *** Синхронный подход *** ")
start_time = time.time()

for url in urls:
    filename = url.split('/')[-1]
    urllib.request.urlretrieve(url, filename)
    print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")
