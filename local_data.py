from fastapi import FastAPI
import redis
import uvicorn
import os

data={}

#Data base stroring Trafic details
redis_host = ""
redis_port = "6379"
r = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)

app = FastAPI()

#Return Local trafic details
@app.get("/road_side")
async def send_trafic_details():
    global data
    keys = r.keys("*")
    for item in keys:
        data[item] = r.get(item)
    print(f"local area indication: {data}")
    return data

@app.post("/init")
async def set_service_endpoint(data: dict):
    global redis_host, r
    redis_host = data["db_endpoint"]
    r = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)

    print(f"Endpoints initialisation Done")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
    print("server running")