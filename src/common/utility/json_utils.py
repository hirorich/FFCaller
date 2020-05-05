# ==================================================
# json共通部品
# ==================================================

# jsonを扱う
import json

# String -> dict
def decode(json_string):
    return json.loads(json_string)

# dict -> String
def encode(json_dict):
    return json.dumps(json_dict, ensure_ascii=False)

