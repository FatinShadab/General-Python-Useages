import os
import glob
import logging
from PIL import Image


class GifMaker:

    def __init__(self, imgs_folder,Image_formate, title, duration, loop, output_folder=os.getcwd(), optimize=False, save_all=True):
        '''
        initializing the GifMaker class and store required data
        '''
        self.input_path = imgs_folder
        self.formate = Image_formate
        self.title = title
        self.duration = duration
        self.loop = loop
        self.save_all = save_all
        self.optimize = optimize
        self.imgs = glob.glob(f"{self.input_path}/*.{self.formate}")
        # Prevent errors by wrong user input.
        if '\\' in output_folder[-1:]:
            self.output_path = output_folder
        else:
            self.output_path = f"{output_folder}\\"

    def make_gif(self):
        '''
        This is the main logic function which useage's
    
            * glob lib for selecting images from a certain floder with a specific formate.
            * Pillow==8.3.2 for make gif from multiple imgs. 
        '''

        # list comprehension
        image_objs = [Image.open(img) for img in self.imgs]

        # Save the gif
        image_objs[0].save(f'{self.output_path}{self.title}.gif', save_all=self.save_all, append_images=image_objs[1:], optimize=self.optimize, duration=self.duration, loop=self.loop)

