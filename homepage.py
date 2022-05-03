# Packages to be imported

from tkinter import *
from tkinter import ttk
from tokenize import String
from PIL import Image, ImageTk
from tkinter import messagebox
from sqlite3 import *
import imutils
import time
import cv2
import csv
import os
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
import pickle
from imutils import paths
import numpy as np
import imutils
from collections import Iterable
import datetime
import smtplib 
from tkinter import messagebox
from tkcalendar import Calendar
from email.mime.multipart import MIMEMultipart 

from email.mime.text import MIMEText 

from email.mime.base import MIMEBase 

from email import encoders 
from pynput.keyboard import Key, Listener

def sendMail():
        
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

        body = "hi! I am hereby sending an attatchment"

        
        # attach the body with the msg instance 

        msg.attach(MIMEText(body, 'plain')) 

        
        # open the file to be sent  
        l=[str(current_time.day),str(current_time.month),str(current_time.year)]
        l="-".join(l)
        
        filename = l+".xlsx"

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
def passChange():
    con=connect('login.db')

    cur=con.cursor()

    cur.execute("SELECT * FROM login")
    p=cur.fetchone()
    
    if p[1]==oldPass.get() and newpass.get()==confirmpass.get():
        cur.execute("update login set Passwd=? WHERE UserName=?",(confirmpass.get(),p[0]))
    else:
        message.showerror("Mismatch","Please enter proper values")
    con.commit()
    con.close()
    messagebox.showinfo("Success","Password changed Successfully!")
    frame4.pack_forget()
    frame1.pack()
def clearpass():
    oldPass.set("")
    newpass.set("")
    confirmpass.set("")
    messagebox.showinfo("Back to home","Back To home page",parent=root)
    frame4.pack_forget()
    frame1.pack()

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

    lbl_dob=Label(Manage_Frame,text="D.O.B",bg="mint cream",fg="black",font=("times new roman",15,"bold"))
    lbl_dob.grid(row=8,column=0,pady=5,padx=30,sticky="w")
    txt_dob=Entry(Manage_Frame,textvariable=dob_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
    txt_dob.grid(row=8,column=1,pady=5,padx=30,sticky="w")



    Btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="mint cream")
    Btn_Frame.place(x=5,y=530,width=430)
    addbtn=Button(Btn_Frame,text="Add",font=("times new roman",12,"bold"),width=10,bg="green",fg="white",command=add_students).grid(row=0,column=0,padx=3,pady=5)
    updatebtn=Button(Btn_Frame,text="Update",font=("times new roman",12,"bold"),bg="green",fg="white",width=10,command=update_data).grid(row=0,column=1,padx=3,pady=5)

    deletebtn=Button(Btn_Frame,text="Delete",font=("times new roman",12,"bold"),bg="green",fg="white",width=10,command=delete_data).grid(row=0,column=2,padx=3,pady=5)
    clearbtn=Button(Btn_Frame,text="Clear",font=("times new roman",12,"bold"),bg="green",fg="white",width=10,command=clear).grid(row=0,column=3,padx=3,pady=5)
    addphotobtn=Button(Btn_Frame,text="Add Photo Sample",font=("times new roman",12,"bold"),bg="green",fg="white",width=16,command=collect_data).grid(row=1,columnspan=2,padx=3,pady=5)
    updatephotobtn=Button(Btn_Frame,text="Update Photo Sample",font=("times new roman",12,"bold"),bg="green",fg="white",width=16,command=update_photos).grid(row=1,column=2,columnspan=2,padx=3,pady=5)

    

        #detail frame
    Details_Frame=Frame(newWindow,bd=4,relief=RIDGE,bg="mint cream")
    Details_Frame.place(x=470,y=10,width=600,height=650)
    
    lbl_search=Label(Details_Frame,text="Search",bg="mint cream",fg="black",font=("times new roman",20,"bold"))
    lbl_search.grid(row=0,column=0,pady=10,padx=5,sticky="w")
    combo_search=ttk.Combobox(Details_Frame,width=10,textvariable=search_by,font=("times new roman",13,"bold"),state="readonly")
    combo_search['values']=("RollNo","Name","Branch", "Year")
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
    Student_table=ttk.Treeview(Table_Frame,columns=("RollNo","Name","Branch","Year","Email","Gender","Contact Info","DOB"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=Student_table.xview)
    scroll_y.config(command=Student_table.yview)
    Student_table.heading("RollNo",anchor=CENTER,text="RollNo")
    Student_table.heading("Name",anchor=CENTER,text="Name")
    Student_table.heading("Branch",anchor=CENTER,text="Branch")
    Student_table.heading("Year",anchor=CENTER,text="Year")
    Student_table.heading("Email",anchor=CENTER,text="Email")
    Student_table.heading("Gender",anchor=CENTER,text="Gender")
    Student_table.heading("Contact Info",anchor=CENTER,text="Contact Info")
    Student_table.heading("DOB",anchor=CENTER,text="dob")
    
    Student_table['show']="headings"
    Student_table.column("RollNo",anchor=CENTER,width=150)
    Student_table.column("Name",anchor=CENTER,width=150)
    Student_table.column("Branch",anchor=CENTER,width=150)
    Student_table.column("Year",anchor=CENTER,width=150)
    Student_table.column("Email",anchor=CENTER,width=150)
    Student_table.column("Gender",anchor=CENTER,width=100)
    Student_table.column("Contact Info",anchor=CENTER,width=150)
    Student_table.column("DOB",anchor=CENTER,width=150)
    
    Student_table.pack(fill=BOTH,expand=1)
    Student_table.bind("<ButtonRelease-1>",get_cursor)
    fetch_data()

def collect_data():
    cascade = 'haarcascade_frontalface_default.xml'
    detector = cv2.CascadeClassifier(cascade)
    dataset = 'dataset'
    sub_data1=year_var.get()
    sub_data = Roll_No_var.get()
    if sub_data=="":
        messagebox.showerror("Error","Roll number feild should not be empty!",parent=newWindow)
    else:
        #path1 = os.path.abspath(os.path.join(dataset, sub_data1))
        path = os.path.abspath(os.path.join(dataset, sub_data))
        if not os.path.isdir(path):
            os.mkdir(path)
        cam = cv2.VideoCapture(0)
        time.sleep(2.0)
        total = 0

        while total < 50:
            
            _, frame = cam.read()
            img = imutils.resize(frame, width=400)
            rects = detector.detectMultiScale(
                cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), scaleFactor=1.1,
                minNeighbors=5, minSize=(30, 30))

            for (x, y, w, h) in rects:
                #cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                p = os.path.sep.join([path, "{}.png".format(
                    str(total).zfill(5))])
                cv2.imwrite(p, img)
                total += 1

            cv2.imshow("Frame", frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break
        messagebox.showinfo("Success","Successfully Collected Images",parent=newWindow)
        cam.release()
        cv2.destroyAllWindows()
    
def update_photos():
    result=messagebox.askquestion("Form",
                           "Do you want to update images?",parent=newWindow)
    if result=='yes':
        collect_data()
    

def add_students():
    if(Roll_No_var.get()=="" or name_var.get()=="" or branch.get()=="" or year_var.get()=="" or email_var.get()=="" or gender_var.get()=="" or contact_var.get()=="" or dob_var.get()==""  ): 
        messagebox.showerror("Error","All feilds are required",parent=newWindow)
    else:
        conn=connect("student.db")
        cur=conn.cursor()
        cur.execute("SELECT RollNo from student")
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
                cur.execute("insert into student values(?,?,?,?,?,?,?,?)",(Roll_No_var.get(),name_var.get(),branch.get(),year_var.get(),email_var.get(),gender_var.get(),contact_var.get(),dob_var.get()))
                conn.commit()
                con1=connect('attendance.db')
                cur1=con1.cursor()
                cur1.execute("INSERT INTO attendance values(?,?,?,?,?,?,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)",(Roll_No_var.get(),name_var.get(),branch.get(),year_var.get(),email_var.get(),0))
                con1.commit()
                con1.close()
                fetch_data()
                clear()
                conn.close()
                messagebox.showinfo("Success","Successfully added",parent=newWindow)
                
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
    dob_var.set("")
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
    dob_var.set(row[7])

def update_data():
    conn=connect("student.db")
    cur=conn.cursor()
    cur.execute("update student set Name=?,Branch=?,year=?,Email=?,Gender=?,Contact=?,DateOfBirth=? WHERE RollNo=?",(name_var.get(),branch.get(),year_var.get(),email_var.get(),gender_var.get(),contact_var.get(),dob_var.get(),Roll_No_var.get()))
    conn.commit()
    con1=connect('attendance.db')
    cur1=con1.cursor()
    cur1.execute("update attendance set Name=?,Branch=?,year=?,mailid=? WHERE RollNumber=?",(name_var.get(),branch.get(),year_var.get(),email_var.get(),Roll_No_var.get()))
    con1.commit()
    con1.close()
    fetch_data()
    clear()
    conn.close()
    messagebox.showinfo("Success","Successfully updated",parent=newWindow)
def delete_data():
    conn=connect("student.db")
    cur=conn.cursor()
    sql_query=f"delete FROM student where RollNo=\'{Roll_No_var.get()}\'"
    cur.execute(sql_query)
    
    conn.commit()
    conn.close()
    conn1=connect("attendance.db")
    cur1=conn1.cursor()
    sql_query=f"delete FROM attendance where RollNo=\'{Roll_No_var.get()}\'"
    cur1.execute(sql_query)
    
    conn1.commit()
    conn1.close()
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
    
def flatten(lis):
    for item in lis:
        if isinstance(item, Iterable) and not isinstance(item, str):
            for x in flatten(item):
                yield x
        else:
            yield item
  

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
    embeddingFile = "output/embeddings.pickle"
    embeddingModel = "openface_nn4.small2.v1.t7"
    recognizerFile = "output/recognizer.pickle"
    labelEncFile = "output/le.pickle"
    conf = 0.5

    print("[INFO] loading face detector...")
    prototxt = "model/deploy.prototxt"
    model = "model/res10_300x300_ssd_iter_140000.caffemodel"
    detector = cv2.dnn.readNetFromCaffe(prototxt, model)

    print("[INFO] loading face recognizer...")
    embedder = cv2.dnn.readNetFromTorch(embeddingModel)

    recognizer = pickle.loads(open(recognizerFile, "rb").read())
    le = pickle.loads(open(labelEncFile, "rb").read())

    Roll_Number = ""
    box = []
    print("[INFO] starting video stream...")
    cam = cv2.VideoCapture(0)
    

    while True:
        _, frame = cam.read()
        frame = imutils.resize(frame, width=600)
        (h, w) = frame.shape[:2]
        imageBlob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0, (300, 300),(104.0, 177.0, 123.0), swapRB=False, crop=False)

        detector.setInput(imageBlob)
        detections = detector.forward()
        
        for i in range(0, detections.shape[2]):

            confidence = detections[0, 0, i, 2]

            if confidence > conf:

                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")

                face = frame[startY:endY, startX:endX]
                (fH, fW) = face.shape[:2]

                if fW < 20 or fH < 20:
                    continue

                faceBlob = cv2.dnn.blobFromImage(face, 1.0 / 255, (96, 96), (0, 0, 0), swapRB=True, crop=False)
                embedder.setInput(faceBlob)
                vec = embedder.forward()

                preds = recognizer.predict_proba(vec)[0]
                j = np.argmax(preds)
                proba = preds[j]
                name = le.classes_[j]
                '''with open('student.csv', 'r') as csvFile:
                    reader = csv.reader(csvFile)
                    for row in reader:
                        box = np.append(box, row)
                        name = str(name)
                        if name in row:
                            person = str(row)
                            #print(name)
                    listString = str(box)
                    #print(box)
                    if name in listString:
                        singleList = list(flatten(box))
                        listlen = len(singleList)
                        Index = singleList.index(name)
                        name = singleList[Index]
                        Roll_Number = singleList[Index + 1]
                        if Roll_Number not in ROLL_NUMBERS:
                            ROLL_NUMBERS.append(Roll_Number)
                            NAMES.append(name)
                        #print(Roll_Number)'''
                if int(proba*100)>80:
                    text = "if your roll number is {} , then press y".format(name)
                elif int(proba*100)<40:
                    text="Unknown Person!"
                else:
                    text="Need a closure look"
                    
                y = startY - 10 if startY - 10 > 10 else startY + 10
                cv2.rectangle(frame, (startX, startY), (endX, endY),
                        (0, 0, 255), 2)
                cv2.putText(frame, text, (startX, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
        cv2.imshow("Frame", frame)
        
        '''
        # Collect all event until released
        with Listener(on_press = show) as listener:   
            listener.join()'''
        
        key=cv2.waitKey(0) &0xFF  
        if key==ord('y'):
            con1=connect('attendance.db')
            cur1=con1.cursor()
            string2="date"+str(current_time.day)
            string1=f"update attendance set {string2}=1 where RollNumber=\'{name}\'"
            cur1.execute(string1)
            con1.commit()
            con1.close()
            break
    cam.release()
    cv2.destroyAllWindows()
def show(key):
            
            #print('\nYou Entered {0}'.format( key))
        
            if key == Key.enter:
                # Stop listener
                con1=connect('attendance.db')
                cur1=con1.cursor()
                string1="update attendance set "+current_time.date+"=1 where RollNumber={}".format(name)
                cur1.execute(string1)
                con1.commit()
                con1.close()
                return False
def changepassword():   
    frame1.pack_forget()
    frame4.pack(pady="165")
def report():
    global newWindow
    newWindow=Toplevel(root)
    newWindow.geometry("500x250+250+250")
    
    check_lbl=Label(newWindow,text="Which kind of report do you want to see?",bg="mint cream",fg="black",font=("times new roman",15,"bold"))
    check_lbl.place(x=90,y=50)
    combo_check=ttk.Combobox(newWindow,textvariable=check_var,font=("times new roman",13,"bold"),state="readonly")
    combo_check['values']=("Daily","Monthly")
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
    if check_var.get()=="Daily":
        
        
        lbl_name=Label(Details_Frame,text="Select date",bg="mint cream",fg="black",font=("times new roman",15,"bold"))
        lbl_name.grid(row=0,column=0,pady=10,padx=5,sticky="w")
       

        
        combo_branch=ttk.Combobox(Details_Frame,textvariable=date_var,font=("times new roman",15,"bold"),state="readonly")
        combo_branch['values']=("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31")
        combo_branch.grid(row=0,column=1,padx=5,pady=10,sticky="w")

    else:
          
        lbl_name=Label(Details_Frame,text="Select date",bg="mint cream",fg="black",font=("times new roman",15,"bold"))
        lbl_name.grid(row=0,column=0,pady=10,padx=5,sticky="w")
       

        
        combo_branch=ttk.Combobox(Details_Frame,textvariable=month_var,font=("times new roman",15,"bold"),state="readonly")
        combo_branch['values']=("Jan","Feb","March","April","May","June","July","Aug","Sept","Oct","Nov","Dec")
        combo_branch.grid(row=0,column=1,padx=5,pady=10,sticky="w")



    
    addbtn=Button(Details_Frame,text="Get Report",font=("times new roman",12,"bold"),width=10,bg="green",fg="white",command=get_report).grid(row=0,column=3,padx=5,pady=10)
    updatebtn=Button(Details_Frame,text="Get CSV file",font=("times new roman",12,"bold"),bg="green",fg="white",width=10,command=get_csv_file).grid(row=0,column=4,padx=5,pady=10)

        

            #detail frame
        
         
    
    #Table frame
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
    
    

        
        
    
def get_report():
    if check_var.get()=="Daily": 
        
        conn=connect("attendance.db")
        cur=conn.cursor()
        string2="date"+date_var.get()
        string1="SELECT RollNumber,Name,Branch,Year,mailid,"+string2+" FROM attendance"
        cur.execute(string1)
        rows=cur.fetchall()
        string3="Attendance Report of "+date_var.get()+"-"+str(current_time.month)+"-"+str(current_time.year)
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
        string2="date"+date_var.get()
        string1="SELECT RollNumber,Name,Branch,Year,mailid,"+string2+" FROM attendance"
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
def train():
    frame1.pack_forget()
    frame2.pack()
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
        dataset = "dataset"

        embeddingFile = "output/embeddings.pickle" #initial name for embedding file
        embeddingModel = "openface_nn4.small2.v1.t7" #initializing model for embedding Pytorch

        #initialization of caffe model for face detection
        prototxt = "model\\deploy.prototxt"
        model =  "model\\res10_300x300_ssd_iter_140000.caffemodel"

        #loading caffe model for face detection
        #detecting face from Image via Caffe deep learning
        detector = cv2.dnn.readNetFromCaffe(prototxt, model)

        #loading pytorch model file for extract facial embeddings
        #extracting facial embeddings via deep learning feature extraction
        embedder = cv2.dnn.readNetFromTorch(embeddingModel)

        #gettiing image paths
        imagePaths = list(paths.list_images(dataset))

        #initialization
        knownEmbeddings = []
        knownNames = []
        total = 0
        conf = 0.9

        #we start to read images one by one to apply face detection and embedding
        for (i, imagePath) in enumerate(imagePaths):
            #print("Processing image {}/{}".format(i + 1,len(imagePaths)))
            name = imagePath.split(os.path.sep)[-2]
            image = cv2.imread(imagePath)
            image = imutils.resize(image, width=600)
            (h, w) = image.shape[:2]
            #converting image to blob for dnn face detection
            imageBlob = cv2.dnn.blobFromImage(
                cv2.resize(image, (300, 300)), 1.0, (300, 300),(104.0, 177.0, 123.0), swapRB=False, crop=False)

            #setting input blob image
            detector.setInput(imageBlob)
            #prediction the face
            detections = detector.forward()

            if len(detections) > 0:
                i = np.argmax(detections[0, 0, :, 2])
                confidence = detections[0, 0, i, 2]

                if confidence > conf:
                    #ROI range of interest
                    box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                    (startX, startY, endX, endY) = box.astype("int")
                    face = image[startY:endY, startX:endX]
                    (fH, fW) = face.shape[:2]

                    if fW < 20 or fH < 20:
                        continue
                    #image to blob for face
                    faceBlob = cv2.dnn.blobFromImage(face, 1.0 / 255, (96, 96), (0, 0, 0), swapRB=True, crop=False)
                    #facial features embedder input image face blob
                    embedder.setInput(faceBlob)
                    vec = embedder.forward()
                    knownNames.append(name)
                    knownEmbeddings.append(vec.flatten())
                    total += 1

        print("Embedding:{0} ".format(total))
        data = {"embeddings": knownEmbeddings, "names": knownNames}
        f = open(embeddingFile, "wb")
        f.write(pickle.dumps(data))
        f.close()
        print("Process Completed")
        #progress['value'] = 50
        root.update_idletasks()
        time.sleep(1)
        #initilizing of embedding & recognizer
        embeddingFile = "output/embeddings.pickle"
        #New & Empty at initial
        recognizerFile = "output/recognizer.pickle"
        labelEncFile = "output/le.pickle"

        print("Loading face embeddings...")
        data = pickle.loads(open(embeddingFile, "rb").read())

        print("Encoding labels...")
        labelEnc = LabelEncoder()
        labels = labelEnc.fit_transform(data["names"])


        print("Training model...")
        recognizer = SVC(C=1.0, kernel="linear", probability=True)
        recognizer.fit(data["embeddings"], labels)

        f = open(recognizerFile, "wb")
        f.write(pickle.dumps(recognizer))
        f.close()

        f = open(labelEncFile, "wb")
        f.write(pickle.dumps(labelEnc))
        f.close()

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



global login_by
Admin_id=""
Admin_pass=""

def Login():
    
    lid1=lid.get()
    lpass1=lpass.get()
    #print(lid1,lpass1)
    con3=connect('login.db')
    cur3=con3.cursor()
    cur3.execute("select * from login")
    p=cur3.fetchall()
    
    #print(p[0][0],p[0][1])
    con3.commit()
    con3.close()
    if(lid1==p[0][0]and lpass1==p[0][1]):
        login_by="Admin"
        Proceed_menu()
    else:
        messagebox.showerror("Invalid Login","Incorrect userId or Password")
        lid.set("")
        lpass.set("")
def Proceed_menu():
    lid.set("")
    lpass.set("")
    f_login.pack_forget()
    frame1.pack(pady=20)



con=connect('student.db')
cur=con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS student(RollNo text Primary key,Name text NOT NULL,Branch text NOT NULL,Year text NOT NULL, Email text NOT NULL,Gender text NOT NULL,Contact text NOT NULL,DateOfBirth text NOT NULL); ")
con.commit()
con.close() 
con2=connect('holiday.db')
cur2=con2.cursor()
cur2.execute("CREATE TABLE IF NOT EXISTS holiday(date_holiday int NOT NULL,month int NOT NULL,year int NOT NULL)")
con2.commit()
con2.close()

con1=connect('attendance.db')
cur1=con1.cursor()
cur1.execute("CREATE TABLE IF NOT EXISTS attendance(RollNumber text PRIMARY KEY,Name text NOT NULL,Branch text NOT NULL,Year text NOT NULL, mailid text NOT NULL,date1 int default 0,date2 int default 0,date3 int default 0,date4 int default 0,date5 int default 0,date6 int default 0,date7 int default 0,date8 int default 0,date9 int default 0,date10 int default 0,date11 int default 0,date12 int default 0,date13 int default 0,date14 int default 0,date15 int default 0,date16 int default 0,date17 int default 0,date18 int default 0,date19 int default 0,date20 int default 0,date21 int default 0,date22 int default 0,date23 int default 0,date24 int default 0,date25 int default 0,date26 int default 0,date27 int default 0,date28 int default 0,date29 int default 0,date30 int default 0,date31 int default 0,total int default 0);")
con1.commit()
con1.close()
con1=connect('attendance_month.db')
cur1=con1.cursor()
cur1.execute("CREATE TABLE IF NOT EXISTS attendance_month(RollNumber text PRIMARY KEY,Name text NOT NULL,Branch text NOT NULL,Year text NOT NULL, mailid text NOT NULL,Jan int default 0,Feb int default 0,March int default 0,April int default 0,May int default 0,June int default 0,July int default 0,Aug int default 0,Sept int default 0,Oct int default 0,Nov int default 0,Dec int default 0);")
con1.commit()
con1.close()
con3=connect('login.db')
cur3=con3.cursor()
cur3.execute("CREATE TABLE IF NOT EXISTS login(UserName text PRIMARY KEY, Passwd text NOT NULL)")
con3.commit()
con3.close()

root=Tk()
root.title("Face Attendance Management System")
root.geometry("1080x700+10+10")
root.maxsize(1080, 700)
root.minsize(1080, 700)
bg=Image.open("GUI/register.jpg")
image=bg.resize((1080, 1000), Image.ANTIALIAS)
bg=ImageTk.PhotoImage(image)
label1=Label(root, image=bg)
label1.place(x=0, y=0)

Roll_No_var=StringVar()
name_var=StringVar()
email_var=StringVar()
gender_var=StringVar()
contact_var=StringVar()
dob_var=StringVar()
address_var=StringVar()
search_by=StringVar()
search_txt=StringVar()
branch=StringVar()
year_var=StringVar()
check_var=StringVar()
date_var=StringVar()
month_var=StringVar()
current_time = datetime.datetime.now()
#login Page Begin


f_login=Frame(root,pady="25",padx="25") #cretaing a Frame which can expand according to the size of the window

lb0 =Label(f_login,text="Enter Details",bg="orange",fg="blue",font="lucida 10 bold",width="35",pady="4").grid(columnspan=3,row=0,pady="15")
lb1 =Label(f_login,text="Enter ID: ",font="lucida 10 bold").grid(column=0,row=2,pady="4")

lid =StringVar()
e1 =Entry(f_login,textvariable=lid,width="28").grid(column=1,row=2)
lb2 =Label(f_login,text="Enter Password: ",font="lucida 10 bold").grid(column=0,row=3,pady="4")

lpass=StringVar()
e2=Entry(f_login,textvariable=lpass,width="28",show='*').grid(column=1,row=3)
btn=Button(f_login,text="login",bg="green",fg="white",width="10",font="lucida 10 bold",command=Login)
btn.grid(columnspan=3,row=5,pady="10")

f_login.pack(pady="165")



#Login Page End



#homePage Begin



frame1=Frame(root,bg="#f2e6ff")
#frame1.pack(pady=20)
m_title=Label(frame1, text="Face Attendance Management System",
              bg="mint cream", fg="black", font=("times new roman", 30, "bold"))
m_title.grid(row=0, columnspan=4, pady=15)
# Add buttons
photo1=Image.open(f"GUI/managestudents.jpg")
photo1=photo1.resize((200, 200), Image.ANTIALIAS)
photo1=ImageTk.PhotoImage(photo1)
button1=Button(frame1, text="Manage Students", image=photo1,
               compound=TOP, font=("times new roman", 15, "bold"), command=manage)
button1.grid(row=1, column=0, padx=30, pady=15)
photo2=Image.open("GUI/train.jpg")
photo2=photo2.resize((200, 200), Image.ANTIALIAS)
photo2=ImageTk.PhotoImage(photo2)

button2=Button(frame1, text="Train", image=photo2, compound=TOP,
               font=("times new roman", 15, "bold"), command=train)
button2.grid(row=1, column=1, padx=30, pady=15)
photo3=Image.open("GUI/timetable.png")
photo3=photo3.resize((200, 200), Image.ANTIALIAS)
photo3=ImageTk.PhotoImage(photo3)
button3=Button(frame1, text="Attendance Report", image=photo3,
               compound=TOP, font=("times new roman", 15, "bold"), command=report)
button3.grid(row=1, column=2, padx=30, pady=15)
photo4=Image.open("GUI/passwordchange.jpg")
photo4=photo4.resize((200, 200), Image.ANTIALIAS)
photo4=ImageTk.PhotoImage(photo4)
button4=Button(frame1, text="Change Password", image=photo4, compound=TOP, font=(
    "times new roman", 15, "bold"), command=changepassword)
button4.grid(row=1, column=3, padx=30, pady=15)
photo5=Image.open("GUI/facedetect.jpg")
photo5=photo5.resize((200, 200), Image.ANTIALIAS)
photo5=ImageTk.PhotoImage(photo5)
button5=Button(frame1, text="Attendance Generator", image=photo5, compound=TOP, font=(
    "times new roman", 15, "bold"), command=detect)
button5.grid(row=2, column=0, padx=30, pady=15)
photo6=Image.open("GUI/holiday.jpg")
photo6=photo6.resize((200, 200), Image.ANTIALIAS)
photo6=ImageTk.PhotoImage(photo6)
button6=Button(frame1, text="Holidays", image=photo6, compound=TOP, font=(
    "times new roman", 15, "bold"), command=holidays)
button6.grid(row=2, column=1, padx=30, pady=15)
photo7=Image.open("GUI/aboutdeveloper.jpg")
photo7=photo7.resize((200, 200), Image.ANTIALIAS)
photo7=ImageTk.PhotoImage(photo7)
button7=Button(frame1, text="About \n Developer", image=photo7,
               compound=TOP, font=("times new roman", 15, "bold"), command=about)
button7.grid(row=2, column=2, padx=30, pady=15)
photo8=Image.open("GUI/logout.jpg")
photo8=photo8.resize((200, 200), Image.ANTIALIAS)
photo8=ImageTk.PhotoImage(photo8)
button8=Button(frame1, text="Exit", image=photo8, compound=TOP,
               font=("times new roman", 15, "bold"), command=logout)
button8.grid(row=2, column=3, padx=30, pady=15)



#home Page End


#Training Page Begin
global content
frame2=Frame(root)
bg1=Image.open("GUI/face.jpg")
image1=bg1.resize((1080,700), Image.ANTIALIAS)
bg1=ImageTk.PhotoImage(image1)

m_title=Label(frame2,image=bg1).pack()
frame5=Frame(frame2).pack()
trainbtn=Button(frame2,text="Start Training",font=("times new roman",20,"bold"),width=20,bg="white",fg="blue",command=train_data)
trainbtn.place(x=400,y=200)
progress = ttk.Progressbar(frame2,orient='horizontal',mode='determinate',length=500)
# place the progressbar
progress.place(x=300,y=350)






#Training Page End

#change PassWord Page Begin
newpass=StringVar()
confirmpass=StringVar()
oldPass=StringVar()

frame4=Frame(root,padx=50,pady=50)
m_title=Label(frame4,text="Change Password",bg="mint cream",fg="black",font=("times new roman",15,"bold"))
m_title.grid(row=0,columnspan=2,pady=20,padx=20)


pwd_old=Label(frame4,text="Old Password",bg="mint cream",fg="black",font=("times new roman",15,"bold"))
pwd_old.grid(row=1,column=0,pady=15,padx=15)

txt_uname=Entry(frame4,textvariable=oldPass,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
txt_uname.grid(row=1,column=1,pady=15,padx=15)

lbl_password=Label(frame4,text=" New Password",bg="mint cream",fg="black",font=("times new roman",15,"bold"))
lbl_password.grid(row=2,column=0,pady=15,padx=15)

txt_password=Entry(frame4,textvariable=newpass,font=("times new roman",15,"bold"),bd=5,relief=GROOVE,show='*')
txt_password.grid(row=2,column=1,pady=15,padx=15)
lbl_password1=Label(frame4,text=" Confirm Password",bg="mint cream",fg="black",font=("times new roman",15,"bold"))
lbl_password1.grid(row=3,column=0,pady=15,padx=15)

txt_password1=Entry(frame4,textvariable=confirmpass,font=("times new roman",15,"bold"),bd=5,relief=GROOVE,show='*')
txt_password1.grid(row=3,column=1,pady=15,padx=15)

loginbtn=Button(frame4,text="Change",font=("times new roman",10,"bold"),width=15,bg="green",fg="white",command=passChange)
loginbtn.grid(row=5,column=0)
clearbtn=Button(frame4,text="Clear",font=("times new roman",10,"bold"),width=15,bg="green",fg="white",command=clearpass)
clearbtn.grid(row=5,column=1)

#change Password Page End


# Execute tkinter
root.mainloop()

