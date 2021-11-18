import pyxel
import random

SIZE_X = 255
SIZE_Y = 255

MAX_RECTS = 10

RECT_MIN_SIZE = 50

ROOM_MAX_SIZE = 45
ROOM_MIN_SIZE = 5


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
    def __init__(self, x, y, weight, height):
        self.x, self.y = x, y
        self.weight, self.height = weight, height

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_weight(self):
        return self.weight

    def get_height(self):
        return self.height


class App:
    def __init__(self):
        pyxel.init(SIZE_X, SIZE_Y)

        self.rects = [
            Rect(0, 0, SIZE_X, SIZE_Y)
        ]

        self.rooms = []

        self.generate_dungeon()

        pyxel.run(self.update, self.draw)

    def update(self):
        pass
        # for rect in self.rect:
        #    print(rect.get_sx(), rect.get_sy(), rect.get_w(), rect.get_h())

    def draw(self):
        pyxel.cls(0)

        for rect in self.rects:
            pyxel.rectb(rect.get_sx(), rect.get_sy(), rect.get_w(), rect.get_h(), 9)

        for room in self.rooms:
            pyxel.rectb(room.get_x(), room.get_y(), room.get_weight(), room.get_height(), 5)

    def generate_dungeon(self):
        for i in range(0, MAX_RECTS):
            if len(self.rects) <= 1:
                rect = random.randint(0, len(self.rects) - 1)
            else:
                rect = random.randint(len(self.rects) - 2, len(self.rects) - 1)

            _sx = self.rects[rect].get_sx()
            _sy = self.rects[rect].get_sy()
            _ex = self.rects[rect].get_ex()
            _ey = self.rects[rect].get_ey()

            is_split = False
            x_or_y = random.randint(0, 1)

            if x_or_y == 0:  # x
                a = _sx + 5
                b = _ex - _sx - 5

                if a < b:
                    print("X", a, b)
                    x = random.randint(a, b)
                    if x - _sx > RECT_MIN_SIZE and _ex - x > RECT_MIN_SIZE:
                        self.rects.append(Rect(_sx, _sy, x, _ey))
                        self.rects.append(Rect(x, _sy, _ex, _ey))
                        is_split = True

            elif x_or_y == 1:  # y
                a = _sy + 5
                b = _ey - _sy - 5

                if a < b:
                    print("Y", a, b)
                    y = random.randint(a, b)
                    if y - _sy > RECT_MIN_SIZE and _ey - y > RECT_MIN_SIZE:
                        self.rects.append(Rect(_sx, _sy, _ex, y))
                        self.rects.append(Rect(_sx, y, _ex, _ey))
                        is_split = True

            if is_split:
                self.rects.remove(self.rects[rect])

#        for rect in self.rects:
#            _width = random.randint(ROOM_MIN_SIZE, ROOM_MAX_SIZE)
#            _height = random.randint(ROOM_MIN_SIZE, ROOM_MAX_SIZE)
#
#            _x = random.randint(rect.get_sx() + 1, rect.get_ex() - _width - 1)
#            _y = random.randint(rect.get_sy() + 1, rect.get_ey() - _height - 1)
#
#            self.rooms.append(Room(_x, _y, _width, _height))


if __name__ == "__main__":
    App()
