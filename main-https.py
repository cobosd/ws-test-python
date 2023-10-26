from flask import Flask, request, jsonify
from flask_talisman import Talisman

app = Flask(__name__)
talisman = Talisman(app)


# Define the parameters that can be received from the weather station.
ALLOWED_PARAMETERS = {
    "MAC", "dateutc", "winddir", "windspeedmph", "windgustmph", "tempf",
    "hourlyrainin", "dailyrainin", "weeklyrainin", "monthlyrainin",
    "yearlyrainin", "totalrainin", "baromrelin", "baromabsin", "humidity",
    "tempinf", "humidityin", "uv", "solarradiation"
}

@app.route('/weather_data', methods=['POST'])
def receive_data():
    # Extract parameters from the request
    data = request.args

    # Validate that all keys in the data are allowed
    for key in data.keys():
        if key not in ALLOWED_PARAMETERS:
            return jsonify({"error": f"Invalid parameter: {key}"}), 400

    # TODO: Process the data as required
    # For now, we just return the received data
    return jsonify(data)

if __name__ == '__main__':
    app.run(port=80)