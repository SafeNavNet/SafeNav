# print(data.json().keys()) to find all keys in dict
import requests


class FilteredPath:
    def get_data(lat1, long1, lat2, long2):
        # generate a token with your client id and client secret
        # print(token.json()['access_token'])
        token = FilteredPath.gen_token()
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
        filtered_path = []
        counter = 0
        for x in path:
            if(counter % 3 == 0):
                filtered_path.append(x)
            counter += 1
        return filtered_path



data1 = FilteredPath.get_data('42.3417707', '-83.0601714', '42.3387803', '-83.0572124')
print(data1)
print
# data2 = FilteredPath.get_data('42.3417707', '-83.0601714', '9.9280694', '-84.0907246')
# print(data2)
data3 = FilteredPath.filter_path(data1)
print(data3)
