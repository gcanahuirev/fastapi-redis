from redismq import queue_push, Redis
from random import choices
from json import loads
from os import environ

# Integrated process
def process_num(message_json: str):
    print("--- Job processing started ---")
    message = loads(message_json)
    a = message['lowest']
    b = message['highest']
    if (a>b): print("The lowest number is greater than the highest number")
    while a<=b:
        print("{}\n".format(a))
        a=a+1
    print("--- Processed successfully ---")

# Isolated process
def process_msg(db: Redis, message_json: str):
    print("--- Job processing started ---")
    message = loads(message_json)
    print(f"Message received: id={message['id']}, msg_num={message['data']['msg_num']}")

    # Simulate processing error
    processed_ok = choices((True, False), weights=(5, 1), k=1)[0]
    if processed_ok:
        print(f"\tProcessed successfully")
    else:
        print(f"\tProcessing failed - requeuing...")
        queue_push(db, message_json, environ["REDIS_QUEUE_MSG"])