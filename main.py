import requests

site = 'https://petstore.swagger.io/v2'
petId = '111'
api_key = 'afawewea'
body = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

res1 = requests.get(f"{site}/pet/findByStatus", params={'status': 'available'},
                    headers={'accept': 'application/json'})
print(f"Запрос 1 - {res1.text}")

res2 = requests.get(f"{site}/pet/{petId}", headers={'accept': 'application/json'})
print(f"Запрос 2 - {res2.text}")

res3 = requests.post(f"{site}/pet/{petId}", params={'name': 'bob', 'status': 'available'},
                     headers={'accept': 'application/json'})
print(f"Запрос 3 - {res3.text}")

res4 = requests.delete(f"{site}/pet/{petId}")
print(f"Запрос 4 - {res4.text}")

res5 = requests.post(f"{site}/pet/{petId}/uploadImage", headers={'accept': 'application/json'})
print(f"Запрос 5 - {res5.text}")

res6 = requests.post(f"{site}/pet", params={'body': body})
print(f"Запрос 6 - {res6.text}")
