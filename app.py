"""This code defines a simple Flask application that can be used to manage surf competitions. The application exposes two endpoints:

/events: This endpoint can be used to get a list of all events, or to create a new event.
/competitors: This endpoint can be used to get a list of all competitors, or to create a new competitor.
The application uses a JSON file to store the data about events and competitors. The JSON file is opened and closed in each endpoint function, so that the data is always up-to-date."""

import json
from flask import Flask, request

app = Flask(__name__)

@app.route("/events", methods=["GET", "POST"])
def events():
    if request.method == "GET":
        # Get all events
        events = []
        with open("events.json", "r") as f:
            events = json.load(f)
        return json.dumps(events)
    elif request.method == "POST":
        # Create a new event
        data = request.get_json()
        event = {
            "name": data["name"],
            "date": data["date"],
            "location": data["location"],
            "type": data["type"]
        }
        with open("events.json", "w") as f:
            json.dump(events + [event], f)
        return "Event created"

@app.route("/competitors", methods=["GET", "POST"])
def competitors():
    if request.method == "GET":
        # Get all competitors
        competitors = []
        with open("competitors.json", "r") as f:
            competitors = json.load(f)
        return json.dumps(competitors)
    elif request.method == "POST":
        # Create a new competitor
        data = request.get_json()
        competitor = {
            "name": data["name"],
            "age": data["age"],
            "surfing_experience": data["surfing_experience"]
        }
        with open("competitors.json", "w") as f:
            json.dump(competitors + [competitor], f)
        return "Competitor created"

if __name__ == "__main__":
    app.run(debug=True)
