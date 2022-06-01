# Packages to be imported
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
'''

Roll_No_var=''
name_var=''
branch=''
email_var=''
year_var=''
gender_var=''
contact_var=''
class MyVideoCapture:
    
    def __init__(self, video_source=0):
        # Open the video source
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)

         # Get video source width and height
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
 
    def get_frame(self):
         if self.vid.isOpened():
             ret, frame = self.vid.read()
             print(ret)
             if ret:
                 # Return a boolean success flag and the current frame converted to BGR
                 return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
             else:
                 return (ret, None)
         else:
             return (ret, None)
 
     # Release the video source when the object is destroyed
    def __del__(self):
         if self.vid.isOpened():
             self.vid.release()
def add_students():
    pass
def update_data():
    pass
def clear():
    pass
def delete_data():
    pass
def collect_data():
    pass
def add_FingerPrint():
    pass

#newWindow = Toplevel(root)
newWindow=Tk()
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
m_title.grid(row=0,columnspan=2,pady=35)

lbl_roll=Label(Manage_Frame,text="Roll No.",bg="mint cream",fg="black",font=("times new roman",15,"bold"))
lbl_roll.grid(row=1,column=0,pady=10,padx=30,sticky="w")
txt_roll=Entry(Manage_Frame,textvariable=Roll_No_var,font=("times new roman",15,"bold"),bd=3,relief=GROOVE)
txt_roll.grid(row=1,column=1,pady=10,padx=30,sticky="w")

lbl_name=Label(Manage_Frame,text="Name",bg="mint cream",fg="black",font=("times new roman",15,"bold"))
lbl_name.grid(row=2,column=0,pady=10,padx=30,sticky="w")
txt_name=Entry(Manage_Frame,textvariable=name_var,font=("times new roman",15,"bold"),bd=3,relief=GROOVE)
txt_name.grid(row=2,column=1,pady=10,padx=30,sticky="w")

lbl_branch=Label(Manage_Frame,text="Branch",bg="mint cream",fg="black",font=("times new roman",15,"bold"))
lbl_branch.grid(row=3,column=0,pady=10,padx=30,sticky="w")
combo_branch=ttk.Combobox(Manage_Frame,textvariable=branch,font=("times new roman",13,"bold"),state="readonly")
combo_branch['values']=("CSE","ECE","EEE","CE","MECH")
combo_branch.grid(row=3,column=1,pady=10,padx=30,sticky="w")

lbl_email=Label(Manage_Frame,text="Email",bg="mint cream",fg="black",font=("times new roman",15,"bold"))
lbl_email.grid(row=4,column=0,pady=10,padx=30,sticky="w")
txt_email=Entry(Manage_Frame,textvariable=email_var,font=("times new roman",15,"bold"),bd=3,relief=GROOVE)
txt_email.grid(row=4,column=1,pady=10,padx=30,sticky="w")

lbl_year=Label(Manage_Frame,text="Year",bg="mint cream",fg="black",font=("times new roman",15,"bold"))
lbl_year.grid(row=5,column=0,pady=10,padx=30,sticky="w")
combo_year=ttk.Combobox(Manage_Frame,textvariable=year_var,font=("times new roman",13,"bold"),state="readonly")
combo_year['values']=("1",'2','3','4')
combo_year.grid(row=5,column=1,padx=30,pady=10,sticky="w")

lbl_gender=Label(Manage_Frame,text="Gender",bg="mint cream",fg="black",font=("times new roman",15,"bold"))
lbl_gender.grid(row=6,column=0,pady=10,padx=30,sticky="w")
combo_gender=ttk.Combobox(Manage_Frame,textvariable=gender_var,font=("times new roman",13,"bold"),state="readonly")
combo_gender['values']=("Male","Female","Other")
combo_gender.grid(row=6,column=1,padx=30,pady=10,sticky="w")


lbl_contact=Label(Manage_Frame,text="Contact",bg="mint cream",fg="black",font=("times new roman",15,"bold"))
lbl_contact.grid(row=7,column=0,pady=10,padx=30,sticky="w")
txt_contact=Entry(Manage_Frame,textvariable=contact_var,font=("times new roman",14,"bold"),bd=3,relief=GROOVE)
txt_contact.grid(row=7,column=1,pady=10,padx=30,sticky="w")





Btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="mint cream")
Btn_Frame.place(x=5,y=530,width=430)
addbtn=Button(Btn_Frame,text="Add",font=("times new roman",12,"bold"),width=10,bg="green",fg="white",command=add_students).grid(row=0,column=0,padx=3,pady=5)
updatebtn=Button(Btn_Frame,text="Update",font=("times new roman",12,"bold"),bg="green",fg="white",width=10,command=update_data).grid(row=0,column=1,padx=3,pady=5)

deletebtn=Button(Btn_Frame,text="Delete",font=("times new roman",12,"bold"),bg="green",fg="white",width=10,command=delete_data).grid(row=0,column=2,padx=3,pady=5)
clearbtn=Button(Btn_Frame,text="Clear",font=("times new roman",12,"bold"),bg="green",fg="white",width=10,command=clear).grid(row=0,column=3,padx=3,pady=5)


    #detail frame
Details_Frame=Frame(newWindow,bd=4,relief=RIDGE,bg="mint cream")
Details_Frame.place(x=470,y=10,width=600,height=650)
#start(Details_Frame,"Face Image")
def start(window1=Details_Frame, window_title="Face Image", video_source=0):
        global vid
        global canvas
        global delay
        global window
        window = window1
        
        
        video_source = video_source
        global vid
        # open video source (by default this will try to open the computer webcam)
        vid = MyVideoCapture(video_source)

        # Create a canvas that can fit the above video source size
        canvas = Canvas(window, width = vid.width, height = vid.height)
        canvas.pack()

        # Button that lets the user take a snapshot
        btn_snapshot=Button(window, text="Snapshot", width=50, command=snapshot)
        btn_snapshot.pack(anchor=CENTER, expand=True)

        # After it is called once, the update method will be automatically called every delay milliseconds
        delay = 15
        update()
        
        window.mainloop()

def snapshot():
        global vid
    # Get a frame from the video source
        ret, frame = vid.get_frame()

        if ret:
            cv2.imwrite("frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

def update():
        #print("update done")
        # Get a frame from the video source
        ret, frame = vid.get_frame()

        if ret:
            photo = ImageTk.PhotoImage(image = Image.fromarray(frame))
            canvas.create_image(0, 0, image = photo, anchor = NW)

        window.after(delay, update)








addphotobtn=Button(Details_Frame,text="Add Facial Image",font=("times new roman",12,"bold"),bg="green",fg="white",width=16,command=start)
addphotobtn.pack(padx=100,pady=50)

mainloop()
'''
import tkinter
import cv2
import PIL.Image, PIL.ImageTk
import time

class App:
    def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source

        # open video source (by default this will try to open the computer webcam)
        self.vid = MyVideoCapture(self.video_source)

        # Create a canvas that can fit the above video source size
        self.canvas = tkinter.Canvas(window, width = self.vid.width, height = self.vid.height)
        self.canvas.pack()

        # Button that lets the user take a snapshot
        self.btn_snapshot=tkinter.Button(window, text="Snapshot", width=50, command=self.snapshot)
        self.btn_snapshot.pack(anchor=tkinter.CENTER, expand=True)

        # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay = 15
        self.update()

        self.window.mainloop()

    def snapshot(self):
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()

        if ret:
            cv2.imwrite("frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

    def update(self):
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()

        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor = tkinter.NW)

        self.window.after(self.delay, self.update)


class MyVideoCapture:
    def __init__(self, video_source=0):
        # Open the video source
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)

        # Get video source width and height
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                # Return a boolean success flag and the current frame converted to BGR
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (ret, None)

    # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()

# Create a window and pass it to the Application object
App(tkinter.Tk(), "Tkinter and OpenCV")
