from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class MainApp(App):
    def build(self):  # Definindo uma função para o botão na tela
        self.contador = 0  # Inicializa o contador em 0
        #orientation='vertical'
        layout = BoxLayout(orientation='vertical',  padding=100, spacing=20) #spacing é para dar espaço da borda da página
        
        self.button = Button(
                text='Clique Aqui', 
            size_hint=(0.4, 0.2),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            background_normal='',
            background_color = ([0, 0, 128, 1]),
            color=(10, 10, 10, 10),  #rgba
            font_size='30sp',  
            border=(5, 5, 5, 5)
        )
        self.button.bind(on_press=self.on_press_button)
        
        self.label = Label(
            text='Qual seu recorde de "clicks"?',
            size_hint=(0.1, 0.1),
            pos_hint={'center_x': 0.5, 'center_y': 0.5})
        
        layout.add_widget(self.button)
        layout.add_widget(self.label)
        
        return layout

    def on_press_button(self, instance):
        self.contador += 1
        self.label.text = f'Você clicou {self.contador} vezes até agora!\n    clique no X para desistir'

if __name__ == '__main__':
    app = MainApp()
    app.run()
