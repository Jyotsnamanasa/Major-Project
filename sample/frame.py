import tkinter
import PIL.Image, PIL.ImageTk
import cv2
import time

global canvas
global window
def get_frame():
         vid=cv2.VideoCapture(0)
         if vid.isOpened():
             ret, frame = vid.read()
             print(ret)
             if ret:
                 # Return a boolean success flag and the current frame converted to BGR
                 return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
             else:
                 return (ret, None)
         else:
             return (ret, None)

def start( window_title, video_source=0):
            window = tkinter.Tk()
            window.title(window_title)

            

            # open video source (by default this will try to open the computer webcam)
            vid = cv2.VideoCapture(video_source)

            # Create a canvas that can fit the above video source size
            canvas = tkinter.Canvas(window, width = vid.get(cv2.CAP_PROP_FRAME_WIDTH), height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
            canvas.pack()
    
            # Button that lets the user take a snapshot
            btn_snapshot=tkinter.Button(window, text="Snapshot", width=50, command=snapshot)
            btn_snapshot.pack(anchor=tkinter.CENTER, expand=True)
    
            # After it is called once, the update method will be automatically called every delay milliseconds
            delay = 15
            update()
    
            window.mainloop()

def snapshot():
        # Get a frame from the video source
        ret, frame = get_frame()

        if ret:
            cv2.imwrite("frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

def update():
        # Get a frame from the video source
        global canvas
        global window
        ret, frame = get_frame()

        if ret:
            photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            #canvas.create_image(0, 0, image = photo, anchor = tkinter.NW)

        #window.after(delay, update)

'''
class MyVideoCapture:
     def __init__( video_source=0):
         # Open the video source
         vid = cv2.VideoCapture(video_source)
         if not vid.isOpened():
             raise ValueError("Unable to open video source", video_source)
 
         # Get video source width and height
         width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
         height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
 
     
 
     # Release the video source when the object is destroyed
     def __del__(:
         if vid.isOpened():
             vid.release()

# Create a window and pass it to the Application object
App(tkinter.Tk(), "Tkinter and OpenCV")'''
start("image")