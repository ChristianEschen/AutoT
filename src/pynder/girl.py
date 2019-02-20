from pynder.models import User
import config as cfg
import os

class Girl(User):
    def init_dirs(self):
        self.dir_images = os.path.join(cfg.Directories.IMAGES,str(self.id))
        self.dir_labels = os.path.join(cfg.Directories.LABELS,str(self.id))
        self.dir_subject_labels = os.path.join(cfg.Directories.LABELS_SUBJECT,str(self.id))
        self.dir_bio = os.path.join(cfg.Directories.BIO,str(self.id))

        os.mkdir(self.dir_images)
        os.mkdir(self.dir_labels)
        os.mkdir(self.dir_subject_labels)
        os.mkdir(self.dir_bio)