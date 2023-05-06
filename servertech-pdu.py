import argparse
from pysnmp.hlapi import *

parser = argparse.ArgumentParser(description='Get or set the description of a ServerTech PDU outlet.')
parser.add_argument('address', metavar='address', type=str,
                    help='the IP address of the PDU')
parser.add_argument('-u', metavar='user', type=str, default='user',
                    help='the SNMPv3 username (default: user)')
parser.add_argument('-a', metavar='auth_protocol', type=str, default='sha',
                    help='the SNMPv3 authentication protocol (default: sha)')
parser.add_argument('-A', metavar='auth_password', type=str, default='password',
                    help='the SNMPv3 authentication password (default: password)')
parser.add_argument('-x', metavar='priv_protocol', type=str, default='des',
                    help='the SNMPv3 privacy protocol (default: des)')
parser.add_argument('-X', metavar='priv_password', type=str, default='password',
                    help='the SNMPv3 privacy password (default: password)')

group = parser.add_mutually_exclusive_group()
group.add_argument('-g', action='store_true', help='list available ports and their status')
group.add_argument('-p', metavar='port', type=int, help='the port number of the outlet to modify')
group.add_argument('-d', metavar='description', type=str, help='the new description for the outlet')

args = parser.parse_args()

address = args.address
user = args.u
auth_protocol = args.a
auth_password = args.A
priv_protocol = args.x
priv_password = args.X

location_oid = '1.3.6.1.4.1.1718.3.2.1.1.3.1.2'
power_status_oid = '1.3.6.1.4.1.1718.3.2.1.1.4.1.1'

errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(SnmpEngine(),
           UsmUserData(user, authPassword=auth_password, authProtocol=getattr(hlapi, 'usmHMAC' + auth_protocol.upper()),
                        privPassword=priv_password, privProtocol=getattr(hlapi, 'usm' + priv_protocol.upper())),
           UdpTransportTarget((address, 161)),
           ContextData(),
           ObjectType(ObjectIdentity(location_oid)),
           ObjectType(ObjectIdentity(power_status_oid))))

if errorIndication:
    print(errorIndication)
elif errorStatus:
    print('%s at %s' % (errorStatus.prettyPrint(), errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
else:
    location = varBinds[0][1].prettyPrint()
    power_status = varBinds[1][1].prettyPrint()
    print('Location: {}'.format(location))
    print('Power Status: {}'.format(power_status))

if args.g:
    port_oid = '1.3.6.1.4.1.1718.3.2.3.1.1'
    desc_oid = '1.3.6.1.4.1.1718.3.2.3.1.2'
    status_oid = '1.3.6.1.4.1.1718.3.2.3.1.4'
    errorIndication, errorStatus, errorIndex, varBinds = next(
        bulkCmd(SnmpEngine(),
                UsmUserData(user, authPassword=auth_password, authProtocol=getattr(hlapi, 'usmHMAC' + auth_protocol.upper()),
                             privPassword=priv_password, privProtocol=getattr(hlapi, 'usm' + priv_protocol.upper())),
                UdpTransportTarget((address, 161)),
                Context
