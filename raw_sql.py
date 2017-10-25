# -*- coding:utf-8 -*-
from consts import DB_URI
from sqlalchemy import create_engine

eng = create_engine(DB_URI)
with eng.connect() as con:
    con.execute('drop table if EXISTS users')
    con.execute('create table users(Id INT PRIMARY KEY AUTO_INCREMENT,'
                'Name VARCHAR(25))')
    con.execute("insert into users(Name) VALUES ('xiaoming')")
    con.execute("insert into users(Name) VALUES ('wanglang')")
    rs =con.execute("select * from users")
    for row in rs:
        print row