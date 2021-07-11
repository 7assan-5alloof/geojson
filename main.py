import json  # Deal with JSON
import urllib.request
import urllib.parse
import urllib.error  # Deal with the Internet
import ssl  # Ignore SSL problems

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Get data to retrieve from Google Places cache endpoint
endpoint = "http://py4e-data.dr-chuck.net/json?"
address = input("Enter address: ")
params = {
    "address": address,
    "key": 42
}

# Retrieve and parse JSON for given location
url = endpoint + urllib.parse.urlencode(params)
str_json = urllib.request.urlopen(url, context=ctx).read().decode()
parsed_json = json.loads(str_json)

# Look up the first place_id
print("Place ID: " + parsed_json["results"][0]["place_id"])
