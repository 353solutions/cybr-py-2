"""
Two utilities to create classes with ease.
- namedtuple
- dataclass
"""

from collections import namedtuple
from dataclasses import dataclass, field


class Location:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        cls = self.__class__.__name__
        return f'{cls}({self.latitude!r}, {self.longitude!r})'


loc = Location(3.2, 2.1)

Location2 = namedtuple('Location', 'x y')
# Location2 = namedtuple('Location', ['x', 'y'])
loc2 = Location2(3.2, 2.1)
print('[1]:', loc2[1], ',len:', len(loc2))
# loc2.x = 10  # error


@dataclass  # @ means a decorator
class Location3:
    x: int
    y: int
    # tags: list[str] = []  # error
    tags: list[str] = field(default_factory=list)


loc3 = Location3(3.2, 2.1)
loc3.x = 10  # OK
