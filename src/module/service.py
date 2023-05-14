import socket


class Service:
    def __init__(self,
                 ip: str,
                 port: int):

        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udp_socket.bind((ip, port))

    def recv(self) -> bytes:
        pass

    def send(self, data, ip, port):
        pass

    def conn(self, ip, port):
        pass
