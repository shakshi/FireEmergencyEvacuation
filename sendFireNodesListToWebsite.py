import requests
import json
#url='https://fir-demoproject-9f0fc.firebaseapp.com/'
url='http://127.0.0.1/'

post_data = {'fireNodes':[2,3,4], 'stuckNodes': [1,12,3,14] }
response = requests.post(url, data=json.dumps(post_data))

print response