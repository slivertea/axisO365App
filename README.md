# Axis O365 Dynamic Network Range Application
Tools for collecting MS o365 definition data, parsing them into readable forms,
removing duplicate and overlaping destinations to consolidate into one "common" group.

This tool can take that data and then transform it into an Axis import CSV for Axis Network Ranges


## Data Sources
#### Microsoft
* Document reference https://learn.microsoft.com/en-us/microsoft-365/enterprise/urls-and-ip-address-ranges?view=o365-worldwide
* JSON source: https://endpoints.office.com/endpoints/worldwide?clientrequestid=b10c5ed1-bad1-445f-b386-b919946339a7
* 3rd Party MVP: https://helgeklein.com/blog/microsoft-office-teams-network-connection-target-hosts-list/
#### Axis
* https://docs.axissecurity.com



## Guidence
#### Summary
A. Collect the source Data
B. Review the human readable output
C. Transform to Axis imports
D. Modify tags, zones, or names accordingly.

#### Step by Step
1. run o365_GetSources.py
2. run o365.py - builds the Axis Import csv file.
3. Login to Atmos Management UI
4. Navigate to Settings -> Destinations
5. remove all applications, if existing, from tag **"ms 365 all apps"**
6. Click the Import button, and Submit
7. Confirm Policy permits accordingly to the **"ms 365 all apps"** tag



## Included Files
#### samples/
* MS o365 sample - json format
* Axis Import CSV - csv for Network Ranges App Types
#### outputs
* axisImport_NR.csv: Axis import files
* output_AppsByDestinations.csv - per destination csv transposition of the origional data.
* output_AppsByName.json - file representing the consolidated and deduplicated object, of the origional data.

#### scripts
* o365_GetSources.py: Downloads and stores the o365 definitions on json format - file samples/sample_365Source.json
* o365.py:  Function source code to transpose, deduplicate, and build an axis bulk import for network rnage

Future state: Automate using the Axis Application API
