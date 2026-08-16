#!/usr/bin/python3
"""Base class."""

import json
import turtle


class Base:
    """Base class for managing id."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base instance."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file."""
        if list_objs is None:
            list_objs = []

        list_dicts = [obj.to_dictionary() for obj in list_objs]

        with open(cls.__name__ + ".json", "w") as file:
            file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Open a window and draw all rectangles and squares."""
        screen = turtle.Screen()
        screen.title("Rectangles and Squares")

        pen = turtle.Turtle()
        pen.speed(0)

        for rectangle in list_rectangles:
            pen.penup()
            pen.goto(rectangle.x, rectangle.y)
            pen.pendown()

            pen.forward(rectangle.width)
            pen.right(90)
            pen.forward(rectangle.height)
            pen.right(90)
            pen.forward(rectangle.width)
            pen.right(90)
            pen.forward(rectangle.height)
            pen.right(90)

        for square in list_squares:
            pen.penup()
            pen.goto(square.x, square.y)
            pen.pendown()

            pen.forward(square.size)
            pen.right(90)
            pen.forward(square.size)
            pen.right(90)
            pen.forward(square.size)
            pen.right(90)
            pen.forward(square.size)
            pen.right(90)

        turtle.done()
