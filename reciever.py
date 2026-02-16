import socket
import struct

PORT = 4210

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", PORT))

print("Listening on port", PORT)


while True:
    data, addr = sock.recvfrom(1024)

    throttle, steering = struct.unpack("Bb", data)

    print(f"Steering: {steering} | Throttle: {throttle} | from: {addr}")