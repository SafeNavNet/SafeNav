import requests


class Path:
    def get_data(lat1, long1, lat2, long2):
        # generate a token with your client id and client secret
        # print(token.json()['access_token'])
        token = Path.gen_token()
        coordinates = long1 + "," + lat1 + "; " + long2 + "," + lat2

        data = requests.post('http://route.arcgis.com/arcgis/rest/services/World/Route/NAServer/Route_World/solve?stops=' + coordinates, params={
            'f': 'json',
            'token': token.json()['access_token'],
            'studyAreas': '[{"geometry":{"x":-117.1956,"y":34.0572}}]'
        })
        return data.json()['routes']['features'][0]['geometry']['paths'][0]

    def gen_token():
        token = requests.post('https://www.arcgis.com/sharing/rest/oauth2/token/', params={
            'f': 'json',
            'client_id': 'OYBSyP4UMttEkIlp',
            'client_secret': '65057b2bafcf4e27bde6bcabff2dcc3c',
            'grant_type': 'client_credentials',
            'expiration': '1440'
        })
        return token

    def filter_path(path):
        for x in path:
            long1 = x[0]
            lat1 = x[1]
            print("latitude: " + lat1 + "longitude: " + long1)

data = Path.get_data('42.3417707', '-83.0601714', '42.3387803', '-83.0572124')
print(data)



# Directions is a list
# print(data.json()['directions'][0])
# print("-----------------------------------------")
# routes is a dictionary
# print(data.json()['routes']['features'][0]['geometry']['paths'][0])
# print(data.json().keys())

