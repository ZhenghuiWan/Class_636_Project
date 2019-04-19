import cv2
import sys
import os
from face_train import Model
from tkinter import *
from PIL import Image, ImageTk

model = Model()
model.load_model(file_path = './model/zhenghuireid.model.h5')    
cascade_path = "/Users/zhenghuiup/anaconda3/pkgs/libopencv-3.4.2-h7c891bd_1/share/OpenCV/haarcascades/haarcascade_frontalface_alt2.xml"    
cascade = cv2.CascadeClassifier(cascade_path)                
faceRects = cascade.detectMultiScale(frame_gray, scaleFactor = 1.2, minNeighbors = 3, minSize = (32, 32))     

image = cv2.imread('./GUI/my_image.jpg')
faceID = model.face_predict(image)   


class Window(Frame):

    def __init__(self, master=None):
        
        Frame.__init__(self, master)   

        self.master = master

        self.init_window()

    def init_window(self):

        self.master.title("GUI")
        self.pack(fill=BOTH, expand=1)

        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)

        file.add_command(label="Exit", command=self.client_exit)

        menu.add_cascade(label="File", menu=file)
        edit = Menu(menu)

        edit.add_command(label="Show Img", command=self.showImg)
        edit.add_command(label="Show Result", command=self.showResult)
        edit.add_command(label="Examine",command=self.examine)

        menu.add_cascade(label="Edit", menu=edit)

    def showImg(self):
        load = Image.open("my_image.jpg")
        render = ImageTk.PhotoImage(load)

        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

    def showResult(self):
        if faceID == 0 :
            text = Label(self, text="Awosome, it is Zhenghui")
        else :
            text = Label(self, text="No No No, It is not Zhenghui")
        text.pack()
        

    def client_exit(self):
        exit()
    
    def examine(self):
        if image == "zhenghui.jpg":
            text = Label(self, text="Correct Answer!")
        else :
            text = Label(self, text="Oops")
        text.pack() 

root = Tk()
root.geometry("400x300")
app = Window(root)

root.mainloop()  