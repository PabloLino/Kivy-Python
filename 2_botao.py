from kivy.app import App
from kivy.uix.button import Button

class MainApp(App):
    def build(self):  #definido uma função para o botão na tela
        button = Button(
            text='Botão acionado!!!', #essa é a mensagem que está grava no botão, podia ser um clique aqui, por exemplo.
            size_hint=(0.15, 0.15),   # defini o tamanho manualmente conforme o tamanho da frase que está gravada no botão, sendo que, se for menor que esse tamanho a frase irá ultrapassar o tamanho do botão, 
            # visualmente não fica bom o texto fora do botão acionador.
            pos_hint={'center_x': 0.5, 'center_y': 0.5}) # centralização do botão
        button.bind(on_press = self.on_press_button)
        return button

    def on_press_button(self, instance):
        print('Você apertou o botão!')

if __name__ == '__main__':
    app = MainApp()
    app.run()

