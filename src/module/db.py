import sqlite3


class UsrDbOperator:
    def __init__(self):
        self.conn = sqlite3.connect('../../data/server.db')
        self.operator = self.conn.cursor()

    def add(self, *args):
        username, password, root_group = args
        cmd_add = f"INSERT INTO USERS (USERNAME, PASSWORD, ROOT_GROUP)" \
                  f" VALUES('{username}' , '{password}', '{root_group}');"
        self.operator.execute(cmd_add)
        print(f"用户信息添加成功username:{username},password:{password},root_group{root_group}")
        self.conn.commit()

    def delete(self, user_id):
        cmd_delete = f"DELETE FROM USERS WHERE ID={user_id}"
        self.operator.execute(cmd_delete)
        self.conn.commit()
        print(f'用户信息删除成功id:{user_id}')

    def change(self):
        pass

    def find(self, username) -> tuple:
        cmd_find = f"SELECT * FROM USERS WHERE USERNAME='{username}'"
        info_user = self.operator.execute(cmd_find)
        user_list = [i for i in info_user]
        print("用户信息查找完毕:", user_list)
        return user_list
        # self.conn.commit()


class TmpDbOperator:
    """
    TMP 数据库操作父类由 db_service 服务中的service类继承
    """
    def __init__(self):
        self.conn_tmp = sqlite3.connect('../../data/tmp.db')
        self.curr_tmp = self.conn_tmp.cursor()

    def find(self, username) -> list:
        cmd_tmp_find = f"""
        SELECT * FROM TMP WHERE USERNAME = '{username}'
        """
        db_object = self.curr_tmp.execute(cmd_tmp_find)
        usr_ip_port = [info for info in db_object]
        return usr_ip_port

    def change(self):
        pass

    def add(self,
            username: str,
            ip_port: tuple):
        """

        :param username:
        :param ip_port:
        :return:
        """
        ip, port = ip_port
        cmd_tmp_add = f"""
        INSERT INTO TMP (USERNAME, IP, PORT) VALUES ('{username}', '{ip}', '{port}');
        """
        self.curr_tmp.execute(cmd_tmp_add)
        self.conn_tmp.commit()
        print(f"用户态增加成功:{username}, {ip}, {port}")

    def delete(self, username: str):
        cmd_tmp_delete = f"""
        DELETE FROM TMP WHERE USERNAME = '{username}';
        """
        self.curr_tmp.execute(cmd_tmp_delete)
        self.conn_tmp.commit()
        print(f"用户态删除成功:{username}")

# db = TmpDbOperator()

# db.add('lyk', ('10.2.2.1', 9092))
# db = DbOperator()
# db.find("HZ2023")
# db.delete(4)
# db.add('laqweddk', '12qweq3131', 0)
