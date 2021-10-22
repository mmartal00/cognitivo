import requests
from pprint import pprint

skey = 'fa5d8e166b8444c082e139694ae140b7'
endpoint = 'https://southcentralus.api.cognitive.microsoft.com/'
vision_url = endpoint + "/vision/v3.2/analyze?visualFeatures=Faces"

documents ={
    "url":"https://www.nombres.pro/wp-content/uploads/2015/10/Nombre-para-grupos-de-amigos.jpg"
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

tot_hombres = 0
tot_mujeres = 0

tot_edad = 0

for rostro in rostros['faces']:
    rostro['gender']
    rostro['age']

    if (rostro['gender'] == 'Male'):
        tot_hombres += 1
    else:
        tot_mujeres += 1

print(tot_hombres)
print(tot_mujeres)

for rostro in rostros['faces']:
    tot_edad = tot_edad + rostro['age']

prom_edad = tot_edad / len(rostros['faces'])

print(int(prom_edad))
