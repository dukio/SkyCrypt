import requests
import json
res = json.loads(requests.get("https://api.hypixel.net/key?key=1324402a-fbd1-4382-8008-411f8ecfad5f").text)
print("The owner of the API key is {api_key}".format(api_key=res["record"]["owner"]))
print("This key has been queried about {api_key} times".format(api_key=res["record"]["totalQueries"]))
print("This key has a query limit of about {api_key}".format(api_key=res["record"]["limit"]))
print("This key has been queried about {api_key} times in the past minute".format(api_key=res["record"]["queriesInPastMin"]))
#Note to self, build API Key false statement