# Packages to be imported

from datetime import date
from fileinput import filename
import time
import pyttsx3
from tkinter import *
from tkinter import ttk
from tokenize import String
from PIL import Image, ImageTk
from tkinter import messagebox
from sqlite3 import *
import face_recognition
import imutils
import time
import cv2
import csv
import requests
import os
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
import pickle
from imutils import paths
import numpy as np
import imutils
from collections.abc import Iterable
import datetime
import smtplib 
from tkinter import messagebox
from tkcalendar import Calendar
from email.mime.multipart import MIMEMultipart 

from email.mime.text import MIMEText 

from email.mime.base import MIMEBase 

from email import encoders 
from pynput.keyboard import Key, Listener
from tkinter import filedialog

import shutil



l=["Jan","Feb","March","April","May","June","July","Aug","Sept","Oct","Nov","Dec"]
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    
    engine.runAndWait()

def sendMail(file1):
        
        fromaddr = "manasamulukutla@gmail.com"

        toaddr = "manasamulukutla@gmail.com"

        
        # instance of MIMEMultipart 

        msg = MIMEMultipart() 

        
        # storing the senders email address   

        msg['From'] = fromaddr 

        
        # storing the receivers email address  

        msg['To'] = toaddr 

        
        # storing the subject  

        msg['Subject'] = "PythonMail"

        
        # string to store the body of the mail 

        body = "Hi! I am hereby sending an attatchment of students attendance report"

        
        # attach the body with the msg instance 

        msg.attach(MIMEText(body, 'plain')) 

        
        # open the file to be sent  
        l=[str(current_time.day),str(current_time.month),str(current_time.year)]
        l="-".join(l)
        
        filename = file1

        attachment = open(filename, "rb") 

        
        # instance of MIMEBase and named as p 

        p = MIMEBase('application', 'octet-stream') 

        
        # To change the payload into encoded form 
        p.set_payload((attachment).read()) 

        
        # encode into base64 
        encoders.encode_base64(p) 

        

        p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 

        
        # attach the instance 'p' to instance 'msg' 
        msg.attach(p) 

        #messagebox.showinfo("Success","Sending Mail")
        # creates SMTP session 

        s = smtplib.SMTP('smtp.gmail.com', 587) 

        
        # start TLS for security 
        s.starttls() 

        
        # Authentication 

        s.login(fromaddr, "mjmanasa") 

        
        # Converts the Multipart msg into a string 

        text = msg.as_string() 

        
        # sending the mail 
        s.sendmail(fromaddr, toaddr, text) 
        
        
        # terminating the session 
        s.quit() 
        #messagebox.showinfo("Success","Successfully sent")
        print("Done!") 

def logout():
    p=messagebox.askquestion("LogOut","Do you really want to logout?")
    #print(p)
    if p=="yes":
        frame1.pack_forget()
        messagebox.showinfo("Success","LogOut Successful")
        f_login.pack(pady="165")
def about():
    newWindow = Toplevel(root)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("About Developer")
 
    # sets the geometry of toplevel
    newWindow.geometry("1080x700+10+10")
    
    # A Label widget to show in toplevel
    Label(newWindow,text ="About Developer",fg="black", font=("times new roman", 30, "bold")).pack(padx=25,pady=30)
    Label(newWindow,text="This Project \n\n\"Smart Attendance System using Face Detection\"\n \n is developed by the students of\n \n\"University College of Engineering Narasaraopet JNTUK\"\n \nunder the esteemed guidance of\n \nDr. G. Madhavi (HOD of CSE). \n\nThe students worked on this project are\n M. Jyotsna Manasa \n P.Sampath Sai \n G.SriLakshmi\n A. Eswar Vinay kumar \nM. DharmaRao",fg="black",font=("times new roman", 20, "bold")).pack(padx=25)
    

def manage():
    global newWindow
    newWindow = Toplevel(root)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("Manage Students")
 
    # sets the geometry of toplevel
    newWindow.geometry("1080x700+10+10")
    newWindow.maxsize(1080, 700)
    newWindow.minsize(1080, 700)
    Manage_Frame=Frame(newWindow,bd=4,relief=RIDGE,bg="mint cream")
    Manage_Frame.place(x=10,y=10,width=450,height=650)
    m_title=Label(Manage_Frame,text="Manage Students",bg="mint cream",fg="black",font=("times new roman",20,"bold"))
    m_title.grid(row=0,columnspan=2,pady=15)

    lbl_roll=Label(Manage_Frame,text="Roll No.",bg="mint cream",fg="black",font=("times new roman",15,"bold"))
    lbl_roll.grid(row=1,column=0,pady=5,padx=30,sticky="w")
    txt_roll=Entry(Manage_Frame,textvariable=Roll_No_var,font=("times new roman",15,"bold"),bd=3,relief=GROOVE)
    txt_roll.grid(row=1,column=1,pady=5,padx=30,sticky="w")

    lbl_name=Label(Manage_Frame,text="Name",bg="mint cream",fg="black",font=("times new roman",15,"bold"))
    lbl_name.grid(row=2,column=0,pady=5,padx=30,sticky="w")
    txt_name=Entry(Manage_Frame,textvariable=name_var,font=("times new roman",15,"bold"),bd=3,relief=GROOVE)
    txt_name.grid(row=2,column=1,pady=5,padx=30,sticky="w")

    lbl_branch=Label(Manage_Frame,text="Branch",bg="mint cream",fg="black",font=("times new roman",15,"bold"))
    lbl_branch.grid(row=3,column=0,pady=5,padx=30,sticky="w")
    combo_branch=ttk.Combobox(Manage_Frame,textvariable=branch,font=("times new roman",13,"bold"),state="readonly")
    combo_branch['values']=("CSE","ECE","EEE","CE","MECH")
    combo_branch.grid(row=3,column=1,pady=5,padx=30,sticky="w")

    lbl_email=Label(Manage_Frame,text="Email",bg="mint cream",fg="black",font=("times new roman",15,"bold"))
    lbl_email.grid(row=4,column=0,pady=5,padx=30,sticky="w")
    txt_email=Entry(Manage_Frame,textvariable=email_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
    txt_email.grid(row=4,column=1,pady=5,padx=30,sticky="w")
    
    lbl_year=Label(Manage_Frame,text="Year",bg="mint cream",fg="black",font=("times new roman",15,"bold"))
    lbl_year.grid(row=5,column=0,pady=5,padx=30,sticky="w")
    combo_year=ttk.Combobox(Manage_Frame,textvariable=year_var,font=("times new roman",13,"bold"),state="readonly")
    combo_year['values']=("1",'2','3','4')
    combo_year.grid(row=5,column=1,padx=30,pady=5,sticky="w")

    lbl_gender=Label(Manage_Frame,text="Gender",bg="mint cream",fg="black",font=("times new roman",15,"bold"))
    lbl_gender.grid(row=6,column=0,pady=5,padx=30,sticky="w")
    combo_gender=ttk.Combobox(Manage_Frame,textvariable=gender_var,font=("times new roman",13,"bold"),state="readonly")
    combo_gender['values']=("Male","Female","Other")
    combo_gender.grid(row=6,column=1,padx=30,pady=5,sticky="w")


    lbl_contact=Label(Manage_Frame,text="Contact",bg="mint cream",fg="black",font=("times new roman",15,"bold"))
    lbl_contact.grid(row=7,column=0,pady=5,padx=30,sticky="w")
    txt_contact=Entry(Manage_Frame,textvariable=contact_var,font=("times new roman",14,"bold"),bd=5,relief=GROOVE)
    txt_contact.grid(row=7,column=1,pady=5,padx=30,sticky="w")

    global addphotobtn,addfingerbtn
    lbl_face=Label(Manage_Frame,text="Capture Face Image",bg="mint cream",fg="black",font=("times new roman",15,"bold"))
    lbl_face.grid(row=8,column=0,pady=5,padx=0,sticky="w")
    addphotobtn=Button(Manage_Frame,text="Add Facial Image",font=("times new roman",12,"bold"),bg="green",fg="white",width=16,command=collect_data)
    addphotobtn.grid(row=8,column=1,padx=0,pady=5)
    
    lbl_finger=Label(Manage_Frame,text="Capture fingerPrint",bg="mint cream",fg="black",font=("times new roman",15,"bold"))
    lbl_finger.grid(row=9,column=0,pady=5,padx=0,sticky="w")
    addfingerbtn=Button(Manage_Frame,text="Add FingerPrint",font=("times new roman",12,"bold"),bg="green",fg="white",width=16,command=add_FingerPrint)
    addfingerbtn.grid(row=9,column=1,padx=0,pady=5)



    Btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="mint cream")
    Btn_Frame.place(x=5,y=530,width=430)
    addbtn=Button(Btn_Frame,text="Add",font=("times new roman",12,"bold"),width=10,bg="green",fg="white",command=add_students).grid(row=0,column=0,padx=3,pady=5)
    updatebtn=Button(Btn_Frame,text="Update",font=("times new roman",12,"bold"),bg="green",fg="white",width=10,command=update_data).grid(row=0,column=1,padx=3,pady=5)

    deletebtn=Button(Btn_Frame,text="Delete",font=("times new roman",12,"bold"),bg="green",fg="white",width=10,command=delete_data).grid(row=0,column=2,padx=3,pady=5)
    clearbtn=Button(Btn_Frame,text="Clear",font=("times new roman",12,"bold"),bg="green",fg="white",width=10,command=clear).grid(row=0,column=3,padx=3,pady=5)
    #addphotobtn=Button(Btn_Frame,text="Add Facial Image",font=("times new roman",12,"bold"),bg="green",fg="white",width=16,command=collect_data).grid(row=1,columnspan=2,padx=3,pady=5)
    #updatephotobtn=Button(Btn_Frame,text="Add FingerPrint",font=("times new roman",12,"bold"),bg="green",fg="white",width=16,command=add_FingerPrint).grid(row=1,column=2,columnspan=2,padx=3,pady=5)

    

        #detail frame
    Details_Frame=Frame(newWindow,bd=4,relief=RIDGE,bg="mint cream")
    Details_Frame.place(x=470,y=10,width=600,height=650)
    
    lbl_search=Label(Details_Frame,text="Search",bg="mint cream",fg="black",font=("times new roman",20,"bold"))
    lbl_search.grid(row=0,column=0,pady=10,padx=5,sticky="w")
    combo_search=ttk.Combobox(Details_Frame,width=10,textvariable=search_by,font=("times new roman",13,"bold"),state="readonly")
    combo_search['values']=("RollNumber","Name","Branch", "Year")
    combo_search.grid(row=0,column=1,padx=5,pady=10,sticky="w")
    txt_search=Entry(Details_Frame,textvariable=search_txt,width=20,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
    txt_search.grid(row=0,column=2,pady=10,padx=5,sticky="w")
    searchbtn=Button(Details_Frame,text="Search",bg="green",fg="white",font=("times new roman",12,"bold"),command=search_data,width=8,pady=5).grid(row=0,column=3,padx=5,pady=10)
    showallbtn=Button(Details_Frame,text="Showall",bg="green",fg="white",font=("times new roman",12,"bold"),command=fetch_data,width=8,pady=5).grid(row=0,column=4,padx=5,pady=10)

    #Table frame
    global Student_table
    Table_Frame=Frame(Details_Frame,bd=4,relief=RIDGE,bg="mint cream")
    Table_Frame.place(x=10,y=70,width=580,height=550)
    scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
    scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
    Student_table=ttk.Treeview(Table_Frame,columns=("RollNumber","Name","Branch","Year","Email","Gender","Contact Info"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=Student_table.xview)
    scroll_y.config(command=Student_table.yview)
    Student_table.heading("RollNumber",anchor=CENTER,text="RollNumber")
    Student_table.heading("Name",anchor=CENTER,text="Name")
    Student_table.heading("Branch",anchor=CENTER,text="Branch")
    Student_table.heading("Year",anchor=CENTER,text="Year")
    Student_table.heading("Email",anchor=CENTER,text="Email")
    Student_table.heading("Gender",anchor=CENTER,text="Gender")
    Student_table.heading("Contact Info",anchor=CENTER,text="Contact Info")
    
    
    Student_table['show']="headings"
    Student_table.column("RollNumber",anchor=CENTER,width=150)
    Student_table.column("Name",anchor=CENTER,width=150)
    Student_table.column("Branch",anchor=CENTER,width=150)
    Student_table.column("Year",anchor=CENTER,width=150)
    Student_table.column("Email",anchor=CENTER,width=150)
    Student_table.column("Gender",anchor=CENTER,width=100)
    Student_table.column("Contact Info",anchor=CENTER,width=150)

    Student_table.pack(fill=BOTH,expand=1)
    Student_table.bind("<ButtonRelease-1>",get_cursor)
    fetch_data()

def collect_data():
    sub_data = Roll_No_var.get()
    if sub_data=="":
        messagebox.showerror("Error","Roll number feild should not be empty!",parent=newWindow)
    else:
        print("Starting video stream...")
        cam = cv2.VideoCapture(0)
        time.sleep(5.0)
        total = 0
        flag=0
        path='Training_images'
        speak(" press y to capture image")
        while True:
            
            _, frame = cam.read()
            img = imutils.resize(frame, width=400)
            
            
            
            #cv2.putText(frame, "press Y to capture image", (10,10),cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 255, 0), 2)
            key = cv2.waitKey(1) & 0xFF
            imgpath=f"Training_images/{Roll_No_var.get()}.png"
            cv2.imshow("frame",frame)
            if key==ord('y'):
                cv2.imwrite(imgpath,frame)
                messagebox.showinfo("success","Image captured Successfully!",parent=newWindow)
                flag=1
                time.sleep(2)
                cam.release()
                cv2.destroyAllWindows()
                break

        addphotobtn['text']="Image captured"    

def add_FingerPrint():
    filename1 = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")),parent=newWindow)
    path1=f'fingerprint/{Roll_No_var.get()}.BMP'
        
    shutil.copy(filename1,path1)
    messagebox.showinfo("success","Successfully selected!",parent=newWindow)
    addfingerbtn['text']='finger print added'
def add_students():
    if(Roll_No_var.get()=="" or name_var.get()=="" or branch.get()=="" or year_var.get()=="" or email_var.get()=="" or gender_var.get()=="" or contact_var.get()==""  ): 
        messagebox.showerror("Error","All feilds are required",parent=newWindow)
    else:
        conn=connect("student.db")
        cur=conn.cursor()
        cur.execute("SELECT RollNumber from student")
        p=cur.fetchall()
        flag=0
        if len(p)>0 :
            name=[]
            for i in p:
                name.append(i[0])
            print(name)
            
            if Roll_No_var.get() in name:
                messagebox.showerror("Error",Roll_No_var.get()+" is already available",parent=newWindow)
            else:
                flag=1
        else:
            flag=1
        if(flag==1):
                cur.execute("insert into student values(?,?,?,?,?,?,?)",(Roll_No_var.get(),name_var.get(),branch.get(),year_var.get(),email_var.get(),gender_var.get(),contact_var.get()))
                conn.commit()
                conn.close()
                print("Data inserted")
                '''con1=connect('attendance.db')
                cur1=con1.cursor()
                cur1.execute("INSERT INTO attendance values(?,?,?,?,?,?,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)",(Roll_No_var.get(),name_var.get(),branch.get(),year_var.get(),email_var.get(),0))
                con1.commit()
                con1.close()'''
                con1=connect('attendance_month.db')
                cur1=con1.cursor()
                cur1.execute("INSERT INTO attendance_month values(?,?,?,?,?,0,0,0,0,0,0,0,0,0,0,0,0)",(Roll_No_var.get(),name_var.get(),branch.get(),year_var.get(),email_var.get()))
                con1.commit()
                con1.close()
                fetch_data()
                clear()
                addfingerbtn['text']="Add FingerPrint"
                addphotobtn['text']="Add Facial Image"
                conn.close()
                messagebox.showinfo("Success","Successfully added",parent=newWindow)
def view_Details():
    newWindow = Toplevel(root)

 
    # sets the title of the
    # Toplevel widget
    newWindow.title("View student Details")

    # sets the geometry of toplevel
    newWindow.geometry("1080x700+10+10")
    newWindow.maxsize(1080, 700)
    newWindow.minsize(1080, 700)
    Details_Frame=Frame(newWindow,bd=4,relief=RIDGE,bg="mint cream")
    Details_Frame.place(x=10,y=10,width=1060,height=680)

    lbl_search=Label(Details_Frame,text="Search",bg="mint cream",fg="black",font=("times new roman",20,"bold"))
    lbl_search.grid(row=0,column=0,pady=10,padx=5,sticky="w")
    combo_search=ttk.Combobox(Details_Frame,width=10,textvariable=search_by,font=("times new roman",13,"bold"),state="readonly")
    combo_search['values']=("RollNumber","Name","Branch", "Year")
    combo_search.grid(row=0,column=1,padx=5,pady=10,sticky="w")
    txt_search=Entry(Details_Frame,textvariable=search_txt,width=20,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
    txt_search.grid(row=0,column=2,pady=10,padx=5,sticky="w")
    searchbtn=Button(Details_Frame,text="Search",bg="green",fg="white",font=("times new roman",12,"bold"),command=search_data,width=8,pady=5).grid(row=0,column=3,padx=5,pady=10)
    showallbtn=Button(Details_Frame,text="Showall",bg="green",fg="white",font=("times new roman",12,"bold"),command=fetch_data,width=8,pady=5).grid(row=0,column=4,padx=5,pady=10)

    #Table frame
    global Student_table
    Table_Frame=Frame(Details_Frame,bd=4,relief=RIDGE,bg="mint cream")
    Table_Frame.place(x=10,y=70,width=1030,height=590)
    scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
    scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
    Student_table=ttk.Treeview(Table_Frame,columns=("RollNumber","Name","Branch","Year","Email","Gender","Contact Info"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=Student_table.xview)
    scroll_y.config(command=Student_table.yview)
    Student_table.heading("RollNumber",anchor=CENTER,text="RollNumber")
    Student_table.heading("Name",anchor=CENTER,text="Name")
    Student_table.heading("Branch",anchor=CENTER,text="Branch")
    Student_table.heading("Year",anchor=CENTER,text="Year")
    Student_table.heading("Email",anchor=CENTER,text="Email")
    Student_table.heading("Gender",anchor=CENTER,text="Gender")
    Student_table.heading("Contact Info",anchor=CENTER,text="Contact Info")


    Student_table['show']="headings"
    Student_table.column("RollNumber",anchor=CENTER,width=150)
    Student_table.column("Name",anchor=CENTER,width=150)
    Student_table.column("Branch",anchor=CENTER,width=150)
    Student_table.column("Year",anchor=CENTER,width=150)
    Student_table.column("Email",anchor=CENTER,width=250)
    Student_table.column("Gender",anchor=CENTER,width=100)
    Student_table.column("Contact Info",anchor=CENTER,width=150)

    Student_table.pack(fill=BOTH,expand=1)
    #Student_table.bind("<ButtonRelease-1>",get_cursor)
    fetch_data()                
def fetch_data():
    conn=connect("student.db")
    cur=conn.cursor()
    search_by.set("")
    search_txt.set("")
    cur.execute("SELECT * FROM student")
    rows=cur.fetchall()
    if len(rows)!=0:
        Student_table.delete(*Student_table.get_children())
        for row in rows:
            Student_table.insert('',END,values=row)
        conn.commit()
    conn.close()
def clear():
    Roll_No_var.set("")
    branch.set("")
    name_var.set("")
    email_var.set("")
    gender_var.set("")
    contact_var.set("")
    year_var.set("")
   
def get_cursor(ev):
    cursor_row=Student_table.focus()
    content=Student_table.item(cursor_row)
    row=content['values']
    Roll_No_var.set(row[0])
    name_var.set(row[1])
    branch.set(row[2])
    year_var.set(row[3])
    email_var.set(row[4])
    gender_var.set(row[5])
    contact_var.set(row[6])
    

def update_data():
    conn=connect("student.db")
    cur=conn.cursor()
    cur.execute("update student set Name=?,Branch=?,year=?,Email=?,Gender=?,Contact=? WHERE RollNumber=?",(name_var.get(),branch.get(),year_var.get(),email_var.get(),gender_var.get(),contact_var.get(),Roll_No_var.get()))
    conn.commit()
    con1=connect('attendance.db')
    cur1=con1.cursor()
    cur1.execute("update attendance set Name=?,Branch=?,year=?,mailid=? WHERE RollNumber=?",(name_var.get(),branch.get(),year_var.get(),email_var.get(),Roll_No_var.get()))
    con1.commit()
    con1.close()
    con2=connect('attendance_month.db')
    cur2=con2.cursor()
    cur2.execute("update attendance_month set Name=?,Branch=?,year=?,mailid=? WHERE RollNumber=?",(name_var.get(),branch.get(),year_var.get(),email_var.get(),Roll_No_var.get()))
    con2.commit()
    con2.close()
    fetch_data()
    clear()
    conn.close()
    messagebox.showinfo("Success","Successfully updated",parent=newWindow)
def delete_data():
    conn=connect("student.db")
    cur=conn.cursor()
    sql_query=f"delete FROM student where RollNumber=\'{Roll_No_var.get()}\'"
    cur.execute(sql_query)
    
    conn.commit()
    conn.close()
    conn1=connect("attendance.db")
    cur1=conn1.cursor()
    sql_query=f"delete FROM attendance where RollNumber=\'{Roll_No_var.get()}\'"
    cur1.execute(sql_query)
    
    conn1.commit()
    conn1.close()
    conn2=connect("attendance_month.db")
    cur2=conn2.cursor()
    sql_query=f"delete FROM attendance_month where RollNumber=\'{Roll_No_var.get()}\'"
    cur2.execute(sql_query)
    
    conn2.commit()
    conn2.close()
    clear()
    fetch_data()
    messagebox.showinfo("Success","Successfully Deleted",parent=newWindow)
def search_data():
    conn=connect("student.db")
    cur=conn.cursor()
    sql_query=f"SELECT * FROM student where {search_by.get()} like '%{search_txt.get()}%'"
    
    cur.execute(sql_query)
    rows=cur.fetchall()
    if len(rows)!=0:
        Student_table.delete(*Student_table.get_children())
        for row in rows:
            Student_table.insert('',END,values=row)
        conn.commit()
    else:
        messagebox.showerror("Error","No Data available",parent=newWindow)
    search_by.set("")
    search_txt.set("")
    conn.close()




def holidays():
    global newWindow
    newWindow = Toplevel(root)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("Add a holiday")
 
    # sets the geometry of toplevel
    newWindow.geometry("1080x700+10+10")
    newWindow.maxsize(1080, 700)
    newWindow.minsize(1080, 700)
    Manage_Frame=Frame(newWindow,bd=4,relief=RIDGE,bg="mint cream")
    Manage_Frame.place(x=10,y=10,width=450,height=650)
    m_title=Label(Manage_Frame,text="Add a holiday",bg="mint cream",fg="black",font=("times new roman",15,"bold"))
    m_title.pack(padx=20,pady=100)
    global cal
    cal = Calendar(Manage_Frame, selectmode = 'day',
                    year = 2022, month = 5,
                    day = 1)
        
    cal.pack(pady = 20)
    Button(Manage_Frame, text = "Add Date",command = add_date).pack(pady = 10)
    
    

        #detail frame
    Details_Frame=Frame(newWindow,bd=4,relief=RIDGE,bg="mint cream")
    Details_Frame.place(x=470,y=10,width=600,height=650)
    
    
    #Table frame
    global holiday_table
    Table_Frame=Frame(Details_Frame,bd=4,relief=RIDGE,bg="mint cream")
    Table_Frame.place(x=10,y=70,width=580,height=550)
    scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
    scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
    holiday_table=ttk.Treeview(Table_Frame,columns=("Day","Month","Year"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=holiday_table.xview)
    scroll_y.config(command=holiday_table.yview)
    holiday_table.heading("Day",anchor=CENTER,text="Day")
    holiday_table.heading("Month",anchor=CENTER,text="Month")
    holiday_table.heading("Year",anchor=CENTER,text="Year")
    
    
    holiday_table['show']="headings"
    holiday_table.column("Day",anchor=CENTER,width=150)
    holiday_table.column("Month",anchor=CENTER,width=150)
    holiday_table.column("Year",anchor=CENTER,width=150)
    
    
    holiday_table.pack(fill=BOTH,expand=1)

    fetch_holiday_data()


    
def fetch_holiday_data():
    conn=connect("holiday.db")
    cur=conn.cursor()

    cur.execute("SELECT * FROM holiday")
    rows=cur.fetchall()
    if len(rows)!=0:
        holiday_table.delete(*holiday_table.get_children())
        for row in rows:
            holiday_table.insert('',END,values=row)
        conn.commit()
    conn.close()
    
def add_date():
    c=cal.get_date().split("/")
    con2=connect('holiday.db')
    cur2=con2.cursor()
    cur2.execute("insert into holiday values(?,?,?);",(c[1],c[0],c[2]))
    con2.commit()
    con2.close()
    messagebox.showinfo("success","Date entered successfully!",parent=newWindow)
    fetch_holiday_data()
    
def detect():
        with open("dataset_faces.dat","rb") as f:
            all_face_encodings=pickle.load(f)
    
        #url="http://[2401:4900:60db:5b74:988e:7a0f:58:35c5]:8080/video"
        cap = cv2.VideoCapture(0)
    
    
        classNames= list(all_face_encodings.keys())
        encodeListKnown=np.array(list(all_face_encodings.values()))
        while True:
            success, img = cap.read()
        # img = captureScreen()
            imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
            imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
            #cv2.imshow("img",imgS)
            facesCurFrame = face_recognition.face_locations(imgS)
            encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

            for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
                matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
                faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
                
                    
        # print(faceDis)
                matchIndex = np.argmin(faceDis)
                prob=(1-faceDis[matchIndex])*100
                if matches[matchIndex]:
                    roll_no = classNames[matchIndex].upper()
                print(faceDis[matchIndex])
                if faceDis[matchIndex]>0.5:
                    roll_no='Unknown'
        # print(name)
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, roll_no, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 2)
                #markAttendance(name)
                print(roll_no)
                if roll_no!='Unknown':
                    speak("Place your finger on fingerprint sensor!")
                    filename1 = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (
                                                       ("all files",
                                                        "*.*")))
                    filename1=cv2.imread(filename1)
                    
                    fingerprint_database_image=cv2.imread(f'C:/Users/Mulukutl/Desktop/sample/fingerprint/{roll_no}.BMP')
                    sift = cv2.SIFT_create()
                    keypoints_1, descriptors_1 = sift.detectAndCompute(filename1, None)
                    keypoints_2, descriptors_2 = sift.detectAndCompute(fingerprint_database_image, None)
                    matches = cv2.FlannBasedMatcher(dict(algorithm=1, trees=10),
                            dict()).knnMatch(descriptors_1, descriptors_2, k=2)
                    match_points = []
   
                    for p, q in matches:
                        if p.distance < 0.1*q.distance:
                            match_points.append(p)
                    keypoints = 0
                    if len(keypoints_1) <= len(keypoints_2):
                        keypoints = len(keypoints_1)            
                    else:
                        keypoints = len(keypoints_2)
                    
                    best_score=len(match_points) / keypoints*100
                    if best_score>90:
                        con=connect('student.db')
                        cur=con.cursor()
                        cur.execute(f"select * from student where RollNumber=\'{roll_no}\'")
                        
                        p=cur.fetchall()
                        print(p)
                        name=p[0][1]
                        branch=p[0][2]
                        year=p[0][3]
                        mailid=p[0][4]
                        con1=connect('attendance.db')
                        cur1=con1.cursor()
                        date1=date.today()
                        time1=time.strftime("%H:%M")
                        status="present"
                        cur1.execute(f"select * from attendance where RollNumber=\'{roll_no}\' and day=\'{date1}\'")
                        p=cur1.fetchall()
                        if len(p)==0:
                            #string3=f"update attendance case total when {string2}=1 then total+1 else total+0"
                            string1=f"insert into attendance values(\'{roll_no}\',\'{name}\',\'{branch}\',\'{year}\',\'{mailid}\',\'{date1}\',\'{time1}\',\'{status}\')"
                            print(string1)
                            #string1=f"update attendance set {string2}=1 where RollNumber=\'{roll_no}\'"
                            #cur1.execute(string3)
                            cur1.execute(string1)
                            con2=connect('attendance_month.db')
                            cur2=con2.cursor()
                            month=int(str(date1).split("-")[1])
                            month=l[month-1]
                            cur2.execute(f"update attendance_month set {month}={month}+1 where RollNumber=\'{roll_no}\'")
                            con2.commit()
                            con2.close()
                            con1.commit()
                            con1.close()
                            time.sleep(3)
                    else:
                        speak("Unauthorised user")
                    
            

            cv2.imshow('Webcam', img)
            cv2.moveWindow('Webcam',400,100)
            key=cv2.waitKey(1)
            if key==ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()   

def report():
    global newWindow
    newWindow=Toplevel(root)
    newWindow.geometry("500x250+250+250")
    
    check_lbl=Label(newWindow,text="Which kind of report do you want to see?",bg="mint cream",fg="black",font=("times new roman",15,"bold"))
    check_lbl.place(x=90,y=50)
    combo_check=ttk.Combobox(newWindow,textvariable=check_var,font=("times new roman",13,"bold"),state="readonly")
    combo_check['values']=("Day wise","Monthly")
    combo_check.place(x=160,y=100)
    Button(newWindow,text="Submit",command=get_frame).place(x=230,y=150)
def get_frame():
    newWindow.destroy()
    global newWindow1
    newWindow1=Toplevel(root)
    newWindow1.title("attendance Report")
 
    # sets the geometry of toplevel
    newWindow1.geometry("1080x700+10+10")
    newWindow1.minsize(1080,700)
    newWindow1.maxsize(1080,700)
    global Details_Frame
    Details_Frame=Frame(newWindow1,bd=4,relief=RIDGE,bg="mint cream")
    Details_Frame.place(x=10,y=10,width=1040,height=650)
    if check_var.get()=="Day wise":
        
        
        lbl_name=Label(Details_Frame,text="Select date",bg="mint cream",fg="black",font=("times new roman",15,"bold"))
        lbl_name.grid(row=0,column=0,pady=10,padx=5,sticky="w")
       

        
        combo_date=ttk.Combobox(Details_Frame,textvariable=date_var3,font=("times new roman",15,"bold"),state="readonly")
        combo_date['values']=("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31")
        combo_date.grid(row=0,column=1,padx=1,pady=10,sticky="w")
        combo_mon=ttk.Combobox(Details_Frame,textvariable=date_var2,font=("times new roman",15,"bold"),state="readonly")
        combo_mon['values']=("01","02","03","04","05","06","07","08","09","10","11","12")
        combo_mon.grid(row=0,column=2,padx=1,pady=10,sticky="w")
       
        
        
        global Attendance_table
        Table_Frame=Frame(Details_Frame,bd=4,relief=RIDGE,bg="mint cream")
        Table_Frame.place(x=10,y=120,width=1000,height=530)
        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        Attendance_table=ttk.Treeview(Table_Frame,columns=("RollNumber","Name","Branch","Year","Email","Day","Time","status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=Attendance_table.xview)
        scroll_y.config(command=Attendance_table.yview)
        Attendance_table.heading("RollNumber",anchor=CENTER,text="RollNumber")
        Attendance_table.heading("Name",anchor=CENTER,text="Name")
        Attendance_table.heading("Branch",anchor=CENTER,text="Branch")
        Attendance_table.heading("Year",anchor=CENTER,text="Year")
        Attendance_table.heading("Email",anchor=CENTER,text="Email")
        Attendance_table.heading("Day",anchor=CENTER,text="Day")
        Attendance_table.heading("Time",anchor=CENTER,text="Time in")
        Attendance_table.heading("status",anchor=CENTER,text="status")
        

        
        Attendance_table['show']="headings"
        Attendance_table.column("RollNumber",anchor=CENTER,width=150)
        Attendance_table.column("Name",anchor=CENTER,width=150)
        Attendance_table.column("Branch",anchor=CENTER,width=150)
        Attendance_table.column("Year",anchor=CENTER,width=150)
        Attendance_table.column("Email",anchor=CENTER,width=150)
        Attendance_table.column("Day",anchor=CENTER,width=150)
        Attendance_table.column("Time",anchor=CENTER,width=150)
        Attendance_table.column("status",anchor=CENTER,width=150)

    else:
          
        lbl_name=Label(Details_Frame,text="Select date",bg="mint cream",fg="black",font=("times new roman",15,"bold"))
        lbl_name.grid(row=0,column=0,pady=10,padx=5,sticky="w")
       

        
        combo_branch=ttk.Combobox(Details_Frame,textvariable=month_var,font=("times new roman",15,"bold"),state="readonly")
        combo_branch['values']=("Jan","Feb","March","April","May","June","July","Aug","Sept","Oct","Nov","Dec")
        combo_branch.grid(row=0,column=1,padx=5,pady=10,sticky="w")
        global Attendance_table
        Table_Frame=Frame(Details_Frame,bd=4,relief=RIDGE,bg="mint cream")
        Table_Frame.place(x=10,y=120,width=1000,height=530)
        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        Attendance_table=ttk.Treeview(Table_Frame,columns=("RollNo","Name","Branch","Year","Email","Attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=Attendance_table.xview)
        scroll_y.config(command=Attendance_table.yview)
        Attendance_table.heading("RollNo",anchor=CENTER,text="RollNo")
        Attendance_table.heading("Name",anchor=CENTER,text="Name")
        Attendance_table.heading("Branch",anchor=CENTER,text="Branch")
        Attendance_table.heading("Year",anchor=CENTER,text="Year")
        Attendance_table.heading("Email",anchor=CENTER,text="Email")
        Attendance_table.heading("Attendance",anchor=CENTER,text="Attendance")

        
        Attendance_table['show']="headings"
        Attendance_table.column("RollNo",anchor=CENTER,width=150)
        Attendance_table.column("Name",anchor=CENTER,width=150)
        Attendance_table.column("Branch",anchor=CENTER,width=150)
        Attendance_table.column("Year",anchor=CENTER,width=150)
        Attendance_table.column("Email",anchor=CENTER,width=150)
        Attendance_table.column("Attendance",anchor=CENTER,width=100)

        
        Attendance_table.pack(fill=BOTH,expand=1)



    
    addbtn=Button(Details_Frame,text="Get Report",font=("times new roman",12,"bold"),width=10,bg="green",fg="white",command=get_report).grid(row=0,column=3,padx=5,pady=10)
    updatebtn=Button(Details_Frame,text="Get CSV file",font=("times new roman",12,"bold"),bg="green",fg="white",width=10,command=get_csv_file).grid(row=0,column=4,padx=5,pady=10)

        

            #detail frame
        
         
    
def get_report():
    if check_var.get()=="Day wise": 
        
        
        
        date_var.set('2022-'+str(date_var2.get())+'-'+str(date_var3.get()))
        print(date_var.get())
        
        conn=connect("attendance.db")
        cur=conn.cursor()
        string2=date_var.get()
        string1=f"SELECT RollNumber,Name,Branch,Year,mailid,day,time,status FROM attendance where day=\'{string2}\'"
        cur.execute(string1)
        rows=cur.fetchall()
        string3="Attendance Report of "+date_var.get()
        Label(Details_Frame,text=string3,font=("times new roman", 20, "bold")).grid(row=1,columnspan=5)
    else:
        conn=connect("attendance_month.db")
        cur=conn.cursor()
        string1="SELECT RollNumber,Name,Branch,Year,mailid,"+month_var.get()+" FROM attendance_month"
        cur.execute(string1)
        rows=cur.fetchall()
        string3="Attendance Report of "+month_var.get()+"-"+str(current_time.year)
        Label(Details_Frame,text=string3,font=("times new roman", 20, "bold")).grid(row=1,columnspan=5)
        
    if len(rows)!=0:
        Attendance_table.delete(*Attendance_table.get_children())
        for row in rows:
            Attendance_table.insert('',END,values=row)
        conn.commit()
    conn.close()
def get_csv_file():
    get_report()
    if check_var.get()=="Daily":
        file1=date_var.get()+"-"+str(current_time.month)+"-"+str(current_time.year)+".csv"
        conn=connect("attendance.db")
        cur=conn.cursor()
        string2=date_var.get()
        string1=f"SELECT RollNumber,Name,Branch,Year,mailid,day,time,status FROM attendance where day=\'{string2}\'"
        cur.execute(string1)
        rows=cur.fetchall()
             
    else:
        file1=month_var.get()+"-"+str(current_time.year)+".csv"
        conn=connect("attendance_month.db")
        cur=conn.cursor()
        string1="SELECT RollNumber,Name,Branch,Year,mailid,"+month_var.get()+" FROM attendance_month"
        cur.execute(string1)
        rows=cur.fetchall()
    with open(file1, 'w') as f:

        writer = csv.writer(f)

        for row in rows:
            writer.writerow(row)
    f.close()
    msg="Generated csv file with name "+ file1+ ". Also mail has sent to the admin"
    messagebox.showinfo("success!",msg,parent=newWindow1)
    sendMail(file1)
def train():
    frame1.pack_forget()
    frame2.pack()
def findEncodings(images):
    
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList
def train_data():
    conn=connect("student.db")
    cur=conn.cursor()
    sql_query="select count(*) from student"
    cur.execute(sql_query)
    p=cur.fetchall()
    conn.commit()
    conn.close()
    if p[0][0]<2:
        messagebox.showinfo("Info","Atleast two data entries are needed")
    else:
        
        
    
        content=Label(frame2,text="Training a Model....",font=("times new roman", 20, "bold")).place(x=350,y=400)
        progress['value'] = 20
        root.update_idletasks()
        time.sleep(1)
        progress['value'] = 40
        root.update_idletasks()
        time.sleep(1)
        print("Process Completed")
        #progress['value'] = 50
        root.update_idletasks()
        time.sleep(1)
        path = 'Training_images'
        images = []
        classNames=[]
        myList = os.listdir(path)
        print(myList)
        for cl in myList:
            curImg = cv2.imread(f'{path}/{cl}')
            images.append(curImg)
            classNames.append(os.path.splitext(cl)[0])
        encodeListKnown = findEncodings(images)
        all_face_encodings=dict(zip(classNames,encodeListKnown))
        with open('dataset_faces.dat', 'wb') as f:
            pickle.dump(all_face_encodings, f)
        print('Encoding Complete')
        progress['value'] = 60
        root.update_idletasks()
        time.sleep(1)
        progress['value'] = 80
        root.update_idletasks()
        time.sleep(1)
        progress['value'] = 100
        time.sleep(1)
        content=Label(frame2,text="Training Completed Successfully!",font=("times new roman", 20, "bold")).place(x=350,y=400)
        messagebox.showinfo("Success","Training completed Successfully!")
        progress['value']=0
    frame2.pack_forget()
    frame1.pack()
def Proceed_menu():
    #lid.set("")
    #lpass.set("")
    f_login.pack_forget()
    frame1.pack(pady=25)
    
    speak("Welcome to HomePage")
def findEncodings_admin(images):
    encodeList = []


    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList
def admin_login():
    print("Login for admin")
    path = 'admin_images'
    images = []
    classNames = []
    myList = os.listdir(path)
    for cl in myList:
        curImg = cv2.imread(f'{path}/{cl}')
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])
    print("1")
    encodeListKnown = findEncodings_admin(images)    
    #url="http://100.101.122.246:8080/video"
    cap = cv2.VideoCapture(0)
    print("2")
    print("starting video stream")
    count=0
    while(True):
        success, img = cap.read()
    # img = captureScreen()
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
    # print(faceDis)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
    # print(name)
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                print(name)
                if name=='ADMIN':
                    cv2.imshow('Webcam', img)
                    cap.release()
                    print(name)
                    
                    cv2.destroyAllWindows()
                    print("destroy")
                    
                    Proceed_menu()
                    break
        #cv2.imshow('Webcam', img)
        #print(count)
        if count==30:
            speak("Not a Valid User")
            cap.release()
            cv2.destroyAllWindows()
            speak("Login again")
            messagebox.showerror("Error","Invalid User/Image not captured.Try Again")
            break
    
                    
con=connect('student.db')
cur=con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS student(RollNumber text Primary key,Name text NOT NULL,Branch text NOT NULL,Year text NOT NULL, Email text NOT NULL,Gender text NOT NULL,Contact text NOT NULL); ")
con.commit()
con.close() 
con2=connect('holiday.db')
cur2=con2.cursor()
cur2.execute("CREATE TABLE IF NOT EXISTS holiday(date_holiday int NOT NULL,month int NOT NULL,year int NOT NULL)")
con2.commit()
con2.close()
con1=connect('attendance.db')
cur1=con1.cursor()
cur1.execute("CREATE TABLE IF NOT EXISTS attendance(RollNumber text PRIMARY KEY,Name text NOT NULL,Branch text NOT NULL,Year text NOT NULL, mailid text NOT NULL,Day date NOT NULL,time timestamp not null,status text not null);")
con1.commit()
con1.close()
con1=connect('attendance_month.db')
cur1=con1.cursor()
cur1.execute("CREATE TABLE IF NOT EXISTS attendance_month(RollNumber text PRIMARY KEY,Name text NOT NULL,Branch text NOT NULL,Year text NOT NULL, mailid text NOT NULL,Jan int default 0,Feb int default 0,March int default 0,April int default 0,May int default 0,June int default 0,July int default 0,Aug int default 0,Sept int default 0,Oct int default 0,Nov int default 0,Dec int default 0);")
con1.commit()
con1.close()


root=Tk()
root.title("Face Attendance Management System")
root.geometry("1080x700+10+10")
root.maxsize(1080, 700)
root.minsize(1080, 700)
bg=Image.open("GUI/register.jpg")
image=bg.resize((1080, 1000))
bg=ImageTk.PhotoImage(image)
label1=Label(root, image=bg)
label1.place(x=0, y=0)





Roll_No_var=StringVar()
name_var=StringVar()
email_var=StringVar()
gender_var=StringVar()
contact_var=StringVar()
address_var=StringVar()
search_by=StringVar()
search_txt=StringVar()
branch=StringVar()
year_var=StringVar()
check_var=StringVar()
date_var=StringVar()
date_var3=StringVar()
date_var2=StringVar()
date_var1=StringVar()
month_var=StringVar()
current_time = datetime.datetime.now()
#login Page Begin


f_login=Frame(root,pady="5",padx="5",bg="#ccffff") #cretaing a Frame which can expand according to the size of the window


photo=Image.open(f"GUI/login.jpg")
photo=photo.resize((200, 200))
photo=ImageTk.PhotoImage(photo)
button1=Button(f_login, text="Login As Admin", image=photo,
               compound=TOP, font=("times new roman", 15, "bold"), command=admin_login)
button1.grid(row=1, column=0, padx=30, pady=15)

photo_=Image.open("GUI/facedetect.jpg")
photo_=photo_.resize((200, 200))
photo_=ImageTk.PhotoImage(photo_)
button5=Button(f_login, text="Attendance Generator", image=photo_, compound=TOP, font=("times new roman", 15, "bold"), command=detect)
button5.grid(row=1, column=1, padx=30, pady=15)



f_login.pack(pady="165")

#Login Page End



#homePage Begin



frame1=Frame(root,bg="#f2e6ff")
#frame1.pack(pady=20)
m_title=Label(frame1, text="Smart Attendance System using Biometrics",
              bg="mint cream", fg="black", font=("times new roman", 30, "bold"))
m_title.grid(row=0, columnspan=3, pady=15)
# Add buttons
photo1=Image.open(f"GUI/managestudents.jpg")
photo1=photo1.resize((200, 200))
photo1=ImageTk.PhotoImage(photo1)
button1=Button(frame1, text="Manage Students", image=photo1,
               compound=TOP, font=("times new roman", 15, "bold"), command=manage)
button1.grid(row=1, column=0, padx=30, pady=15)
photo2=Image.open("GUI/train.jpg")
photo2=photo2.resize((200, 200))
photo2=ImageTk.PhotoImage(photo2)

button2=Button(frame1, text="Train", image=photo2, compound=TOP,
               font=("times new roman", 15, "bold"), command=train)
button2.grid(row=1, column=1, padx=30, pady=15)
photo3=Image.open("GUI/timetable.png")
photo3=photo3.resize((200, 200))
photo3=ImageTk.PhotoImage(photo3)
button3=Button(frame1, text="Attendance Report", image=photo3,
               compound=TOP, font=("times new roman", 15, "bold"), command=report)
button3.grid(row=1, column=2, padx=30, pady=15)

photo7=Image.open("GUI/aboutdeveloper.jpg")
photo7=photo7.resize((200, 200))
photo7=ImageTk.PhotoImage(photo7)
button7=Button(frame1, text="About Developer", image=photo7,
               compound=TOP, font=("times new roman", 15, "bold"), command=about)
button7.grid(row=2, column=0, padx=30, pady=15)

photo6=Image.open("GUI/holiday.jpg")
photo6=photo6.resize((200, 200))
photo6=ImageTk.PhotoImage(photo6)
button6=Button(frame1, text="Holidays", image=photo6, compound=TOP, font=(
    "times new roman", 15, "bold"), command=holidays)
button6.grid(row=2, column=1, padx=30, pady=15)

photo8=Image.open("GUI/logout.jpg")
photo8=photo8.resize((200, 200))
photo8=ImageTk.PhotoImage(photo8)
button8=Button(frame1, text="Exit", image=photo8, compound=TOP,
               font=("times new roman", 15, "bold"), command=logout)
button8.grid(row=2, column=2, padx=30, pady=15)



#home Page End


#Training Page Begin
global content
frame2=Frame(root)
bg1=Image.open("GUI/face.jpg")
image1=bg1.resize((1080,700))
bg1=ImageTk.PhotoImage(image1)

m_title=Label(frame2,image=bg1).pack()
frame5=Frame(frame2).pack()
trainbtn=Button(frame2,text="Start Training",font=("times new roman",20,"bold"),width=20,bg="white",fg="blue",command=train_data)
trainbtn.place(x=400,y=200)
progress = ttk.Progressbar(frame2,orient='horizontal',mode='determinate',length=500)
# place the progressbar
progress.place(x=300,y=350)
#Training Page End


# Execute tkinter
root.mainloop()

