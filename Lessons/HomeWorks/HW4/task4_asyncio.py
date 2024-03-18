import asyncio
import aiohttp
import time
import urllib.request   # В асинхронном подходе с urllib возникли трудности. Использовал классику.

urls = ['https://u4help.ru/photo/photo1.jpg',
        'https://u4help.ru/photo/photo_2.jpg',
        'https://u4help.ru/photo/photo_3.jpg',
        'https://u4help.ru/photo/photo_4.jpg',
        'https://u4help.ru/photo/photo_5.jpg',
        ]


async def download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            filename = url.split('/')[-1]
            with open(filename, 'wb') as f:
                f.write(await response.read())
            print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")


async def main():
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(download(url))
        tasks.append(task)
    await asyncio.gather(*tasks)

print(" *** Асинхронный подход *** ")
start_time = time.time()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
