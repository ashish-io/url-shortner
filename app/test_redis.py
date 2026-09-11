import asyncio
import redis.asyncio as redis  # note: different import than before

async def main():
    r = redis.Redis(host="localhost", port=6379, decode_responses=True)

    await r.set("greeting", "hello from async python")
    value = await r.get("greeting")

    print(value)

    await r.aclose()  # close the connection cleanly

asyncio.run(main())
