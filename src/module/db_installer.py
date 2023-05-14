import sqlite3


class DbInstaller:
    def __init__(self):
        self.conn = sqlite3.connect('../../data/server.db')
        print("-------------用户数据库初始化成功-------------")
        self.conn2 = sqlite3.connect('../../data/tmp.db')
        print("-------------验证数据库初始化成功-------------")
        self.operator = self.conn.cursor()
        print("---------用户数据库游标对象初始化成功-----------")
        self.operator_tmp = self.conn2.cursor()
        print("---------验证数据库游标对象初始化成功-----------")

    def init_user_tables(self):
        cmd_create_table = """
        CREATE TABLE USERS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        USERNAME TEXT NOT NULL,
        PASSWORD TEXT NOT NULL,
        ROOT_GROUP INTEGER NOT NULL
        );
        """
        self.operator.execute(cmd_create_table)
        self.conn.commit()
        print("----------用户数据库用户表初始化完成---------------")

    def init_tmp_tables(self):
        cmd_create_table = """
        CREATE TABLE TMP(
        USERNAME TEXT PRIMARY KEY ,
        IP INTEGER NOT NULL ,
        PORT INTEGER NOT NULL     
        );
        """
        self.operator_tmp.execute(cmd_create_table)
        self.conn2.commit()
        print("------------IP数据库初始化完成--------------")


if __name__ == '__main__':
    installer = DbInstaller()
    installer.init_tmp_tables()
