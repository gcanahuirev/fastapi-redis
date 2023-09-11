from job import process_msg
from os import environ

import redismq

def main():
    """
    Consumes items from the redis queue
    """
    print("The consumer is working...")
    # Connect to Redis
    db = redismq.redis_db()

    while True:
        try:
            # This blocks until an item is received
            message_json = redismq.queue_pop(db, environ["REDIS_QUEUE_MSG"])
            process_msg(db, message_json)
        except KeyboardInterrupt:
            print("The consumer is not working!!!")
            break

if __name__ == '__main__':
    main()
