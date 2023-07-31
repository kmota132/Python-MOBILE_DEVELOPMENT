from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.core.window import Window
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.lang import Builder



class MeuApp(MDApp):
    Window.size = (300, 600)

    def build(self):  
        pass    
    
MeuApp().run()


    