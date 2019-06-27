# messenger.py - contains functions to create different kinds of messages like info or error


# color the text, usage: print bcolors.WARNING + "Warning: No active frommets remain. Continue?" + bcolors.ENDC
BCOLORS = {
    'HEADER': '\033[95m',
    'OKBLUE': '\033[94m',
    'OKGREEN': '\033[92m',
    'WARNING': '\033[93m',
    'FAIL': '\033[91m',
    'ENDC': '\033[0m',
    'BOLD': '\033[1m',
    'UNDERLINE': '\033[4m'
}


# Information message
def info(message):
    print(BCOLORS['OKBLUE'] + message + BCOLORS['ENDC'])


# Action message
def action(message):
    print(BCOLORS['OKGREEN'] + message + BCOLORS['ENDC'])


# Error message
def error(message):
    print(BCOLORS['FAIL'] + message + BCOLORS['ENDC'])
