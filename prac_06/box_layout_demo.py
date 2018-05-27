from kivy.app import App
from kivy.lang import Builder



#Create a class for the demo box

class BoxLayoutDemo(App):

# This function is for the Kivi box builder

    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

# This function is for the displaying on the buttom of the Kivi box

    def handle_greet(self):
        print("test")
        self.root.ids.output_label.text = "Hello " + self.root.ids.input_name.text


#This function is for displaying the first message that will appear after starting the program.
    def handle_clear(self):
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = "Enter your name"


BoxLayoutDemo().run()