from sys import argv
from datetime import datetime
import subprocess

import socket

target = argv[1]

def port_scan(target):
    try:
        ip = socket.gethostname(target)

        print(f'Scanning target {ip}')
        print('Time started:', datetime.now())

        for port in range(0, 65536):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex(ip, port)
            if result == 0:
                print('Port {}: Open'.format(port))
            sock.close()
    
    except socket.gaierror:
        print('Hostname could not be resolved')
    
    except socket.error:
        print('Could not connect to the server/IP')
port_scan()