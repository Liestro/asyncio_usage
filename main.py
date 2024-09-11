import asyncio
import time

async def one_sec_sleep():
    print("start one_sec_sleep")
    await asyncio.sleep(1)
    print("end one_sec_sleep")

async def two_sec_sleep():
    print("start two_sec_sleep")
    await asyncio.sleep(2)
    print("end two_sec_sleep")

async def three_sec_sleep():
    print("start three_sec_sleep")
    await asyncio.sleep(3)
    print("end three_sec_sleep")

async def main():
    tasks = [asyncio.create_task(one_sec_sleep()),
             asyncio.create_task(two_sec_sleep()),
             asyncio.create_task(three_sec_sleep())]
    
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    print(time.time() - start)