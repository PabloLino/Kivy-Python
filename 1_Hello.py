#criando aplicações com a biblioteca Kivy, no cmd primeiramente deve-se executar os comandos para instalar a biblioteca Kivy.
#python3 -m venv kivy_project     depois executar      python -m pip install kivy
#todo aplicativo Kivy precisa da subclasseApp e da função build(). 
#aqui ficará as definições da interface do usuário.


''' telinha responsiva '''


from kivy.app import App                            # base do aplicativo
from kivy.uix.label import Label                    # import de classe para textos na interface gráfica

class MainApp(App):
    def build(self):
        label=Label(
            text='Olá Kivy!',
            size_hint=(0.9, None),                      #posicionamento do texto (opcional), valores entre 0 e 1, pode-se usar None também
            pos_hint={'center_x': 0.5,'center_y': 0.9}  #posicionamento do texto (opcional), pode-se usar também: pos_hint={'x': 0.1, 'top': 1} ou usar right
            )
        return label
if __name__ =='__main__':
    app = MainApp()
    app.run()