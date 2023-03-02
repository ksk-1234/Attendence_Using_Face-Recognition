from tkinter import*
from tkinter import ttk
from train import Train
from PIL import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
import os

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face_Recogonition_System")

# This part is image labels setting start 
        # backgorund image 
        bg1=Image.open(r"C:\Users\siddula durga prasad\Documents\Python_Test_Projects\Images_GUI\bg3.jpg")
        bg1=bg1.resize((1750,900),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=0,width=1366,height=768)

        #title section
        title_lb1 = Label(bg_img,text="ATTENDANCE USING FACE RECOGNITION",font=("verdana",40,"bold"),bg="black",fg="white")
        title_lb1.place(x=0,y=0,width=1366,height=75)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # student button 1
        std_img_btn=Image.open(r"C:\Users\siddula durga prasad\Documents\Python_Test_Projects\Images_GUI\std1.png")
        std_img_btn=std_img_btn.resize((250,240),Image.ANTIALIAS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.student_pannels,image=self.std_img1,cursor="hand2")
        std_b1.place(x=20,y=100,width=250,height=250)

        std_b1_1 = Button(bg_img,command=self.student_pannels,text="Student Details",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=20,y=350,width=250,height=45)

        # Detect Face  button 2
        det_img_btn=Image.open(r"C:\Users\siddula durga prasad\Documents\Python_Test_Projects\Images_GUI\det1.jpg")
        det_img_btn=det_img_btn.resize((250,250),Image.ANTIALIAS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,command=self.face_rec,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=559,y=100,width=250,height=250)

        det_b1_1 = Button(bg_img,command=self.face_rec,text="Face Detection",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        det_b1_1.place(x=559,y=350,width=250,height=45)

         # Attendance System  button 3
        att_img_btn=Image.open(r"C:\Users\siddula durga prasad\Documents\Python_Test_Projects\Images_GUI\att.jpg")
        att_img_btn=att_img_btn.resize((250,250),Image.ANTIALIAS)
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,command=self.attendance_pannel,image=self.att_img1,cursor="hand2",)
        att_b1.place(x=1080,y=100,width=250,height=250)

        att_b1_1 = Button(bg_img,command=self.attendance_pannel,text="Attendance",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        att_b1_1.place(x=1080,y=330,width=250,height=45)

         # Train   button 5
        tra_img_btn=Image.open(r"C:\Users\siddula durga prasad\Documents\Python_Test_Projects\Images_GUI\tra1.jpg")
        tra_img_btn=tra_img_btn.resize((250,250),Image.ANTIALIAS)
        self.tra_img1=ImageTk.PhotoImage(tra_img_btn)

        tra_b1 = Button(bg_img,command=self.train_pannels,image=self.tra_img1,cursor="hand2",)
        tra_b1.place(x=290,y=360,width=250,height=250)

        tra_b1_1 = Button(bg_img,command=self.train_pannels,text="Data Train",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        tra_b1_1.place(x=290,y=610,width=250,height=45)

        # exit   button 8
        exi_img_btn=Image.open(r"C:\Users\siddula durga prasad\Documents\Python_Test_Projects\Images_GUI\exit.png")
        exi_img_btn=exi_img_btn.resize((200,200),Image.ANTIALIAS)
        self.exi_img1=ImageTk.PhotoImage(exi_img_btn)

        exi_b1 = Button(bg_img,command=self.Close,image=self.exi_img1,cursor="hand2",)
        exi_b1.place(x=820,y=360,width=250,height=250)

        exi_b1_1 = Button(bg_img,command=self.Close,text="Exit",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        exi_b1_1.place(x=820,y=610,width=250,height=45)

# ==================Funtion for Open Images Folder==================
    def open_img(self):
        os.startfile("dataset")
# ==================Functions Buttons=====================
    def student_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    
    def face_rec(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
    
    def attendance_pannel(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def Close(self):
        root.destroy()
    
if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
