"""The Py3 Socket server module."""
import binascii
import hashlib
import sys
import socket
import time

SOCKET_ADDRESS = "127.0.0.1"
SOCKET_PORT = 6996
BUFFER_SIZE = 2048


def build_server_tcp(address: str, port: int):
    """Builds an TCP server."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((address, port))
    sock.listen(1)
    print("Successfully running at {0}:{1}.".format(address, str(port)))
    clients_treated = 0

    with open("log_tcp.txt", "w") as logger:
        while True:
            connection, address = sock.accept()
            clients_treated += 1
            print("Received client no. {0}.".format(clients_treated))
            logger.write("Received client {0} ({1}:{2})\n".format
                         (
                             clients_treated,
                             str(address[0]),
                             str(address[1])
                         ))

            thistime = time.strftime(
                "%d/%m/%Y %H:%M:%S", time.localtime(time.time()))
            logger.write("Time: {0}.\n\n".format(thistime))

            connection.close()
            logger.flush()

            if input("Continue receiving clients? y/anything") == "y":
                break

    print("Server closed.")


def build_server_udp(address: str, port: int):
    """Builds an UDP server."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((address, port))
    clients_treated = 0

    with open("log_udp.txt", "w") as logger:
        while True:
            data, address = sock.recvfrom(BUFFER_SIZE)
            clients_treated += 1
            logger.write("Received client {0} ({1}:{2})\n".format
                         (
                             clients_treated,
                             str(address[0]),
                             str(address[1])
                         ))

            thistime = time.strftime(
                "%d/%m/%Y %H:%M:%S", time.localtime(time.time()))
            logger.write("Time: {0}.\n".format(thistime))

            logger.write("Data ({0}): \"{1}\".\n".format(str(len(data)), data.decode("UTF-8")))
            hexstring = binascii.hexlify(data)
            logger.write("HEX: \"{0}\".\n".format(hexstring.decode("UTF-8")))

            md5 = hashlib.md5()
            md5.update(hexstring)
            md5f = md5.hexdigest()
            logger.write("MD5 of HEX: \"{0}\".\n".format(md5f))

            sha256 = hashlib.sha256()
            sha256.update(hexstring)
            sha256f = sha256.hexdigest()
            logger.write("SHA256 of HEX: \"{0}\".\n".format(sha256f))

            logger.flush()
            if input("Continue receiving clients? y/anything") == "y":
                break

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Must specify mode (TCP/UDP).")
        exit()

    MODE = sys.argv[1]
    if MODE == "TCP":
        build_server_tcp(SOCKET_ADDRESS, SOCKET_PORT)
    elif MODE == "UDP":
        build_server_udp(SOCKET_ADDRESS, SOCKET_PORT)
    else:
        print("Unable to determine what you want.")

