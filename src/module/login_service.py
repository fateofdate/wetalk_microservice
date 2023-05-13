import socket
import threading
from db import DbOperator
from hashlib import md5
import time


class Grander:
    # 初始化数据库
    def __init__(self):
        self.DbOperator = DbOperator()
        self.hash_md5 = md5()

    def _md5_pwd(self, password: str) -> str:
        """
        md5加密模块
        :param password: 传入的密码字符串
        :return: 返回md5加密后的字符串
        """
        self.hash_md5.update(password.encode("utf-8"))
        return self.hash_md5.hexdigest()

    def _get_users_info(self, username: str) -> tuple:
        """
        获取用户信息
        :param username: 用户名
        :return: 返回一个元组类型 (ID, 用户名, 密码哈希值, 权限组)
        """
        return self.DbOperator.find(username)

    def verify_users(self,
                     username: str,
                     password: str) -> bool:
        """
        用户登录验证
        :param username: 用户传入的用户名
        :param password: 用户传入的密码
        :return: 返回是否登录 True为登录, False为禁止登录
        """
        if len(self._get_users_info(username)) != 0:
            _, username_db, pwd_md5, _ = self._get_users_info(username)
            if pwd_md5 == self._md5_pwd(password):
                return True
            return False
        return False

    def exist_users_verify(self, username: str) -> bool:
        """
        判断用户是否存在
        :param username: 用户传入的用户名
        :return: 返回是否存在该用户名，存在则为True，不存在为False
        """
        if len(self._get_users_info(username)) == 0:
            return True
        else:
            return False

    def register_users(self,
                       username: str,
                       password: str,
                       verify_pwd: str
                       ) -> int:
        """
        用户注册
        :param username: 用户传入用户名
        :param password: 用户传入密码
        :param verify_pwd: 二次确认密码
        :return: 0 成功注册 1 两次密码不相等 2 用户名已经存在
        """
        if self.exist_users_verify(username):
            return 2
        if password != verify_pwd:
            return 1
        self.DbOperator.add(username, password, 1)
        return 0

    # 管理员指令判断
    def condition_cmd(self):
        pass


class LoginService:
    IP_LIST = dict()
    # USER_LIST = dict()
    # USER_STATU = dict()
    DB_SERVICE_INFO = ("0.0.0.0", 8081)

    def __init__(self):
        self.grander = Grander()
        print("----------守护者加载完成--------------")
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(('0.0.0.0', 8080))
        print("--------socket服务器初始化完成--------")

    def _error_send(self,
                    ip_port: tuple,
                    data: str):
        """
        错误返回代码
        :param ip_port: ip与port构成的元组
        :param data: 错误代码
        :return: None
        """
        self._send_data(ip_port, bytes(data.encode("utf-8")))

    def _first_conn_save_ip(self):
        data, ip = self._recv()
        if data.decode("utf-8") not in self.IP_LIST:
            self.IP_LIST[data] = ip

    def _recv(self) -> tuple:
        """
        接受方法,可用于登陆校验
        :return: tuple
        """
        data, ip = self.socket.recvfrom(1024)
        return data, ip
        # print(ip)
        # if ip not in self.USER_LIST.keys():
        #     self.USER_LIST[data] = ip
        #
        # print(str(data.decode('utf_8')))
        # self.send_all_data(data)
        # user_ip, port = self.socket.getpeername()
        # print(user_ip)
        # self.socket.sendto(b'hello', ('192.168.0.13', 9090))

    def _send_data(self,
                   ip_port: tuple,
                   data: bytes):
        """

        :param ip_port: 元组ip与port
        :param data: bytes类型的数据
        :return: None
        """
        self.socket.sendto(data, ip_port)

    def login(self):
        """
        这里要写db的微服务组 14/05/2023 未完成
        :return:
        """
        data, ip_port = self._recv()
        self.IP_LIST[data[0]] = ip_port

        if self.grander.verify_users(data[0], data[1]):    # 这里写DB的微服务组
            pass
        self._send_data(ip_port, bytes(1))


class Login(LoginService):

    def login(self):
        pass

    # 发送信息给所有用户
    # def _send_all_data(self,
    #                    user_ip: tuple,
    #                    data: bytes):
    #     """
    #
    #     :param user_ip: ip与port 元组
    #     :param data: 发送内容
    #     :return: None
    #     """
    #     for ip_port in self.USER_LIST.keys():
    #         if ip_port != user_ip:
    #             self.socket.sendto(data, ip_port)




