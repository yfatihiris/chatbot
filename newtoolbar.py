import json
from math import cos, sin, radians
from random import random
from kivy.lang import Builder
from kivy.uix.modalview import ModalView
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.properties import ListProperty, NumericProperty
from kivy.graphics import Line, Color, Ellipse
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.floatlayout import MDFloatLayout


Builder.load_string(
"""
#:import NoTransition kivy.uix.screenmanager.NoTransition
#:import ChatBot only_chat_screen.ChatBot
#:import rgba kivy.utils.rgba

<BImage@ButtonBehavior+Image>:
    on_release: 
        self.parent.select.text = self.source
        self.parent.modal.dismiss()

<ProfileSelect>:
    id: modal
    size_hint: .5, .5
    BoxLayout:
        orientation: 'vertical'
        Label:
            id: selected
            text: ''
            size_hint_y: .1
        GridLayout:
            modal: modal
            cols: 3
            select: selected
            BImage:
                source: 'avatar/gönder simgesi-10.png'
            BImage:
                source: 'avatar/gönder simgesi-11.png'
            BImage:
                source: 'avatar/gönder simgesi-12.png'
            BImage:
                source: 'avatar/gönder simgesi-13.png'
            BImage:
                source: 'avatar/gönder simgesi-14.png'


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

<CircleLabel>:
    canvas.before:
        PushMatrix
        Rotate:
            angle: self.angle
            axis: 0, 0, 1
            origin: self.center
    canvas.after:
        PopMatrix

<NewToolBar>:
    name: 'main_app'
    md_bg_color: rgba(228, 245, 247, 255)
    on_pre_enter:
        profile.load_profile()
    ScreenManager:
        id: scr
        transition: NoTransition()
        MDScreen:
            name: "giris"
            MDFloatLayout:
                MDFloatLayout:
                    md_bg_color: rgba(178, 178, 178, 255)
                    size_hint : 1, .002
                    pos_hint: {"center_x": .5, "center_y": .89}
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
                    text: "Click Bird for Practice"
                    size_hint: .45, .15
                    font_size: "20sp"
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .3}
                    color: rgba(135, 133, 193, 255)
                Image:
                    source: 'images/start_icon.JPG'
                    size_hint: .45, .5
                    pos_hint: {"center_x": .5, "center_y": .5}
        MDScreen:
            md_bg_color: rgba(245, 212, 39, 255)
            name: "home"
            MDLabel:
                text: ""
                pos_hint: {"center_y": .5}
                halign: "center"
            Image:
                source: 'images/ARKA PLAN-01.jpg'
                size_hint: 1, 1.4
                pos_hint: {"center_x": .5, "center_y": .5}
            ScreenManager:
                ChatBot
        MDScreen:
            name: "search"
            on_pre_enter: score.draw()
            MDLabel:
                text: ""
                pos_hint: {"center_y": .5}
                halign: "center"
            MDFloatLayout:
                md_bg_color: rgba(228, 245, 247, 255)
                Profile:
                    id: profile
                    size_hint: .6, .3
                    pos_hint: {"center_x": .5, "center_y": .75}
                Score:
                    id: score
                    circle_size: 100
                    pos_hint: {"center_x": .5, "center_y": .37}
                MDLabel:
                    text: app.username
                    font_name: "BPoppins"
                    font_size: "25sp"
                    pos_hint: {"center_x": .5, "center_y": .37}
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: rgba(15, 152, 169, 255)
                MDLabel:
                    text: ""
                    font_name: "BPoppins"
                    font_size: "15sp"
                    pos_hint: {"center_x": .5, "center_y": .075}
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: rgba(15, 152, 169, 255)
        MDScreen:
            name: "home1"
            MDFloatLayout:
                MDFloatLayout:
                    MDLabel:
                        text: "Settings"
                        pos_hint: {"center_y": .83}
                        halign: "center"
                        font_name: "BPoppins"
                        font_size: "30sp"
                        theme_text_color: "Custom"
                        text_color: rgba(15, 152, 169, 255)
                    MDLabel:
                        text: "Username"
                        pos_hint: {"center_y": .7}
                        halign: "center"
                        font_name: "BPoppins"
                        font_size: "20sp"
                        theme_text_color: "Custom"
                        text_color: rgba(15, 152, 169, 255)
                    CustomLabel:
                        text: app.username
                        pos_hint: {"center_y": .65}
                        font_size: "15sp"
                        
                    CustomLabel:
                        text: ""
                        pos_hint: {"center_y": .65}
                    CustomLabel:
                        text: "E-Mail"
                        pos_hint: {"center_y": .55}
                        font_size: "20sp"
                    CustomLabel:
                        text: app.email
                        pos_hint: {"center_y": .5}
                        font_size: "15sp"
                    CustomLabel:
                        text: "Account Type"
                        pos_hint: {"center_y": .4}
                        font_size: "20sp"
                    
                    CustomLabel:
                        text: "Premium"
                        pos_hint: {"center_y": .35}
                        font_size: "15sp"
                    CustomLabel:
                        text: ""
                        pos_hint: {"center_y": .35}
                    CustomLabel:    
                        text: "Application Language"
                        pos_hint: {"center_y": .25}
                        font_size: "20sp"
                    CustomLabel:
                        text: "English"
                        pos_hint: {"center_y": .2}
                        font_size: "15sp"
                    CustomLabel:
                        text: ""
                        pos_hint: {"center_y": .2}
                    CustomLabel:
                        text: "About Us"
                        pos_hint: {"center_y": .1}
                        font_size: "20sp"
                    MDTextButton
                        text: ""
                        size_hint: .15, .15
                        pos_hint: {"center_x": .5, "center_y": .1}
                        background_color: 0,0,0,0
                        on_release:
                            scr.current = "about"
        
        MDScreen:
            name: "about"
            MDFloatLayout:
                MDFloatLayout:
                    MDLabel:
                        text: "names"
                        pos_hint: {"center_y": .83}
                        halign: "center"
                        font_name: "BPoppins"
                        font_size: "30sp"
                        theme_text_color: "Custom"
                        text_color: rgba(15, 152, 169, 255)
                    MDIconButton:
                        icon: "arrow-left"
                        pos_hint: {"center_y": .83}
                        user_font_size: "30sp"
                        theme_text_color: "Custom"
                        text_color: rgba(15, 152, 169, 255)
                        on_release:
                            scr.current = "home1"
        
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
                        text: "Notification 1 will be here"
                        font_name: "BPoppins"
                        font_size: "27sp"
                        size_hint: .8, None
                        halign: "center"
                        theme_text_color: "Custom"
                        text_color: rgba(15, 152, 169, 255)
                        pos_hint: {"center_x": .5, "center_y": .82}
                        canvas.before:
                            Color:
                                rgb: rgba(228, 245, 247, 1)
                            RoundedRectangle:
                                size: self.size
                                pos: self.pos
                                radius: [23, 23, 23, 23]
                                
                    MDLabel:
                        text: "Notification 2 will be here"
                        font_name: "BPoppins"
                        font_size: "27sp"
                        size_hint: .8, None
                        halign: "center"
                        theme_text_color: "Custom"
                        text_color: rgba(15, 152, 169, 255)
                        pos_hint: {"center_x": .5, "center_y": .73}
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
            md_bg_color: rgba(245, 212, 39, 255)
            name: "search2"
            error_box: error_box
            Image:
                source: 'images/ARKA PLAN-01.jpg'
                size_hint: 1, 1.4
                pos_hint: {"center_x": .5, "center_y": .5}
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
                    pos_hint: {'top': 10}
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
"""
)


class CircleLabel(Label):
    angle = NumericProperty(0)
    origin = ListProperty([])
    font_size = 22


class NavBar(MDFloatLayout):
    pass


class NewToolBar(MDScreen):
    pass


class ProfileSelect(ModalView):
    pass


class Profile(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()
        try:
            with open("../user_details.json") as f:
                self.details = json.load(f)
        except FileNotFoundError:
            self.details = {}
            with open("../user_details.json", "w") as f:
                json.dump(self.details, f)

    def load_profile(self):
        profile_image = self.details.get(self.app.username, {}).get("profile")
        if profile_image:
            self.source = profile_image
        else:
            self.source = "avatar/gönder simgesi-10.png"

    def on_release(self):
        ProfileSelect(on_dismiss=self.profile_pic).open()

    def profile_pic(self, inst):
        self.source = inst.ids.selected.text
        self.details[self.app.username] = {"profile": self.source}
        with open("../user_details.json", "w") as f:
            json.dump(self.details, f)


class Score(Widget):
    segments = ListProperty(
        [
            random(), random(), random(), random(), random(), random(), random(), random(),
            random(), random(), random(), random(), random(), random(), random(), random()
        ]
    )

    def draw(self, dt=None):
        self.canvas.clear()
        self.clear_widgets()
        segments = 16
        seg = 22.5
        with self.canvas:
            for i in range(1, segments + 1):
                Color(1.0 / segments * i, 1, 1, mode="hsv")
                Line(
                    circle=[
                        Window.width * self.pos_hint["center_x"],
                        Window.height * self.pos_hint["center_y"],
                        self.circle_size/2,
                        (seg * i - 1),
                        (seg * i + seg),
                    ],
                    width=self.circle_size * max(0.2, self.segments[i - 1]),
                    cap="none",
                )
                Color(rgb=(0, 0, 0))
                Ellipse(
                    pos=(
                        Window.width * self.pos_hint["center_x"] - self.circle_size/2,
                        Window.height * self.pos_hint["center_y"] - self.circle_size/2,
                    ),
                    size=(self.circle_size, self.circle_size)
                )
        self.labels()

    def labels(self):
        for i in range(16):
            mid = i * 22.5 + 90 - 11.25
            self.add_widget(CircleLabel(color=(1, .5, .75, 1),
                                        text=f'{int(self.segments[-(i+1)]*100)}',
                                        center=(
                     cos(radians(mid)) * Window.width * min(.9, max(.5, self.segments[-(i+1)])) * self.pos_hint['center_x'] +
                     Window.width * self.pos_hint['center_x'],
                     sin(radians(mid)) * Window.height * min(.9, max(.5, self.segments[-(i+1)])) * self.pos_hint['center_y'] +
                     Window.height * self.pos_hint['center_y']),
                                        angle=mid+270
                                       )
                            )


if __name__ == "__main__":

    class BottomNavbar(MDApp):
        def build(self):
            return NewToolBar()

    BottomNavbar().run()
