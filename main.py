import tkinter
import cv2  # pip install opencv-python 
import PIL.Image,PIL.ImageTk    # pip install pillow
from functools import partial
import threading
import time


SET_WIDTH=800
SET_HEIGHT=500

window=tkinter.Tk()
window.title('Football Goal Line Technology VAR')

cv_image=cv2.cvtColor(cv2.imread('E:\programming\Python projects\Football Goal LIne Technology\\var.jpg'),cv2.COLOR_BGR2RGB)
image=PIL.Image.fromarray(cv_image)
image = image.resize((SET_WIDTH,SET_HEIGHT))
photo=PIL.ImageTk.PhotoImage(image)

canvas=tkinter.Canvas(window,width=SET_WIDTH,height=SET_HEIGHT)
image_on_canvas=canvas.create_image(0,0, ancho=tkinter.NW, image=photo)
canvas.pack()

# Buttons to control playback
stream=cv2.VideoCapture("E:\programming\Python projects\Football Goal LIne Technology\clip2.mp4")   

def play(speed):
    print(f"speed is {speed}")
    frame1=stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES,frame1 + speed)

    grabbed,frame=stream.read()
            
    image=PIL.Image.fromarray(frame)
    image=image.resize(size=(SET_WIDTH,SET_HEIGHT),resample=PIL.Image.BOX)
    frame=PIL.ImageTk.PhotoImage(image)
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)



def pending(decision):
    # 1. display Checking Decision 
    def image_show(arg): 
        frame=cv2.cvtColor(cv2.imread(arg),cv2.COLOR_BGR2RGB)
        image=PIL.Image.fromarray(frame)
        image=image.resize(size=(SET_WIDTH,SET_HEIGHT),resample=PIL.Image.BOX)
        frame=PIL.ImageTk.PhotoImage(image)
        canvas.image=frame
        canvas.create_image(0,0,image=frame,anchor=tkinter.NW)

    image_show('E:\programming\Python projects\Football Goal LIne Technology\Checking.jpg')
    time.sleep(1)

    # 2. Display sponsor image
    image_show('E:\programming\Python projects\Football Goal LIne Technology\Sponsor.jpg')
    

    time.sleep(1.5)

    if decision=="goal":
        image_show("E:\programming\Python projects\Football Goal LIne Technology\goal.jpg")
        time.sleep(2)
        image_show('E:\programming\Python projects\Football Goal LIne Technology\Dsgoal.jpg')
    else:
        image_show("E:\programming\Python projects\Football Goal LIne Technology\\nogoal.jpg")
        time.sleep(2)
        image_show("E:\programming\Python projects\Football Goal LIne Technology\Dsnogoal.jpg")

    

def goal():
    thread=threading.Thread(target=pending, args=("goal",))
    thread.daemon=1
    thread.start()

def nogoal():
    thread=threading.Thread(target=pending, args=("nogoal",))
    thread.daemon=1
    thread.start()

btn=tkinter.Button(window,text="<< Previous (fast)",width=50,pady=5,command=partial(play,-15))
btn.pack()

btn=tkinter.Button(window,text="<< Previous (slow)",width=50,pady=5,command=partial(play,-2))
btn.pack()

btn=tkinter.Button(window,text="Next (slow) >>",width=50,pady=5,command=partial(play,2))
btn.pack()

btn=tkinter.Button(window,text="Next (fast) >>",width=50,pady=5,command=partial(play,15))
btn.pack()

btn=tkinter.Button(window,text="Goal",width=50,pady=5,command=goal)
btn.pack()

btn=tkinter.Button(window,text="No Goal",width=50,pady=5,command=nogoal)
btn.pack()

window.mainloop()