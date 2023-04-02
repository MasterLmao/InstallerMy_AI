import tkinter # pip install tk/tkinter
import customtkinter # pip install customtkinter
import PIL.Image # pip install Pillow
from PIL import ImageTk, Image
from tkinter import *
from tkinter import messagebox
import math
import os
import sys
import time
from GDriveDownload import GoogleDriveDownload
from unrar import rarfile # pip install unrar
from rarfile import RarFile 
import shutil

URL_DOWNLOAD = "https://drive.google.com/file/d/1VExAhPEltrlCR9tmutXUiqmg-bVjY95y/view?usp=share_link"
# FILE_PATH = r"D:\ProgramCode\Python\AI\LISA\GoogleDrive\Files"

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")



class InstallerAI():
    
    def on_enter_user(self,e):
        self.username.delete(0, "end")


    def on_leave_user(self,e):
        name = self.username.get()
        if name == "":
            self.username.insert(0, "Username")
            

    def on_enter_password(self,e):
        self.password.delete(0, "end")

    def on_leave_password(self,e):
        name = self.password.get()
        if name == "":
            self.password.insert(0, "Password")  
    
    def on_enter_dirpath(self,e):
        self.select_dir.delete(0, "end")


    def on_leave_dirpath(self,e):
        path = self.select_dir.get()
        if path == "":
            self.select_dir.insert(0, "Select Directory")
        else:
            pass
    
    
    
    def __init__(self):
        self.app = customtkinter.CTk()
        self.app.geometry("720x480")
        self.app.title("Set Up")
        self.app.configure(bg="#fff")
        self.app.resizable(False,False)

        self.img_background = ImageTk.PhotoImage(PIL.Image.open(r"background.png"))
        background = customtkinter.CTkLabel(master=self.app, image=self.img_background)
        background.pack()
        self.menu_login()
        self.app.mainloop()
    
    def Progress_bar(self,progress, total):
        KB = 111
        percent = 100 * (progress/float(total))
        # print(int(percent))
        Percent = str(int(percent))
        self.percentage.configure(text=Percent + "%")
        self.percentage.update()
            
        self.progress_bar.set(float(percent)/100)
    
    
   
    def Exit(self):
        self.setup.destroy()
        
        
        
    def folder_path(self):
        self.Status.configure(text="Start Download File: Artifficial_Intelligent.rar")
        folder_dir = open("folderpath.txt", "r")
        folder = folder_dir.read()
        # print(folder)
        FILE_PATH = folder.replace("/","\\")
        # print(f)
        # Download(f)
        # Tải file rar về giải nén:
        GoogleDriveDownload.DownloadFile(url = URL_DOWNLOAD, dir_path= FILE_PATH) 
        self.Status.configure(text="Download Complete!!!")
        time.sleep(0.5)

        self.Status.configure(text="Start Extracting file: Artifficial_Intelligent.rar")
        filename = "Artifficial_Intelligent.rar"
        foldername = "Artifficial_Intelligent"
        try:
            rarfile.UNRAR_TOOL = r"C:\Program Files (x86)\UnrarDLL\x64\UnRAR64.dll"
        except:
            shutil.copytree("UnrarDLL",r"C:\Users\kenha\Desktop/UnrarDLL")
            
        file_path = os.path.join(FILE_PATH, filename)
        folder_path = os.path.join(FILE_PATH, foldername)
        # print(FILE_PATH)
        # print(file_path)
                
        self.Status.configure(text="Start Extracting file: Artifficial_Intelligent")
        numbers = [x * 5 for x in range(2000, 3000)]
        result = []
        self.Progress_bar(0, len(numbers))
            
        for i,x in enumerate(numbers):
            result.append(math.factorial(x))
            rf = rarfile.RarFile(file_path)
            rf.extractall(FILE_PATH)
            self.Progress_bar(i + 1, len(numbers))  
            
        self.Status.configure(text="Done!!!")
        
        try:
            button_exit = customtkinter.CTkButton(master=self.Frame, width=220, text="Finished!", cursor="hand2", command=self.Exit, corner_radius=6)
            button_exit.place(x=100, y=255)
            self.dir_path = customtkinter.CTkLabel(master=self.Frame, text=f"The folder install is in: {folder_path}", font=('Century Gothic',12))
            self.dir_path.place(x=65, y=225)
        except:
            sys.exit()
        
    
    def change_dir(self):
        # print("change")
        folderpath = customtkinter.filedialog.askdirectory(title="Select Folder To Install A.I")
        f = open("folderpath.txt", "w")
        f.write(folderpath)
        f.close()
        folder = open("folderpath.txt", "r")
        folder_dir = folder.read()
        
        select_dir = customtkinter.CTkEntry(master=self.Frame, width=350, placeholder_text=folder_dir)
        select_dir.place(x=150, y=110)
        select_dir.insert(0, folder_dir)
        folder_download = select_dir.get()
        f_download = open("folderpath.txt", "w")
        folder_ = f_download.write(folder_download)
        
        self.percentage = customtkinter.CTkLabel(master=self.Frame, text="0%")
        self.percentage.place(x=50, y=143)
        
        self.progress_bar = customtkinter.CTkProgressBar(master=self.Frame, width=430)
        self.progress_bar.set(0.5)
        self.progress_bar.place(x=90, y=150)
        
        button_install = customtkinter.CTkButton(master=self.Frame, width=220, text="Install", cursor="hand2", command=self.folder_path, corner_radius=6)
        button_install.place(x=50, y=255)
        
        self.Status = customtkinter.CTkLabel(master=self.Frame, text="", font=('Century Gothic',12))
        self.Status.place(x=65, y=225)

        
        
        
    def start_install(self):
        # print("1")
        self.app.destroy()

        customtkinter.set_appearance_mode("Dark")
        customtkinter.set_default_color_theme("dark-blue")

        self.setup = customtkinter.CTk()
        self.setup.geometry("720x480")
        self.setup.title("Set Up")
        self.setup.configure(bg="#fff")
        self.setup.resizable(False,False)
        
        self.Frame = customtkinter.CTkFrame(master=self.setup, width=550 , height=480, corner_radius=15)
        self.Frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        
        
        self.select_dir = customtkinter.CTkEntry(master=self.Frame, width=350, placeholder_text="Select Directory")
        self.select_dir.place(x=150, y=110)
        self.select_dir.insert(0, "Select Directory")
        self.select_dir.bind("<FocusIn>", self.on_enter_dirpath)
        self.select_dir.bind("<FocusOut>", self.on_leave_dirpath)
        
        
        button_select_path = customtkinter.CTkButton(master=self.Frame, width=100, height=30, text="Change", cursor="hand2", command=self.change_dir, corner_radius=6)
        button_select_path.place(x=45, y=110)
        
        
        self.setup.mainloop()
        

        
        

    def Sign_up():
        print("test")


    def Login(self):    
        user = self.username.get() # self.
        pword = self.password.get() # password
        file_user = r"username.txt"
        file_password = r"password.txt"
        try:
            us = open(file_user, "r")
            us_lg = us.read()
            ps = open(file_password, "r")
            ps_lg = ps.read()
            
            if user == us_lg and pword == ps_lg:
                # print("Hello Everyone")
                self.start_install()
            elif user != us_lg and pword != ps_lg:
                # print("Invalid self. and password")
                self.Error_Label.configure(text="Invalid self. and password")
            elif user != us_lg:
                # print("Invalid username")
                self.Error_Label.configure(text="Invalid username")
            elif pword != ps_lg:
                # print("Invalid password")
                self.Error_Label.configure(text="Invalid password")
        
        except: 
            self.Error_Label.configure(text="Can't find your account!!!")


    
    def Remember_me(self):    
        user = self.username.get() # username
        pword = self.password.get() # password
        file_user = r"username.txt"
        file_password = r"password.txt"
        try:
            us = open(file_user, "r")
            us_lg = us.read()
            ps = open(file_password, "r")
            ps_lg = ps.read()
            
            if user == us_lg and pword == ps_lg:
                # print("Hello Everyone")
                pass
            elif user != us_lg and pword != ps_lg:
                # print("Invalid username and password")
                self.Error_Label.configure(text="Invalid username and password")
            elif user != us_lg:
                # print("Invalid username")
                self.Error_Label.configure(text="Invalid username")
            elif pword != ps_lg:
                # print("Invalid password")
                self.Error_Label.configure(text="Invalid password")
        
        except: 
            self.Error_Label.configure(text="Can't find your account!!!")    
        
    
    def menu_login(self):
        frame = customtkinter.CTkFrame(master=self.app, width=320 , height=360, corner_radius=15)
        frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        label = customtkinter.CTkLabel(master=frame, text="Login System Install AI", font=("Roboto", 20, "bold"))
        label.place(x=50, y=45)
        
        
        self.username = customtkinter.CTkEntry(master=frame, width=220, placeholder_text="Username")
        self.username.place(x=50, y=110)
        self.username.insert(0, "Username")
        self.username.bind('<FocusIn>', self.on_enter_user)
        self.username.bind('<FocusOut>', self.on_leave_user)
        
        
        self.password = customtkinter.CTkEntry(master=frame, width=220, placeholder_text="self.Password", show="*")
        self.password.place(x=50, y=165)
        self.password.insert(0, "Password")
        self.password.bind('<FocusIn>', self.on_enter_password)
        self.password.bind('<FocusOut>', self.on_leave_password)

        forg_psword=customtkinter.CTkLabel(master=frame, text="Forget password?",font=('Century Gothic',12))
        forg_psword.place(x=170,y=195)

        button_lg = customtkinter.CTkButton(master=frame, width=220, text="Login", cursor="hand2", command=self.Login, corner_radius=6)
        button_lg.place(x=50, y=255)

        checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me", command=self.Remember_me)
        checkbox.place(x=50, y=200)

        account=customtkinter.CTkLabel(master=frame, text="Dont't have an account?",font=('Microsoft YaHei UI Light',12))
        account.place(x=50, y=285)

        button_signup = customtkinter.CTkButton(master=frame, width=220, text="Sign up", cursor="hand2", command=self.Sign_up, corner_radius=6)
        button_signup.place(x=50, y=320)

        self.Error_Label = customtkinter.CTkLabel(master=frame, text="", font=('Century Gothic',12), text_color="red")
        self.Error_Label.place(x=65, y=225)
    
        
        
InstallerAI()