from pynder.models import User
import config as cfg
import os
import misc

class Girl(User):
    def init_dirs(self):
        self.dir_images = os.path.join(cfg.Directories.IMAGES,str(self.id))
        self.dir_labels = os.path.join(cfg.Directories.LABELS,str(self.id))
        self.dir_label_user = os.path.join(cfg.Directories.LABEL_USER,str(self.id))
        self.dir_bio = os.path.join(cfg.Directories.BIO,str(self.id))

        
        os.mkdir(self.dir_images)
        os.mkdir(self.dir_labels)
        os.mkdir(self.dir_label_user)
        os.mkdir(self.dir_bio)

    
    def like_(self):
        misc.label_image(self.dir_labels, 1)
        
    def dislike_(self):
        misc.label_image(self.dir_labels, 0)    

    def like_user(self):
        misc.label_user(self.dir_label_user, 1)
        self.like()

    def super_like_user(self):
        misc.label_user(self.dir_label_user, 1)
        try:
            self.superlike()
        except:
            self.user.like()
            
    def dislike_user(self):
        misc.label_user(self.dir_label_user, 0)
        self.dislike()
