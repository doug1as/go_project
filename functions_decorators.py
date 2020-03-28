def decorator_author():
    print("""
#######################################################################
#            ____         ____            _           _               #
#           / ___| ___   |  _ \ _ __ ___ (_) ___  ___| |_             #
#          | |  _ / _ \  | |_) | '__/ _ \| |/ _ \/ __| __|            #
#          | |_| | (_) | |  __/| | | (_) | |  __/ (__| |_             #
#           \____|\___/  |_|   |_|  \___// |\___|\___|\__|            #
#                                      |__/                           #
#                                                                     #
# Name: Go Script                                                     #
# Version: 0.1.0                                                      #
# Summary: Multi-vendor script to collect some commands/informations  #
# Home-page: https://github.com/doug1as/go_project                    #
# Author: Douglas Rodrigues                                           #
# Author-email: doug1as@outlook.com                                   #
#                                                                     #
#######################################################################
""")

def decorator_astherisc(how_many):
    for astherisc in range(how_many):
        print('*')


def decorator_begin(vendor, hostname, ip):
    print("# ==============================================\n#     GETTING ELEMENT SETTINGS\n# ==============================================")
    print("------------------------------")
    print('VENDOR: ' + str(vendor.upper()))
    print('HOSTNAME: ' + str(hostname.upper()))
    print('IP: ' + str(ip))
    print("------------------------------")
    print("# ==============================================\n#     GETTING ELEMENT SETTINGS\n# ==============================================")


def decorator_end(vendor, hostname, ip, prompt):
    print("# ==============================================\n#     ENDING CAPTURE IN THE ELEMENT\n# ==============================================")
    print('VENDOR: ' + str(vendor.upper()))
    print('HOSTNAME: ' + str(hostname.upper()))
    print('PROMPT: ' + str(prompt.upper()))
    print('IP: ' + str(ip))
    print("# ==============================================\n#     ENDING CAPTURE IN THE ELEMENT\n# ==============================================")


def decorator_command_begin(command):
    command_begin = "# ================================================================\n#  STARTING COMMAND CAPTURE: " + str(command) + "\n# ================================================================\n"
    command_begin_str = str(command_begin)
    return command_begin_str
#print(decorator_command_begin('TESTE'))


def decorator_command_end(command):
    command_end = "\n# ================================================================\n#  ENDING COMMAND CAPTURE: " + str(command) + "\n# ================================================================\n"
    command_end_str = str(command_end)
    return command_end_str
#print(decorator_command_end('TESTE'))


def decorator_final(total_time):
    print("# ==============================================\n#     FINISHING CAPTURE SCRIPT:\n#     RUNTIME: " + str(total_time) + "\n# ==============================================")


def decorator_current_command(command):
    print('CAPTURING COMMAND: ' + str(command))