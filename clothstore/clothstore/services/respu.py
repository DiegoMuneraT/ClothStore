key = "febGO1ffXYUGaErwspj5aRWnTWHfxsCzJqVU6CVv"

import requests
import json

response = requests.get("https://api.printful.com/mockup-generator/task?task_key=gt-593550195", headers= {'Authorization': f'Bearer {key}'})
data = json.loads(response.content)
print(data)