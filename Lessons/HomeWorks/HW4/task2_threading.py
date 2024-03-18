import urllib.request
import threading
import time

urls = ['https://u4help.ru/photo/photo1.jpg',
        'https://u4help.ru/photo/photo_2.jpg',
        'https://u4help.ru/photo/photo_3.jpg',
        'https://u4help.ru/photo/photo_4.jpg',
        'https://u4help.ru/photo/photo_5.jpg',
        ]


def download(url):
    filename = url.split('/')[-1]
    urllib.request.urlretrieve(url, filename)
    print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")


print(" *** Многопоточный подход *** ")
threads = []
start_time = time.time()

for url in urls:
    thread = threading.Thread(target=download, args=[url])
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
