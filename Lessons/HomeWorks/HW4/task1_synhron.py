import time
import urllib.request
import parser


urls = parser.st_parser()

print(" *** Синхронный подход *** ")
start_time = time.time()

for url in urls:
    filename = url.split('/')[-1]
    urllib.request.urlretrieve(url, filename)
    print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")
