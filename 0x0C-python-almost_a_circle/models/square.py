#!/usr/bin/python3
"""A square reprentation that inherits from,
rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """defines the square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializes the values"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a printable"""
        sid = self.id
        sx = self.x
        sy = self.y
        siz = self.width
        return "[Square] ({}) {}/{} - {}".format(sid, sx, sy, siz)

    @property
    def size(self):
        """gets the size"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates the values"""
        ups = ['id', 'size', 'x', 'y']
        if args:
            for i, j in enumerate(args):
                if i <= 3:
                    if ups[i] == 'size':
                        setattr(self, 'width', j)
                        setattr(self, 'height', j)
                    else:
                        setattr(self, ups[i], j)
        else:
            for i, j in kwargs.items():
                if i == 'size':
                    setattr(self, 'width', j)
                    setattr(self, 'height', j)
                else:
                    setattr(self, i, j)

    def to_dictionary(self):
        dic = {}
        atr = ['id', 'size', 'x', 'y']
        for i in atr:
            if i == 'size':
                dic[i] = getattr(self, 'width')
            else:
                dic[i] = getattr(self, i)
        return dic
