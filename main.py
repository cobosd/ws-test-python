import datetime
from typing import List
from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

class WeatherDataItem(BaseModel):
    macAddress: str
    lastData: dict
    info: dict

@app.post("/latest/weather_data")
def receive_data(data: List[WeatherDataItem]):
    # TODO: Process the data as required
    # For now, we just return the received data
    return data

@app.get("/time")
def get_time():
    return {"time": current_time}

@app.get("/get/latest")
def get_time():

    # Define the URL of the server
    url = "http://127.0.0.1:3000/weather/report"

    try:
        # Send a GET request to the server
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse and print the response content
            data = response.json()  # Assuming the server returns JSON data
            print("Weather Report:")
            print(data)
            return data
        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=3001)
