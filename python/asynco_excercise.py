import asyncio
import time
start_time = time.time()


async def print_Exercise():
    await asyncio.sleep(2)
    print("Python Exercises!")


# async def main():
#     await print_Exercise()
#
# asyncio.run(main())

async def name1():
    await asyncio.sleep(1)
    print("Tinsae")


async def name2():
    await asyncio.sleep(2)
    print("Getachew")


async def name3():
    await asyncio.sleep(3)
    print("Kebede")


# async def main():
#     # await name1()
#     # await name2()
#     # await name3()
#
#     task = [
#         name2(),
#         name1(),
#         name3()
#     ]
#
#     await asyncio.gather(*task)
#
#
# asyncio.run(main())


async def run_loop():
    for n in range(1,8):
        await asyncio.sleep(1)
        print(n)


async def main():
    await run_loop()

asyncio.run(main())
end_time = time.time()
print(end_time-start_time)