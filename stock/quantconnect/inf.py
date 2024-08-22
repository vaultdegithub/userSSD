# quantconnect: 
User_ID= '301909'
Token= '70243180ad551bfd2994fbd8d6c245507830d62baf79241b1ea0a7ce04593004'

import base64
import hashlib
import time
import requests

# Get timestamp
timestamp = str(int(time.time()))
time_stamped_token = Token + ':' + timestamp

# Get hased API token
hashed_token = hashlib.sha256(time_stamped_token.encode('utf-8')).hexdigest()
authentication = "{}:{}".format(User_ID, hashed_token)
api_token = base64.b64encode(authentication.encode('utf-8')).decode('ascii')

# Create headers dictionary.
headers = {
    'Authorization': 'Basic %s' % api_token,
    'Timestamp': timestamp
}

# Create POST Request with headers (optional: Json Content as data argument).
response = requests.post("https://www.quantconnect.com/api/v2", 
                         data = {}, 
                         json = {},    # Some request requires json param (must remove the data param in this case)
                         headers = headers)
print(response.text)