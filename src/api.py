from pydantic import BaseModel
from fastapi import FastAPI
from os import environ

import redismq

app = FastAPI()

class JobData(BaseModel):
    lowest: int
    highest: int

@app.get("/")
def index():
    return {
        "success": True,
        "message": "pong"
    }

@app.post("/job")
def post_job(job: JobData):
    # Connect to Redis
    db = redismq.redis_db()

    # Publish one item
    message_json = job.model_dump_json()
    job_instance = redismq.queue_push(
        db,
        message_json,
        environ["REDIS_QUEUE_NUM"]
    )
    return {
        "success": True,
        "message": "Current list size: {}".format(job_instance)
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
