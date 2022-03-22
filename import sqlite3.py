import sqlite3
con = sqlite3.connect("sample.db",check_same_thread=False);
def getAll():
    query="select * from student"
    cur = con.cursor()
    cur.execute(query)
    all_data=cur.fetchall()
    con.commit()
    return(all_data)

def insert(data):
    query1 = "create table if not exists student(Name varchar(10),Rollno varchar(20),Mark int(3))"
    params = (data["Name"],data["Rollno"])
    query = "insert into student values(?,?,?)"
    cur=con.cursor()
    cur.execute(query1)
    cur.execute(query,params)
    cur.commit()