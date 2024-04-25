import requests
import json
import os
import csv

#Define static values
TOKEN = os.getenv('AXIS_TOKEN')
axisUrl = "https://admin-api.axissecurity.com/api/v1.0/applications?pageSize=100&pageNumber=1"
o365Url = "https://endpoints.office.com/endpoints/worldwide?clientrequestid=b10c5ed1-bad1-445f-b386-b919946339a7"
sourceO365JS = "samples/sample_o365Source.json"
apiToken = 'Bearer '+TOKEN
payload = ""
headers = {
    'Authorization': apiToken,
    'Content-Type': 'application/json'
}



#STEP1 - Collect existing o365 data
o365Source = (requests.request("GET", o365Url, headers=headers, data=payload).json())
# Dump output to the sample file
with open(sourceO365JS, 'w', encoding='utf-8') as fh:
    json.dump(o365Source, fh, ensure_ascii=False, indent=4)
#print (json.dumps(o365Source))
