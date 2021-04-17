# encoding = utf-8
#  建库语句
createdatabase = 'CREATE DATABASE IF NOT EXISTS automation DEFAULT CHARSET utf8mb4 COLLATE utf8mb4_general_ci;'
#  建表语句
createtable = """
        CREATE TABLE automationdata(
             ID int primary key not null auto_increment comment '主键',
            testData varchar(40) unique not null comment '姓名',
            expectData varchar(40) not null comment '城市'
        )engine = innodb character set utf8mb4 comment '测试数据表';
    """
#  插入数据
insertdata = "insert into automationdata(testData, expectData) values(%s, %s);"
datalist = [('selenium xml DataDriven', 'davieyang'), ('selenium excel DataDriven', 'davieyang'),
            ('selenium ddt data list', 'davieyang')]
#  删表语句
droptable = 'DROP TABLE testdata;'
#  查询语句
selectdata = "select * from automationdata"
