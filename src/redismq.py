from redis import Redis
from os import environ

def redis_db():
    db = Redis(
        host=environ["REDIS_HOST"],
        port=int(environ["REDIS_PORT"]),
        db=int(environ["REDIS_DB_NUMBER"]),
        password=environ["REDIS_PASSWORD"],
        decode_responses=True
    )

    # Make sure redis is up and running
    db.ping()
    return db

def queue_push(db: Redis, message, queue: str ):
    # Push to tail of the queue (left of the list)
    current_list_size = db.lpush(queue, message)
    return current_list_size

def queue_pop(db: Redis, queue: str):
    # Pop from head of the queue (right of the list)
    # The `b` in `brpop` indicates this is a blocking call (waits until an item becomes available)
    _, message_json = db.brpop(queue)
    return message_json
