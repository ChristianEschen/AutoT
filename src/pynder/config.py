import os

class Directories:
    DATA = 'data'
    IMAGES = os.path.join(DATA,'images')
    LABELS = os.path.join(DATA,'labels')
    LABEL_USER = os.path.join(DATA,'label_user')
    BIO = os.path.join(DATA,'bio')

class Locations:
    COPENHAGEN_LAT = 55.6761
    COPENHAGEN_LON = 12.5683
    OSLO_LAT = 59.9139
    OSLO_LON = 10.7522
    AARHUS_LAT = 10.2039
    AARHUS_LON = 56.1629

class Current_Location:
    LAT = Locations.COPENHAGEN_LAT
    LON = Locations.COPENHAGEN_LON

class Image:
    WIDTH = 600

class Canvas:
    WIDTH = 640
    HEIGHT = 800

class Mobile_User_Agent:
    AGENT = r"Mozilla/5.0 (Linux; U; en-gb; KFTHWI Build/JDQ39) AppleWebKit/535.19 (KHTML, like Gecko) Silk/3.16 Safari/535.19"

class Facebook_Auth:
    FB_AUTH = FB_AUTH = "https://www.facebook.com/v2.6/dialog/oauth?redirect_uri=fb464891386855067%3A%2F%2Fauthorize%2F&display=touch&state=%7B%22challenge%22%3A%22IUUkEUqIGud332lfu%252BMJhxL4Wlc%253D%22%2C%220_auth_logger_id%22%3A%2230F06532-A1B9-4B10-BB28-B29956C71AB1%22%2C%22com.facebook.sdk_client_state%22%3Atrue%2C%223_method%22%3A%22sfvc_auth%22%7D&scope=user_birthday%2Cuser_photos%2Cuser_education_history%2Cemail%2Cuser_relationship_details%2Cuser_friends%2Cuser_work_history%2Cuser_likes&response_type=token%2Csigned_request&default_audience=friends&return_scopes=true&auth_type=rerequest&client_id=464891386855067&ret=login&sdk=ios&logger_id=30F06532-A1B9-4B10-BB28-B29956C71AB1&ext=1470840777&hash=AeZqkIcf-NEW6vBd"

