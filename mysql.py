#!/usr/bin/python
# -*- coding:utf-8 -*-
import pymysql.cursors

class Mysql:

  def queryData(self):
      config = {
          'host': '127.0.0.1',
          'port': 3306,
          'user': 'root',
          'password': '1225',#密码
          'db': 'MeiZi',
          'charset': 'utf8',
          'cursorclass': pymysql.cursors.DictCursor,
      }
      # Connect to the database
      connection = pymysql.connect(**config)

      try:
          with connection.cursor() as  cursor:
              sql = "SELECT * FROM home_meizi" #sql语句
              cursor.execute(sql)
              row = cursor.fetchall() #我这边查询的是第一条的数据
              print(row)
              result = {"msg": "ok", "data": row, "code": 200}
              return result
          connection.commit()
      finally:
          connection.close()