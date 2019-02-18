import os

class Directories:
    DATA = '../../data'
    IMAGES = os.path.join(DATA,'images')
    LABELS = os.path.join(DATA,'labels')
    LABELS_SUBJECT = os.path.join(DATA,'labels_subject')
    BIO = os.path.join(DATA,'bio')