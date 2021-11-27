from collections import namedtuple
Point = namedtuple("point", "x, y")
p = Point(x=1, y=2)

# print(p) = Point(x=1, y=2)
# print(p[0]) # = 1
# print(p.x) # = 1

# print(getattr(p, 'y')) = 2

# print(p._asdict()) # = OrderedDict(['x',1),('y',2)])

# print(p.count('x')) = 0

# print(p._fields) = ('x','y')


