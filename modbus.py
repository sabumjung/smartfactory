
import socket
import struct
import time


# Create a TCP/IP socket
TCP_IP = '127.0.0.1'

# Modubus 해당 설정포트
TCP_PORT = 502
BUFFER_SIZE = 39   #39
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((TCP_IP, TCP_PORT))

#7번 : 함수코드
#8~9번 : 제어주소
#10~11번 : 요청/응답 예
#functionCode : 함수코드, 7번째에 위치함(0번부터 시작)
#UnitID

try:
    # Switch Plug On then Off
    unitId = 16   ##16 # Plug Socket
    functionCode = 5 ##5 # Write Single coil

    # Modbus Packet Write
    print("\nSwitching Plug ON...")
    coilId = 1
    req = struct.pack('12B', 0x00, 0x00, 0x00, 0x00, 0x00, 0x06, int(unitId), int(functionCode), 0x08, int(coilId), 0x00, 0x00)
    sock.send(req)
    print("TX: (%s)" %req)

    # Modbus Packet Read
    rec = sock.recv(BUFFER_SIZE)
    print("RX: (%s)" % rec)
    time.sleep(2)

    print("\nSwitching Plug OFF...")

    # Modbus Packet Write
    coilId = 2
    req = struct.pack('12B', 0x00, 0x00, 0x00, 0x00, 0x00, 0x06, int(unitId), int(functionCode), 0x00, int(coilId), 0xff, 0x00)
    sock.send(req)
    print("TX: (%s)" % req)

    # Modbus Packet Read
    rec = sock.recv(BUFFER_SIZE)
    print("RX: (%s)" % rec)
    time.sleep(2)

finally:
    print('\nCLOSING SOCKET')
    sock.close()





#!/usr/bin/env python
# -*- coding: utf_8 -*-

 #Modbus TestKit: Implementation of Modbus protocol in python

 #(C)2009 - Luc Jean - luc.jean@gmail.com
 #(C)2009 - Apidev - http://www.apidev.fr

 #This is distributed under GNU LGPL license, see license.txt


'''
import sys

# add logging capability
import logging
import threading

import modbus_tk
import modbus_tk.defines as cst
import modbus_tk.modbus as modbus
import modbus_tk.modbus_tcp as modbus_tcp

#모드버스에 대한 로그를 생성함
logger = modbus_tk.utils.create_logger(name="console", record_format="%(message)s")

if __name__ == "__main__":

    try:
        # Create the server
        server = modbus_tcp.TcpServer(502,"127.0.0.1",30,None)
        logger.info("running...")
        logger.info("enter 'quit' for closing the server")

        server.start()

        slave_1 = server.add_slave(1)
        slave_1.add_block('0', cst.HOLDING_REGISTERS, 100, 100)
        while True:
            cmd = sys.stdin.readline()
            args = cmd.split(' ')
            if cmd.find('quit') == 0:
                sys.stdout.write('bye-bye\r\n')
                break
            elif args[0] == 'add_slave':
                slave_id = int(args[1])
                server.add_slave(slave_id)
                sys.stdout.write('done: slave %d added\r\n' % (slave_id))
            elif args[0] == 'add_block':
                slave_id = int(args[1])
                name = args[2]
                block_type = int(args[3])
                starting_address = int(args[4])
                length = int(args[5])
                slave = server.get_slave(slave_id)
                slave.add_block(name, block_type, starting_address, length)
                sys.stdout.write('done: block %s added\r\n' % (name))
            elif args[0] == 'set_values':
                slave_id = int(args[1])
                name = args[2]
                address = int(args[3])
                values = []
                for v in args[4:]:
                    values.append(int(v))
                slave = server.get_slave(slave_id)
                slave.set_values(name, address, values)
                values = slave.get_values(name, address, len(values))
                sys.stdout.write('done: values written: %s\r\n' % (str(values)))
            elif args[0] == 'get_values':
                slave_id = int(args[1])
                name = args[2]
                address = int(args[3])
                length = int(args[4])
                slave = server.get_slave(slave_id)
                values = slave.get_values(name, address, length)
                sys.stdout.write('done: values read: %s\r\n' % (str(values)))
            else:
                sys.stdout.write("unknown command %s\r\n" % (args[0]))
    finally:
        server.stop()

'''