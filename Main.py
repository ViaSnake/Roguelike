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

        self.rect = [
            Rect(0, 0, SIZE_X, SIZE_Y)
        ]

        for i in range(0, 5):
            self.split(random.randint(0, len(self.rect) - 1))

        pyxel.run(self.update, self.draw)

    def update(self):
        pass
        #for rect in self.rect:
        #    print(rect.get_sx(), rect.get_sy(), rect.get_w(), rect.get_h())

    def draw(self):
        pyxel.cls(0)

        for rect in self.rect:
            pyxel.rectb(rect.get_sx(), rect.get_sy(), rect.get_w(), rect.get_h(), 9)

    def split(self, rect):
        print(rect)
        _sx = self.rect[rect].get_sx()
        _sy = self.rect[rect].get_sy()
        _ex = self.rect[rect].get_ex()
        _ey = self.rect[rect].get_ey()

        is_split = False
        x_or_y = random.randint(0, 1)

        if x_or_y == 0: # x
            a = _sx + 5
            b = _ex - _sx - 5

            if a < b:
                print("X", a, b)
                x = random.randint(a, b)
                if x - _sx > 50 and _ex - x > 50:
                    self.rect.append(Rect(_sx, _sy, x, _ey))
                    self.rect.append(Rect(x, _sy, _ex, _ey))
                    is_split = True

        elif x_or_y == 1: # y
            a = _sy + 5
            b = _ey - _sy - 5

            if a < b:
                print("Y", a, b)
                y = random.randint(a, b)
                if y - _sy > 50 and _ey - y > 50:
                    self.rect.append(Rect(_sx, _sy, _ex, y))
                    self.rect.append(Rect(_sx, y, _ex, _ey))
                    is_split = True
        
        if is_split:
            self.rect.remove(self.rect[rect])

if __name__ == "__main__":
    App()
