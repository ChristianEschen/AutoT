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
import numpy as np
def key(event):
    print("pressed", repr(event.char))

class Liker():
    def __init__(self, path,csv_path):
        self.path=path
        self.csv_path=csv_path
        self.root = tkinter.Tk()

        self.liking()
        self.disliking()
        self.label=0

    def liking(self):
        self.label=1
        with open(self.csv_path+'/Label.csv','w') as f1:
            writer=csv.writer(f1, delimiter='\t',lineterminator='\n',)
            writer.writerow([str(self.label)])
        
        self.root.destroy
        self.root.quit()
    def disliking(self):
        self.label=0
        with open(self.csv_path+'/Label.csv','w') as f1:
            writer=csv.writer(f1, delimiter='\t',lineterminator='\n',)
            writer.writerow([str(self.label)])
         
        self.root.destroy
        self.root.quit()
    def write_labels(self):
        print('h')
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
        bottomFrame=tkinter.Frame(self.root)
        bottomFrame.pack()
        botton1=tkinter.Button(bottomFrame,text="dislike",fg="red",command=self.disliking)
        botton2=tkinter.Button(bottomFrame,text="like",fg="green",command= self.liking)
        botton1.pack()
        botton2.pack()
        # self.root.destroy()
        self.root.mainloop()


output_folder_img ='/home/christian/PYNDER_PROJECT/Mined_data/Images'
output_folder_labels ='/home/christian/PYNDER_PROJECT/Mined_data/Labels'

my_facebook_id=#
Lat_copenhagen = 55.6761
Lon_copenhagen = 12.5683
email = #
password = #
MOBILE_USER_AGENT = r"Mozilla/5.0 (Linux; U; en-gb; KFTHWI Build/JDQ39) AppleWebKit/535.19 (KHTML, like Gecko) Silk/3.16 Safari/535.19"
FB_AUTH = "https://www.facebook.com/v2.6/dialog/oauth?redirect_uri=fb464891386855067%3A%2F%2Fauthorize%2F&display=touch&state=%7B%22challenge%22%3A%22IUUkEUqIGud332lfu%252BMJhxL4Wlc%253D%22%2C%220_auth_logger_id%22%3A%2230F06532-A1B9-4B10-BB28-B29956C71AB1%22%2C%22com.facebook.sdk_client_state%22%3Atrue%2C%223_method%22%3A%22sfvc_auth%22%7D&scope=user_birthday%2Cuser_photos%2Cuser_education_history%2Cemail%2Cuser_relationship_details%2Cuser_friends%2Cuser_work_history%2Cuser_likes&response_type=token%2Csigned_request&default_audience=friends&return_scopes=true&auth_type=rerequest&client_id=464891386855067&ret=login&sdk=ios&logger_id=30F06532-A1B9-4B10-BB28-B29956C71AB1&ext=1470840777&hash=AeZqkIcf-NEW6vBd"

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
    if os.path.isdir(user_dir):
        print('UID already in use!')
        break
    os.mkdir(user_dir)
    os.mkdir(user_dir_csv)
    for x in range(0,len(user._photos)):
        image_url=user._photos[x]["url"]
        filedata = requests.get(image_url, allow_redirects=True) 
        open(os.path.join(user_dir,str(x)), 'wb').write(filedata.content)

        #GUI_start(os.path.join(user_dir,str(x)))
        like=Liker(os.path.join(user_dir,str(x)),user_dir_csv)
        like.load_image()
        print('hello')
       # Label=input("Press Enter to continue...")
        



    #    with open(os.path.join(user_dir,str(x)+".jpg"), 'wb') as f:  
      #      f.write(datatowrite)

        print('done')