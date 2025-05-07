# 2D games where players look for keys
## OO: A way to model code. 2 Things
# - classes: common behaviour, define functionallity  (car blueprint)
# - instances: know state (attributes) and classs  (specific car)


# Player is a class
class Player:
    game = 'OASIS'  # class attribute, shared among instances
    num_players = 0

    # dunder init is a method
    # it's a special method, called on instance creation
    # self is provided by Python, it is the current instance
    def __init__(self, name):
        self.name = name  # instance attribute, specific to the instance
        self.num_players += 1


# p1 is an instance of Player
p1 = Player('Parzival')
print('p1:', p1)
# p1.name = 'Parzival'
print('name:', p1.name)
print('game:', p1.game)

p2 = Player('Art3mis')
# p2.name = 'Art3mis'
print('name (2):', p2.name)
print('game (2):', p2.game)

print('num players:', p1.num_players)

# attribute are stored in a dict called __dict__
print(p1.__dict__)
print(Player.__dict__)


def find_attr(obj, name):
    """Simulate attribute lookup.

    Like the built-in getattr.
    """
    # First look at instance dict
    if name in obj.__dict__:
        print(f'found {name} in instance')
        return obj.__dict__[name]

    cls = obj.__class__
    if name in cls.__dict__:
        print(f'found {name} in class')
        return cls.__dict__[name]

    raise AttributeError(name)


find_attr(p1, 'name')
find_attr(p1, 'game')
# find_attr(p1, 'color')  # AttributeError

print(isinstance(p1, Player))  # True
print(isinstance(p1, list))  # False
# using isinstance is a "code smell"
