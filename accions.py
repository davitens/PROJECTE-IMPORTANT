from pyboy import PyBoy, WindowEvent

class Accions:
    def __init__(self, pyboy):
        self.pyboy = pyboy

    def boto_A(self):
        self.pyboy.send_input(WindowEvent.PRESS_BUTTON_A)
        self.pyboy.tick()
        self.pyboy.send_input(WindowEvent.RELEASE_BUTTON_A)
        
    def boto_B(self):
        self.pyboy.send_input(WindowEvent.PRESS_BUTTON_B)
        self.pyboy.tick()
        self.pyboy.send_input(WindowEvent.RELEASE_BUTTON_B)
        
    def boto_UP(self):
        self.pyboy.send_input(WindowEvent.PRESS_ARROW_UP)
        self.pyboy.tick()
        self.pyboy.send_input(WindowEvent.RELEASE_ARROW_UP)
        
    def boto_DOWN(self):
        self.pyboy.send_input(WindowEvent.PRESS_ARROW_DOWN)
        self.pyboy.tick()
        self.pyboy.send_input(WindowEvent.RELEASE_ARROW_DOWN)
        
    def boto_RIGHT(self):
        self.pyboy.send_input(WindowEvent.PRESS_ARROW_RIGHT)
        self.pyboy.tick()
        self.pyboy.send_input(WindowEvent.RELEASE_ARROW_RIGHT)

    def boto_LEFT(self):
        self.pyboy.send_input(WindowEvent.PRESS_ARROW_LEFT)
        self.pyboy.tick()
        self.pyboy.send_input(WindowEvent.RELEASE_ARROW_LEFT)

    def boto_START(self):
        self.pyboy.send_input(WindowEvent.PRESS_BUTTON_START)
        self.pyboy.tick()
        self.pyboy.send_input(WindowEvent.RELEASE_BUTTON_START)

    def boto_SELECT(self):
        self.pyboy.send_input(WindowEvent.PRESS_BUTTON_SELECT)
        self.pyboy.tick()
        self.pyboy.send_input(WindowEvent.RELEASE_BUTTON_SELECT)