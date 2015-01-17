#!/usr/bin/python

from boto.route53.connection import Route53Connection
from boto.route53.record import ResourceRecordSets
import getopt
import sys
import urllib2

def getZone(zoneName, connection):
    for zone in connection.get_zones():
        if zone.name == zoneName:
	    return zone
        else:
	    continue
    return

def updateARecordOnZone(dns_name, zone, ip):
    record = zone.find_records(dns_name, "A")

    if record:
	if record.resource_records[0] != ip:
            print("Zone IP is: " + record.resource_records[0])	
	    print("Updating zone record")
            zone.update_record(record, ip)
	else:
            print("Zone IP is: " + record.resource_records[0])	
            print("Not updating, already up to date")
    else:
	print("Creating zone record")
	zone.add_record("A", dns_name, ip)



def main(argv):

    zone = ''
    dns_name = ''

    opts, args = getopt.getopt(argv, "z:d:",["zone=","dns_name="])
    
    if len(argv) != 4:
	print("You must provide arguments in the form...")
	print('dyndns.py -z zone.com. -d host.zone.com.')
	sys.exit(2)
    for opt, arg in opts:
        if opt in ("-z", "--zone"):
	    zone = arg
	elif opt in ("-d", "--dns_name"):
	    dns_name = arg
    if zone == '' or dns_name == '':
	print("You must provide arguments in the form...")
	print('dyndns.py -z zone.com. -d host.zone.com.')
	sys.exit(2)

    getIpStream = urllib2.urlopen('http://ipinfo.io/ip')
    ip = getIpStream.read().rstrip();
    print("Local IP is: " + ip)
    
    r53 = Route53Connection()
    zoneTarget = getZone(zone, r53)

    if zoneTarget:
        updateARecordOnZone(dns_name, zoneTarget, ip)
    else:
        print('Zone not found.')

if __name__ == "__main__":
    main(sys.argv[1:])



