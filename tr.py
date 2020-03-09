import MySQLdb
import sqlite3
con=MySQLdb.connect("localhost","root","","first")
c=con.cursor()
#sql="create table st(id int,name char(50),address char(30),salary int)"
#sql="drop table st"
#sql ="create table f(code int not null ,name char(20),salary int,constraint pk primary key (code))"
sql="select * from f where code=1"
code=[]
name=[]
salary=[]
try:
    c.execute(sql)
    var=c.fetchall()
    for el in var:
        code.append(el[0])
        name.append(el[1])
        salary.append(el[2])
    print (code,name,salary)
except:
    con.rollback()
print (len(code))
con.close
