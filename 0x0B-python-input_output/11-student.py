#!/usr/bin/python3
"""A class that defines a student obj"""


class Student():
    """defiens the class"""

    def __init__(self, first_name, last_name, age):
        """initializes the variables"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrives dictionary representation of Student"""
        my_dict = dict()
        if type(attrs) is list and all(type(x) is str for x in attrs):
            for x in attrs:
                if x in self.__dict__:
                    my_dict.update({x: self.__dict__[x]})
            return my_dict
        return self.__dict__

    def reload_from_json(self, json):
        """a method that replaes all the attributes"""
        my_dic = dict()
        for x in json:
            my_dic.update({x: json[x]})
        return my_dic
