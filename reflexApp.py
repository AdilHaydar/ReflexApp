from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from time import sleep, time
from random import randint
from kivy.properties import NumericProperty
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.graphics import Color


Window.size = (300, 500)

helper = """
ScreenManager:

    MenuScreen:

    ReflexScreen:
    
    MainScreen:
    
    AimScreen:
    
<Ball>:
    size_hint: None, None
    size: 40, 40
    canvas:
        Ellipse:
            pos: self.pos
            size: self.size
            
<AimWidget>
    ball: pong_ball
    
    Ball:
        id: pong_ball
        center: root.center
    
   
        
<AimScreen>
    id: aim
    name: 'aim'
    label: remainingLabel
    AimWidget:
        id: widget
    Label:
        font_size: 40
        color: 0,0,0,1
        id: remainingLabel
        center_x: root.center_x
        center_y: root.center_y
        text: str(root.label)
        
<MainScreen>:
    id: main
    name: 'main'
    
    BoxLayout:
        orientation: 'vertical'

        MDToolbar:
            title: 'Test Your Reflex'
            elevation:10
            left_action_items: [["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
            
        Widget:  
        
    MDRectangleFlatButton:
        text: 'R E F L E X'
        on_press: root.manager.current = 'reflex'
        size_hint_x: None
        size_hint_y: None
        width: 20
        height: 30
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        md_bg_color: 0.2,0.3,0.6,0.1
        text_color: 0.2, 0.5, 0.6, 1
    
    MDRectangleFlatButton:
        text: 'A I M'
        on_press: root.manager.current = 'aim'
        size_hint_x: None
        size_hint_y: None
        width: 20
        height: 30
        pos_hint: {'center_x':0.5, 'center_y':0.4}
        md_bg_color: 0.2,0.3,0.6,0.1
        text_color: 0.2, 0.5, 0.6, 1
    
    MDLabel:
        id: score_label
        valign: 'center'
        halign: 'center'
        size_hint_y: None
        color: (1,0,0,0.8)


<ReflexScreen>:
    id: reflex
    name: 'reflex'

    Button:
        id: reflex_button
        text: 'Wait Change The Color'
        font_size: '20sp'
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        on_press: root.manager.current = 'main'
        size_hint_x: None
        size_hint_y: None
        width: 300
        height: 500
        background_color: 1,0,0,0.8

<MenuScreen>
    id: menu
    name: 'menu'

   
    Screen:
        BoxLayout:
            orientation: 'vertical'
    
            MDToolbar:
                title: 'Test Your Reflex'
                elevation:10
                left_action_items: [["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
            Widget:
    
        MDRectangleFlatButton:
            text: 'R E F L E X'
            on_press: root.manager.current = 'reflex'
            size_hint_x: None
            size_hint_y: None
            width: 20
            height: 30
            pos_hint: {'center_x':0.5, 'center_y':0.5}
            md_bg_color: 0.2,0.3,0.6,0.1
            text_color: 0.2, 0.5, 0.6, 1
        
        MDRectangleFlatButton:
            text: 'A I M'
            on_press: root.manager.current = 'aim'
            size_hint_x: None
            size_hint_y: None
            width: 20
            height: 30
            pos_hint: {'center_x':0.5, 'center_y':0.4}
            md_bg_color: 0.2,0.3,0.6,0.1
            text_color: 0.2, 0.5, 0.6, 1
        
        
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'
                
                ScrollView:
                    
                    MDList:
                        OneLineIconListItem:
                            text: 'Profile'
                            IconLeftWidget:
                                icon: 'account'
                        OneLineIconListItem:
                            text: 'Upload'
                            IconLeftWidget:
                                icon: 'file-upload'
                        OneLineIconListItem:
                            text: 'Logout'
                            IconLeftWidget:
                                icon: 'logout'
           
"""

#center_x: 175
#center_y: 275

class Ball(Widget):
    pos_x = NumericProperty()
    pos_y = NumericProperty()


class AimWidget(Widget):

    def update(self, dt):
        pass

class AimScreen(Screen):

    starter = NumericProperty()
    ender = NumericProperty()
    #label = ObjectProperty() buna gerek yok

    aim = AimWidget()
    Clock.schedule_interval(aim.update, 1.0/60.0)
    def on_pre_enter(self, *args):
        self.remaining = 30
        self.label.text = str(self.remaining)
        self.check = True
        print(self.check)
        self.ids.widget.ball.center = [150,250]

    def on_touch_down(self, touch):
        ball = self.ids.widget.ball

        if (touch.x >= ball.center_x-20 and touch.x <= ball.center_x+20) and (touch.y >= ball.center_y-20 and touch.y <= ball.center_y+20):
            if self.remaining == 30:
                self.starter = time()
            self.remaining -= 1
            ball.center = [randint(20,280),randint(20,480)]
        if self.remaining == 0:
            self.ender = time()
            self.manager.current = 'main'
        self.label.text = str(self.remaining)
    def on_leave(self, *args):
        self.difference = str(round(self.ender - self.starter, 4) * 1000)
        self.manager.get_screen('main').ids.score_label.text = (self.difference[0:2]+"."+self.difference[2:4]+" Seconds")

class ReflexScreen(Screen):
    start = NumericProperty()
    end = NumericProperty()

    def on_pre_enter(self, *args):
        self.ids.reflex_button.background_color = (1, 0, 0, 0.8)
        self.ids.reflex_button.text = "Wait Change The Color"

    def on_enter(self, *args):
        """Event fired when the screen is displayed: the entering animation is
        complete."""
        sleep(randint(1,6))

        self.ids.reflex_button.background_color = (0,1,0,0.8)

        self.ids.reflex_button.text = 'CLICK !!!'
        self.start = time()

        #return start

    def get_time_diff(self):
        return self.end - self.start

    def on_pre_leave(self, *args):
        self.end = time()

    def on_leave(self, *args):
            self.difference = round(self.end-self.start,4) * 1000
            self.manager.get_screen('main').ids.score_label.text = str(round(self.difference, 4))+" MS "
            #return end

class MainScreen(Screen):
    pass

class MenuScreen(Screen):
    pass

class ReflexApp(MDApp):

    def build(self):
        screen = Builder.load_string(helper)
        screen.canvas.add(Color(1,0,0))
        return screen

ReflexApp().run()




