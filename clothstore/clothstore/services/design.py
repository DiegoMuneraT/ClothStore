import requests
import json

class ShirtDesign():
    def getDesign(self, pk):
        request = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pk}/")
        data = json.loads(request.content)
        return(data["sprites"]["other"]["official-artwork"]["front_default"])