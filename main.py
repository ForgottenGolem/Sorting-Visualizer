# imports
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
import random
import sort
from kivy.clock import Clock


class MyGrid(Widget):
    layStairs = ObjectProperty(None)
    btnRandomize = ObjectProperty(None)
    btnStart = ObjectProperty(None)
    btnBubble = ObjectProperty(None)
    btnSelection = ObjectProperty(None)
    btnInsertion = ObjectProperty(None)
    r_List = list(range(1, 11))
    currentSort = "bubble"

    # updates stairs visual without colored bar
    def update_stairs(self):
        self.layStairs.clear_widgets()
        for i in range(10):
            self.layStairs.add_widget(
                Button(size_hint=(0.1, self.r_List[i]/10)))

    def prsRandomize(self):
        self.r_List = random.sample(range(1, 11), 10)
        self.i_num = 0
        self.j_num = 0
        self.update_stairs()

    def prsStart(self):
        self.btnRandomize.disabled = True
        self.btnStart.disabled = True
        self.function_interval = Clock.schedule_interval(self.Start, 0.25)

    def prsBubble(self):
        self.currentSort = "bubble"
        self.btnBubble.disabled = True
        self.btnSelection.disabled = False
        self.btnInsertion.disabled = False

    def prsSelection(self):
        self.currentSort = "selection"
        self.btnSelection.disabled = True
        self.btnBubble.disabled = False
        self.btnInsertion.disabled = False

    def prsInsertion(self):
        self.currentSort = "insertion"
        self.btnInsertion.disabled = True
        self.btnBubble.disabled = False
        self.btnSelection.disabled = False

    def Start(self, *args):
        if (self.r_List == list(range(1, 11))):
            self.update_stairs()
            self.function_interval.cancel()
            self.btnRandomize.disabled = False
            self.btnStart.disabled = False
        else:
            if (self.currentSort == "bubble"):
                result = sort.bubble(self.r_List, self.i_num, self.j_num)
            elif (self.currentSort == "selection"):
                result = sort.selection(self.r_List, self.i_num)
            elif (self.currentSort == "insertion"):
                result = sort.insertion(self.r_List, self.i_num)

            self.r_List = result[0]
            self.i_num = result[1]
            self.j_num = result[2]
            self.layStairs.clear_widgets()

            # update stairs visual with colored bar
            for i in range(10):
                if (i == self.j_num):
                    self.layStairs.add_widget(
                        Button(size_hint=(0.1, self.r_List[i]/10), background_color=(0.902, 0.224, 0.275)))
                else:
                    self.layStairs.add_widget(
                        Button(size_hint=(0.1, self.r_List[i]/10)))


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()
