import asyncio     # асинхронный подход использует один поток для параллельных задач (зародился в python 3.4)


async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(1)  # await другие корутины (функции) могут использовать ресурсы на выполнение задач


async def print_letters():
    for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
        print(letter)
        await asyncio.sleep(0.7)  # await если кому-то надо, пользуйтесь ресурсами пока жду


async def main():
    task1 = asyncio.create_task(print_numbers())
    task2 = asyncio.create_task(print_letters())
    await task1
    await task2


asyncio.run(main())  # создается цикл событий
