#!/usr/bin/env python3

"""
    Name: Go Script
    Version: 0.1.0
    Summary: Multi-vendor script to collect some commands/informations
    Home-page: https://github.com/doug1as/go_project
    Author: Douglas Rodrigues
    Author-email: doug1as@outlook.com
    License: MIT
    Requires: netmiko==3.0.0, paramiko
"""

# Importing required modules
import csv
from netmiko import ConnectHandler
from datetime import datetime
import functions_decorators

def all_devices(username, password, hostname, ip, device_type, vendor, row_vendor):
    # Current date and time for creating .log file
    now = datetime.today()
    text_date_hour = now.strftime("%Y%m%d-%H%M%S")
    # File that will be recorded with the outputs of the commands
    output_log = open("{}-{}_OUTPUT.log".format(text_date_hour, hostname.upper()), "a")
    # Print 3 asterisk (s) and inform element that is being accessed starting the capture
    functions_decorators.decorator_astherisc(3)
    functions_decorators.decorator_begin(vendor, hostname, ip)
    functions_decorators.decorator_astherisc(1)
    # Accessing the element of the time
    element = {'device_type': device_type, 'host': ip, 'username': username, 'password': password}
    host_connect = ConnectHandler(**element)
    # Looping commands contained in commands.csv
    with open('commands.csv', encoding='utf8', errors='ignore') as commands_csv_file:
        commands = csv.DictReader(commands_csv_file, delimiter=';')
        for row in commands:
            if row[row_vendor] == '':
                break
            output_log.write(functions_decorators.decorator_command_begin(row[row_vendor]))
            output = host_connect.send_command(row[row_vendor])
            # Informing command by command on the execution screen!
            functions_decorators.decorator_current_command(row[row_vendor])
            # Writing output to .log file
            for line in output:
                output_log.write(line)
            output_log.write(functions_decorators.decorator_command_end(row[row_vendor]))
            output_log.write('\n')
            # Closing .log file
            # output_log.close () # No need because the "with open" block does this automatically
    # Print and inform element that was accessed and we are finalizing the capture
    functions_decorators.decorator_end(vendor, hostname, ip, host_connect.find_prompt())
