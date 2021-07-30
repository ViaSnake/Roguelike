from mazelib import Maze
from mazelib.generate.DungeonRooms import DungeonRooms

m = Maze()
m.generator = DungeonRooms(24, 33, rooms=[[(3,3), (7,7)]])
m.generate()

print(m)