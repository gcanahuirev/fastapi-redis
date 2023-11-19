from bullmq import Worker, Job
from datetime import datetime
from json import dumps
from os import environ

import asyncio

async def process(job: Job, token: str):
    date = datetime.fromtimestamp(job.timestamp/1000).strftime('%Y-%m-%d %H:%M:%S')
    new_job = {
        "id": job.id,
        "name": job.name,
        "data": job.data,
        "token": token,
        "date": date,
    }
    result = dumps(new_job, indent=2)
    print(result)
    await asyncio.sleep(2)
    return "done"

async def main():
    # Feel free to remove the connection parameter, if your redis runs on localhost
    worker = Worker(
        environ["BULLMQ_QUEUE_SUB"],
        process, # type: ignore
        {
            "connection": {
                "host": environ["REDIS_HOST"],
                "port": int(environ["REDIS_PORT"]),
                "db": int(environ["REDIS_DB_NUMBER"]),
                "password": environ["REDIS_PASSWORD"],
            },
            "prefix": "bull"
        }
    )

    # This while loop is just for the sake of this example
    # you won't need it in practice.
    while True: # Add some breaking conditions here
        await asyncio.sleep(1)

    # When no need to process more jobs we should close the worker
    await worker.close()

if __name__ == "__main__":
    asyncio.run(main())