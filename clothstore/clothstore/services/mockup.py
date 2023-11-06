from os import environ
import requests
import json

api_key = "a8fc8571-8e54-4151-9382-9c753118c972"

#api_key = environ.get('API_KEY_MOCKUP')

class ShirtMockup():
    def defaultShirt(self, image):
        nr = 520
        url = "https://api.mediamodifier.com/v2/mockup/render"
        #image placeholder
        #image = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/197.png"

        payload = {
            "nr": nr,
            "layer_inputs": [
                {
                    "id": "juqu6evm8k4dtcu835p",
                    "data": image,
                    "checked": True
                }
            ]
        }
        headers = {
            "api_key": api_key,
            "Content-Type": "application/json",
            "Accept": "application/json"
            } 

        response = requests.post(url, json=payload, headers=headers)
        image_url = json.loads(response.content)
        return image_url.get("url")