from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager

from screens.in_screen import InScreen



class MourMapsApp(MDApp):
    title = "MourMaps"
    screens = []
    
    def build(self):
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        self.root = MDScreenManager()
        self.kvs_loader()
        self.screens.append(InScreen(name="in_screen"))
        self.root.add_widget(self.screens[0])
        return self.root
    
    
    def kvs_loader(self):
        Builder.load_file("screens/in_screen.kv")
    
    

MourMapsApp().run()