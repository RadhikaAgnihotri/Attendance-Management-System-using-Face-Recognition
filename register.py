from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import random
import time
import datetime
import mysql.connector
from main import Face_Recognition_System

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")	
        self.root.geometry("1600x900+0+0")
        
        #variables
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        self.var_check=IntVar()
        
        
        #bg img
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\VPA\Desktop\A.M.S\Project visual images\sp.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)
        
        #left img
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\VPA\Desktop\A.M.S\Project visual images\reg.jpg")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,width=470,height=550)
        
        #main frame
        frame=Frame(self.root,bg="beige")
        frame.place(x=520,y=100,width=800,height=550)
        
        register_lbl=Label(frame,text="REGISTER HERE",font=("Times New Roman",20,"bold"),fg="darkgreen",bg="beige")
        register_lbl.place(x=20,y=20)
        
        
        #labels
        
        #row1
        fname=Label(frame,text="First Name",font=("Times New Roman",20,"bold"),bg="beige")
        fname.place(x=50,y=100)
        
        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("Times New Roman",20,"bold"))
        fname_entry.place(x=50,y=130,width=250)
        
        l_name=Label(frame,text="Last Name",font=("Times New Roman",20,"bold"),bg="beige",fg="black")
        l_name.place(x=370,y=100)
        
        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("Times New Roman",20,"bold"))
        self.txt_lname.place(x=370,y=130,width=250)
        
        #row2
        
        contact=Label(frame,text="Contact No.",font=("Times New Roman",20,"bold"),bg="beige",fg="black")
        contact.place(x=50,y=170)
        
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("Times New Roman",20,"bold"))
        self.txt_contact.place(x=50,y=200,width=250)
        
        email=Label(frame,text="Email",font=("Times New Roman",20,"bold"),bg="beige",fg="black")
        email.place(x=370,y=170)
        
        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("Times New Roman",20,"bold"))
        self.txt_email.place(x=370,y=200,width=250)
        
        
        #row3
        
        security_Q=Label(frame,text="Select Security Question",font=("Times New Roman",20,"bold"),bg="beige",fg="black")
        security_Q.place(x=50,y=240)
        
        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("Times New Roman",20,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place", "Your Favorite Food", "Your Pet Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)
        
        
        security_A=Label(frame,text="Security Answer",font=("Times New Roman",20,"bold"),bg="beige",fg="black")
        security_A.place(x=370,y=240)
        
        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("Times New Roman",20,"bold"))
        self.txt_security.place(x=370,y=270,width=250)
        
        #row4
        
        pswd=Label(frame,text="Password",font=("Times New Roman",20,"bold"),bg="beige",fg="black")
        pswd.place(x=50,y=310)
        
        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("Times New Roman",20,"bold"))
        self.txt_pswd.place(x=50,y=340,width=250)
        
        confirm_pswd=Label(frame,text="Confirm Password",font=("Times New Roman",20,"bold"),bg="beige",fg="black")
        confirm_pswd.place(x=370,y=310)
        
        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("Times New Roman",20,"bold"))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)
        
        #check button
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I agree to the terms and conditions",font=("Times New Roman",14,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=390)
        
        #button
        img=Image.open(r"C:\Users\VPA\Desktop\A.M.S\Project visual images\regbtn.jpg")
        img=img.resize((200,50),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("Times New Roman",15,"bold"))
        b1.place(x=10,y=430,width=200)
        
        img1=Image.open(r"C:\Users\VPA\Desktop\A.M.S\Project visual images\loginbtn.jpg")
        img1=img1.resize((200,50),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b2=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2",font=("Times New Roman",15,"bold"))
        b2.place(x=330,y=430,width=200)
        
        
    #function declaration
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Passwords don't match")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree to the terms and conditions")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="R@dhavallabh108",database="database1")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error", "Email already registered")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_fname.get(),
                                                                                    self.var_lname.get(),
                                                                                    self.var_contact.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_securityQ.get(),
                                                                                    self.var_securityA.get(),
                                                                                    self.var_pass.get()))
            conn.commit()   
            conn.close()
            messagebox.showinfo("Success","User details have been registered successfully")     
    
        
        
        
        
 
 
 
if __name__ == "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop() 
        