from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFillRoundFlatButton
from random import choice
from datetime import datetime
from kivy.graphics.texture import Texture
import cv2
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.utils import get_color_from_hex

class Tab(MDScreen, MDTabsBase):
    pass
class Togetheram(ScreenManager):
    overlay_color = get_color_from_hex("#2e82ff")
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.capture = cv2.VideoCapture(0)
        Clock.schedule_interval(self.update, 1.0 / 30.0)
            
        
    def open_keyboard(self, instance_textinput):
        if instance_textinput.focus and instance_textinput.keyboard_mode == 'default':
            instance_textinput._keyboard = self.root.get_root_window().request_keyboard(
                self._keyboard_closed, instance_textinput, 'text'
            )
            instance_textinput._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _keyboard_closed(self):
        pass

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'enter':
            self.root.ids.text_field.focus = False
        return True
    
    def update(self, dt):
        ret, frame = self.capture.read()
        if ret:
            buf1 = cv2.flip(frame, 0)
            buf = buf1.tostring()
            texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
            self.ids.camera_view.texture = texture
    
    def take_photo(self, *args):
        ret, frame = self.capture.read()
        if ret:
            current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            photo_path = f"image_{current_time}.png"
            cv2.imwrite(photo_path, frame)
        
    def dlog(self):
        self.dialog = MDDialog(
            text = "Check your phone's Internet connection and try again.",
            elevation = .05,
            radius=[45, 45, 45, 45],
            md_bg_color = (255/255, 255/255, 255/255),
            buttons = [
                MDFillRoundFlatButton(text = "OK", on_release = self.dlg, md_bg_color = (255/255, 255/255, 255/255),
                                      theme_text_color = "Custom",
                                      text_color = (46/255, 130/255, 255/255),
                                      )
            ],
        )
        self.dialog.open()
        
    def work_dlg(self, *args):
        self.dialog.dismiss()
    
    def dlg(self, *args):
        self.dialog.dismiss()

    # اعضای لیست#################################
    def select(self, root):
        root.current = "select"
        root.transition.direction = "up"
    def main_scrn(self, root):
        root.current = "main"
        root.transition.direction = "down"
    def textinput(self, root):
        root.current = "textinput"
        root.transition.direction = "up"
    def contact(self, root):
        root.current = "contact"
        root.transition.direction = "up"
    def camera(self, root):
        root.current = "camera"
        root.transition.direction = "up"
    def bg(self, root):
        root.current = "bg"
        root.transition.direction = "up"
    def chat(self, root):
        root.current = "chats"
        root.transition.direction = "up"
    def mom(self, root):
        root.current = "Mom"
        root.transition.direction = "up"
    def bro(self, root):
        root.current = "brother"
        root.transition.direction = "up"
    def am(self, root):
        root.current = "am"
        root.transition.direction = "up"
    def za(self, root):
        root.current = "za"
        root.transition.direction = "up"
    def su(self, root):
        root.current = "su"
        root.transition.direction = "up"
    def d2(self, root):
        root.current = "d2"
        root.transition.direction = "up"
    def za2(self, root):
        root.current = "za2"
        root.transition.direction = "up"
    def ma(self, root):
        root.current = "ma"
        root.transition.direction = "up"
    def sa(self, root):
        root.current = "sa"
        root.transition.direction = "up"
    def ra(self, root):
        root.current = "ra"
        root.transition.direction = "up"
    def hc(self, root):
        root.current = "hc"
        root.transition.direction = "up"
    def mc(self, root):
        root.current = "mc"
        root.transition.direction = "up"
    def mc2(self, root):
        root.current = "mc2"
        root.transition.direction = "up"
    # اعضای لیست################################
    def change_background_color(self, screen):
        # انتخاب رنگ تصادفی از میان رنگ‌های تعریف شده
        colors = [(1, .5, 0, 1),
                  (206/255, 128/255, 255/255),
                  (255/255, 38/255, 84/255),
                  (0/255, 245/255, 52/255),
                  (97/255, 216/255, 255/255),
                  (255/255, 26/255, 188/255),
                  (0/255, 165/255, 35/255),
                  (157/255, 0/255, 255/255),
                  (0/255, 162/255, 255/255),
                  (0/255, 0/255, 239/255),
                  (56/255, 255/255, 154/255),
                  (50/255, 79/255, 104/255),
                  (175/255, 0/255, 91/255),
                  (255/255, 252/255, 0/255),
                  (197/255, 96/255, 46/255),
                  (255/255, 222/255, 0/255),
                  (73/255, 158/255, 71/255),
                  (220/255, 154/255, 224/255),
                  (170/255, 157/255, 149/255),
                  (176/255, 75/255, 0/255)]   
        random_color = choice(colors)
        screen.md_bg_color = random_color
        
    def open_cam(self):
        self.current = "camera"
        
    def set_selection_mode(self, instance_selection_list, mode):
        if mode:
            md_bg_color = self.overlay_color
            left_action_items = [["arrow-left", lambda x: self.ids.selection_list.unselected_all(),]]
            right_action_items = [["pin"], ["delete"], ["dots-vertical"]]
        else:
            md_bg_color = get_color_from_hex("#2e82ff")
            left_action_items = [[""]]
            right_action_items = [["camera-outline", lambda x: self.open_cam()],["magnify"], ["dots-vertical"]]
            self.ids.toolbar.title = "Togetheram"

        Animation(md_bg_color=md_bg_color, d=0.2).start(self.ids.toolbar)
        self.ids.toolbar.left_action_items = left_action_items
        self.ids.toolbar.right_action_items = right_action_items

    def on_selected(self, instance_selection_list, instance_selection_item):
        self.ids.toolbar.title = str(
            len(instance_selection_list.get_selected_list_items())
        )

    def on_unselected(self, instance_selection_list, instance_selection_item):
        if instance_selection_list.get_selected_list_items():
            self.ids.toolbar.title = str(
                len(instance_selection_list.get_selected_list_items())
            )
        
        
    Builder.load_file("Togetheram.kv")
    
class Main(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        return Togetheram()
    def change_screen_color(self):
        screen = self.root.get_screen("textinput")
        self.root.change_background_color(screen)
    
Main().run()
