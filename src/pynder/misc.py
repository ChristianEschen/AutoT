import config as cfg
import robobrowser
import re
import os
import csv
import PIL
import requests

def get_access_token(email, password):
    s = robobrowser.RoboBrowser(user_agent=cfg.Mobile_User_Agent.AGENT, parser="lxml")
    s.open(cfg.Facebook_Auth.FB_AUTH)
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

def init_directories():
    dirs = [cfg.Directories.DATA, cfg.Directories.IMAGES, cfg.Directories.LABELS, 
            cfg.Directories.LABEL_USER, cfg.Directories.BIO]

    for d in dirs:
        if os.path.isdir(d) == False:
            os.mkdir(d)

def label_image(path, label):
    write_file(path + '/labels.csv', str(label))

def label_user(path, label):
    write_file(path + '/label_user.csv', str(label))
    
def save_bio(path, bio):
    write_file(path + '/bio.txt', bio)

def write_file(path, content):
    with open(path,'a+') as f:
        writer = csv.writer(f, delimiter='\t',lineterminator='\n')
        writer.writerow([content])

def save_image(url, path):
        filedata = requests.get(url, allow_redirects=True) 
        with open(path, 'wb') as f:
            f.write(filedata.content)

def resize_image(pil_img):
        wpercent = cfg.Image.WIDTH / float(pil_img.size[0])
        hsize = int((float(pil_img.size[1])*float(wpercent)))
        return pil_img.resize((cfg.Image.WIDTH,hsize), PIL.Image.ANTIALIAS)

def download_image(url, path):
        filedata = requests.get(url, allow_redirects=True) 
        with open(path, 'wb') as f:
            f.write(filedata.content)

def download_images(user):
    for i in range(len(user._photos)):
        download_image(user._photos[i]["url"], user.dir_images + "/" + str(i))

def load_image(image_path):
        pil_img = resize_image(PIL.Image.open(image_path))
        return PIL.ImageTk.PhotoImage(pil_img)

def load_images(path):
        imgs = []
        count = 0
        for f in os.listdir(path):
            imgs.append(path + "/" + str(count))
            count += 1
        return imgs