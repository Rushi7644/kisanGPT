import json

with open("offline_data.json", "r") as f:
    OFFLINE_DATA = json.load(f)

def get_offline_answer(query):
    query = query.lower()
    for key in OFFLINE_DATA:
        if key in query:
            return OFFLINE_DATA[key]
    return None
