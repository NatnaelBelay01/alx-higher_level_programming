#!/usr/bin/python3
"""A base object that lays the foundations
for the future objects
"""
import json
import os.path


class Base():
    """Class base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the values"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns a json string"""
        if list_dictionaries is None or []:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """returns a list from the jason string"""
        if json_string is None or "":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes json string to a file"""
        nam = "{}.json".format(cls.__name__)
        lst_d = []
        if not list_objs:
            pass
        else:
            for i in list_objs:
                lst_d.append(i.to_dictionary())
        with open(nam, 'w', encoding="utf-8") as f:
            f.write(cls.to_json_string(lst_d))

    @classmethod
    def create(cls, **dictionary):
        """creates an instance"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """loads from afile"""
        obj = []
        nam = "{}.json".format(str(cls.__name__))
        if os.path.exists(nam) is False:
            return []
        with open(nam, 'r', encoding="utf-8") as f:
            fil = f.read()
        jsn = cls.from_json_string(fil)
        for i in jsn:
            obj.append(cls.create(**i))
        return obj
