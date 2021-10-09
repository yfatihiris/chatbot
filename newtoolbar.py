from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.floatlayout import MDFloatLayout

Window.size = (310, 580)

Builder.load_string("""
#:import NoTransition kivy.uix.screenmanager.NoTransition
#:import ChatBot only_chat_screen.ChatBot
#:import rgba kivy.utils.rgba

<IconB@MDIconButton>:
    ripple_scale: 0
    user_font_size: "30sp"
    theme_text_color: "Custom"
    active: self.parent.active == self if self.parent else False
    text_color: rgba(90, 14, 5, 255) if self.active else rgba(240, 103, 86, 255)
    
    on_release:
        self.parent.active = self
        app.root.get_screen('main_app').ids.scr.current = self.name

<IconC@ButtonBehavior+Image>
    images: '', ''
    source: self.images[bool(self.active)]
    active: self.parent.active == self if self.parent else False
    size_hint: None, None
    pos_hint: {"center_x": .525, "center_y": .5}
    mipmap: True
    
    size: dp(42), dp(42)
    
    on_release:
        self.parent.active = self
        app.root.get_screen('main_app').ids.scr.current = self.name

<CustomLabel@MDLabel>:
    halign: "center"
    font_name: "BPoppins"
    font_size: "12sp"
    theme_text_color: "Custom"
    text_color: rgba(15, 152, 169, 255)

<NewToolBar>:
    name: 'main_app'
    md_bg_color: rgba(228, 245, 247, 255)
    ScreenManager:
        id: scr
        transition: NoTransition()
        MDScreen:
            name: "giris"
            MDFloatLayout:
                MDLabel:
                    text: "Hello Sir"
                    font_name: "BPoppins"
                    font_size: "35sp"
                    size_hint: .8, .2
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: rgba(53, 56, 60, 1)
                    pos_hint: {"center_x": .5, "center_y": .75}
                MDFloatLayout:
                    size_hint: .25, .25
                    pos_hint: {"center_x": .5, "center_y": .5}
                    canvas:
                        Color:
                            rgba: rgba(1, 170, 23, 255)        
                        RoundedRectangle:
                            size: self.size
                            pos: self.pos
                            radius: [22, 22, 22, 22]
                Button:
                    text: "hey"
                    size_hint: .25, .25
                    pos_hint: {"center_x": .5, "center_y": .5}
                    background_color: 0,0,0,0
                    on_release:
                        scr.current = "home"
                MDLabel:
                    text: ""
                    size_hint: .45, .5
                    pos_hint: {"center_x": .5, "center_y": .1}
                    halign: "center"
                Image:
                    source: 'images/start_icon.JPG'
        MDScreen:
            name: "home"
            MDLabel:
                text: "start logo"
                pos_hint: {"center_y": .5}
                halign: "center"
            Image:
                source: 'images/ARKA PLAN-01.jpg'
            ScreenManager:
                ChatBot
        MDScreen:
            name: "search"
            MDLabel:
                text: ""
                pos_hint: {"center_y": .5}
                halign: "center"
            MDFloatLayout:
                md_bg_color: rgba(228, 245, 247, 255)
                Image:
                    source:"images/chatbot.jpg"
                    size_hint: .6, .3
                    pos_hint: {"center_x": .5, "center_y": .75}
                MDLabel:
                    text: app.username
                    font_name: "BPoppins"
                    font_size: "25sp"
                    pos_hint: {"center_x": .5, "center_y": .52}
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: rgba(15, 152, 169, 255)
                MDLabel:
                    text: "Fatih İriş"
                    font_name: "BPoppins"
                    font_size: "15sp"
                    pos_hint: {"center_x": .5, "center_y": .46}
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: rgba(15, 152, 169, 255)
                MDLabel:
                    text: "Son Skor"
                    font_name: "BPoppins"
                    font_size: "25sp"
                    pos_hint: {"center_x": .5, "center_y": .35}
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: rgba(15, 152, 169, 255)
                MDFloatLayout:
                    md_bg_color: rgba(178, 178, 178, 255)
                    size_hint : 2, .002
                    pos_hint: {"center_x": .3, "center_y": .3}
                MDLabel:
                    text: "20"
                    font_name: "BPoppins"
                    font_size: "15sp"
                    pos_hint: {"center_x": .5, "center_y": .25}
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: rgba(15, 152, 169, 255)
                MDFloatLayout:
                    md_bg_color: rgba(178, 178, 178, 255)
                    size_hint : 2, .002
                    pos_hint: {"center_x": .1, "center_y": .2}
        MDScreen:
            name: "home1"
            MDFloatLayout:
                MDFloatLayout:
                    MDLabel:
                        text: "hesap"
                        pos_hint: {"center_y": .75}
                        halign: "center"
                        font_name: "BPoppins"
                        font_size: "12sp"
                        theme_text_color: "Custom"
                        text_color: rgba(15, 152, 169, 255)
                    CustomLabel:
                        text: app.username
                        pos_hint: {"center_y": .7}
                    CustomLabel:
                        text: ""
                        pos_hint: {"center_y": .65}
                    CustomLabel:
                        text: "eposta"
                        pos_hint: {"center_y": .6}
                    CustomLabel:
                        text: app.email
                        pos_hint: {"center_y": .55}
                    CustomLabel:
                        text: "ülke/bölge"
                        pos_hint: {"center_y": .5}
                    CustomLabel:
                        text: ""
                        pos_hint: {"center_y": .45}
                    CustomLabel:
                        text: "Premium Abonelik"
                        pos_hint: {"center_y": .4}
                    CustomLabel:
                        text: "Genel"
                        pos_hint: {"center_y": .35}
                    CustomLabel:    
                        text: "Bildirimler"
                        pos_hint: {"center_y": .3}
                    CustomLabel:
                        text: "arayüz dili"
                        pos_hint: {"center_y": .25}
                    CustomLabel:
                        text: "türkçe"
                        pos_hint: {"center_y": .2}
                    CustomLabel:
                        text: "hakkımızda"
                        pos_hint: {"center_y": .15}
        MDScreen:
            name: "search1"
            md_bg_color: rgba(15, 152, 169, 255)
            BoxLayout:
                pos_hint: {"top": .9}
                orientation: "vertical"
            ScrollView:
                size_hint_y: .77
                pos_hint: {"x": 0, "y": .116}
                do_scroll_x: False
                do_scroll_y: True
                BoxLayout:
                    orientation: 'vertical'
                    size: (root.width, root.height)
                    height: self.minimum_height
                    size_hint: None, None
                    pso_hint: {'top': 10}
                    cols: 1
                    spacing: 5
                    MDLabel:
                        text: "Hello Sir Notification"
                        font_name: "BPoppins"
                        font_size: "35sp"
                        size_hint: .8, None
                        halign: "center"
                        theme_text_color: "Custom"
                        text_color: rgba(15, 152, 169, 255)
                        pos_hint: {"center_x": .5, "center_y": .75}
                        canvas.before:
                            Color:
                                rgb: rgba(228, 245, 247, 1)
                            RoundedRectangle:
                                size: self.size
                                pos: self.pos
                                radius: [23, 23, 23, 23]
                    Button:
                        size_hint_y: None
                        
                    Button:
                        size_hint_y: None
                    Button:
                        size_hint_y: None
        MDScreen:
            name: "search2"
            error_box: error_box
            Image:
                source: 'images/ARKA PLAN-01.jpg'
            ScrollView:
                size_hint_y: .77
                pos_hint: {"x": 0, "y": .116}
                do_scroll_x: False
                do_scroll_y: True
                BoxLayout:
                    id: error_box
                    orientation: 'vertical'
                    size: (root.width, root.height)
                    height: self.minimum_height
                    size_hint: None, None
                    pso_hint: {'top': 10}
                    cols: 1
                    spacing: 5
    NavBar:
        size_hint: 1, .1
        pos_hint: {"center_x": .5, "center_y": .95}
        md_bg_color: rgba(228, 245, 247, 255)
        panel_color: 1, 1, 1, 1
        MDBoxLayout:
            spacing: 28
            adaptive_size: True
            pos_hint: {"center_x": .525, "center_y": .5}
            active: None
            IconC:
                images: "icons/gönder simgesi-08.png", "icons/gönder simgesi-09.png"
                name: "home"
            IconC:
                images: "icons/gönder simgesi-05.png", "icons/gönder simgesi-04.png"
                name: "search"
            IconC:
                images: "icons/gönder simgesi-03.png", "icons/gönder simgesi-02.png"
                name: "home1"
            IconC:
                images: "icons/gönder simgesi-07.png", "icons/gönder simgesi-06.png"
                name: "search1"
            IconC:
                images: "icons/gönder simgesi-10.png", "icons/gönder simgesi-11.png"
                name: "search2"
""")


class NavBar(MDFloatLayout):
    pass


class NewToolBar(MDScreen):
    pass


if __name__ == "__main__":

    class BottomNavbar(MDApp):
        def build(self):
            return NewToolBar()

    BottomNavbar().run()
