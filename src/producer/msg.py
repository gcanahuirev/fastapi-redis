from datetime import datetime
from json import dumps
from time import sleep
from uuid import uuid4
from os import environ

import redismq
import random

def main(num_msg: int, delay: float = 1):
    """
    Publisher items for the Redis queue
    """
    # Connect to Redis
    db = redismq.redis_db()

    for i in range(num_msg):
        message = {
            "id": str(uuid4()),
            "ts": datetime.utcnow().isoformat(),
            "data": {
                "msg_num": i,
                "x": random.randrange(0, 100),
                "y": random.randrange(0, 100),
            },
        }

        message_json = dumps(message)

        print(f"Sending message {i+1} (id={message['id']})")
        redismq.queue_push(db, message_json, environ["REDIS_QUEUE_MSG"])

        sleep(delay)

if __name__ == "__main__":
    main(10, 1)