import sqlite3


class DbInstaller:
    def __init__(self):
        self.conn = sqlite3.connect('../../data/server.db')
        print("-------------数据库初始化成功-------------")
        self.operator = self.conn.cursor()
        print("---------数据库游标对象初始化成功-----------")

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
        print("--------数据库用户表创建完成---------------")


if __name__ == '__main__':
    installer = DbInstaller()
    installer.init_user_tables()
