from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
# import random
# import time
# import datetime
import mysql.connector
from main import Face_Recognition_System



def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()
    

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1530x790+0+0")
        
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\VPA\Desktop\A.M.S\Project visual images\sp.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        
        # img_top=Image.open(r"Project visual images\sp.jpg" )
        # img_top=img_top.resize((1530,720),Image.ANTIALIAS)
        # self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        # f_lbl=Label(self.root,image=self.photoimg_top)
        # f_lbl.place(x=0,y=55,width=1530,height=720)
        
        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)
        
        img1=Image.open(r"C:\Users\VPA\Desktop\A.M.S\Project visual images\login.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)
        
        get_str=Label(frame,text="Get Started",font=("Times New Roman",22,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)
        
        #label
        usernamelbl=Label(frame,text="Username",font=("Times New Roman",15,"bold"),fg="white",bg="black")
        usernamelbl.place(x=70,y=155)
        
        self.txtuser=ttk.Entry(frame,font=("Times New Roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)
        
        passwordlbl=Label(frame,text="Password",font=("Times New Roman",15,"bold"),fg="white",bg="black")
        passwordlbl.place(x=70,y=225)
        
        self.txtpass=ttk.Entry(frame,font=("Times New Roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)
        
        #Icon images for username and password
        img2=Image.open(r"C:\Users\VPA\Desktop\A.M.S\Project visual images\un1.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg2.place(x=650,y=323,width=25,height=25)
        
        img3=Image.open(r"C:\Users\VPA\Desktop\A.M.S\Project visual images\un2.png")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg3.place(x=650,y=394,width=25,height=25)
        
        #login button
        loginbtn=Button(frame,command=self.login,text="Login",font=("Times New Roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="purple",activeforeground="white",activebackground="purple")
        loginbtn.place(x=110,y=300,width=120,height=35)
        
        #register button
        registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("Times New Roman",11,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=15,y=350,width=160)
        
        #forget button
        forgetbtn=Button(frame,text="Forgot Password",command=self.forgot_password_window,font=("Times New Roman",11,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgetbtn.place(x=10,y=377,width=160)
        
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
            
        
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all fields required")
        elif self.txtuser.get()== "kapu" and self.txtpass.get()== "ashu":
            # messagebox.showinfo("Success","Welcome!")
        
            open_main=messagebox.askyesno("YesNo", "Access only to admin")
            messagebox.showinfo("Success","Welcome")
            if open_main>0:
                self.new_window=Toplevel(self.root)
                self.app=Face_Recognition_System(self.new_window)
            else:
                if not open_main:
                    return 
            conn.commit()
            self.clear()
            conn.close()
            
            
                
            
        
        # else:
            # conn=mysql.connector.connect(host="localhost",username="root",password="R@dhavallabh108",database="database1")
            # my_cursor=conn.cursor()
            # my_cursor.execute("select * from register where email=%s and password=%s", self.txtuser.get(), self.txtpass.get()) 
            # row=my_cursor.fetchone()
            # if row==None:
            #     messagebox.showerror("Error","Invalid username and password")
            # else:
                # open_main=messagebox.askyesno("YesNo", "Access only to admin")
                # messagebox.showinfo("Success","Welcome")
                
                # if open_main>0:
                #     self.new_window=Toplevel(self.root)
                #     self.app=Face_Recognition_System(self.new_window)
                # else:
                #     if not open_main:
                #         return 
            # conn.commit()
            # self.clear()
            # conn.close()    
            
                        
    def clear(self):
        self.txtuser.set("")
        self.txtpass.set("")
        
        
        
        
    #reset passoword
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error", "Select the security question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error", "Please enter the answer",parent=self.root2) 
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="R@dhavallabh108",database="database1")
            my_cursor=conn.cursor()
            qury=("select * from register where email=%s and securityQ = %s and securityA=%s")
            vlaue=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get())
            my_cursor.execute(qury,vlaue)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error", "Please enter correct answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)
                
                conn.commit()
                conn.close()
                messagebox.showinfo("Info", "Your password has been reset, now login with new password",parent=self.root2)
                self.root2.destroy()    
                       
            
        
    
    #Forgot password window                
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error", "Please enter the email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="R@dhavallabh108",database="database1")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            # print(row)
            
            if row==None:
                messagebox.showerror("Error", "Please enter a valid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")  
                
                l=Label(self.root2,text="Forgot Password",font=("helvetica",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1) 
                
                security_Q=Label(self.root2,text="Select Security Question",font=("Times New Roman",20,"bold"),bg="beige",fg="black")
                security_Q.place(x=50,y=80)
        
                self.combo_security_Q=ttk.Combobox(self.root2,font=("Times New Roman",20,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place", "Your Favorite Food", "Your Pet Name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)
        
        
                security_A=Label(self.root2,text="Security Answer",font=("Times New Roman",20,"bold"),bg="beige",fg="black")
                security_A.place(x=50,y=150)
        
                self.txt_security=ttk.Entry(self.root2,font=("Times New Roman",20,"bold"))
                self.txt_security.place(x=50,y=180,width=250)
                
                
                new_password=Label(self.root2,text="New Password",font=("Times New Roman",20,"bold"),bg="beige",fg="black")
                new_password.place(x=50,y=220)
        
                self.txt_newpass=ttk.Entry(self.root2,font=("Times New Roman",20,"bold"))
                self.txt_newpass.place(x=50,y=250,width=250) 
                
                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("Times New Roman",20,"bold"),bg="dark green",fg="white")
                btn.place(x=100,y=290)
                           
                       
            
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
        b1=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2",font=("Times New Roman",15,"bold"))
        b1.place(x=330,y=430,width=200)
        
        
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
        
    def return_login(self):
        self.root.destroy()
        
if __name__ == "__main__":
    main()
    
    
        