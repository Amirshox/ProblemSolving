import asyncio
import time


async def do_work(s: str, delay_s: float = 1.0):
    print(f"{s} started")
    await asyncio.sleep(delay_s)
    print(f"{s} done")


async def main():
    start = time.perf_counter()
    todo = ['get package', 'Laundry', 'bake cake']

    tasks = [asyncio.create_task(do_work(s)) for s in todo]
    done, pending = await asyncio.wait(tasks)

    for task in done:
        print(task.result())

    end = time.perf_counter()
    print(f"finished in {end - start} seconds")


if __name__ == '__main__':
    asyncio.run(main())
