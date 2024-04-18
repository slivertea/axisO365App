import requests
import json
import os
import csv

#Define static values
TOKEN = os.getenv('AXIS_TOKEN')
axisUrl = "https://admin-api.axissecurity.com/api/v1.0/applications?pageSize=100&pageNumber=1"
o365Url = "https://endpoints.office.com/endpoints/worldwide?clientrequestid=b10c5ed1-bad1-445f-b386-b919946339a7"
localo365file = "sample_o365Source.json"
csvParseFile='outputCSVparse.csv'
apiToken = 'Bearer '+TOKEN
payload = ""
headers = {
    'Authorization': apiToken,
    'Content-Type': 'application/json'
}


#STEP1 - Collect existing o365 data - either online or local json input.json file
## Collect from online direct
#o365Source = (requests.request("GET", o365Url, headers=headers, data=payload).json())
#o365SourceJS = json.dumps(o365Source)
# Dump output to the sample file
#with open(localo365file, 'w', encoding='utf-8') as fh:
    #Write to file
#    json.dump(o365Source, fh, ensure_ascii=False, indent=4)
## Collect form existing localo365file sample_o365Source.json by default
with open(localo365file, 'r', encoding='utf-8') as fh:
    o365Source = json.load(fh)


apps = []
for o365Id in o365Source:
    #print (o365Id['serviceAreaDisplayName'], o365Id.keys())
    # Destinations
    # URL
    if "urls" in o365Id.keys():
        for url in o365Id['urls']:
            app = {
                "id": o365Id['id'],
                "category": o365Id['category'],
                "name": o365Id['serviceAreaDisplayName'],
                "destination": url,
                "tcpPorts": None,
                "udpPorts": None,
                "required": o365Id['required'],
                "notes": None
            }
            if "tcpPorts" in o365Id.keys():
                app['tcpPorts'] = o365Id['tcpPorts']
            if "udpPorts" in o365Id.keys():
                app['udpPorts'] = o365Id['udpPorts']
            if "notes" in o365Id.keys():
                app['notes'] = o365Id['notes']
            apps.append(app)
    # IP Address
    if "ips" in o365Id.keys():
        for iP in o365Id['ips']:
            if ":" in iP:
                () # Skip ipv6
            else:
                app = {
                    "id": o365Id['id'],
                    "category": o365Id['category'],
                    "name": o365Id['serviceAreaDisplayName'],
                    "destination": iP,
                    "tcpPorts": None,
                    "udpPorts": None,
                    "required": o365Id['required'],
                    "notes": None
                }
            if "tcpPorts" in o365Id.keys():
                app['tcpPorts'] = o365Id['tcpPorts']
            if "udpPorts" in o365Id.keys():
                app['udpPorts'] = o365Id['udpPorts']
            if "notes" in o365Id.keys():
                app['notes'] = o365Id['notes']
            apps.append(app)


# Dump to JSON for API automation
apiBodyTemplate = {
"name":None,
"type": "NetworkRange",
"enabled": True,
"networkRangeApplicationData": {
        "ipRangesOrCIDRs": [],
        "dnsSearches": [],
        "excludedDnsSearches": [],
        "enableICMP": True,
        #"portsAndProtocols": ["1-10","11-20:tcp","21-30:udp","40","45:tcp"]
        "portsAndProtocols": []
    },
"connectorZoneID": None
}
# Dump to CSV for parsing
fields = apps[0].keys()
with open(csvParseFile, 'w') as csvFh:
    writer = csv.DictWriter(csvFh, fieldnames=fields)
    writer.writeheader()
    writer.writerows(apps)
