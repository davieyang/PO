# encoding = utf-8
"""
__title__ = ''
__author__ = 'davieyang'
__mtime__ = '2018/4/21'
"""
import pymysql


class Parse_Mysql(object):  # 定义解析Mysql类
    def __init__(self, host, port, dbName, username, password, charset):
        """
        初始化类
        :param host:
        :param port:
        :param dbName:
        :param username:
        :param password:
        :param charset:
        """
        self.conn = pymysql.connect(
            host=host,
            port=port,
            db=dbName,
            user=username,
            password=password,
            charset=charset
        )
        self.cur = self.conn.cursor()

    def create_database(self, createdb):
        """
        建库函数，执行sql语句建库
        :param createdb:
        :return:
        """
        try:
            self.cur.execute(createdb)
        except pymysql.Error as e:
            raise e
        else:
            self.cur.close()
            self.conn.commit()
            self.conn.close()
            print(u"建据库成功...")

    def create_table(self, database, createtable):
        """
        建表函数，执行sql语句进行建表
        :param database:
        :param createtable:
        :return:
        """
        try:
            self.conn.select_db(database)
            self.cur.execute(createtable)
        except pymysql.Error as e:
            raise e
        else:
            self.cur.close()
            self.conn.commit()
            self.conn.close()
            print(u"建表成功...")

    def insert_data(self, database, insertdata, datalist):
        """
        执行SQL语句进行表数据插入
        :param database:
        :param insertdata:
        :param datalist:
        :return:
        """
        try:
            self.conn.select_db(database)
            self.cur.executemany(insertdata, datalist)
        except pymysql.Error as e:
            raise e
        else:
            self.conn.commit()
            print(u"初始数据插入成功")
            self.cur.close()
            self.conn.close()

    def select_data_from_table(self, database, selectdata):
        """
        执行SQL查询语句进行查询数据
        :param database:
        :param selectdata:
        :return:
        """
        try:
            self.conn.select_db(database)
            self.cur.execute(selectdata)
            dataTuple = self.cur.fetchall()
            return dataTuple
        except pymysql.Error as e:
            raise e

    def drop_table(self, database, droptable):
        """
        执行删表SQL进行删表
        :param database:
        :param droptable:
        :return:
        """
        try:
            self.conn.select_db(database)
            self.cur.execute(droptable)
        except pymysql.Error as e:
            raise e
        else:
            self.cur.close()
            self.conn.commit()
            self.conn.close()
            print(u"删表成功...")

    def close_database(self):
        """
        关闭数据库连接
        :return:
        """
        self.cur.close()
        self.conn.commit()
        self.conn.close()


if __name__ == "__main__":
    db = Parse_Mysql(
        host="localhost",
        port=3306,
        dbName="mysql",
        username="root",
        password="",
        charset="utf8"
    )
    # createdatabase = 'CREATE DATABASE IF NOT EXISTS automation DEFAULT CHARSET utf8mb4 COLLATE utf8mb4_general_ci;'
    # db.create_database(createdatabase)
    # createtable = """
    #    CREATE TABLE automationdata(
    #         ID int primary key not null auto_increment comment '主键',
    #        NAME varchar(40) unique not null comment '姓名',
    #        City varchar(40) not null comment '城市'
    #    )engine = innodb character set utf8mb4 comment '测试数据表';
    #"""
    # db.create_table("automation", createtable)
    # insertdata = "insert into automationdata(NAME, City) values(%s, %s);"
    # datalist = [('selenium xml DataDriven', 'davieyang'),('selenium excel DataDriven', 'davieyang'),('selenium ddt data list', 'davieyang')]
    selectdata = "select * from automationdata"
    # db.insert_data("automation", insertdata, datalist)
    data = db.select_data_from_table("automation", selectdata)
    print(data)

