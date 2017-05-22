#!/usr/bin/env python
# Python Network Programming Cookbook -- Chapter -1

import socket, sys, argparse
from binascii import hexlify
#
def print_machine_info():
    print('GETTING MACHINE INFO')
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    print("Host name: {}".format(host_name))
    print("IP Address: {}".format(ip_address))

def get_remote_machine_info():
    print('GETTING REMOTE HOST IPs')
    remote_host = 'www.python.org'
    remote_host2 = 'www.pytgo.org'
    try:
        print('{}: IP address : {}'.format(remote_host2, socket.gethostbyname(remote_host2)))
    except(socket.error, err.msg):
        print(remote_host, ':', err_msg)


def convert_ip4_address():
    # loop through a list of ips
    print('CONVERTING IPs')
    for ip_addr in [socket.gethostbyname(socket.gethostname()), socket.gethostbyname('www.python.org')]:
        packed_ip_addr = socket.inet_aton(ip_addr)
        unpacked_ip_addr = socket.inet_ntoa(packed_ip_addr)
        print('IP Address: {} => Packed: {}, Unpacked: {}'.format(ip_addr, hexlify(packed_ip_addr), unpacked_ip_addr))

def find_service_name():
    print('FINDING SERVICE NAMES')
    protocolname = 'tcp'
    for port in [80, 25]:
        print('Port: {} => service name: {}'.format(port, socket.getservbyport(port, protocolname)))
    print("Port: {} => service name: {}".format(53, socket.getservbyport(53, 'udp')))

def convert_integer():
    print('CONVERTING INTEGERS INTO NETWORK/HOST BYTE ORDERS')
    data = 1234
    # 32-bit
    print('ORIGINAL: {} => Long: (host byte order: {}, Network byte order: {})'.format(data, socket.ntohl(data), socket.htonl(data)))
    # 16-bit
    print('ORIGINAL: {} => Short: (host byte order: {}, Network byte order: {})'.format(data, socket.ntohs(data), socket.htons(data)))

def test_socket_timeout():
    print('GETTING AND SETTING SOCKET TIMEOUTS')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Default socket timeout: {}".format(s.gettimeout()))
    s.settimeout(100)
    print("Current socket timeout: {}".format(s.gettimeout()))

# setup argument parsing
parser = argparse.ArgumentParser(description='Socket Error Examples')
parser.add_argument('--host', action="store", dest="host", required=False)
parser.add_argument('--port', action="store", dest="port", type=int, required=False)
parser.add_argument('--file', action="store", dest="file", required=False)

given_args = parser.parse_args()
host = given_args.host
port = given_args.port
filename = given_args.file
print(given_args)

def network_error_handling(host, port, filename):
    # First block: creating a socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except(socket.error, e):
        print("Error creating socket: {}".format(e))
    # Second block: connect to a given host/port
    try:
        s.connect((host, port))
    except (socket.gaierror, string):
        print('Address-related error connecting to server: {}'.format(string))
        sys.exit(1)
    except(socket.error, e):
        print('Connection error: {}'.format(e))
        sys.exit(1)
    # # Third block: sending data
    try:
        string = 'GET {} HTTP/1.0\r\n\r\n'.format(filename)
        s.sendall(string.encode())
    except(socket.error, e):
        print('Error sending data: {}'.format(e))
        sys.exit(1)

    while 1:
        # Fourth block: waiting to receive data from remote host
        try:
            buf = s.recv(2048)
        except(socket.error, e):
            print('Error receiving data: {}'.format(e))
            sys.exit(1)
        if not len(buf):
            break
        # write the data
        sys.stdout.write(str(buf))

SEND_BUF_SIZE = 4096
RECV_BUF_SIZE = 4096

def modify_buff_size():
    print('MODIFYING BUFFER SIZE')
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # get size of the socket's send buffer
    bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print('Buffer size [BEFORE]: {}'.format(bufsize))

    sock.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, SEND_BUF_SIZE)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, RECV_BUF_SIZE)

    bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print('Buffer size [AFTER]: {}'.format(bufsize))


if __name__ == '__main__':
    print_machine_info()
    get_remote_machine_info()
    convert_ip4_address()
    find_service_name()
    convert_integer()
    test_socket_timeout()
    modify_buff_size()
    if len(sys.argv) > 0:
        network_error_handling(host, port, filename)
