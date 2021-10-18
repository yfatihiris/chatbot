import requests
from kivy.core.text import LabelBase
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivyauth.utils import auto_login, login_providers
from kivyauth.facebook_auth import login_facebook, initialize_fb
from kivyauth.google_auth import login_google, initialize_google
from kivyauth.twitter_auth import login_twitter, initialize_twitter
Window.size = (310, 580)

help_str = """
#:import NewToolBar newtoolbar.NewToolBar

<ImageB@ButtonBehavior+Image>:
    on_release:
        app.oauth_login(self.source)

ScreenManager:
    MainScreen:
    LoginScreen:
    SignupScreen:
    NewToolBar:

<MainScreen>:
    name: "main"
    MDFloatLayout:
        md_bg_color: 1, 1, 1, 1
        Image:
            source: "images/assets1.jpeg"
            size_hint: .15, .15
            pos_hint: {"center_x": .18, "center_y":.92}
        Image:
            source: "images/assets2.jpeg"
            size_hint: .8, .8
            pos_hint: {"center_x": .5, "center_y":.65}
        MDLabel:
            text: "H e l l o !"
            font_name: "BPoppins"
            font_size: "23sp"
            pos_hint: {"center_y": .38}
            halign: "center"
            color: rgba(15, 152, 169, 255)
        MDLabel:
            text: "Best place to practice English"
            font_name: "MPoppins"
            font_size: "13sp"
            size_hint_x: .85
            pos_hint: {"center_x": .5, "center_y": .3}
            halign: "center"
            color: rgba(127, 127, 127, 255)
        Button:
            text: "LOGIN"
            size_hint: .66, .065
            pos_hint: {"center_x": .5, "center_y": .18}
            background_color: 0, 0, 0, 0
            font_name: "BPoppins"
            on_release:
                root.manager.transition.direction = "left"
                root.manager.current = "login"
            canvas.before:
                Color:
                    rgb: rgba(15, 152, 169, 255)
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [5]
        Button:
            text: "SIGNUP"
            size_hint: .66, .065
            pos_hint: {"center_x": .5, "center_y": .09}
            background_color: 0, 0, 0, 0
            font_name: "BPoppins"
            color: rgba(15, 152, 169, 255)
            on_release:
                root.manager.transition.direction = "left"
                root.manager.current = "signup"
            canvas.before:
                Color:
                    rgb: rgba(15, 152, 169, 255)
                Line:
                    width: 1.2
                    rounded_rectangle: self.x, self.y, self.width, self.height, 5, 5, 5, 5, 100
<LoginScreen>:
    name: "login"
    MDFloatLayout:
        md_bg_color: 1, 1, 1, 1
        MDIconButton:
            icon: "arrow-left"
            pos_hint: {"center_y": .95}
            user_font_size: "30sp"
            theme_text_color: "Custom"
            text_color: rgba(15, 152, 169, 255)
            on_release:
                root.manager.transition.direction = "right"
                root.manager.current = "main"
    MDLabel:
        text: "W e l c o m e !"
        font_name: "BPoppins"
        font_size: "26sp"
        pos_hint: {"center_x": .6, "center_y": .85}
        color: rgba(15, 152, 169, 255)
    MDLabel:
        text: "Sign in to continue"
        font_name: "MPoppins"
        font_size: "18sp"
        pos_hint: {"center_x": .6, "center_y": .79}
        color: rgba(135, 133, 193, 255)
    MDFloatLayout:
        size_hint: .7, .07
        pos_hint: {"center_x": .5, "center_y": .63}
        TextInput:
            id:login_email
            hint_text: "Email"
            font_name: "MPoppins"
            size_hint_y: .75
            pos_hint: {"center_x": .43,    "center_y": .5}
            background_color: 1, 1, 1, 0
            foreground_color: rgba(15, 152, 169, 255)
            cursor_color: rgba(15, 152, 169, 255)
            font_size: "14sp"
            cursor_width: "2sp"
            multiline: False
            helper_text: "Required"
            helper_text_mode:  "on_error"
            required: True
        MDFloatLayout:
            pos_hint: {"center_x": .45, "center_y": 0}
            size_hint_y: .03
            md_bg_color: rgba(178,178,178,255)
    MDFloatLayout:
        size_hint: .7, .07
        pos_hint: {"center_x": .5, "center_y": .5}
        TextInput:
            id:login_password
            hint_text: "Password"
            font_name: "MPoppins"
            size_hint_y: .75
            pos_hint: {"center_x": .43,    "center_y": .5}
            background_color: 1, 1, 1, 0
            foreground_color: rgba(15, 152, 169, 255)
            cursor_color: rgba(15, 152, 169, 255)
            font_size: "14sp"
            cursor_width: "2sp"
            multiline: False
            password: True
            helper_text: 'Required'
            helper_text_mode:  'on_error'
            required: True
        MDFloatLayout:
            pos_hint: {"center_x": .45, "center_y": 0}
            size_hint_y: .03
            md_bg_color: rgba(178,178,178,255)
    Button:
        text: "LOGIN"
        size_hint: .66, .065
        pos_hint: {"center_x": .5, "center_y": .34}
        background_color: 0, 0, 0, 0
        font_name: "BPoppins"
        canvas.before:
            Color:
                rgb: rgba(15, 152, 169, 255)
            RoundedRectangle:
                size: self.size
                pos: self.pos
                radius: [5]
        on_press:
            app.login(login_email.text, login_password.text)
            app.username_changer
    MDTextButton:
        text: "Forgot Password?"
        pos_hint: {"center_x": .5, "center_y": .28}
        color: rgba(68, 78, 132, 255)
        font_size: "12sp"
        font_name: "BPoppins"
    MDLabel:
        text: "or"
        color: rgba(15, 152, 169, 255)
        pos_hint: {"center_y": .22}
        font_size: "13sp"
        font_name: "BPoppins"
        halign: "center"
    MDFloatLayout:
        md_bg_color: rgba(178, 178, 178, 255)
        size_hint : .3, .002
        pos_hint: {"center_x": .3, "center_y": .218}
    MDFloatLayout:
        md_bg_color: rgba(178, 178, 178, 255)
        size_hint : .3, .002
        pos_hint: {"center_x": .7, "center_y": .218}
    MDLabel:
        text: "Social Media Login"
        font_name: "BPoppins"
        font_size: "13sp"
        halign: "center"
        pos_hint: {"center_y": .16}
        color: rgba(135, 133, 193, 255)
    MDGridLayout:
        cols: 3
        size_hint: .48, .07
        pos_hint: {"center_x": .5, "center_y": .1}
        ImageB:
            source: "images/google.png"
            mipmap: True
        ImageB:
            source: "images/facebook.png"
            mipmap: True
        ImageB:
            source: "images/apple.png"
            mipmap: True
    MDLabel:
        text: "Don't have an account?"
        font_name: "BPoppins"
        font_size: "11sp"
        pos_hint: {"center_x": .68, "center_y": .04}
        color: rgba(135, 133, 193, 255)
    MDTextButton:
        text: "Sign up"
        font_name: "BPoppins"
        font_size: "11sp"
        pos_hint: {"center_x": .75, "center_y": .04}
        color: rgba(15, 152, 169, 255)
        on_release:
            root.manager.transition.direction = "left"
            root.manager.current = "signup"                                                 
<SignupScreen>:
    name: "signup"
    MDFloatLayout:
        md_bg_color: 1, 1, 1, 1
        MDIconButton:
            icon: "arrow-left"
            pos_hint: {"center_y": .95}
            user_font_size: "30sp"
            theme_text_color: "Custom"
            text_color: rgba(15, 152, 169, 255)
            on_release:
                root.manager.transition.direction = "right"
                root.manager.current = "main"
    MDLabel:
        text: "H i !"
        font_name: "BPoppins"
        font_size: "26sp"
        pos_hint: {"center_x": .6, "center_y": .85}
        color: rgba(15, 152, 169, 255)
    MDLabel:
        text: "Create a new account"
        font_name: "MPoppins"
        font_size: "18sp"
        pos_hint: {"center_x": .6, "center_y": .79}
        color: rgba(135, 133, 193, 255)
    MDFloatLayout:
        size_hint: .7, .07
        pos_hint: {"center_x": .5, "center_y": .68}
        TextInput:
            id:signup_username
            hint_text: "Username"
            font_name: "MPoppins"
            size_hint_y: .75
            pos_hint: {"center_x": .43,    "center_y": .5}
            background_color: 1, 1, 1, 0
            foreground_color: rgba(15, 152, 169, 255)
            cursor_color: rgba(15, 152, 169, 255)
            font_size: "14sp"
            cursor_width: "2sp"
            multiline: False
            helper_text:'Required'
            helper_text_mode:  'on_error'
            required: True
        MDFloatLayout:
            pos_hint: {"center_x": .45, "center_y": 0}
            size_hint_y: .03
            md_bg_color: rgba(178,178,178,255)
    MDFloatLayout:
        size_hint: .7, .07
        pos_hint: {"center_x": .5, "center_y": .56}
        TextInput:
            id:signup_email
            hint_text: "Email"
            font_name: "MPoppins"
            size_hint_y: .75
            pos_hint: {"center_x": .43,    "center_y": .5}
            background_color: 1, 1, 1, 0
            foreground_color: rgba(15, 152, 169, 255)
            cursor_color: rgba(15, 152, 169, 255)
            font_size: "14sp"
            cursor_width: "2sp"
            multiline: False
            helper_text:'Required'
            helper_text_mode:  'on_error'
            required: True
        MDFloatLayout:
            pos_hint: {"center_x": .45, "center_y": 0}
            size_hint_y: .03
            md_bg_color: rgba(178,178,178,255)
    MDFloatLayout:
        size_hint: .7, .07
        pos_hint: {"center_x": .5, "center_y": .44}
        TextInput:
            id:signup_password
            hint_text: "Password"
            font_name:  "MPoppins"
            size_hint_y: .75
            pos_hint: {"center_x": .43, "center_y": .5}
            background_color: 1, 1, 1, 0
            foreground_color: rgba(15, 152, 169, 255)
            cursor_color: rgba(15, 152, 169, 255)
            font_size: "14sp"
            cursor_width: "2sp"
            multiline: False
            password: True
            helper_text:'Required'
            helper_text_mode:  'on_error'
            required: True
        MDFloatLayout:
            pos_hint: {"center_x": .45, "center_y": 0}
            size_hint_y: .03
            md_bg_color: rgba(178,178,178,255)
    Button:
        text: "SIGNUP"
        size_hint: .66, .065
        pos_hint: {"center_x": .5, "center_y": .3}
        background_color: 0, 0, 0, 0
        font_name: "BPoppins"
        canvas.before:
            Color:
                rgb: rgba(15, 152, 169, 255)
            RoundedRectangle:
                size: self.size
                pos: self.pos
                radius: [5]
        on_press: app.signup()
    MDLabel:
        text: "or"
        color: rgba(15, 152, 169, 255)
        pos_hint: {"center_y": .22}
        font_size: "13sp"
        font_name: "BPoppins"
        halign: "center"
    MDFloatLayout:
        md_bg_color: rgba(178, 178, 178, 255)
        size_hint : .3, .002
        pos_hint: {"center_x": .3, "center_y": .218}
    MDFloatLayout:
        md_bg_color: rgba(178, 178, 178, 255)
        size_hint : .3, .002
        pos_hint: {"center_x": .7, "center_y": .218}
    MDLabel:
        text: "Social Media Login"
        font_name: "BPoppins"
        font_size: "13sp"
        halign: "center"
        pos_hint: {"center_y": .16}
        color: rgba(135, 133, 193, 255)
    MDGridLayout:
        cols: 3
        size_hint: .48, .07
        pos_hint: {"center_x": .5, "center_y": .1}
        Image:
            source: "images/google.png"
        Image:
            source: "images/facebook.png"
        Image:
            source: "images/apple.png"
    MDLabel:
        text: "Already have an account?"
        font_name: "BPoppins"
        font_size: "11sp"
        pos_hint: {"center_x": .68, "center_y": .04}
        color: rgba(135, 133, 193, 255)
    MDTextButton:
        text: "Sign in"
        font_name: "BPoppins"
        font_size: "11sp"
        pos_hint: {"center_x": .79, "center_y": .04}
        color: rgba(15, 152, 169, 255)
        on_release:
            root.manager.transition.direction = "left"
            root.manager.current = "login"
"""


class MainScreen(Screen):
    pass


class LoginScreen(Screen):
    pass


class SignupScreen(Screen):
    pass


class AcceptScreen(Screen):
    pass


class LoginApp(MDApp):
    username = StringProperty()
    email = StringProperty()

    def build(self):
        self.url = "https://login-96571-default-rtdb.firebaseio.com/.json"
        initialize_fb(self.oauth_passed, self.oauth_failed)
        initialize_google(self.oauth_passed, self.oauth_failed)
        try:
            initialize_twitter(self.oauth_passed, self.oauth_failed)
        except NotImplementedError as e:
            print('Twitter login unavailable')
        return Builder.load_string(help_str)

    def on_start(self):
        try:
            if auto_login(login_providers.google):
                self.current_provider = login_providers.google
            elif auto_login(login_providers.facebook):
                self.current_provider = login_providers.facebook
            elif auto_login(login_providers.twitter):
                self.current_provider = login_providers.twitter
        except NotImplementedError as e:
            print(e)

    def signup(self):
        signupEmail = self.root.get_screen("signup").ids.signup_email.text
        signupPassword = self.root.get_screen("signup").ids.signup_password.text
        signupUsername = self.root.get_screen("signup").ids.signup_username.text
        if (
            signupEmail.split() == []
            or signupPassword.split() == []
            or signupUsername.split() == []
        ):
            cancel_btn_username_dialogue = MDFlatButton(
                text="Retry", on_release=self.close_username_dialog
            )
            self.dialog = MDDialog(
                title="Invalid Input",
                text="Please Enter a valid Input",
                size_hint=(0.7, 0.2),
                buttons=[cancel_btn_username_dialogue],
            )
            self.dialog.open()
        if len(signupUsername.split()) > 1:
            cancel_btn_username_dialogue = MDFlatButton(
                text="Retry", on_release=self.close_username_dialog
            )
            self.dialog = MDDialog(
                title="Invalid Username",
                text="Please enter username without space",
                size_hint=(0.7, 0.2),
                buttons=[cancel_btn_username_dialogue],
            )
            self.dialog.open()
        else:
            signup_info = {
                signupEmail: {{"Password": signupPassword, "Username": signupUsername}}
            }
            requests.patch(url=self.url, json=signup_info)
            self.root.current = "login"

    auth = "DUU5VDWxXtDmOykzuJVl36HN5sYaMKdPrd1jRXYN"

    def login(self, email, password):
        loginEmail = email
        loginPassword = password
        self.login_check = False
        supported_loginEmail = loginEmail.replace(".", "-")
        supported_loginPassword = loginPassword.replace(".", "-")
        request = requests.get(self.url + "?auth=" + self.auth)
        data = request.json()
        if (
            supported_loginEmail in data
            and supported_loginPassword == data[supported_loginEmail]["Password"]
        ):
            self.email = supported_loginEmail
            self.username = data[supported_loginEmail]["Username"]
            self.login_check = True
            self.root.current = "main_app"
        else:
            print("user no longer exists")
            cancel_btn_username_dialogue = MDFlatButton(
                text="Retry", on_release=self.close_username_dialog
            )
            self.dialog = MDDialog(
                title="Invalid Email or Password",
                text="Please Enter a valid Email or Password",
                size_hint=(0.7, 0.2),
                buttons=[cancel_btn_username_dialogue],
            )
            self.dialog.open()

    def close_username_dialog(self, obj):
        self.dialog.dismiss()

    def username_changer(self):
        if self.login_check:
            self.strng.get_screen(
                "accept"
            ).ids.username_info.text = f"welcome {self.username}"

    def oauth_login(self, social):
        socials = {'facebook': login_facebook, 'google': login_google, 'twitter': login_twitter}
        for s in socials:
            if s in social:
                socials[s]()

    def oauth_passed(self, name, email, profile):
        pass

    def oauth_failed(self):
        pass


if __name__ == "__main__":
    LabelBase.register(name="Poppins", fn_regular="fonts/Poppins-Regular.ttf")
    LabelBase.register(name="MPoppins", fn_regular="fonts/Poppins-Medium.ttf")
    LabelBase.register(name="BPoppins", fn_regular="fonts/Poppins-Semibold.ttf")
    LoginApp().run()
