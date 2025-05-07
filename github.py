# Serialization: Convert object in Python to bytes & back
# Formats: JSON, YAML, CSV, TOML, Protocol buffers, XML, ...

# Types: JSON <-> Python
# null <-> None
# string <-> str
# true/false <-> True/False (bool)
# number <-> int, float (complex, ...)
# array <-> list
# object <-> dict
# MIA:
# str (2025-05-07T18:57:14), int (seconds since epoch) <-> datetime
# str (base64 encoding) <-> bytes
# comments

# json module API
# loads, dumps: str/bytes
# load, dump: file like objects
# load: JSON -> Python
# dump: Python -> JSON
import json

event = {
    'action': 'start',
    'image': 'ubuntu',
    'count': 1,
    'tags': ['qa', 'us-1']
}  # fmt: off

data = json.dumps(event)
print(data)
# data['image']  # error: data is a str
print('data type:', type(data))

event2 = json.loads(data)
print(event2['image'])
