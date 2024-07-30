from kivy.app import App
from kivy.uix.button import Button

class MainApp(App):
    def build(self): 
        self.contador = 0  # Inicializa o contador em 0
        
        button = Button(
            text='Botão acionado!!!',
            size_hint=(0.15, 0.15),
            pos_hint={'center_x': 0.5, 'center_y': 0.5})
        button.bind(on_press=self.on_press_button)
        return button

    def on_press_button(self, instance):
        self.contador += 1
        print(f'Você apertou o botão!  {self.contador} vezes')

if __name__ == '__main__':
    app = MainApp()
    app.run()
