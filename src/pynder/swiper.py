import tkinter as tk
import config as cfg
from girl import Girl
import PIL
import glob
import os
import misc
import pynder

class Swiper():
    def __init__(self, session):
        self.users = session.nearby_users()
        self.create_view()
        self.next_user()
        
        tk.mainloop()
    
    def create_view(self):
        self.view = tk.Tk()
        self.view.title('Swiper')
        self.canvas = tk.Canvas(self.view, width=cfg.Canvas.WIDTH, height=cfg.Canvas.HEIGHT, bg='white')
        self.canvas.grid(row=3, column=3)
        
       
    def swap_image(self, image_path):
        self.current_img = misc.load_image(image_path)
        self.canvas.itemconfig(self.current_canvas_img, image = self.current_img)

    def set_user_view(self):
        self.canvas.delete("all")
        self.canvas.create_text(20,20,anchor=tk.NW,
                        fill="darkblue",
                        font="Times 20 italic bold",
                        text="Like or dislike user")

    def next_image(self):
        if(self.cnt < len(self.images)-1):
            self.cnt += 1

        if(self.cnt == len(self.images)-1):
            self.set_binds_user()
            self.set_user_view()
        else:
            misc.download_image(self.current_user._photos[self.cnt]["url"],
                            self.current_user.dir_images + "/" + str(self.cnt))
            self.swap_image(self.images[self.cnt])

    def like(self):
        self.current_user.like_()
        self.next_image()

    def dislike(self):
        self.current_user.dislike_()
        self.next_image()

    def like_user(self):
        self.current_user.like_user()
        self.next_user()

    def super_like_user(self):
        self.current_user.super_like_user()

    def dislike_user(self):
        self.current_user.dislike_user
        self.next_user()

    def set_binds(self):
        self.view.bind('<Right>',  lambda e:self.like())
        self.view.bind('<Left>',  lambda e:self.dislike())

    def set_binds_user(self):
        self.view.bind('<Right>',  lambda e:self.like_user())
        self.view.bind('<Left>',  lambda e:self.dislike_user())
        self.view.bind('<Up>',  lambda e:self.super_like_user())
        
    def next_user(self):
        self.cnt = 0
        self.canvas.delete("all")
        self.current_canvas_img = self.canvas.create_image(20, 20, anchor=tk.NW)
        self.set_binds()
        self.current_user = next(self.users)
        self.current_user.__class__ = Girl
        self.current_user.init_dirs()
        misc.download_images(self.current_user)
        misc.save_bio(self.current_user.dir_bio, self.current_user.bio)
        self.images = misc.load_images(self.current_user.dir_images)
        self.swap_image(self.images[self.cnt])
        
    