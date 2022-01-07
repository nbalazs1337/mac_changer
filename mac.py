#!/usr/bin/env python

import subprocess
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface name")
    parser.add_option("-m", "--mac", dest="new_mac", help="New Mac Address")
    # options will contain the wlan and 00:11..
    # arguments will contain --interface --mac
    (options, arguments) = parser.parse_args()
    # ia din consola valorile introduse de mine
    if not options.interface:
        #code to handle error
        parser.error("[!!!] Please specify an interface, use --help for info")
    elif not options.new_mac:
        #to handle error
        parser.error("[!!!] Please specify a new mac_adress, use --help for info")

    return options


def change_mac(interface, new_mac):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    print(" [@] MAC Adress changed for " + interface+ " to " +new_mac+" successfully")



options = get_arguments()
change_mac(options.interface, options.new_mac)
