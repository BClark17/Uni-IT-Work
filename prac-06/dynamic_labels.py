from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.strings = ["Bob Brown", "Cat Cyan", "Oren Ochre", "Bailey Clark"]

    def build(self):
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.strings:
            temp_label = Label(text=name, id=name)
            self.root.ids.entries_box.add_widget(temp_label)

DynamicLabelsApp().run()
