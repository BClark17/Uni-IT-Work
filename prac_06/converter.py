from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class MilesToKilometers(App):
    def build(self):
        Window.size = (400, 80)
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('converter.kv')
        return self.root

    def handle_convert(self, miles):
        try:
            result = int(miles) / 0.62137119
            self.root.ids.km_value.text = str(result)
        except ValueError:
            self.root.ids.km_value.text = "Enter VALID NUMBER and hit enter!"

    def handle_increment(self, value, miles):
        try:
            if not miles:
                miles = 0
            result = int(miles) + value
            self.root.ids.mile_value.text = str(result)
        except ValueError:
            self.root.ids.km_value.text = "VALID NUMBER plz!"


MilesToKilometers().run()
