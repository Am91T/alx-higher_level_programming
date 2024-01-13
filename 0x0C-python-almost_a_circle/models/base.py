#!/usr/bin/python3
""" Base Module """
import json
import csv
import turtle
import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'



class Base:
    """
    Base class with a simple identifier generation machanism.

    Attibutes:
    - id (int): An identifier assigned to instances of the Base class.
    - __nb_objects (int): A class variable representing the totale number
    of Base class instances created.

    Methods:
    - __init__(self, id=None): Initializes a Base instance
    with a specified identifier if none is provided.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a Base instance.

        Parameters:
            id (int, optional): An optional identifier for the instance.
            If None, a unique identifier is assigned.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries """
        if not list_dictionaries or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file """
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            file.write(
                cls.to_json_string([obj.to_dictionary() for obj in list_objs])
            )

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list represented by json_string """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            raise ValueError("Unsupported class for create method")

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances loaded from a file """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_string = file.read()
                list_dicts = cls.from_json_string(json_string)
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Serializes and saves list_objs to a CSV file """
        filename = cls.__name__ + ".csv"
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """ Deserializes and loads instances from a CSV file """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                if cls.__name__ == "Rectangle":
                    return [cls.create(
                        id=int(row[0]), width=int(row[1]), height=int(row[2]),
                        x=int(row[3]), y=int(row[4])
                    ) for row in reader]
                elif cls.__name__ == "Square":
                    return [cls.create(
                        id=int(row[0]), size=int(row[1]), x=int(row[2]), y=int(row[3])
                    ) for row in reader]
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ Opens a window and draws all the Rectangles and Squares """
        window = turtle.Screen()
        window.bgcolor("white")

        pen = turtle.Turtle()
        pen.speed(2)

        for rect in list_rectangles:
            pen.penup()
            pen.goto(rect.x, rect.y)
            pen.pendown()
            pen.color("blue")
            pen.forward(rect.width)
            pen.left(90)
            pen.forward(rect.height)
            pen.left(90)
            pen.forward(rect.width)
            pen.left(90)
            pen.forward(rect.height)
            pen.left(90)

        for square in list_squares:
            pen.penup()
            pen.goto(square.x, square.y)
            pen.pendown()
            pen.color("red")
            pen.forward(square.size)
            pen.left(90)
            pen.forward(square.size)
            pen.left(90)
            pen.forward(square.size)
            pen.left(90)
            pen.forward(square.size)
            pen.left(90)

        turtle.done()
