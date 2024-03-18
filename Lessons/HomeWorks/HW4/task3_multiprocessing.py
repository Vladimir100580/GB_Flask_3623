from multiprocessing import Process
import urllib.request
import time

urls = ['https://u4help.ru/photo/photo1.jpg',
        'https://u4help.ru/photo/photo_2.jpg',
        'https://u4help.ru/photo/photo_3.jpg',
        'https://u4help.ru/photo/photo_4.jpg',
        'https://u4help.ru/photo/photo_5.jpg',
        ]


def download(url):
    filename = url.split('/')[-1] + '.jpg'
    urllib.request.urlretrieve(url, filename)
    print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")


print(" *** Многопроцессорный подход *** ")
processes = []
start_time = time.time()

if __name__ == '__main__':
    for url in urls:
        process = Process(target=download, args=(url,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
