import os

ip_or_host = input('digite o ip ou host a ser verificado: ')

os.system(f'ping -n 6 {ip_or_host}')