from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
#from kivy.uix.screenmanager import Screen, ScreenManager


Window.size = (1280, 720)

class ContentNavigationDrawer(BoxLayout):
    pass

class MainApp(MDApp):

    def build(self):
        screen = Builder.load_file('UI.kv')
        return screen

    def camera(self):
        print("camera button clicked from scan screeb!")

    def choose_file_scan(self):
        print("choose button clicked from scan screen!")

    def choose_file_create(self):
        print("choose button clicked from create screen!")

    def create(self):
        print("create button clicked from create screen!")

if __name__ == "__main__":
    MainApp().run()