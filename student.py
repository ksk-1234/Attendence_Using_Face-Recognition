from os import close
from tkinter import*
from tkinter import ttk
from tkinter import font
from tkinter.font import BOLD, Font 
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector.connection import MySQLConnection
import cv2

class Student:
    def __init__(self,root):
        self.root=root 
        self.root.geometry("1500x800+0+0")
        self.root.title("Attendance using face recognition/student details")

        #variables
        self.var_n=StringVar()
        self.var_r=StringVar()
        self.var_b=StringVar()
        self.var_y=StringVar()
        self.var_p=StringVar()
        self.var_e=StringVar()

        #background 
        img=Image.open(r"C:\Users\siddula durga prasad\Desktop\face recognition\project_images\img1.jpg")
        img=img.resize((1380,800),Image.ANTIALIAS)
        self.picimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.picimg)
        bg_img.place(x=0,y=0,width=1380,height=800)
        
        #label placed on background
        tlabel=Label(bg_img,text="STUDENT DETAILS",font=("times new roman",40,"bold"),bg="black",fg="white")
        tlabel.place(x=0,y=0,width=1380,height=80)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=150,y=100,width=1100,height=580)

        #left label frame
        lframe=LabelFrame(main_frame,bd=2,relief=RIDGE,text="STUDENT DETAILS",font=50)
        lframe.place(x=15,y=10,width=515,height=560)
        img=Image.open(r"C:\Users\siddula durga prasad\Desktop\face recognition\project_images\studentimg.png")
        img=img.resize((500,250),Image.ANTIALIAS)
        self.pic1img=ImageTk.PhotoImage(img)

        flable=Label(lframe,image=self.pic1img)
        flable.place(x=5,y=0,width=500,height=250)

        #student details
        nframe=LabelFrame(lframe,bd=2,relief=RIDGE,text="ENTER YOUR DETAILS",font=(30),pady=20)
        nframe.place(x=20,y=250,width=465,height=280)

        #student name
        namelabel=Label(nframe,text="STUDENT NAME:")
        namelabel.place(x=4,y=0,width=150,height=20)
        
        nameip=ttk.Entry(nframe,textvariable=self.var_n,width=20)
        nameip.place(x=125,y=1,width=150,height=20)
        
        #year
        yearlabel=Label(nframe,text="YEAR:")
        yearlabel.place(x=0,y=30,width=100,height=20)
        
        yearcombo=ttk.Combobox(nframe,textvariable=self.var_y,width=20)
        yearcombo["values"]=("Select Year","I B.TECH","II B.TECH","III B.TECH","IV B.TECH",)
        yearcombo.current(0)
        yearcombo.place(x=125,y=30,width=150,height=20)

        #roll number
        stunolabel=Label(nframe,text="ROLL NUMBER:")
        stunolabel.place(x=0,y=60,width=150,height=20)


        rnoip=ttk.Entry(nframe,textvariable=self.var_r,width=20)
        rnoip.place(x=125,y=60,width=150,height=20)
  
        #branch
        branchlabel=ttk.Label(nframe,text="BRANCH:")
        branchlabel.place(x=32,y=90,width=150,height=20)

        branchcombo=ttk.Combobox(nframe,textvariable=self.var_b,width=20)
        branchcombo["values"]=("Select Branch","CSE","IT","ECE","MECH","CIVIL")
        branchcombo.current(0)
        branchcombo.place(x=125,y=90,width=150,height=20)

        #phone no
        pnolabel=Label(nframe,text="PHONE NO:")
        pnolabel.place(x=4,y=120,width=125,height=20)
        
        stupnoip=ttk.Entry(nframe,textvariable=self.var_p,width=20)
        stupnoip.place(x=125,y=120,width=150,height=20)

        #email
        emaillabel=Label(nframe,text="EMAIL:")
        emaillabel.place(x=4,y=150,width=95,height=20)
        
        emailip=ttk.Entry(nframe,textvariable=self.var_e,width=20)
        emailip.place(x=125,y=150,width=150,height=20)

        #radio buttons
        self.var_radio1=StringVar()
        btn1=ttk.Radiobutton(nframe,variable=self.var_radio1,text="Take Photo",value="YES")
        btn1.place(x=30,y=172,width=200,height=20)

        btn2=ttk.Radiobutton(nframe,variable=self.var_radio1,text="No Photo",value="NO")
        btn2.place(x=125,y=172,width=100,height=20)

        #btn frame
        btnframe=Frame(nframe,bd=2,relief=RIDGE)
        btnframe.place(x=5,y=200,width=268,height=30)

        savebtn=Button(btnframe,command=self.add_data,text="Save",width=8,bg="blue",fg="white")
        savebtn.grid(row=0,column=0)
        updatebtn=Button(btnframe,command=self.update_data,text="Update",width=8,bg="blue",fg="white")
        updatebtn.grid(row=0,column=1)
        deletebtn=Button(btnframe,command=self.delete_data,text="Delete",width=8,bg="blue",fg="white")
        deletebtn.grid(row=0,column=2)
        resetbtn=Button(btnframe,text="Reset",command=self.reset_data,width=8,bg="blue",fg="white")
        resetbtn.grid(row=0,column=3)

        #btn frame 2
        btn2frame=Frame(nframe,bd=2,relief=RIDGE)
        btn2frame.place(x=290,y=140,width=157,height=94)

        takepicbtn=Button(btn2frame,text="Take Photo",command=self.gen_dataset,width=20,height=2,bg="dark green",fg="white")
        takepicbtn.grid(row=0,column=0,pady=3,padx=2)
        updatepicbtn=Button(btn2frame,text="Update Photo",width=20,height=2,bg="dark green",fg="white")
        updatepicbtn.grid(row=1,column=0)

        #img
        img1=Image.open(r"C:\Users\siddula durga prasad\Desktop\face recognition\project_images\profile.png")
        img1=img1.resize((125,125),Image.ANTIALIAS)
        self.picimg1=ImageTk.PhotoImage(img1)

        bg_img1=Label(self.root,image=self.picimg1)
        bg_img1.place(x=495,y=425,width=125,height=125)

        #right label frame
        rframe=LabelFrame(main_frame,bd=2,relief=RIDGE,text="SEARCH DETAILS",font=(30))
        rframe.place(x=545,y=10,width=535,height=560)

        img2=Image.open(r"C:\Users\siddula durga prasad\Desktop\face recognition\project_images\searchimg.jpg")
        img2=img2.resize((520,100),Image.ANTIALIAS)
        self.pic2img=ImageTk.PhotoImage(img2)

        f1lable=Label(rframe,image=self.pic2img)
        f1lable.place(x=5,y=0,width=520,height=100)
        
        #search system
        sframe=LabelFrame(rframe,bd=2,relief=RIDGE,text="Search System",font=(10))
        sframe.place(x=7,y=110,width=515,height=55)

        searchbylabel=Label(sframe,text="Search By:",font=(1),bg="purple",fg="yellow")
        searchbylabel.place(x=5,y=4,width=90,height=25)

        scombo=ttk.Combobox(sframe,width=20)
        scombo["values"]=("Select ","Roll No","Branch")
        scombo.current(0)
        scombo.place(x=105,y=5,width=100,height=20)

        sip=ttk.Entry(sframe,width=20)
        sip.place(x=210,y=5,width=120,height=20)

        #btns
        sbtn1=Button(sframe,text="Search",font=(2))
        sbtn1.place(x=350,y=5,width=70,height=20)
        sbtn2=Button(sframe,text="Show All",font=(2))
        sbtn2.place(x=430,y=5,width=70,height=20)

        #student table
        stable=Frame(rframe,bd=2,relief=RIDGE)
        stable.place(x=7,y=170,width=515,height=360)

        scrollx=ttk.Scrollbar(stable,orient=HORIZONTAL)
        scrolly=ttk.Scrollbar(stable,orient=VERTICAL)

        self.stable=ttk.Treeview(stable,column=("n","y","r","b","p","e","ph"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)

        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.stable.xview)
        scrolly.config(command=self.stable.yview)

        self.stable.heading("n",text="Student Name")
        self.stable.heading("y",text="Year")
        self.stable.heading("r",text="Roll Number")
        self.stable.heading("b",text="Branch")
        self.stable.heading("p",text="Phone Number")
        self.stable.heading("e",text="Email ID")
        self.stable.heading("ph",text="Photo Sample Status")

        self.stable["show"]="headings"

        self.stable.column("n",width=100)
        self.stable.column("r",width=100)
        self.stable.column("y",width=100)
        self.stable.column("b",width=100)
        self.stable.column("p",width=100)
        self.stable.column("e",width=100)
        self.stable.column("ph",width=150)

        self.stable.pack(fill=BOTH,expand=1)
        self.stable.bind("<ButtonRelease>",self.getcursor)
        self.fetch_data()

    #functions
    def add_data(self):
        if (self.var_n.get()=="" or self.var_r.get()=="" or self.var_y.get()=="Select Year" or self.var_b.get()=="Select Branch" or self.var_p.get()=="" or self.var_e.get()==""):
            messagebox.showerror("ERROR","All Fields are required",parent=self.root)
        else:
            try:
                con=mysql.connector.connect(host="localhost",username="root",passwd="root",database="face_recognition")
                mycursor=con.cursor()
                mycursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_n.get(),
                                                                                    self.var_y.get(),
                                                                                    self.var_r.get(),
                                                                                    self.var_b.get(),
                                                                                    self.var_p.get(),
                                                                                    self.var_e.get(), 
                                                                                    self.var_radio1.get() 
                                                                                ))
                con.commit()
                self.fetch_data()
                con.close()
                messagebox,messagebox.showinfo("SUCCESS","Student Details has been added Successfully",parent=self.root)                                                                                                                       
            except Exception as es:
                messagebox.showerror("ERROR",f"Due To :{str(es)}",parent=self.root)                                                                    
    def fetch_data(self):
        con=mysql.connector.connect(host="localhost",username="root",passwd="root",database="face_recognition")
        mycursor=con.cursor()
        mycursor.execute("select * from student ")
        data=mycursor.fetchall()

        if len(data)!=0:
            self.stable.delete(*self.stable.get_children())
            for i in data:
                self.stable.insert("",END,values=i)
            con.commit()
            con.close()

    def getcursor(self,event=""):
        cursorfocus=self.stable.focus()
        content=self.stable.item(cursorfocus)
        data=content["values"]

        self.var_n.set(data[0]),
        self.var_y.set(data[1]),
        self.var_r.set(data[2]),
        self.var_b.set(data[3]),
        self.var_p.set(data[4]),
        self.var_e.set(data[5]),
        self.var_radio1.set(data[6])

    def update_data(self):
        if (self.var_n.get()=="" or self.var_r.get()=="" or self.var_y.get()=="Select year" or self.var_b.get()=="Select Branch" or self.var_p.get()=="" or self.var_e.get()==""):
            messagebox.showerror("ERROR","All Fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    con=mysql.connector.connect(host="localhost",username="root",passwd="root",database="face_recognition")
                    mycursor=con.cursor()
                    mycursor.execute("update student set Name=%s,Year=%s,Branch=%s,Phoneno=%s,Email=%s,Photosample=%s where Rollno=%s",(
                                                                                                                                         self.var_n.get(),
                                                                                                                                         self.var_y.get(),
                                                                                                                                         self.var_b.get(),
                                                                                                                                         self.var_p.get(),
                                                                                                                                         self.var_e.get(),
                                                                                                                                         self.var_radio1.get(),
                                                                                                                                         self.var_r.get()
                                                                                                                                                    
                                                                                                                                                ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("SUCCESS","Student details updated successfully",parent=self.root)
                con.commit()
                self.fetch_data()
                con.close()
            except Exception as es:
                messagebox.showerror("ERROR",f"Due To:{str(es)}",parent=self.root)

    def delete_data(self):
        if self.var_r.get()=="":
            messagebox.showerror("ERROR","Roll Number must be requried",parent=self.root)
        else:
            try:
                de=messagebox.askyesno("DELETE PAGE","Do you want to delete this student details",parent=self.root)
                if de>0:
                    con=mysql.connector.connect(host="localhost",username="root",passwd="root",database="face_recognition")
                    mycursor=con.cursor()
                    sql="delete from student where Rollno=%s"
                    val=(self.var_r.get(),)
                    mycursor.execute(sql,val)
                else:
                    if not de:
                        return
                con.commit()
                self.fetch_data()
                con.close()
                messagebox.showinfo("DELETE","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("ERROR",f"Due To:{str(es)}",parent=self.root)

    def reset_data(self):
        self.var_n.set("")
        self.var_r.set("")
        self.var_b.set("Select Branch")
        self.var_y.set("Select Year")
        self.var_p.set("")
        self.var_e.set("")

    def gen_dataset(self):
        if self.var_n.get()=="" or self.var_r.get()=="" or self.var_y.get()=="Select Year" or self.var_b.get()=="Select Branch" or self.var_p.get()=="" or self.var_e.get()=="":
            messagebox.showerror("ERROR","All Fields are required",parent=self.root)
        else:
            try:
                con=mysql.connector.connect(host="localhost",username="root",passwd="root",database="face_recognition")
                mycursor=con.cursor()
                mycursor.execute("select * from student")
                myresult=mycursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                mycursor.execute("update student set Name=%s,Year=%s,Branch=%s,Phoneno=%s,Email=%s,Photosample=%s where Rollno=%s",(
                                                                                                                                                self.var_n.get(),
                                                                                                                                                self.var_y.get(),
                                                                                                                                                self.var_b.get(),
                                                                                                                                                self.var_p.get(),
                                                                                                                                                self.var_e.get(), 
                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                self.var_r.get()==id+1
                                                                                                                                            ))
                con.commit()
                self.fetch_data()
                self.reset_data()
                con.close()

                faceclassifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def facecropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=faceclassifier.detectMultiScale(gray,1.3,5)

                    for (x,y,w,h)in faces:
                        facecropped=img[y:y+h,x:x+w]
                        return facecropped

                cap=cv2.VideoCapture(0)
                imgid=0
                while True:
                    ret,myframe=cap.read()
                    if facecropped(myframe) is not None:
                        imgid+=1
                        face=cv2.resize(facecropped(myframe),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data_img/user."+str(id)+"."+str(imgid)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(imgid),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(imgid)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed.")
            except Exception as s:
                messagebox.showerror("ERROR",f"Due To:{str(s)}",parent=self.root)

if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
