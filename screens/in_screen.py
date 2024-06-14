from kivymd.uix.screen import MDScreen
from kivy.garden.mapview import MapView


class InScreen(MDScreen):
    
    def on_enter(self, *args):
        self.ids.primary_lay.add_widget(MapView(zoom=10, lat=52.5, lon=13.4))