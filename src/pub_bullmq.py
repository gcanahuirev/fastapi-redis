from bullmq import Queue
from os import environ

import asyncio

async def main():
    queue = Queue(
        environ["BULLMQ_QUEUE_PUB"],
        {
            "host": environ["REDIS_HOST"],
            "port": int(environ["REDIS_PORT"]),
            "db": int(environ["REDIS_DB_NUMBER"]),
            "password": environ["REDIS_PASSWORD"],
        },
        {
            "prefix": "bull"
        }
    )
    # Add a job with data { "foo": "bar" } to the queue
    await queue.add("job_test", {"foo": "bar2"})

    # Close when done adding jobs
    await queue.close()

if __name__ == "__main__":
    asyncio.run(main())