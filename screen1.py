#import nltk
#from nltk.corpus import stopwords //not needed because we hardcoded the library
from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'system')
Config.set('graphics', 'resizable', False)
from random import sample
import kivy 
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivy.core.text import LabelBase
from kivy.config import Config
from kivy.app import App

 
# 0 being off 1 being on as in true / false
# you can use 0 or 1 && True or False

kivy.require('1.9.0')
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
import query_retrieval
import query

# The screen manager is a widget
# dedicated to managing multiple screens for your application.
from kivy.uix.screenmanager import (ScreenManager, Screen, SlideTransition)


# You can create your kv code in the Python file
screen_helper = '''
#:import utils kivy.utils

ScreenManager:
    Menu:
        name: 'Menu'
    Input_User:
        name: 'Input'
    Results:
        name: 'Results'

<Menu>:
    Widget:
        canvas:
            Color:
                rgba:213/255, 228/255, 237/255, 1
            Rectangle:
                size: self.size
                pos: self.pos
    FloatLayout:
        #title
        Label:
            text: 
                """Trending:
                Presidential
                Candidates"""
            pos_hint: {'center_x': .62, 'center_y': .66} 
            size_hint: 1, 0.1
            font_size: self.width/12
            font_name:"Quincy Bold"
            color: '#39586B'
            
        Image: #twt icon
            source: 'demo.png'
            pos_hint: {'center_x': .55, 'center_y': .46}
            size_hint: (1.3,1.3)
        Image: #rt
            source: 'demo5.png'
            pos_hint: {'center_x': .47, 'center_y': .46}
            size_hint: (1.0,1.0)
        
        #catchphrase
        Label:
            text: 
                """Retrieve unbiased online data effectively
                regarding your presidential candidate."""
            pos_hint: {'center_x': .555, 'center_y': .365} 
            size_hint: 1, 0.1
            font_size: self.width/35
            font_name:"Poppins"
            color: '#39586B'
            
        Button:
            text: "START"
            background_color :'#587180'
            size_hint: (.25,.10)
            pos_hint: {'center_x': .35, 'center_y': .13}
            background_normal: ""

            on_press:
                # You can define the duration of the change
                # and the direction of the slide
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'Input'

        Button:
            text: "QUIT"
            background_color :'#587180'
            size_hint: (.25,.10)
            pos_hint: {'center_x': .65, 'center_y': .13}
            background_normal: ""

            on_press:
                quit()

<Input_User>:
    Widget:
        canvas:
            Color:
            #rgba(213, 228, 237, 1)
                rgba:213/255, 228/255, 237/255, 1
            Rectangle:
                size: self.size
                pos: self.pos   
    FloatLayout:
        Image:
            source: 'demo2.png'
            pos_hint: {'center_x': .55, 'center_y': .64}
            size_hint: (0.9,0.9)
        Image:
            source: 'line.png'
            pos_hint: {'center_x': .50, 'center_y': .50}
            size_hint: (1.1,1.1)
        Button:
            text: "Enter search query"
            background_color :'#587180'
            size_hint: (.50,.07)
            font_size: self.width/20
            font_name:"Poppins"
            pos_hint: {'center_x': .70, 'center_y': .68}
            background_normal: ""
        Button:
            size_hint: (.50,.07)
            pos_hint: {'center_x': .70, 'center_y': .60}
            background_color :'#A6C3D4'
            background_normal: ""   
        
        #guidelines
        Label:
            text: "GUIDELINES"
            size_hint: (.50,.07)
            font_size: self.width/13
            color: '#39586B'
            font_name:"Quincy Bold"
            pos_hint: {'center_x': .20, 'center_y': .75}
                
        Label:
            text: 
                """The application will skim through the
                whole of Twitter searching for tweets
                that include your query input and
                during what time period."""

            size_hint: (.50,.07)
            font_size: self.width/28
            color: '#39586B'
            font_name:"Poppins"
            pos_hint: {'center_x': .21, 'center_y': .62}
        
        Label:
            text: 
                """When searching for the presidential
                candidate as query, it is best to put
                their first and last name to avoid the
                results showing their names as well.
                (i.e. Leni Robredo, Bongbong Marcos
                etc.)"""

            size_hint: (.50,.07)
            font_size: self.width/28
            color: '#39586B'
            font_name:"Poppins"
            pos_hint: {'center_x': .21, 'center_y': .41}
        
        Label:
            text: 
                """The longer the time period, the
                longer the retrieving would be."""

            size_hint: (.50,.07)
            font_size: self.width/28
            color: '#39586B'
            font_name:"Poppins"
            pos_hint: {'center_x': .18, 'center_y': .24}
        

        #INPUT DATES TO RETRIEVE
        Button:
            text: "Enter time period"
            background_color :'#587180'
            size_hint: (.50,.07)
            font_size: self.width/20
            font_name:"Poppins"
            pos_hint: {'center_x': .70, 'center_y': .50}
            background_normal: ""

        #START
        Label:
            text: "start"
            size_hint: (.50,.07)
            font_size: self.width/20
            color: '#39586B'
            font_name:"Poppins"
            pos_hint: {'center_x': .57, 'center_y': .37}
        Button:
            size_hint: (.24,.07)
            pos_hint: {'center_x': .57, 'center_y': .42}
            background_color :'#A6C3D4'
            background_normal: ""
        #END        
        Label:
            text: "end"
            size_hint: (.50,.07)
            font_size: self.width/20
            font_name:"Poppins"
            color: '#39586B'
            pos_hint: {'center_x': .83, 'center_y': .37}
        Button:
            size_hint: (.24,.07)
            pos_hint: {'center_x': .83, 'center_y': .42}
            background_color :'#A6C3D4'
            background_normal: ""
            
        Label:
            text: "NOTE: Please write the date in the format YYYY-MM-DD (2022-04-20)" 
            font_size: 12
            color: '#39586B'
            font_name:"Poppins Italic"
            pos_hint: {'center_x': .70, 'center_y': .30}
        
        Button:
            text: "SEE RESULTS"
            background_color :'#587180'
            background_normal: ""
            font_name:"Quincy Bold"
            size_hint: (.15,.05)
            pos_hint: {'center_x': .67, 'center_y': .10}
            
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'Results'
                #root.manager.get_screen('Results').ids.final_output.text = root.inputs(name_input.text, start_input.text, end_input.text) 
                root.manager.get_screen('Results').ids.top10.text = name_input.text
                root.manager.get_screen('Results').ids.input_start.text = start_input.text
                root.manager.get_screen('Results').ids.input_end.text = end_input.text

        Button:
            text: "RETURN"
            background_color :'#587180'
            background_normal: ""
            font_name:"Quincy Bold"
            size_hint: (.15,.05)
            pos_hint: {'center_x': .85, 'center_y': .10}

            on_press:
                root.manager.transition.direction = 'right'
                root.manager.transition.duration = 1
                root.manager.current = 'Menu'
                
    
        MDTextField: 
            id: name_input
            icon_right_color: app.theme_cls.primary_color
            background_color :'#A6C3D4'
            background_normal: ""
            #hint_text: "Enter name: (ex.leni, bbm, isko)"
            pos_hint:{'center_x': 0.7, 'center_y': 0.60}
            size_hint_x:None
            width:375

        MDTextField: 
            id: start_input
            pos_hint: {'center_x': .57, 'center_y': .42}
            background_color :'#A6C3D4'
            background_normal: ""
            #hint_text: "ENTER DATE"
            size_hint_x:None
            width:150

        MDTextField:
            id: end_input
            icon_right_color: app.theme_cls.primary_color
            width:150
            size_hint_x:None
            pos_hint: {'center_x': .83, 'center_y': .42}
            background_color :'#A6C3D4'
            background_normal: ""
            #hint_text: "ENTER DATE"
             
<Results>:
    Widget:
        canvas:
            Color:
                rgba:213/255, 228/255, 237/255, 1
            Rectangle:
                size: self.size
                pos: self.pos
    FloatLayout:
        Image:
            source: 'demo2.png'
            pos_hint: {'center_x': .50, 'center_y': .55}
            size_hint: (1.1,1.1)
        Image:
            source: 'line.png'
            pos_hint: {'center_x': .60, 'center_y': .50}
            size_hint: (1.1,1.1)
        Label:
            id: final_output
            text: ""
            multiline: True
            color:'#39586B'
            background_color : '#FFFFFF'
            background_normal: ""
            font_name:"Poppins"
            size_hint: 1, None
            text_size: self.width/1.1, None
            pos_hint: {'center_x': .58, 'center_y': .45} 
        Label:
            id: final_output1
            text: ""
            multiline: True
            color:'#39586B'
            background_color : '#FFFFFF'
            background_normal: ""
            font_name:"Poppins"
            font_size: self.width/50
            size_hint: 0.5, 0.5
            text_size: self.width/1.5, self.height/1
            pos_hint: {'center_x': .75, 'center_y': .45} 
        
        Label:
            text: ""
            id: top10
            color: (1,1,1,0)
            font_name:"Poppins"
            font_size: self.width/10
            size_hint: (.20,.07)
            pos_hint: {'center_x': .50, 'center_y': .85} 


        Label:
            text: "(WORD - WORD COUNT - PERCENTAGE)"
            color:'#39586B'
            background_color: '#FFFFFF'
            background_normal: ""
            font_name:"Poppins Italic"
            size_hint: (.15,.05)
            pos_hint: {'center_x': .25, 'center_y': .65} 

        Label:
            text: ""
            id: input_start
            color: (1,1,1,0)
            background_color: '#FFFFFF'
            background_normal: ""
            font_name:"Poppins"
            size_hint: (.20,.05)
            pos_hint: {'center_x': .50, 'center_y': .75} 
        Label:
            text: ""
            id: input_end
            color: (1,1,1,0)
            background_color: '#FFFFFF'
            background_normal: ""
            font_name:"Poppins"
            size_hint: (.20,.05)
            pos_hint: {'center_x': .80, 'center_y': .75} 

        Label:
            text: "Since: " + input_start.text
            color:'#39586B'
            background_color: '#FFFFFF'
            background_normal: ""
            font_name:"Poppins Italic"
            size_hint: (.15,.05)
            pos_hint: {'center_x': .25, 'center_y': .80} 
        Label:
            text: "Until: " + input_end.text
            color:'#39586B'
            background_color: '#FFFFFF'
            background_normal: ""
            font_name:"Poppins Italic"
            size_hint: (.15,.05)
            pos_hint: {'center_x': .75, 'center_y': .80} 
        Button:
            text: "Top 10 Words Associated"
            color:'#39586B'
            background_color : '#FFFFFF'
            background_normal: ""
            font_name:"Poppins"
            font_size: self.width/15
            size_hint: (.30,.06)
            pos_hint: {'center_x': .25, 'center_y': .75} 
            on_press:
                final_output.text = root.inputs(top10.text, input_start.text, input_end.text) 
        Button:
            text: "with " + top10.text + " :"
            color:'#39586B'
            background_normal: ""
            background_color : '#FFFFFF'
            font_name:"Poppins"
            font_size: self.width/15
            size_hint: (.30,.06)
            pos_hint: {'center_x': .25, 'center_y': .70} 
            
        Button:
            text: "Top 3 Tweets Associated"
            color:'#39586B'
            background_color : '#FFFFFF'
            background_normal: ""
            font_name:"Poppins"
            font_size: self.width/15
            size_hint: (.30,.06)
            pos_hint: {'center_x': .75, 'center_y': .75} 
            on_press:
                final_output1.text = root.inputs1(top10.text, input_start.text, input_end.text) 
        Button:
            text: "with " + top10.text + " :"
            color:'#39586B'
            background_color : '#FFFFFF'
            background_normal: ""
            font_name:"Poppins"
            font_size: self.width/15
            size_hint: (.30,.06)
            pos_hint: {'center_x': .75, 'center_y': .70} 
        Button:
            text: "AGAIN"
            background_color: '#587180'
            background_normal: ""
            font_name:"Quincy Bold"
            size_hint: (.15,.05)
            pos_hint: {'center_x': .67, 'center_y': .10} 
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.transition.duration = 1
                root.manager.current = 'Input'

        Button:
            text: "QUIT"
            background_color :'#587180'
            font_name:"Quincy Bold"
            size_hint: (.15,.05)
            pos_hint: {'center_x': .85, 'center_y': .10}
            background_normal: ""

            on_press:
                quit()
        
'''
  
# Create a class for all screens in which you can include
# helpful methods specific to that screen
class Menu(Screen):
    pass
  
class Input_User(Screen):
    def __init__(self, **kwargs):
        super(Input_User, self).__init__(**kwargs)

    def rewrite(self, user_input):
        #output = "Top 10 Words Associated With '" + user_input + "' :"
        return user_input

    
    
    
class Results(Screen):
    def __init__(self, **kwargs):
        super(Results, self).__init__(**kwargs)

    def inputs(self, query, since, until):
        output = query_retrieval.tweets(query, since, until)
        return output

    def inputs1(self, query1, since, until):
        output = query.tweets(query1, since, until)
        return output
   

    
    
     
  

#fonts

LabelBase.register(name='Quincy Bold', 
                   fn_regular='QuincyCF-Bold.ttf')
LabelBase.register(name='Poppins Italic', 
                   fn_regular='Poppins-MediumItalic.ttf')
LabelBase.register(name='Poppins', 
                   fn_regular='Poppins-Medium.ttf')

# The ScreenManager controls moving between screens
screen_manager = ScreenManager()


# Add the screens to the manager and then supply a name
# that is used to switch screens

screen_manager.add_widget(Menu(name ="Menu"))
screen_manager.add_widget(Input_User(name ="Input"))
screen_manager.add_widget(Results(name ="Results"))


class TPA(MDApp):
    def build(self):
        screen = FloatLayout()
        Window.clearcolor = (1,0,0,1)
        self.theme_cls.primary_palette = "Blue"
        Window.size = (850, 600)
        self.screen = Builder.load_string(screen_helper)
        screen.add_widget(self.screen)
        
        return screen
       



# run the app
if __name__ == "__main__":
    app = TPA()
    app.run()
    