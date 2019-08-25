##
##
import pexpect
import getpass
from os import system

def getShowVersion(username, password, ip):

    child = pexpect.spawnu('ssh -l ' + username + ' -c aes128-cbc ' + ip)

    child.expect(['Password:'])
    child.sendline(password)

    child.expect(['#'])
    child.sendline('terminal length 0')

    child.expect(['#'])
    child.sendline('show version')

    child.expect(['#'])
    node_show_version = child.before

    try:
        with open('/tmp/config.cfg', 'w') as f:
            f.write(node_show_version)
    except:
        print('Unable to create file!!!')

def printHostname():

    try:
        with open('/tmp/config.cfg') as f:
            for line in f:
                if 'uptime' in line:
                    hostname = line.strip().split(' ')[0]
    except FileNotFoundError:
        print('Unable to locate file!')

    return hostname

def printModel():

    try:
        with open('/tmp/config.cfg', 'r') as f:
            for line in f:
                if 'Model number' in line:
                    model = line.split(':')[1].lstrip().strip()
    except FileNotFoundError:
        print('Unable to locate file!')

    return model

def printIOSVersion():
    try:
        with open('/tmp/config.cfg', 'r') as f:
            for line in f:
                if 'IOS Software' in line:
                    ios = line.strip().split(',')[2].split(' ')[2]
    except FileNotFoundError:
        print('Unable to locate file!')

    return ios

def main():
    system('clear')

    username = input('Enter your username: ')
    password = getpass.getpass('Enter your password: ')

    print()
    print()
    print('{:25} {:15} {:20} {:10}'.format('Node Hostname', 'IP', 'Model', 'IOS Version'))
    print('-' * 80)

    try:
        with open('ips.txt') as f:
            for line in f:
                ip = line.strip()
                getShowVersion(username, password, ip)
                hostname = printHostname()
                model = printModel()
                ios = printIOSVersion()
                print('{:25} {:15} {:20} {:10}'.format(hostname, ip, model, ios))
    except FileNotFoundError:
        print('Unable to OPEN file for reading!')

    print()

if __name__ == '__main__':
    main()

##
## End of file...
