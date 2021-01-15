from collections import namedtuple

# Basic example
Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)
print(p[0] + p[1])  # 33

x, y = p
print(x, y)  # 11 22
print(p.x + p.y)  # 33
print(Point(x=11, y=22))  # Point(x=11, y=22)
