import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.bind(('192.168.0.13', 8080))
# client.bind(('192.168.0.13', 8081))
# client.connect(('192.168.0.13', 9091))
client.connect(('192.168.0.13', 9091))
# client.connect(('47.236.23.14', 3389))
send_address = ('192.168.0.13', 9091)
# send_address = ('47.236.23.14', 3389)

while True:
    # data = client.recv(1024).decode("utf-8")
    # print(data)
    username = input("输入用户名")
    password = input("输入密码")
    package = f"#{username}@{password}"
    client.sendto(package.encode("utf-8"), send_address)
    data = client.recv(1024).decode("utf-8")
    print(data)
# def send():
#     while True:
#         data = input('输入你要发送的消息')
#         client.sendto(bytes(data.encode('utf-8')), send_address)
#         if len(data) >= 1:
#             continue
#
#
# def recv():
#     while True:
#         data = client.recv(1024)
#         print("\n" + data.decode())
#         continue
#
#
# t1 = threading.Thread(target=send)
# t2 = threading.Thread(target=recv)
# t2.start()
# t1.start()



