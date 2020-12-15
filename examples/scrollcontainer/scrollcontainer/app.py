import toga
from toga.constants import COLUMN, ROW
from toga.style import Pack


class Item(toga.Box):
    def __init__(self, text):
        super().__init__(style=Pack(direction=COLUMN))

        row = toga.Box(style=Pack(direction=ROW, padding_right=10))

        if toga.platform.current_platform != 'android':  # Divider does not yet exist on Android
            hline = toga.Divider()
            hline.style.padding_top = 5
            hline.style.padding_bottom = 5
            for x in range(1,10):
                label = toga.Label(text+", "+str(x))
                row.add(label)
            self.add(row)
            self.add(hline)
        else:
            for x in range(10):
                label = toga.Label(text+", "+str(x))
                row.add(label)
            self.add(row)


class ScrollContainerApp(toga.App):
    def startup(self):
        box = toga.Box()
        box.style.direction = COLUMN
        box.style.padding = 10
        self.vscrolling = True
        self.hscrolling = False
        self.scroller = toga.ScrollContainer(horizontal=self.hscrolling, vertical=self.vscrolling)
        switch_box = toga.Box(style=Pack(direction=ROW))
        switch_box.add(toga.Switch('vertical scrolling', is_on=self.vscrolling, on_toggle=self.handle_vscrolling))
        switch_box.add(toga.Switch('horizontal scrolling', is_on=self.hscrolling, on_toggle=self.handle_hscrolling))
        box.add(switch_box)

        for x in range(100):
            label_text = 'Label {}'.format(x)
            box.add(Item(label_text))

        self.scroller.content = box

        self.main_window = toga.MainWindow(self.name, size=(400, 700))
        self.main_window.content = self.scroller
        self.main_window.show()

    def handle_hscrolling(self, widget):
        self.hscrolling = widget.is_on
        self.scroller.horizontal = self.hscrolling

    def handle_vscrolling(self, widget):
        self.vscrolling = widget.is_on
        self.scroller.vertical = self.vscrolling


def main():
    return ScrollContainerApp('ScrollContainer', 'org.beeware.widgets.scrollcontainer')


if __name__ == '__main__':
    app = main()
    app.main_loop()
