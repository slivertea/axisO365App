import requests
import json
import os
import csv

#Define static values
TOKEN = os.getenv('AXIS_TOKEN')
axisUrl = "https://admin-api.axissecurity.com/api/v1.0/applications?pageSize=100&pageNumber=1"
o365Url = "https://endpoints.office.com/endpoints/worldwide?clientrequestid=b10c5ed1-bad1-445f-b386-b919946339a7"
localo365file = "sample_o365Source.json"
apiToken = 'Bearer '+TOKEN
payload = ""
headers = {
    'Authorization': apiToken,
    'Content-Type': 'application/json'
}

outputDict={
"Optimized": {},
"Default": {},
"Allow": {}
}

#STEP1 - Collect existing o365 data
o365Source = (requests.request("GET", o365Url, headers=headers, data=payload).json())
o365SourceJS = json.dumps(o365Source)
# Dump output to the sample file
with open(localo365file, 'w', encoding='utf-8') as fh:
    #Write to file
    json.dump(o365Source, fh, ensure_ascii=False, indent=4)
#print (json.dumps(o365Source))

print (o365Source[0].keys())
for o365Items in o365Source:
    if o365Items['category'] == 'Optimize':
        #print ("FOUND")
        print (o365Items['serviceArea'], "Found")
    #print ((o365Items['serviceArea']), (o365Items['category']), (o365Items['required']))
