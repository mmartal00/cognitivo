import requests
from pprint import pprint

skey = 'fa5d8e166b8444c082e139694ae140b7'
endpoint = 'https://southcentralus.api.cognitive.microsoft.com/'
vision_url = endpoint + "/vision/v3.2/analyze?visualFeatures=Faces&details=Landmarks"

documents ={
    "url":"https://m0.her.ie/wp-content/uploads/2014/08/bswovofmmnbuf7anqmvf.jpg"
}

_headers = {"Ocp-Apim-Subscription-Key": skey}
_response=requests.post(vision_url, headers=_headers, json=documents)
rostros = _response.json()

pprint(rostros)


for rostro in rostros['faces']:
    pprint(rostro)
