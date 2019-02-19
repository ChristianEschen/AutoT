import config as cfg
import robobrowser
import re
import os

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
            cfg.Directories.LABELS_SUBJECT, cfg.Directories.BIO]

    for d in dirs:
        if os.path.isdir(d) == False:
            os.mkdir(d)