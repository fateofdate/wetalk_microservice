import re
import socket
from db import TmpDbOperator
from service import Service


class MetaService(Service):

    def send(self, data, ip, port):
        a = (ip, port)
        self.udp_socket.sendto(data, a)
        print("1")

    def recv(self) -> bytes:
        data = self.udp_socket.recv(1024)
        return data

    def conn(self, ip, port):
        self.udp_socket.connect((ip, port))


class MetaTmpDbService:
    WE_TALK_INFO = ('0.0.0.0', 9093)
    tmp_db = TmpDbOperator()

    def __init__(self):
        self.tmp_db = TmpDbOperator()
        print("-------建议端口9092--------")
        ip = input("输入监听IP")
        port = int(input("输入监听端口"))
        # super(MetaTmpDbService, self).__init__(ip, port)
        self.service = MetaService(ip, port)
        self.service.conn('192.168.0.13', 9091)

    def add_to(self, username: str, ip_port: tuple):
        print(f"添加 {username}{ip_port}")
        self.tmp_db.add(username, ip_port)
        print('1')

    def change(self):
        pass

    def delete(self, username: str):
        self.tmp_db.delete(username)

    def find(self, username) -> list:
        return self.tmp_db.find(username)

    def send(self, data, ip, port):
        print("正在发送中")
        self.service.send(data, ip, port)
        print("已发送")

    def start(self):
        msg = self.service.recv()
        msg = msg.decode("utf-8")
        print(msg)
        try:
            username = re.findall('#(.*?)@', msg)[0]
            ip = re.findall('@(.*?)%', msg)[0]
            port = re.findall('%(.*?)%', msg)[0]
            self.add_to(username, (ip, port))
            self.send(f"用户 {username} 已上线".encode("utf-8"), ip, 9091)
        except (ValueError, OSError, TypeError):
            pass


db_service = MetaTmpDbService()


while True:
    db_service.start()
