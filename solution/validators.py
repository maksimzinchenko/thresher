import json

MAX_FACTORIAL_VALUE = 150000

def validate(message):
    if isinstance(message, int) or \
        isinstance(message, float) or \
        isinstance(message, dict):
        raise ValueError("Value error")
    request = json.loads(message)
    if ("number" in request.keys()) and (not isinstance(request["number"], int)):
        raise ValueError("Value error")
        raise ValueError("Value error")
    if ("number" in request.keys()) and (request["number"] > 150000):
        raise ValueError("Value error")
    if ("task_id" in request.keys()) and (not isinstance(request["number"], str)):
        raise ValueError("Value error")
    return request