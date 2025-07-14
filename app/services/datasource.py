import json
import os

def load_data():
    path = os.path.join(os.path.dirname(__file__), "..", "data", "info.json")
    with open(path, "r") as file:
        return json.load(file)

DATA = load_data()
