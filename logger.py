import json


def log_request(intent_data, message, response):

    log_entry = {
        "intent": intent_data["intent"],
        "confidence": intent_data["confidence"],
        "user_message": message,
        "final_response": response
    }

    with open("route_log.jsonl", "a") as f:
        f.write(json.dumps(log_entry) + "\n")
