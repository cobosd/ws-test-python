from fastapi import FastAPI, Query, HTTPException

app = FastAPI()

# Define the parameters that can be received from the weather station.
ALLOWED_PARAMETERS = {
    "MAC", "dateutc", "winddir", "windspeedmph", "windgustmph", "tempf",
    "hourlyrainin", "dailyrainin", "weeklyrainin", "monthlyrainin",
    "yearlyrainin", "totalrainin", "baromrelin", "baromabsin", "humidity",
    "tempinf", "humidityin", "uv", "solarradiation"
}

@app.post("/weather_data/")
def receive_data(**data: str):
    # Validate that all keys in the data are allowed
    for key in data.keys():
        if key not in ALLOWED_PARAMETERS:
            raise HTTPException(status_code=400, detail=f"Invalid parameter: {key}")

    # TODO: Process the data as required
    # For now, we just return the received data
    return data

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=80)
