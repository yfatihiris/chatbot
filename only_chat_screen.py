from functools import partial
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.properties import StringProperty, NumericProperty
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen


Builder.load_string("""
<Command>
    size_hint_y: None
    pos_hint: {"right": .98}
    height: self.texture_size[1]
    padding: 12, 10
    theme_text_color: "Custom"
    text_color: rgba(15, 152, 169, 255)
    join: True
    join_left: True
    cross: False
    canvas.before:
        Color:
            rgb: rgba(100, 100, 100, 255)
        RoundedRectangle:
            size: self.width + 4, self.height + 4
            pos: self.x - 2, self.y - 2
            radius: [23, 23, 23, 23]
        Color:
            rgb: rgba(228, 245, 247, 255)
        RoundedRectangle:
            size: self.width, self.height
            pos: self.pos
            radius: [23, 23, 23, 23]
        Color:
            rgba: rgba(228, 245, 247, (self.join or 0) * 255)
        Rectangle:
            size: self.width * .15, self.height
            pos: [self.right - self.width * .15, self.x][self.join_left or 0], self.y - self.height * .6
        Ellipse:
            pos: [self.right - self.width * .15, self.x][self.join_left or 0], self.y - self.height * .7
            size: self.width * .15, self.width * .15
            angle_start: 90
            angle_end: 270
    canvas.after:
        Color:
            rgba: 1, 1, 1, ((self.cross or 0) * .75)
        Rectangle:
            pos: (self.right - self.width*.2, self.y + (self.height - self.width*.2) * .5)
            size: self.width*.2, self.width*.2
            source: 'icons/gönder simgesi-11.png'
    on_touch_down:
        root.parent.remove_widget(self) if self.cross and self.collide_point(*args[1].pos) \
        and args[1].x > (self.right - self.width*.2) else ''

<Response>
    size_hint_y: None
    pos_hint: {"x": .02}
    height: self.texture_size[1]
    padding: 12, 10
    join_left: False
    canvas.before:
        Color:
            rgb: rgba(228, 245, 247, 1)
        RoundedRectangle:
            size: self.width, self.height
            pos: self.pos
            radius: [23, 23, 23, 23]

<ResponseBox>
    Response
<ChatBot>:
    bot_name: bot_name
    text_input: text_input
    chat_list: chat_list
    name: "chats"

    MDFloatLayout:
        MDFloatLayout:
            md_bg_color: rgba(245, 245, 245, 255)
            size_hint_y: .11
            pos_hint: {"center_y": .95}
            MDLabel:
                id: bot_name
                text: ""
                pos_hint: {"center_y": .5}
                halign: "center"
                font_name: "BPoppins"
                font_size: "25sp"
                theme_text_color: "Custom"
                text_color: rgba(53, 56, 60, 255)
        ScrollView:
            size_hint_y: .77
            pos_hint: {"x": 0, "y": .116}
            do_scroll_x: False
            do_scroll_y: True
            BoxLayout:
                id: chat_list
                orientation: 'vertical'
                size: (root.width, root.height)
                height: self.minimum_height
                size_hint: None, None
                pso_hint: {'top': 10}
                cols: 1
                spacing: 5
        MDFloatLayout:
            md_bg_color: rgba(245, 245, 245, 255)
            size_hint_y: .11
            MDFloatLayout:
                size_hint: .8, .75
                pos_hint: {"center_x": .43, "center_y": .5}
                canvas:
                    Color:
                        rgb: rgba(238, 238, 238, 255)
                    RoundedRectangle:
                        size: self.size
                        pos: self.pos
                        radius: [23, 23, 23, 23]
                TextInput:
                    id: text_input
                    hint_text: "Type your message..."
                    size_hint: 1, None
                    pos_hint: {"center_x": 0.5, "center_y": .5}
                    font_size: "18sp"
                    height: self.minimum_height
                    multiline: False
                    cursor_color: rgba(15, 152, 169, 255)
                    cursor_width: "2sp"
                    foreground_color: rgba(15, 152, 169, 255)
                    background_color: 0,0,0,0
                    padding: 15
                    font_name: "Poppins"
                    
            MDIconButton:
                icon: "send"
                pos_hint: {"center_x": .91, "center_y": .5}
                user_font_size: "18sp"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                md_bg_color: rgba(15, 152, 169, 255)
                on_release: root.send()
""")


class Command(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    font_name = "Poppins"
    font_size = 17


class Response(Command):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    font_name = "Poppins"
    font_size = 17


class ChatBot(MDScreen):
    def change_screen(self, name):
        self.manager.current = name

    def response(self, value, *args):
        response_string = ""
        if value.lower() == "hello":
            response_string = "Hello. I am Your Personal Assistant."
        elif value.lower() == "how are you?":
            response_string = "I'm doing well. Thanks!"
        if response_string:
            self.chat_list.add_widget(Response(text=response_string, size_hint_x=0.55))
        else:
            response_string = "Sorry could you say that again?"
            for resp in self.chat_list.children[:2]:
                resp.join = False
            command = self.chat_list.children[0]
            command.pos_hint = {"right": 0.90}
            command.size_hint_x += 0.08
            self.chat_list.children[0].cross = True
            self.chat_list.add_widget(
                Response(text=response_string, size_hint_x=0.55, join=False)
            )
            app = MDApp.get_running_app()
            app.root.get_screen("main_app").ids.scr.get_screen(
                "search2"
            ).error_box.add_widget(Command(text=command.text, size_hint=(0.5, None)))

    def send(self):
        value = self.text_input.text
        if self.text_input != "":
            sizes = {6: 0.22, 11: 0.32, 16: 0.45, 21: 0.58, 26: 0.71}
            for length, sze in sizes.items():
                if len(value) < length:
                    size = sze
                    halign = "center"
                    break
            else:
                size = 0.77
                halign = "left"
            self.chat_list.add_widget(
                Command(text=value, size_hint_x=0.5, halign=halign)
            )
            Clock.schedule_once(partial(self.response, value), 2)
            self.text_input.text = ""


if __name__ == "__main__":

    class ChatBotApp(MDApp):
        def build(self):
            sm = ScreenManager()
            sm.add_widget(ChatBot())
            return sm

    ChatBotApp().run()
