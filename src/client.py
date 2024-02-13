#!/usr/bin/env python3
import socket
import json

if __name__ == '__main__':
    msgFromClient       = "Hello UDP Server"
    serverAddressPort   = ("127.0.0.1", 20001)
    bufferSize          = 1024

    # Create a UDP socket at client side
    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)   
    count = 1; numCubes = 3
    while True:
        cube_dict = {}
        for i in range(numCubes):
            detect_dict = {}
            detect_dict['probability'] = 0.5
            detect_dict['xmin'] = 10
            detect_dict['xmax'] = 15
            detect_dict['ymin'] = 11
            detect_dict['ymax'] = 16
            detect_dict['Class'] = 'cube'
            detect_dict['xmin_dist'] = 12
            detect_dict['ymin_dist'] = 13
            cube_dict['Cube' + str(i)] = detect_dict
        string_dict = json.dumps(cube_dict)            
        bytesToSend = str.encode(string_dict)
        # Send to server using created UDP socket
        UDPClientSocket.sendto(bytesToSend, serverAddressPort)