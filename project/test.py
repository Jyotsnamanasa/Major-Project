'''from sqlite3 import *
from datetime import date
import time

roll='18031A0521'
branch='CSE'
name='jyotsna'
year='4'
mailid='mjmanasa2015@gmail.com'
date1=date.today()
time1=time.strftime("%H:%M")
status="present"
con=connect("sample.db")
cur=con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS sample(RollNumber text PRIMARY KEY,Name text NOT NULL,Branch text NOT NULL,Year text NOT NULL, mailid text NOT NULL,Day date NOT NULL,time timestamp not null,status text not null);")
#cur.execute("insert into sample values(?,?,?,?,?,?,?,?)",(roll,name,branch,year,mailid,date1,time1,status))
cur.execute("select * from sample")
p=cur.fetchall()
print(p)
con.commit()
con.close()
import glob
import shutil
import os

src_dir = "Training_images/1.png"
dst_dir = "admin_images/1.png"
#for jpgfile in glob.iglob(os.path.join(src_dir, "*.jpg")):
shutil.copy(src_dir, dst_dir)'''
from sqlite3 import *
con=connect('attendance.db')
cur=con.cursor()
cur.execute("select * from attendance ")

p=cur.fetchall()
print(p)