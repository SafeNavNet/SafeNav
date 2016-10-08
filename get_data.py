import requests

# generate a token with your client id and client secret
token = requests.post('https://www.arcgis.com/sharing/rest/oauth2/token/', 
	params={
  'f': 'json',
  'client_id': 'OYBSyP4UMttEkIlp',
  'client_secret': '65057b2bafcf4e27bde6bcabff2dcc3c',
  'grant_type': 'client_credentials',
  'expiration': '1440'
})

print(token.json()['access_token'])


lat1 = '42.3417707'
long1 = '-83.0601714'
lat2 = '42.3387803'
long2 = '-83.0572124'

coordinates = long1 + "," + lat1 + "; " + long2 + "," + lat2

data = requests.post('http://route.arcgis.com/arcgis/rest/services/World/Route/NAServer/Route_World/solve?stops=' + coordinates, params={

  'f': 'json',
  'token': token.json()['access_token'],
  'studyAreas': '[{"geometry":{"x":-117.1956,"y":34.0572}}]'
})

# Directions is a list
print(data.json()['directions'][0])
print("-----------------------------------------")
# routes is a dictionary
print(data.json()['routes']['features'][0]['geometry']['paths'])
print(data.json().keys())
