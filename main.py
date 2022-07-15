from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
import subprocess

Window.size=(350, 650)

String_Builder = """
Screen:
    ScreenManager: 
        id: screen_manager
        MainScreen:

<MainScreen>
    name: "main"
    MDNavigationLayout:
        ScreenManager:
            Screen:
                id: main
                MDLabel:
                    text: "IPV Changer"
                    pos_hint: {"center_y": 0.7}
                    halign: 'center'
                    font_style: "H3"
                
                MDFlatButton:
                    text: "On"
                    pos_hint: {"center_x": 0.7,"center_y": 0.2}
                    line_color: 1,1,1,1
                    on_release: app.on()
                MDFlatButton:
                    text: "Off"
                    pos_hint: {"center_x": 0.3,"center_y": 0.2}
                    line_color: 1,1,1,1
                    on_release: app.off()
                                                
"""

class MainScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(MainScreen(name="main"))


class Changer(MDApp):
    def build(self):
        self.theme_cls.theme_style='Dark'
        AppBuilder = Builder.load_string(String_Builder)
        return AppBuilder

    def Off(self):
        subprocess.run(f'netsh interface ipv4 set address name="Ethernet" static 192.168.1.30 mask=255.255.255.0', capture_output=True,shell=True, text=True)
    def On(self):
        subprocess.run(f'netsh interface ipv4 set address name="Ethernet" source=dhcp', capture_output=True,shell=True, text=True)

Changer().run()
