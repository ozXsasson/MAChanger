#!/usr/bin/env python

import subprocess
import optparse
import re
import random

def getArgu():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    parser.add_option("-r", "--random", dest="random", help="Generate random MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("--- Please specify an interface, use --help for more info")
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


def generateMAC():
    digits = [random.choice('0123456789ABCDEF') for _ in range(11)]
    second_digit = random.choice('02468ACE')
    digits.insert(1, second_digit)
    mac_address = ':'.join(''.join(digits[i:i + 2]) for i in range(0, 12, 2))
    return mac_address

options = getArgu()
newMAC = generateMAC()
myMAC = getMAC(options.interface)
print("*** Current MAC = " + myMAC)


if options.new_mac:
    changeMAC(options.interface, options.new_mac)
else:
    changeMAC(options.interface, newMAC)

myMAC = getMAC(options.interface)
print("*** MAC address was successfully changed to " + myMAC)
