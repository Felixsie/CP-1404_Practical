from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty




class SimpleApp(App):
    status_text = StringProperty()

# This function is to crate a new lines with each data in the lists.

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Felix Widyanto Oetomo Sie", "Bob Brown", "Cat Cyan", "Oren Ochre"]

#This function is to build the message box.

    def build(self):
        self.title = "List of Names"
        self.root = Builder.load_file('list_of_names.kv')
        self.create_label()
        return self.root

# This function is to create the label for the names.

    def create_label(self):
        for name in self.names:
            self.status_text = "{}".format(name)

SimpleApp().run()
