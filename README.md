# Axis O365 Dynamic Network Range Application


** Application for dynamic O365 configuration from
** Microsoft


## Sources
* https://docs.axissecurity.com
* Document reference https://learn.microsoft.com/en-us/microsoft-365/enterprise/urls-and-ip-address-ranges?view=o365-worldwide
* JSON source: https://endpoints.office.com/endpoints/worldwide?clientrequestid=b10c5ed1-bad1-445f-b386-b919946339a7

## Guidence
1. run o365_GetSources.py
2. run o365.py - builds the Axis Import csv file.
3. Login to Atmos Management UI
4. Navigate to Settings -> Destinations
5. remove all applications, if existing, from tag **"ms 365 all apps"**
6. Click the Import button, and Submit
7. Confirm Policy permits accordingly to the **"ms 365 all apps"** tag

## data
Samples included under samples/:
* an o365 json sample
* a manual bulk import, for network range, to Axis.


python scripts:
* o365_GetSources.py: Downloads and stores the o365 definitions on json format - file samples/sample_365Source.json
* o365.py:  Function source code to transpose, deduplicate, and build an axis bulk import for network rnage

Future state: Automate using the Axis Application API
