from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


def logout():
    frame1.pack_forget()


def manage():
    pass


def about():
    root7 = Toplevel(root)
    root7.title("About Developer")
    root7.geometry("1080x700+10+10")
    root7.maxsize(1080, 700)

    root7.minsize(1080, 700)
    bg7 = Image.open("GUI/register.jpg")
    image = bg7.resize((1080, 1000), Image.ANTIALIAS)
    bg7 = ImageTk.PhotoImage(image)
    label7 = Label(root, image=bg)
    label7.place(x=0, y=0)
    frame7 = Frame(root, bg="#330033")
    frame7.pack(pady=20)
    m_title = Label(frame7, text="About Developer", bg="mint cream",fg="black", font=("times new roman", 30, "bold")).pack()
    m_content = Label(frame7, text="This Project \"Smart Attendance System using Face Detection\" is developed by the students of \"University College of Engineering Narasaraopet JNTUK\" under the esteemed guidence of Dr.G. Madhavi (HOD of CSE). The students worked on this project are\n M. Jyotsna Manasa\n P.Sampath\n A. Eswar\n G.SriLakshmi\n M. DharmaRao")
    root7.mainloop()

def samples():
    pass
def detect():
    pass
def changepassword():
    pass
def report():
    pass
def train():
    pass


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
frame1=Frame(root, bg="#330033")
frame1.pack(pady=20)
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
button3=Button(frame1, text="Attendence Report", image=photo3,
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
button5=Button(frame1, text="Face Detection", image=photo5, compound=TOP, font=(
    "times new roman", 15, "bold"), command=detect)
button5.grid(row=2, column=0, padx=30, pady=15)
photo6=Image.open("GUI/photosamples.jpg")
photo6=photo6.resize((200, 200), Image.ANTIALIAS)
photo6=ImageTk.PhotoImage(photo6)
button6=Button(frame1, text="Photo Samples", image=photo6, compound=TOP, font=(
    "times new roman", 15, "bold"), command=samples)
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





# Execute tkinter
root.mainloop()
