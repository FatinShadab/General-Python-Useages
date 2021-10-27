from plyer import notification
from pytube import YouTube

from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

Main_Grid = '''
BoxLayout:
    orientation: 'vertical'

    MDToolbar:
        title: 'YouFast Downloader'
        md_bg_color: .2, .2, .2, 1
        specific_text_color: 1, .3, .2, 1

    MDBottomNavigation:
        panel_color: .2, .2, .2, 1

        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Home'
            icon: 'home'

            Image:
                id: imageView
                source: 'youtube.png'

        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Download'
            icon: 'download'

            MDTextField:
                id: URL
                hint_text: 'Enter Url'
                pos_hint: {'center_x': 0.5, 'center_y': 0.7}
                size_hint_x: None
                width:300

            MDTextField:
                id: RES
                hint_text: 'Enter Resolution'
                helper_text: "720p,  144p"
                helper_text_mode: "on_focus"
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width:300

            MDRectangleFlatButton:
                text: 'DONE'
                pos_hint:{"center_x": .5, "center_y": .2}
                on_press:
                    ur_l = URL.text
                    re_s = RES.text
                    app.store_data(ur_l, re_s)
                    app.download_tem()
'''


class YouFast(MDApp):
    def __init__(self, **kwargs):
        self.title = 'YouFast Downloader'
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Red"
        self.URL = None
        self.RES = None
        self.dialog = None
        self.yt = None
        self.sm = ScreenManager()
        super().__init__(**kwargs)
        self.grid = Builder.load_string(Main_Grid)

    def build(self):
        self.sm.add_widget(YouFast.home_grid(self))
        return self.sm

    def home_grid(self):
        screen = Screen()
        screen.add_widget(self.grid)
        return screen

    def store_data(self, a, b):
        try:
            self.URL = a
            self.RES = b
            self.yt = YouTube(self.URL)
        except:
            try:
                if not self.dialog:
                    self.dialog = MDDialog(
                        title=f"Enter valid HTTP Address and Resolution!!",
                        size_hint=(.5, 1),
                    )
                self.dialog.open()
            except:
                pass

    def download_tem(self):
        try:
            if not self.dialog:
                self.dialog = MDDialog(
                    title=f"{self.yt.title}   - {int(self.yt.length) / 60}m",
                    size_hint=(.5, 1),
                    buttons=[
                        MDFlatButton(
                            text='DOWNLOAD', text_color=self.theme_cls.primary_color, on_press=self.download
                        ),
                    ],
                )
            self.dialog.open()
        except:
            pass

    def download(self, obj):
        try:
            notification.notify(title='YouFast -Downloading', message=f'Downloading  -{self.yt.title}')
            if self.RES >= '720' or self.RES >= '720p':
                select = self.yt.streams.filter(progressive=True, file_extension='mp4').first()
                select.download()
            elif self.RES <= '144' or self.RES <= '144p':
                select = self.yt.streams.filter(progressive=True, file_extension='mp4').last()
                select.download()
            else:
                select = self.yt.streams.filter(progressive=True, file_extension='mp4').last()
                select.download()
            notification.notify(title='YouFast -Downloaded', message=f'{self.yt.title} -Download Completed!')
        except:
            pass


if __name__ == '__main__':
    YouFast().run()
