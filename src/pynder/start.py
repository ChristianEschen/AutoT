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
from swiper import Swiper

misc.init_directories()
  
session = pynder.Session(facebook_id=login_config.User.FACEBOOKID, facebook_token=misc.get_access_token(login_config.User.EMAIL,login_config.User.PASSWORD))
#session.matches() # get users you have already been matched with
session.update_location(cfg.Current_Location.LAT, cfg.Current_Location.LON) # updates latitude and longitude for your profile
#session.profile  # your profile. If you update its attributes they will be updated on Tinder.
#users = session.nearby_users() # returns a iterable of users nearby

Swiper(session)
