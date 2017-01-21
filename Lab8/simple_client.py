"""Simple socket client for the simple socket client."""
import sys
import socket
import time

SOCKET_ADDRESS = "127.0.0.1"
SOCKET_PORT = 6996


def build_client_tcp(address: str, port: int):
    """Builds the TCP client."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((address, port))
        time.sleep(1)
        sock.close()
    except:
        print("Cannot connect to the target server.")

def build_client_udp(address: str, port: int, message: str):
    """Builds the UDP client."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(message.encode(), (address, port))

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("You must give as args the mode, server address, the port and the message to send.")
        exit()

    MODE = sys.argv[1]
    SOCKET_ADDRESS = sys.argv[2]
    SOCKET_PORT = int(sys.argv[3])
    MESSAGE = sys.argv[4]

    if MODE == "TCP":
        build_client_tcp(SOCKET_ADDRESS, SOCKET_PORT)
    elif MODE == "UDP":
        build_client_udp(SOCKET_ADDRESS, SOCKET_PORT, MESSAGE)
    else:
        print("Unable to determine what you want.")
