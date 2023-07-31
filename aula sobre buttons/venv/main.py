from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton, MDIconButton , MDFloatingActionButton , MDRaisedButton , MDRectangleFlatButton, MDRectangleFlatIconButton

class MeuApp(MDApp):
    Window.size = (300, 600)
    def build(self):  # R G B
        # label = MDLabel(text="Hello World", halign='center', theme_text_color='Custom', text_color=(0, 1, 0, 1))  # CUSTON: SERVE PARA CUSTOMIZAR QUALQUER COR
        boxLayout = MDBoxLayout(  #
            orientation='vertical',  # orientaçao do botao
            spacing =15,
            pos_hint={'center_x': 0.5, 'center_y': 0.5}  # pos hint : posisao  dentro do app
        )

        btn1 = MDFlatButton(
            text='Login',
            pos_hint={'center_x': 0.5, 'center_y': 1}
        )

        btn2 = MDIconButton(
            icon='home',
            pos_hint={'center_x': 0.5, 'center_y': 1}
        )
        
        btn3 = MDFloatingActionButton(
            icon='plus',
            pos_hint={'center_x': 0.5, 'center_y': 1}
        )


        btn4 = MDRaisedButton(#propriedade text 
            text ='Pagina Inicial',
            pos_hint={'center_x': 0.5, 'center_y': 1}
        )
        
        btn5 = MDRectangleFlatButton( #propriedade text
            text='Login',
            pos_hint={'center_x': 0.5, 'center_y': 1}
        )  
        
        btn6 = MDRectangleFlatIconButton( #propriedade text e icon
            text='Pagina Inicial',
            icon = 'home',
            pos_hint={'center_x': 0.5, 'center_y': 1}
        )  

        boxLayout.add_widget(btn1)
        boxLayout.add_widget(btn2)
        boxLayout.add_widget(btn3)
        boxLayout.add_widget(btn4)
        boxLayout.add_widget(btn5)
        boxLayout.add_widget(btn6)


        return boxLayout

MeuApp().run()


    