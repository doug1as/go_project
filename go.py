#!/usr/bin/env python3

# Copyright (C) 2020-2020  Douglas Rodrigues <douglas.rsilva@outlook.com.br>
#
# This file is part of Go Project.
#
# Go Project is free software; you can redistribute it and/or modify it under the
# terms of the GNU Lesser General Public License as published by the Free
# Software Foundation; either version 2.1 of the License, or (at your option)
# any later version.
#
# Go Project is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
#    Name: Go Script
#    Version: 0.1.0
#    Summary: Multi-vendor script to collect some commands/informations
#    Home-page: https://github.com/doug1as/go_project
#    Author: Douglas Rodrigues
#    Author-email: doug1as@outlook.com
#    License: GPL
#    Requires: netmiko==3.0.0, paramiko
#


# Importing required modules
import logging
import os
import platform
import csv
import getpass
import functions_decorators
import go_vendors
from datetime import datetime

# Printing author informations
functions_decorators.decorator_author()

# Generating log file for analysis when needed
#logging.basicConfig(filename='go.log', level=logging.DEBUG)
#logger = logging.getLogger("netmiko")

# Getting start date and time for measure elapsed time
start = datetime.today()

# Obtaining credentials
username = str(input("Inform your TACACS user: "))
password = getpass.getpass("Inform your TACACS password: ")

# Getting home directory for user, and find correct ssh config file for respective jump server
operational_system = platform.system()

if operational_system == 'Windows':
    ssh_file_location = os.path.expanduser("~\.ssh\\")
elif operational_system == 'Linux':
    ssh_file_location = os.path.expanduser("~/.ssh/")
else:
    print("This Operating System Isn't Supported By This Script !")

#Getting Current Directory
current_directory = os.getcwd()

# Open and read device list to be accessed for obtain configurations, named elements.csv
with open(os.path.join(current_directory, 'elements.csv'), encoding='utf8', errors='ignore') as elements_csv_file:
    elements = csv.DictReader(elements_csv_file, delimiter=';')
    for row in elements:
        hostname = row['HOSTNAME']
        ip = row['IP']
        vendor = row['VENDOR']
        device_type = row['DEVICE_TYPE']
        jump_host = row['JUMP_HOST']

        #Finding correct jump server and allocating ssh/config properly
        if jump_host == 'vivo_1':
            ssh_config = ssh_file_location + 'config-vivo1'
        elif jump_host == 'vivo_2':
            ssh_config = ssh_file_location + 'config-vivo2'
        else:
            ssh_config = '~/.ssh/config'
        
        if device_type == 'brocade_nos':
            row_vendor = "BROCADE_NOS"
            go_vendors.all_devices(username, password, hostname, ip, device_type, vendor, row_vendor, ssh_config)
        elif device_type == 'cisco_ios':
            row_vendor = "CISCO_IOS"
            go_vendors.all_devices(username, password, hostname, ip, device_type, vendor, row_vendor, ssh_config)
        elif device_type == 'cisco_xe':
            row_vendor = "CISCO_IOSXE"
            go_vendors.all_devices(username, password, hostname, ip, device_type, vendor, row_vendor, ssh_config)
        elif device_type == 'cisco_xr':
            row_vendor = "CISCO_IOSXR"
            go_vendors.all_devices(username, password, hostname, ip, device_type, vendor, row_vendor, ssh_config)
        elif device_type == 'cisco_nxos':
            row_vendor = "CISCO_NXOS"
            go_vendors.all_devices(username, password, hostname, ip, device_type, vendor, row_vendor, ssh_config)
        elif device_type == 'extreme_telnet':
            row_vendor = "EXTREME_EXOS"
            go_vendors.all_devices(username, password, hostname, ip, device_type, vendor, row_vendor, ssh_config)
        elif device_type == 'hp_comware':
            row_vendor = "HP_COMWARE"
            go_vendors.all_devices(username, password, hostname, ip, device_type, vendor, row_vendor, ssh_config)
        elif device_type == 'ruckus_fastiron':
            row_vendor = "RUCKUS_FASTIRON"
            go_vendors.all_devices(username, password, hostname, ip, device_type, vendor, row_vendor, ssh_config)
        else:
            functions_decorators.decorator_astherisc(3)
            print("Something's Wrong With Next Element in elements.csv Archive, in Device Type column, please verify !")
            print("Device Type: " + str(device_type) + " With Hostname: " + str(hostname.upper()) + " is unsupported !")


# Final greeting
end = datetime.today()
total_time = end - start
functions_decorators.decorator_astherisc(3)
functions_decorators.decorator_final(total_time)
