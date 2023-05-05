
import socket
from termcolor import colored

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def portScan():
    host = input("[+] Enter a host to scan: ")
    port = int(input("[+] Enter a port to scan: "))
    if socket.connect_ex((host, port)):
        print(colored(f"[!!] Port {port} on {host} is closed", 'red'))
    else:
        print(colored(f"[+] Port {port} on Host {host} is open", 'green'))

