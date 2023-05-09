#Uses pan-python package to connect to a Palo Alto fw.
#The package is on github and there are some docs you can use to see some examples.
#The fw config uses XML. You'll have to know how XML and XML_PATH works to understand how to push and where to modify the config. 

import pan.xapi

def get_pan_credentials(fw):
 cred =  {}
 cred['api_username'] = "username"
 cred['api_password'] = "password"
 cred['hostname'] = fw
 return cred

# XML 
xml_data ='<hostname>PA-FW</hostname>'
xpath = "/config/devices/entry[@name='localhost.localdomain']/deviceconfig/system/hostname"
print (xml_data)

# connect to the FW using the credentials
ip = "192.168.1.1"
credentials = get_pan_credentials(ip)
print (credentials)
xapi = pan.xapi.PanXapi(**credentials)
print ('connect to %s' % ip)

#edit the config at the xpath
print ("xpath: %s" % xpath)
print ("edit config")
xapi.edit(xpath,element=xml_data)

#commit the config
print ("commit config")
xapi.commit('<commit/>')
print  ("done")
