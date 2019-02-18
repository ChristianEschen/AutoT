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
<<<<<<< HEAD
import numpy as np
output_folder = '../../data'
if os.path.isdir(output_folder)==False:
        os.mkdir(output_folder)

output_folder_img =os.path.join(output_folder,'images')#'/home/christian/PYNDER_PROJECT/Mined_data/Images'
output_folder_labels =os.path.join(output_folder,'Labels')#output_folder_labels ='/home/christian/PYNDER_PROJECT/Mined_data/Labels'
output_folder_labels_subject =os.path.join(output_folder,'Labels_subject')#output_folder_labels ='/home/christian/PYNDER_PROJECT/Mined_data/Labels'

output_folder_bio =os.path.join(output_folder,'bio')#output_folder_bio='/home/christian/PYNDER_PROJECT/Mined_data/Bio'
if os.path.isdir(output_folder_img)==False:
        os.mkdir(output_folder_img)

if os.path.isdir(output_folder_labels)==False:
        os.mkdir(output_folder_labels)

if os.path.isdir(output_folder_bio)==False:
        os.mkdir(output_folder_bio)

if os.path.isdir(output_folder_labels_subject)==False:
        os.mkdir(output_folder_labels_subject)

my_facebook_id="1371605974"
=======
import login_config
import config as cfg
import numpy as np
dirs = [cfg.Directories.DATA, cfg.Directories.IMAGES, cfg.Directories.LABELS, 
            cfg.Directories.LABELS_SUBJECT, cfg.Directories.BIO]

for d in dirs:
    if os.path.isdir(d) == False:
        os.mkdir(d)





my_facebook_id= login_config.User.FACEBOOKID
>>>>>>> 526c559d79d3bb2d69fcb06c95c556b8c629457e
Lat_copenhagen = 55.6761
Lon_copenhagen = 12.5683
Lat_oslo=59.9139
Lon_oslo=10.7522
Lon_aarhus=56.1629
Lat_aarhus = 10.2039
<<<<<<< HEAD
email = "jakob.broesboel@gmail.com"
password = "123qweasd"
=======
email = login_config.User.EMAIL
password = login_config.User.PASSWORD
>>>>>>> 526c559d79d3bb2d69fcb06c95c556b8c629457e
MOBILE_USER_AGENT = r"Mozilla/5.0 (Linux; U; en-gb; KFTHWI Build/JDQ39) AppleWebKit/535.19 (KHTML, like Gecko) Silk/3.16 Safari/535.19"
FB_AUTH = "https://www.facebook.com/v2.6/dialog/oauth?redirect_uri=fb464891386855067%3A%2F%2Fauthorize%2F&display=touch&state=%7B%22challenge%22%3A%22IUUkEUqIGud332lfu%252BMJhxL4Wlc%253D%22%2C%220_auth_logger_id%22%3A%2230F06532-A1B9-4B10-BB28-B29956C71AB1%22%2C%22com.facebook.sdk_client_state%22%3Atrue%2C%223_method%22%3A%22sfvc_auth%22%7D&scope=user_birthday%2Cuser_photos%2Cuser_education_history%2Cemail%2Cuser_relationship_details%2Cuser_friends%2Cuser_work_history%2Cuser_likes&response_type=token%2Csigned_request&default_audience=friends&return_scopes=true&auth_type=rerequest&client_id=464891386855067&ret=login&sdk=ios&logger_id=30F06532-A1B9-4B10-BB28-B29956C71AB1&ext=1470840777&hash=AeZqkIcf-NEW6vBd"

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


def get_access_token(email, password):
    s = robobrowser.RoboBrowser(user_agent=MOBILE_USER_AGENT, parser="lxml")
    s.open(FB_AUTH)
    f = s.get_form()
    f["pass"] = password
    f["email"] = email
    s.submit_form(f)
    f = s.get_form()
    if f.submit_fields.get('__CONFIRM__'):
        s.submit_form(f, submit=f.submit_fields['__CONFIRM__'])
    else:
        raise Exception("Couldn't find the continue button. Maybe you supplied the wrong login credentials? Or maybe Facebook is asking a security question?")
    access_token = re.search(r"access_token=([\w\d]+)", s.response.content.decode()).groups()[0]
    return access_token
    
get_access_token(email, password) #This is not really safe as you will have your email and password locally visible on your pc    
session = pynder.Session(facebook_id=my_facebook_id, facebook_token=get_access_token(email,password))
session.matches() # get users you have already been matched with
session.update_location(Lat_copenhagen, Lon_copenhagen) # updates latitude and longitude for your profile
session.profile  # your profile. If you update its attributes they will be updated on Tinder.
users = session.nearby_users() # returns a iterable of users nearby

nr_swipes =999999999999999999
for i in range(0,nr_swipes):
    uid =uuid.uuid4()
    user=next(users)

<<<<<<< HEAD

    user.bio # their biography
    user.name # their name
    user.thumbnails #a list of thumbnails of photo URLS
    user.age # their age
    user.birth_date # their birth_date
    user.ping_time # last online
    user.distance_km # distane from you
    user.common_connections # friends in common
    user.get_photos(width=640) # a list of photo URLS with either of these widths ["84","172","320","640"]
    #user.instagram_username # instagram username
    #user.instagram_photos # a list of instagram photos with these fields for each photo: 'image','link','thumbnail'
    user.schools # list of schools
    user.jobs # list of jobs
    user_dir= os.path.join(output_folder_img,str(uid))
    user_dir_csv= os.path.join(output_folder_labels,str(uid))
    user_dir_csv_subject= os.path.join(output_folder_labels_subject,str(uid))
    user_dir_bio= os.path.join(output_folder_bio,str(uid))
=======
    user_dir= os.path.join(cfg.Directories.IMAGES,str(uid))
    user_dir_csv= os.path.join(cfg.Directories.LABELS,str(uid))
    user_dir_csv_subject= os.path.join(cfg.Directories.LABELS_SUBJECT,str(uid))
    user_dir_bio= os.path.join(cfg.Directories.BIO,str(uid))
>>>>>>> 526c559d79d3bb2d69fcb06c95c556b8c629457e
    
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
