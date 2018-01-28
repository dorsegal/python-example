import boto3
from collections import defaultdict
from pprint import pprint

# Get a list of available services
services = boto3.session.Session().get_available_services()

regions = defaultdict(list)
elements = defaultdict()

# Get all region from each service
for service in services:
    r = boto3.session.Session().get_available_regions(service)
    for region in r:
        regions[region].append(service)

# Print all available regions
print "Avaiblable regions:\n---------------------------"
for r in sorted(regions.keys()):
    print r
print

# User selects region from list
region = raw_input("Please specify region: ")

# Print available service based on region
print "---------------------------\n\nList of available services:"
for service in regions[region]:
    print service
print

# User selects service from list
service = raw_input("---------------------------\n\nselect service to decribe: ")


# Getting available methods for selected service
client = boto3.client(service)
for v in client._PY_TO_OP_NAME.items():
    elements[str(v[1])]=str(v[0])

# Getting available methods for selected service
for element in sorted(elements):
    print element

# Run the selected method
command = raw_input("---------------------------\n\nselect command to execute: ")
command = 'pprint (client.' + elements[command] + '())'
exec command

