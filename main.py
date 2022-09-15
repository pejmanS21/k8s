from fastapi import FastAPI, Request
import random
import time


app = FastAPI()

blip_condition = [True, False]


@app.get('/')
def index(request: Request):
    client_host = request.client.host
    client_port = request.client.port
    return {"status": 200, "client_host": client_host, "client_port": client_port}


@app.get("/blip")
def get_blip():
    time.sleep(random.randint(1, 30))
    if random.choice(blip_condition):
        return {"message": "You disappear with Thanos snap!"}
    return {"message": "You survive the Thanos snap!"}
