import json

def validate(message):
    if isinstance(message, int) or \
        isinstance(message, float) or \
        isinstance(message, dict):
        raise ValueError("Value error")
    request = json.loads(message)
    return request