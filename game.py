# 2D games where players look for keys
## OO: A way to model code. 2 Things
# - classes: common behaviour, define functionallity  (car blueprint)
# - instances: know state (attributes) and classs  (specific car)


# Player is a class
class Player:
    game = 'OASIS'  # class attribute, shared among instances
    num_players = 0

    # dunder init is a method
    # dunder methods are known as "special" (or "magic") methods
    # it's a special method, called on instance creation
    # self is provided by Python, it is the current instance
    def __init__(self, name):
        self.name = name  # instance attribute, specific to the instance
        Player.num_players += 1
        self.x, self.y = 0, 0
        # self.num_players += 1  # BUG:
        # self.num_players = self.num_players + 1
        self.keys = set()
        self.health = 100

    # method
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def found(self, key):
        if key not in {'copper', 'jade', 'crystal'}:
            raise ValueError(f'unknown key: {key!r}')

        self.keys.add(key)

    # String representation for users
    # def __str__(self):
    #     return f'{self.name} at {self.x}/{self.y} holding {self.keys}'

    # String representation for developers
    # Usually a way to create such an object
    # Write at least __repr__ in all your classes
    def __repr__(self):
        # self can be Player or any class that inherit from it
        cls = self.__class__.__name__
        return f'{cls}({self.name!r})'


class Admin(Player):
    def revive(self, other):
        other.health = 100


# Exercise:
# Add a "keys" attribute to player, should start with empty set
# Add a "found(key)" method that will add key to the keys attribute
#   It should err is key is not one of 'jade', 'crystal', 'copper'

# p1 is an instance of Player
p1 = Player('Parzival')
print('p1:', p1)
# p1.name = 'Parzival'
print('name:', p1.name)
print('game:', p1.game)

p1.move(10, 20)  # p1.move is a "bound method"
# Player.move(p1, 10, 20) # Works, but don't write code like that :)
print('loc:', p1.x, p1.y)
p1.found('jade')
p1.found('jade')
print('keys:', p1.keys)

p2 = Player('Art3mis')
# p2.name = 'Art3mis'
print('name (2):', p2.name)
print('game (2):', p2.game)

print('num players:', p1.num_players)

# attribute are stored in a dict called __dict__
print(p1.__dict__)
print(Player.__dict__)

a1 = Admin('James')
a1.revive(p1)


def print_names(items: list[Player]):
    for item in items:
        print(item.name)


print_names([p1, a1])


def find_attr(obj, name):
    """Simulate attribute lookup.

    Like the built-in getattr.
    """
    # First look at instance dict
    if name in obj.__dict__:
        print(f'found {name} in instance')
        return obj.__dict__[name]

    # next look at the dict
    cls = obj.__class__
    if name in cls.__dict__:
        print(f'found {name} in class')
        return cls.__dict__[name]

    # MRO: Method resolution order
    # Flattened hierarchy
    for parent in cls.__mro__:
        if name in parent.__dict__:
            print(f'found {name} in {parent.__name__}')
            return parent.__dict__[name]

    raise AttributeError(name)


find_attr(p1, 'name')  # instance
find_attr(p1, 'game')  # class
find_attr(a1, 'game')  # parent
# find_attr(p1, 'color')  # AttributeError

print(isinstance(p1, Player))  # True
print(isinstance(p1, list))  # False
# using isinstance is a "code smell"

# Aside: str vs repr
x, y = 1, '1'
print(f'x={x}, y={y}')  # by default, print uses __str__
print(f'x={x!r}, y={y!r}')
