import pyxel
import random

SIZE_X = 255
SIZE_Y = 255

class Rect:
    def __init__(self, sx, sy, ex, ey):
        self.sx, self.sy = sx, sy
        self.ex, self.ey = ex, ey
    
    def get_sx(self):
        return self.sx

    def get_sy(self):
        return self.sy
    
    def get_ex(self):
        return self.ex
    
    def get_ey(self):
        return self.ey

    def get_w(self):
        return self.ex - self.sx
    
    def get_h(self):
        return self.ey - self.sy

class Room:
    def __init__(self, sx, sy, ex, ey):
        self.sx, self.sy = sx, sy
        self.ex, self.ey = ex, ey

    def get_sx(self):
        return self.sx

    def get_sy(self):
        return self.sy
    
    def get_ex(self):
        return self.ex
    
    def get_ey(self):
        return self.ey

    def get_w(self):
        return self.ex - self.sx
    
    def get_h(self):
        return self.ey - self.sy

class App:
    def __init__(self):
        pyxel.init(SIZE_X, SIZE_Y)

        self.rect = []

        pyxel.run(self.update, self.draw)

    def update(self):
        for rect in self.rect:
            print(rect.get_sx(), rect.get_sy(), rect.get_w(), rect.get_h())

    def draw(self):
        pyxel.cls(0)

        for rect in self.rect:
            pyxel.rect(rect.get_sx(), rect.get_sy(), rect.get_w(), rect.get_h(), 9)

    def generate(self):
        pass

if __name__ == "__main__":
    App()
