import sqlite3


class DB:
    dbpath = '../res/db/users.db'
    conn = sqlite3.connect(dbpath, check_same_thread=False)
    cursor = conn.cursor()

    def __int__(self):
        self.conn = sqlite3.connect(self.dbpath, check_same_thread=False)
        print(1)

    def user_exist_check(self, user_id):
        query = f'SELECT user_id FROM users WHERE user_id="{user_id}"'
        result = 0
        try:
            if self.cursor.execute(query).fetchall()[0][0] == user_id:
                result = 200
            else:
                result = 400
        except Exception as e:
            print(e)
            result = 400
        return result
        # print(self.cursor.execute(query).fetchall())

    def get_all(self, data):
        print(data)
