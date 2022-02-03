import asyncio
from fastapi import FastAPI, Response, status
from models.dbinfo import Info, Payload
from config.db import conn
from schemas.schema import serializetoDict, serializetoList
from bson import ObjectId
from collections import deque


app = FastAPI()
consumer_queue = deque()  

@app.get("/")
async def hi():
    message = "Hi from test API"
    return {message}


async def consume_queue(payload):
    objId = payload["unique_identifier"]
    await asyncio.sleep(10)
    # Find the object and update if found
    conn.local.user.find_one_and_update({"_id": ObjectId(objId)}, {
        "$set": dict(Info(number1=payload["number1"], number2=payload["number2"], answer=payload["number1"] + payload["number2"]))
    })
    # Remove from queue when processed
    consumer_queue.popleft()


@app.get("/calculate/number1/number2")
async def calculate(number1: int, number2: int, payload: Payload):
    # Build object to insert in MongoDB
    info = Info(number1=number1, number2=number2, answer=-1)
    # Insert the info object
    result = conn.local.user.insert_one(dict(info))
    curr_payload = dict(**payload.dict())
    # Add the payload to Queue
    consumer_queue.append(curr_payload)
    # Create async task and execute/consume from queue
    asyncio.create_task(consume_queue(curr_payload))
    return {str(result.inserted_id)}


@app.get("/get_answer/identifier/", status_code=200)
async def answer(id: str, response: Response):
    message = ""
    try:
        obj = dict(conn.local.user.find_one({"_id": ObjectId(id)}))
        answer = int(obj["answer"])
        # Found object but answer not calculated
        if answer == -1:
            message = "Please wait."
        # Found object and answer calculated
        else:
            message = "{}".format(answer)

        return {message}
    except:
        # Not found make status 404
        response.status_code = status.HTTP_404_NOT_FOUND

