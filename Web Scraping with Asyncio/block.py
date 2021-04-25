
import asyncio, pprint, time

async def asleeper(seconds):
	start = time.time()
	print(f"a\t{seconds}s")
	print("hello")
	await asyncio.sleep(seconds)
	end = time.time() - start
	print(f"done : {end}")


#asyncio.run(asleeper(12))
#print("hello world")

loop = asyncio.get_event_loop()

done, pending = loop.run_until_complete(asyncio.wait([
	asleeper(5), asleeper(6), asleeper(7), asleeper(8), asleeper(9), asleeper(10)
	]))

print(done, pending)




'''


import asyncio
import random


async def coro(tag):
    print(">", tag)
    await asyncio.sleep(random.uniform(0.5, 5))
    print("<", tag)
    return tag


loop = asyncio.get_event_loop()

tasks = [coro(i) for i in range(1, 11)]

print("Get first result:")
finished, unfinished = loop.run_until_complete(
    asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED))

for task in finished:
    print(task.result())
print("unfinished:", len(unfinished))

print("Get more results in 2 seconds:")
finished2, unfinished2 = loop.run_until_complete(
    asyncio.wait(unfinished, timeout=2))

for task in finished2:
    print(task.result())
print("unfinished2:", len(unfinished2))

print("Get all other results:")
finished3, unfinished3 = loop.run_until_complete(asyncio.wait(unfinished2))

for task in finished3:
    print(task.result())

loop.close()
'''

