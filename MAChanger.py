#!/usr/bin/env python

import subprocess
import optparse
import re

def getArgu():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("--- Please specify an interface, use --help for more info")
    elif not options.new_mac:
        parser.error("--- Please specify a new mac, use --help for more info")
    return options
def changeMAC(interface, new_mac):
    print("*** Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
def getMAC(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("--- Could not read MAC address")


options = getArgu()

myMAC = getMAC(options.interface)
print("*** Current MAC = " + str(myMAC))

changeMAC(options.interface, options.new_mac)

myMAC = getMAC(options.interface)
if myMAC == options.new_mac:
    print("*** MAC address was successfully changed to " + myMAC)
else:
    print("--- MAC adddress did not get changed.")