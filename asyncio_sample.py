import asyncio

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def do():
    await asyncio.gather(say_after(2,"Hello"), say_after(1,"World"))

print("Going to print!")
asyncio.run(do())
