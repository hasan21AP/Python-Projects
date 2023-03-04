from kivy.app import App
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
from kivy.animation import Animation as an
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex
from random import randint
from time import sleep

class Popups(Popup):
    def __init__(self,title,txt, **kwargs):
        super(Popups).__init__(**kwargs)
        self.size_hint = [None,None]
        self.size = [300,140]
        self.pos_hint = {"top":.7,"center_x":.5}
        self.title = title
        self.title_size = "15sp"
        self.separator_height = 5
        self.separator_color = get_color_from_hex("#FFFFFF")
        self.the_container = FloatLayout(size_hint=[1,1])
        self.warning = Label(text=txt.title(),font_size="18sp",bold=True,size_hint=[.9,.3],pos_hint={"center_y":.6,"center_x":.5})

class ManagerSc(ScreenManager):
    pass

class HomePage(Screen):
    pass

class PlayPage(Screen):
    pass

class MyGameApp(App):
    def build(self):
        clicked = ""
        clock = 0
        opp = ""
        you = ""
        self.title = "Rock,Paper and Scissor"
        Window.size = (700,500)
        return Builder.load_file("RPC.kv")


if __name__ == "__main__":
    game = MyGameApp()
    game.run()