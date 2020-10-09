# -*- coding:utf-8 -*-
"""
@author:hyongchang
@file:test_case_07.py
@time:2020/07/01
"""
import pymysql

class PyMySQLUtils:

    def __init__(self, host, user, password, database, port, charset="utf8"):
        try:
            self.conn = pymysql.connect(host, user, password, database, port, charset=charset)
            self.cursor = self.conn.cursor()
        except pymysql.err.OperationalError as err:
            print(err.args)

    def query_fetchone(self, sql, args=None):
        self.cursor.execute(sql, args=args)
        return self.cursor.fetchone()

    def query_fetchmany(self, sql, size=1, args=None):
        self.cursor.execute(sql, args=args)
        return self.cursor.fetchmany(size=size)

    def query_fecthall(self, sql, args=None):
        self.cursor.execute(sql, args=args)
        return self.cursor.fetchall()

    def __exec_sql(self,sql,args=None):
        try:
            self.cursor.execute(sql, args=args)
            count = self.cursor.rowcount
            self.conn.commit()
            return count
        except:
            self.conn.rollback()
            raise pymysql.err.raise_mysql_exception(args)
    def insert_db(self, sql, args=None):
        return self.__exec_sql(sql, args=args)

    def update_db(self, sql, args=None):
        return self.__exec_sql(sql, args=args)

    def delete_db(self, sql, args=None):
        return self.__exec_sql(sql, args=args)

    def close(self):
        self.cursor.close()
        self.conn.close()

