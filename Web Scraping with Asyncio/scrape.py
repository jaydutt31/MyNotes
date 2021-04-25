import asyncio 
import time



iteration_times = [1,3,2,4]

def sleeper(seconds, i=-1):
	if i != -1:
		print(f"{i}\t{seconds}s")
	time.sleep(seconds)

def run():
	for i, seconds in enumerate(iteration_times):
		sleeper(seonds, i = i)

async def a_sleeper(seconds, i=-1):
	if i != -1:
		print(f"{i}\t{seconds}s")
	await asyncio.sleep(seconds)
	return "abc"

async def a_run():
	for i, seconds in enumerate(iteration_times):
		await (a_sleeper(seconds, i =1))
		data = await asyncio.wait_for(a_run(), timeout=10)
		print(data)

asyncio.run(a_run())
#data = asyncio.wait_for(a_run(), timeout=10)
