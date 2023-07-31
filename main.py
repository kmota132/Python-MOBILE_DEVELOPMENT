#importar o APP , Builder , (gui)
#criar app
#criar a funçao build
from kivy.app import App
from kivy.lang import Builder
import requests

GUI = Builder.load_file("tela.kv")

class MeuApp(App):
    def build(self):
        return GUI
    
    def on_start(self):
        self.root.ids["moeda1"].text = f"Dolar R$ {self.pegar_cotacao('USD')}"
        self.root.ids["moeda2"].text = f"Euro R$ {self.pegar_cotacao('EUR')}"
        self.root.ids["moeda3"].text = f"Bitcoin R$ {self.pegar_cotacao('BTC')}"
        self.root.ids["moeda4"].text = f"Novo Sol R$ {self.pegar_cotacao('PEN')}"
        return super().on_start()
    
    def pegar_cotacao(self, moeda):
        link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        cotacao = dic_requisicao[f"{moeda}BRL"]["bid"]
        return cotacao

MeuApp().run()