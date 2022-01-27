import re
import requests
import urllib.request


class FaceBook:
    ''' A class to handle facebook video download requests from OAV Downloder. '''

    def __init__(self, link):
        ''' Initializing the FaceBook class Instance with video url. '''

        # The video url
        self.link = link

        # Creating a custom title for the video.
        self.auth, self.video_id = link.split('/')[3], link.split('/')[5]
        self.name = f"{self.auth}-{self.video_id}"

    def download_url(self):
        ''' This function returns a online stream url for the video and 
        it can be manually download from there. '''

        # The html data retrived from  the url.
        html = requests.get(self.link)  

        # trying to get the downloadable url for (hd/sd)video from the html data.
        try:
            # downloadable url for HD video.
            url = re.search('hd_src:"(.+?)"',html.text)[1]
        except:
            # downloadable url for SD video.
            url = re.search('sd_src:"(.+?)"',html.text)[1]

        return url
    
    def download(self):
        ''' The download function is responsible for downloading the video 
        by calling the download_url function. '''
        try:
            
            # doenloads the video from the url from download_url method.
            urllib.request.urlretrieve(self.download_url(), f"{self.name}.mp4")
            
        except (ConnectionResetError) as e:
            print(f'Slow Internet Connection, please check your Internet Connection!')
        except:
            print(f'Slow Internet Connection, please check your Internet Connection!')
        


#!!! TEST CODE BLOCK !!!
if __name__ == "__main__":
    facebook_dl = FaceBook(link=input("Video url: "))
    facebook_dl.download()




