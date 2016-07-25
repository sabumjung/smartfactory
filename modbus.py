# Data acquisition from Modus register

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
