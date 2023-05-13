import sqlite3


class DbOperator:
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
        print("用户信息查找完毕:", user_list[0])
        return user_list[0]
        # self.conn.commit()

# db = DbOperator()
# db.find("HZ2023")
# db.delete(4)
# db.add('laqweddk', '12qweq3131', 0)
