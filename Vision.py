import requests
from pprint import pprint

skey = 'fa5d8e166b8444c082e139694ae140b7'
endpoint = 'https://southcentralus.api.cognitive.microsoft.com/'
vision_url = endpoint + "/vision/v3.2/analyze?visualFeatures=Faces&details=Landmarks"

documents ={
    "url":"https://clutchpoints.com/wp-content/uploads/2020/07/NBA-legends-best-final-games.jpg"
}

_headers = {"Ocp-Apim-Subscription-Key": skey}
_response=requests.post(vision_url, headers=_headers, json=documents)
rostros = _response.json()

# pprint(rostros)
# print(rostros['faces'][0]['age'])
# print(rostros['faces'][0]['gender'])

# print(rostros['faces'][1]['age'])
# print(rostros['faces'][1]['gender'])

# print(rostros['faces'][2]['age'])
# print(rostros['faces'][2]['gender'])

for rostro in rostros['faces']:
    pprint(rostro)
    print(rostro['age'])
    print(rostro['gender'])