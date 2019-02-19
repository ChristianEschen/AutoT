import matplotlib.pyplot as plt
import pynder
import robobrowser
import re
import os
import requests
import uuid
import PIL
import tkinter
from PIL import Image, ImageTk
import csv
import login_config
import config as cfg
import numpy as np
import misc
from girl import Girl

misc.init_directories()



class Liker_subject():
    def __init__(self,csv_path_subject,user):
        self.root2 = tkinter.Tk()
        self.csv_path_subject=csv_path_subject
        self.user = user
    def liking2(self):
        with open(self.csv_path_subject+'/Label_subject.csv','a') as f1:
            writer=csv.writer(f1, delimiter='\t',lineterminator='\n',)
            writer.writerow([1])
        self.user.like()
        self.root2.destroy()
        self.root2.quit()
    def superliking2(self):
        with open(self.csv_path_subject+'/Label_subject.csv','a') as f1:
            writer=csv.writer(f1, delimiter='\t',lineterminator='\n',)
            writer.writerow([1])
        try:
            self.user.superlike()
        except:
            self.user.like()
            print('No superlikes remaining!')
        self.root2.destroy()
        self.root2.quit()
    def disliking2(self):
        with open(self.csv_path_subject+'/Label_subject.csv','a') as f1:
            writer=csv.writer(f1, delimiter='\t',lineterminator='\n',)
            writer.writerow([0])
        self.user.dislike()
        self.root2.destroy()
        self.root2.quit()

    def desicion(self):
        panel2=tkinter.Frame(self.root2)
        panel2 = tkinter.Label(self.root2, text='like?: Press "0" for dislike and "1" for like')
        panel2.pack()
        bottomFrame2=tkinter.Frame(self.root2)
        bottomFrame2.pack()
        botton3=tkinter.Button(text='like', command=self.liking2)
        botton4=tkinter.Button(text='dislike', command=self.disliking2)
        botton5=tkinter.Button(text='super like', command=self.superliking2)
        botton3.pack()
        botton4.pack()
        botton5.pack()
        self.root2.bind('0',  lambda e:self.disliking2())
        self.root2.bind('1',  lambda e:self.liking2())
        self.root2.bind('2',  lambda e:self.superliking2())
        self.root2.mainloop()

class Liker():
    def __init__(self, path,csv_path,bio_path,user):
        self.path=path
        self.bio_path=bio_path
        self.csv_path=csv_path
        self.user=user
        self.root = tkinter.Tk()
        self.root.title(self.user.name+","+str(self.user.age)+'years')
    def liking(self):
        with open(self.csv_path+'/Label.csv','a') as f1:
            writer=csv.writer(f1, delimiter='\t',lineterminator='\n',)
            writer.writerow([1])
        f= open(os.path.join(self.bio_path,"bio.txt"),"w+")
        f.write(self.user.bio)
        self.root.destroy()
        self.root.quit()
    def disliking(self):
        with open(self.csv_path+'/Label.csv','a') as f1:
            writer=csv.writer(f1, delimiter='\t',lineterminator='\n',)
            writer.writerow([0])
        f= open(os.path.join(self.bio_path,"bio.txt"),"w+")
        f.write(self.user.bio)
        self.root.destroy()
        self.root.quit()
    def load_image(self):
        mywidth = 600
        pil_img=PIL.Image.open(self.path)
        wpercent = (mywidth/float(pil_img.size[0]))
        hsize = int((float(pil_img.size[1])*float(wpercent)))
        pil_img = pil_img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
        img = ImageTk.PhotoImage(pil_img)
        panel=tkinter.Frame(self.root)
        panel = tkinter.Label(self.root, image = img)
        panel.pack()
        text=tkinter.Frame(self.root)
        text= tkinter.Label(self.root,text='Press "0" for dislike and "1" for like')
        text.pack()
        bottomFrame=tkinter.Frame(self.root)
        bottomFrame.pack()
        botton1=tkinter.Button(bottomFrame,text="dislike",fg="red",command=self.disliking)
        botton2=tkinter.Button(bottomFrame,text="like",fg="green",command= self.liking)
        botton1.pack()
        botton2.pack()
        char_list = [self.user.bio[j]for j in range(len(self.user.bio)) if ord(self.user.bio[j]) in range(65536)]
        self.user.bio=''
        for j in char_list:
            self.user.bio=self.user.bio+j
        self.user.bio
        Text_=tkinter.Label(self.root,text=self.user.bio, anchor='w').pack(fill='both')
        self.root.bind('0',  lambda e:self.disliking())
        self.root.bind('1',  lambda e:self.liking())
        self.root.mainloop()



    
session = pynder.Session(facebook_id=login_config.User.FACEBOOKID, facebook_token=misc.get_access_token(login_config.User.EMAIL,login_config.User.PASSWORD))
session.matches() # get users you have already been matched with
session.update_location(cfg.Current_Location.LAT, cfg.Current_Location.LON) # updates latitude and longitude for your profile
session.profile  # your profile. If you update its attributes they will be updated on Tinder.
users = session.nearby_users() # returns a iterable of users nearby

while(True):
    uid =uuid.uuid4()
    user=next(users)

    user.__class__ = Girl
    hack = user.derp()

    user_dir= os.path.join(cfg.Directories.IMAGES,str(uid))
    user_dir_csv= os.path.join(cfg.Directories.LABELS,str(uid))
    user_dir_csv_subject= os.path.join(cfg.Directories.LABELS_SUBJECT,str(uid))
    user_dir_bio= os.path.join(cfg.Directories.BIO,str(uid))
    
    if os.path.isdir(user_dir):
        print('UID already in use!')
        break
    os.mkdir(user_dir)
    os.mkdir(user_dir_csv)
    os.mkdir(user_dir_csv_subject)
    os.mkdir(user_dir_bio)
    for x in range(0,len(user._photos)):
        image_url=user._photos[x]["url"]
        filedata = requests.get(image_url, allow_redirects=True) 
        open(os.path.join(user_dir,str(x)), 'wb').write(filedata.content)

        like=Liker(os.path.join(user_dir,str(x)),user_dir_csv,user_dir_bio,user)
        like.load_image()
        if x==(len(user._photos)-1):
            like_subject=Liker_subject(user_dir_csv_subject,user)
            like_subject.desicion()

        print( "Image",str(x),"of",user.name)
