import os
import logging
from images2gif import GifMaker

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

def run(imgs_folder, Image_formate, title, duration, loop, output_folder):
    if len(output_folder) != 0:
        Maker = GifMaker(
            imgs_folder=imgs_folder,
            Image_formate=Image_formate,
            title=title,
            duration=duration,
            loop=loop,
            output_folder=output_folder
        )
    else:
        Maker = GifMaker(
            imgs_folder=imgs_folder,
            Image_formate=Image_formate,
            title=title,
            duration=duration,
            loop=loop,
        )
    try:
        Maker.make_gif()
        os.system('cls')
        logging.warning(f'{Maker.title}.gif is saved in {Maker.output_path}{Maker.title}.gif successfully!\n')
    except:
        os.system('cls')
        logging.exception(f"Couldn't create {self.title}.gif !! \n")

def user_input():
    print("To use default settings press Enter\n")
    imgs_folder=input("Folder address for images --> ")
    Image_formate=input("Image formate to filter --> ")
    title=input("GIF title --> ")
    duration=int(input("Duration of per image in gif(ms) --> "))
    loop=int(input("Loop images -->"))
    output_folder=input("Output folder path (default: Current working directory) -->")

    run(imgs_folder, Image_formate, title, duration, loop, output_folder)

def app(cmd=0):
    user_input()
    cmd = input("Enter q to quit / r to continue")
    if cmd == "r":
        os.system('cls')
        app(cmd=cmd)
    elif cmd == "q":
        os.system('cls')

if __name__ == "__main__":
    app()


