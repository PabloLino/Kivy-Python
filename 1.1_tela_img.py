from kivy.app import App                           
from kivy.uix.label import Label
from kivy.uix.image import Image, AsyncImage   #importa  classe para colocar imagem, Image para puxar do pc e AsyncImage para puxar da web           
from kivy.uix.boxlayout import BoxLayout
#from kivy.uix. pesquisando dessa forma podemos encontrar diversos layouts disponíveis

class MainApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        label = Label(
            text='inserindo imagem!\n kkkkkkkjjjjj',
            size_hint=(0.1, 0.1),                      
            pos_hint={'center_x': 0.5,'center_y': 0.9}
            )
        
        img = AsyncImage(
                source='https://m.media-amazon.com/images/I/61U0FIe2itL._AC_UF894,1000_QL80_.jpg',
                size_hint =(0.3,0.3),
                pos_hint= {'center_x':0.5,'center_y':0.5})
        
        layout.add_widget(label)
        layout.add_widget(img)
        return layout

if __name__ =='__main__':
    app = MainApp()
    app.run()

