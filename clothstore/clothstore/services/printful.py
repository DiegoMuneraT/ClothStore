key = "febGO1ffXYUGaErwspj5aRWnTWHfxsCzJqVU6CVv"

import requests
import json
import time

#data = json.loads(request.content)
class PrintfulApi():
  def printfulMockup(self, image):
    payload = { 
      "variant_ids": [
        14359
      ],
      "format": "jpg",
      "files": [
        {
          "placement": "front",
          "image_url": image,
          "position": {
            "area_width": 1800,
            "area_height": 2400,
            "width": 1800,
            "height": 1800,
            "top": 300,
            "left": 0
          }
        },
        {
          "placement": "back",
          "image_url": image,
          "position": {
            "area_width": 1800,
            "area_height": 2400,
            "width": 1800,
            "height": 1800,
            "top": 300,
            "left": 0
          }
        }
      ]
    }
    request = requests.post("https://api.printful.com/mockup-generator/create-task/567",json=payload ,headers= {'Authorization': f'Bearer {key}'})
    data = json.loads(request.content)
    print(data)
    #task_key = data["result"][0]
    task_key = data["result"].pop("task_key")
    print(task_key)
    time.sleep(6)
    response = requests.get(f"https://api.printful.com/mockup-generator/task?task_key={task_key}", headers= {'Authorization': f'Bearer {key}'})
    image_url = json.loads(response.content)
    mockups_urls = []
    for mockup in image_url["result"]["mockups"]:
      mockups_urls.append(mockup["mockup_url"])
    return mockups_urls[0]



