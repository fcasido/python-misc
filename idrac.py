#user@ubuntu-user-vm:~/SCRIPTS$ python idrac.py
#('192.168.1.100', 'https://192.168.1.100/redfish/v1/Systems/System.Embedded.1')
#('Model Number: ', u'PowerEdge R740')
#('Serial Number: ', u'ABC12345')
#('Service Tag: ', u'XYZ12345')
#('Memory: ', 256)
#('Processor_model: ', u'Intel(R) Xeon(R) Platinum 8168 CPU @ 2.70GHz')


import requests
import json
import pprint
# Set the iDRAC IP address, username and password
idrac_ip = '192.168.1.100'
username = 'username'
password = 'password'

# Set the API URLs for each component
system_url = ('https://%s/redfish/v1/Systems/System.Embedded.1' % idrac_ip)
processor_url = ('https://%s/redfish/v1/Systems/System.Embedded.1/Processors' % idrac_ip)

print (idrac_ip,system_url)
# Set the headers for authentication
headers = {'Content-Type': 'application/json'}

# Create a session to handle authentication
session = requests.Session()
session.auth = (username, password)

# Send a GET request to the system API URL
response = session.get(system_url, headers=headers, verify=False)

# Convert the response content to a JSON object
system_data = json.loads(response.content)

# Extract the model number and serial number from the system JSON object
model_number = system_data['Model']
serial_number = system_data['SerialNumber']
service_tag = system_data['SKU']
memory = system_data['MemorySummary']['TotalSystemMemoryGiB']
processor_model = system_data['ProcessorSummary']['Model']


# Send a GET request to the processor API URL
response = session.get(processor_url, headers=headers)

# Convert the response content to a JSON object
processor_data = json.loads(response.content)


# Print the model number, serial number, and processor information
print("Model Number: " , model_number)
print("Serial Number: ", serial_number)
print("Service Tag: ", service_tag)
print("Memory: ", memory)
print("Processor_model: ", processor_model))
