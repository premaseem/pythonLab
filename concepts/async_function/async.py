import time
import asyncio


def is_prime(x):

    return not any(x//i == x/i for i in range(x-1, 1, -1))


async def highest_prime_below(x):

    print('Highest prime below %d' % x)
    for y in range(x-1, 0, -1):
        if is_prime(y):
            print('→ Highest prime below %d is %d' % (x, y))
            return y
        await asyncio.sleep(0.01)
    return None


async def main():

    t0 = time.time()

    # a blocking call
    # await highest_prime_below(100000)
    # await highest_prime_below(10000)
    # await highest_prime_below(1000)

    # Non Blocking call
    await asyncio.wait( [
        highest_prime_below(100000),
        highest_prime_below(10000),
        highest_prime_below(1000)
    ] )
    t1 = time.time()
    print("took {:.2f} ms".format(1000*(t1-t0)))

# main()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
# loop.close()