from kivy.app import App #App - основной класс для создания приложений на киви
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

Window.size = (360, 640)

class Container(GridLayout):
    def calculate(self, *args):
        try:
            calc_entry = self.label.text
            ans = str(eval(calc_entry))
            self.label.text = ans
        except Exception:
            self.label.text = "Error!"
            pass

    def drop(self, *args):
        self.label.text = ""




class CalckApp(App):
    def build(self):
        return Container()


if __name__ == '__main__':
    CalckApp().run()

