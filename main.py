import os
from random import random
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Line
import numpy as np
from kivy.utils import platform

# Import cv2 only on desktop (not available on Android)
if platform not in ('android', 'ios'):
    import cv2
else:
    cv2 = None

# Dual-stack Model Handling
if platform == 'android':
    try:
        from tflite_runtime.interpreter import Interpreter
    except ImportError:
        # Fallback or error handling if needed
        Interpreter = None
else:
    from tensorflow import keras
    import tensorflow as tf

from kivy.uix.boxlayout import BoxLayout

from random import random
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.stacklayout import StackLayout
from kivy.clock import Clock
from kivy.uix.slider import Slider
from kivy.core.window import Window
from kivy.app import App

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.widget import Widget
from kivy.config import Config
from kivy.graphics import Line

# Text-to-speech: use pyttsx3 on desktop, plyer.tts on Android
if platform == 'android':
    try:
        from plyer import tts
        pyttsx3 = None  # Not available on Android
    except ImportError:
        tts = None
        pyttsx3 = None
else:
    # Desktop platform
    try:
        import pyttsx3
        tts = None
    except ImportError:
        pyttsx3 = None
        tts = None


import math
import kivy_variables

from array import *
import numpy as  np

from PIL import Image
from kivy.graphics import Color, Ellipse, Line, Rectangle
from kivy.graphics.texture import Texture
import random

from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

thickness = 2.5

from kivy.uix.label import Label
from kivy.uix.popup import Popup

class Widgets(Widget):
    def btn(self):
        show_popup()

class MyPopup(Popup):
    pass

class P(FloatLayout):
    pass

class Painter(Widget):
    counter = 0
    if platform != 'android':
        engine = pyttsx3.init()

    def speak(self, text):
        if platform == 'android':
             if tts:
                 tts.speak(text)
        else:
             self.engine.say(text)
             self.engine.runAndWait()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.touch_data = []

    def on_touch_down(self, touch):
        color = (random.random(), 1, 1)
        with self.canvas:
            touch.ud['line'] = Line(points=(touch.x, touch.y), width=thickness)
            self.touch_data.append({'id': touch.id, 'points': [touch.x, touch.y]})

    def on_touch_move(self, touch):
        if 'line' in touch.ud:
            touch.ud['line'].points += [touch.x, touch.y]
            self.touch_data[-1]['points'] += [touch.x, touch.y]
            
            
    #def on_touch_up(self, touch):
    #    if 'line' in touch.ud:
     #       print("INFO: Touch released!")
     #       self.recognize_handwriting(touch)
            # Create an instance of MyClass
            #DrawScreen().recognize_handwriting()

    def recognize_handwriting(self):
        
        coordinates = [data['points'] for data in self.touch_data]
                                   
        for i in coordinates:   
            y1 = i[1]
            yn = i[-1]
            y_diff = y1 - yn
            x0 = i[0]
            xn = i[-2]
            x_diff = xn - x0
            
        img = self.export_as_image()
        img.save('temp.png')
        
        # Preprocessing
        img_cv = cv2.imread('temp.png', cv2.IMREAD_GRAYSCALE)
        img_resized = cv2.resize(img_cv, (128, 128))
        img_inverted = cv2.bitwise_not(img_resized)
        tst_image = np.array(img_inverted, dtype='float32')
        tst_image /= 255.0
        tst_image = np.expand_dims(tst_image, axis=2) # (128, 128, 1)
        tst_image = np.expand_dims(tst_image, axis=0) # (1, 128, 128, 1)

        predicted_class = 0
        
        if platform == 'android':
             # TFLite Inference
             try:
                 interpreter = Interpreter(model_path="modelchar.tflite")
                 interpreter.allocate_tensors()
                 input_details = interpreter.get_input_details()
                 output_details = interpreter.get_output_details()
                 
                 # Set input tensor
                 interpreter.set_tensor(input_details[0]['index'], tst_image)
                 interpreter.invoke()
                 
                 # Get output tensor
                 output_data = interpreter.get_tensor(output_details[0]['index'])
                 predicted_class = np.argmax(output_data)
                 
             except Exception as e:
                 print(f"Error in TFLite inference: {e}")
                 return # Exit or show error popup
        else:
             # Standard TensorFlow Inference
             model = tf.keras.models.load_model('modelchar.hdf5') 
             predicted_probs = model.predict(tst_image)
             predicted_class = np.argmax(predicted_probs)
           
        c = predicted_class
        cv2.waitKey()
            

        if c==0:
            print("Letter is ain")
            if (x_diff) < 0:
                print ('stroke_seq of "Aen" is not ok')
                show = P()
                popupWindow = Popup(title="Popup Window", content=Label(text="wrong stroke order"), size_hint=(None,None),size=(200,200),pos_hint={'top': 1, 'right': 1})
                popupWindow.open()
            else:                                           
                print('stroke_seq of "Aen" is ok')
                show = P()
                popupWindow = Popup(title="Popup Window", content=Label(text="right stroke order "), size_hint=(None,None),size=(200,200),pos_hint={'top': 1, 'right': 1})
                popupWindow.open() 
    

        elif c==1:
            print("Letter is alif'ا'")
            if (y_diff) < 0: 
               show = P()
               popupWindow = Popup(title="Popup Window", content=Label(text="wrong stroke order "), size_hint=(None,None),size=(200,200),pos_hint={'top': 1, 'right': 1})
               popupWindow.open()
            else:                                           
                    
               show = P()
               popupWindow = Popup(title="Popup Window", content=Label(text="right stroke order "), size_hint=(None,None),size=(200,200),pos_hint={'top': 1, 'right': 1})
               popupWindow.open() 

        elif c==2:
            print("Letter is bay'ب'")
            if (x_diff) > 0: 
                print ('stroke_seq of "Bey" is not ok')
                show = P()
                popupWindow = Popup(title="Popup Window", content=Label(text='wrong stroke order'), size_hint=(None,None),size=(200,200),pos_hint={'top': 1, 'right': 1})
                popupWindow.open()
            else:                                           
                print('stroke_seq of "jeem" is ok')
                show = P()
                popupWindow = Popup(title="Popup Window", content=Label(text='right stroke order' ), size_hint=(None,None),size=(200,200),pos_hint={'top': 1, 'right': 1})
                popupWindow.open()
            
        elif c==3:
            print("Letter is daal'د'")
            if (y_diff) < 0: 
                print ('stroke_seq of "Daal" is not ok')
                show = P()
                popupWindow = Popup(title="Popup Window", content=Label(text='wrong stroke order'), size_hint=(None,None),size=(200,200),pos_hint={'top': 1, 'right': 1})
                popupWindow.open()
            else:                                           
                print('stroke_seq of "Daal" is ok')
                show = P()
                popupWindow = Popup(title="Popup Window", content=Label(text='right stroke order'), size_hint=(None,None),size=(200,200),pos_hint={'top': 1, 'right': 1})
                popupWindow.open()
        elif c==4:
            print("Letter is gol haa'ہ'")
            show = P()
            popupWindow = Popup(title="Popup Window", content=Label(text="Letter is unknown "), size_hint=(None,None),size=(200,200),pos_hint={'top': 1, 'right': 1})
            popupWindow.open()
    
        elif c==5:
            print("Letter is haa'ح'")
            if (x_diff) < 0:     
                print ('stroke_seq of "jeem" is not ok')
                show = P()
                popupWindow = Popup(title="Popup Window", content=Label(text="wronge stroke order "), size_hint=(None,None),size=(200,200),pos_hint={'top': 1, 'right': 1})
                popupWindow.open()
            else:                                           
                print('stroke_seq of "jeem" is ok')
                show = P()
                popupWindow = Popup(title="Popup Window", content=Label(text="Right stroke order "), size_hint=(None,None),size=(200,200),pos_hint={'top': 1, 'right': 1})
                popupWindow.open()
                

        elif c==6:
            print("Letter is laam'ل'")
            if (y_diff) < 0:
                show = P()
                popupWindow = Popup(title="Popup Window", content=Label(text="wronge stroke order "), size_hint=(None,None),size=(200,200),pos_hint={'top': 1, 'right': 1})
                popupWindow.open()
            else:                                           
                   
                show = P()
                popupWindow = Popup(title="Popup Window", content=Label(text="Right stroke order "), size_hint=(None,None),size=(200,200),pos_hint={'top': 1, 'right': 1})
                popupWindow.open()

        elif c==7:
            print("Letter is meem'م'")
            if (y_diff) < 0: 
                show = P()
                popupWindow = Popup(title="Popup Window", content=Label(text="wronge stroke order "), size_hint=(None,None),size=(200,200),pos_hint={'top': 1, 'right': 1})
                popupWindow.open()
            else:                                           
                  
                show = P()
                popupWindow = Popup(title="Popup Window", content=Label(text="right stroke order "), size_hint=(None,None),size=(200,200),pos_hint={'top': 1, 'right': 1})
                popupWindow.open()

                    
        elif c==8:
            print("Letter is noon ghuna'ن'")
            if (x_diff) > 0: 
                 show = P()
                 popupWindow = Popup(title="Popup Window", content=Label(text="wronge stroke order "), size_hint=(None,None),size=(200,200),pos_hint={'top': 1, 'right': 1})
                 popupWindow.open()
            else:                                           
                    
                 show = P()
                 popupWindow = Popup(title="Popup Window", content=Label(text="Right stroke order "), size_hint=(None,None),size=(200,200),pos_hint={'top': 1, 'right': 1})
                 popupWindow.open()

        elif c==9:
            print("Letter is wao'و'")
            if (y_diff) < 0: 
                print ('stroke_seq of "Daal" is not ok')
                show = P()
                popupWindow = Popup(title="Popup Window", content=Label(text="wronge stroke order "), size_hint=(None,None),size=(200,200),pos_hint={'top': 1, 'right': 1})
                popupWindow.open()
            else:                                           
                print('stroke_seq of "Daal" is ok')
                show = P()
                popupWindow = Popup(title="Popup Window", content=Label(text="right stroke order "), size_hint=(None,None),size=(200,200),pos_hint={'top': 1, 'right': 1})
                popupWindow.open()

        else:
            print("Letter is unknown")
            show = P()
            popupWindow = Popup(title="Popup Window", content=Label(text="Letter is unknown "), size_hint=(None,None),size=(200,200),pos_hint={'top': 1, 'right': 1})
            popupWindow.open()
###################################### For time calculation ##########################
# end
       # print(f'Time: {time.time() - start}')

######################################################################################


        
        
        
 
    
class MainScreen(Screen):

    def exit_app(self):
        print("INFO: Exiting program.")
        # Builder.unload_file("app.kv")
        App.get_running_app().stop()
        # Window.close()

class DrawScreen(Screen):
    if platform != 'android':
        engine = pyttsx3.init()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
#############################################################################
        ## Calculate the size and position of the canvas
        #screen_width, screen_height = Window.size
        #canvas_width = screen_width * 0.8
        #canvas_height = screen_height * 0.6
        #canvas_x = (screen_width - canvas_width) / 2
        #canvas_y = (screen_height - canvas_height) / 2
        
       # # Create the canvas with a background color and border
       # with self.canvas:
        #    Color(0, 0, 0, 0) # set background color to gray
         #   self.rect = Rectangle(pos=self.pos, size=self.size)
         #   Color(1, 0, 0, 1) # set border color to red
         #   Line(rectangle=(canvas_x, canvas_y, canvas_width, canvas_height), width=2)
        
    #def on_size(self, *args):
      #  self.rect.size = self.size

    #def on_pos(self, *args):
    #    self.rect.pos = self.pos
##############################################################################
    def change_image(self):
        image_path = os.path.join(os.getcwd(), 'characters')
        images = [f for f in os.listdir(image_path) if f.endswith('.JPG') or f.endswith('.jpg')]
        image_file = random.choice(images)
        self.ids.image.source = os.path.join(image_path, image_file)    

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None
        

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        print('INFO: The key', keycode, 'has been pressed')
        if keycode[1] == 'c':
            self.on_release_clear()
        return True # return True to accept the key
        

    def on_release_clear(self):
        kivy_variables.touch_data = []
        self.ids.painter.canvas.clear()
        print("INFO: Data cleared.")

    def recognize_handwriting(self):
        self.ids.painter.recognize_handwriting()


class ScreenManagement(ScreenManager):
    pass

presentation = Builder.load_file("app.kv")

class MainApp(App):
    
    def build(self):
        
        return presentation
    
        
if __name__ == "__main__":
    MainApp().run()
