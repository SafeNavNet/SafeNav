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

data = requests.post('http://route.arcgis.com/arcgis/rest/services/World/Route/NAServer/Route_World/solve?stops=-117.1957,34.0564; -117.184,34.0546', params={
  'f': 'json',
  'token': token.json()['access_token'],
  'studyAreas': '[{"geometry":{"x":-117.1956,"y":34.0572}}]'
})

print(data.json())
