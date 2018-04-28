# -*- coding:utf-8 -*-
#
import MySQLdb


class MySqlCreater(object):
    def __init__(self, host, port, user, passwd, db, charset='utf8'):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.db = db
        self.charset = charset
        self.conn = None
        self.cursor = None

    def open(self):
        self.conn = MySQLdb.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            passwd=self.passwd,
            db=self.db,
            charset=self.charset
        )
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close

    def execute(self, sql, params=[]):
        try:
            self.open()
            self.cursor.execute(sql, params)
            self.conn.commit()
            self.close()
        except Exception as e:
            print(e)

    def fetchone(self, sql, params=[]):
        try:
            self.open()
            self.cursor.execute(sql, params)
            result = self.cursor.fetchone()
            self.close()
            return result
        except Exception as e:
            print(e)

    def fetchall(self, sql, params=[]):
        try:
            self.open()
            self.cursor.execute(sql, params)
            result = self.cursor.fetchall()
            self.close()
            return result
        except Exception as e:
            print(e)


if __name__ == '__main__':
    """
    name = raw_input("请输入姓名：")
    gender = raw_input("请输入性别：")

    sql = "insert into students(name, gender) values(%s, %s)"
    params = [name, gender]
    mysql = MySqlCreater("10.10.120.12", 3306, "root", "root", "students")
    mysql.execute(sql, params)
    """
    sql = "select stuid, name from students where stuid>2"
    mysql = MySqlCreater("10.10.120.12", 3306, "root", "root", "students")
    result = mysql.fetchall(sql)
    print(result)
    # 输出结果为元组