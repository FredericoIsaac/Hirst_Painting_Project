import colorgram
from turtle import Turtle, Screen
import random


def tuple_of_rgb(file):
    pallet_colours = []
    colors_jpg = colorgram.extract(file, 30)
    for color in colors_jpg:
        red = color.rgb.r
        green = color.rgb.g
        blue = color.rgb.b
        pallet_colours.append((red, green, blue))

    return pallet_colours


# colors = tuple_of_rgb("hirst_painting.jpg")

color_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53),
              (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48),
              (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155),
              (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120),
              (202, 185, 190), (40, 72, 82), (46, 73, 62), (47, 66, 82)]


tim = Turtle()
tim.speed("fastest")
screen = Screen()
screen.colormode(255)

tim.pu()

y = -250

for _ in range(10):
    tim.goto(-225, y)
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
    y += 50

tim.hideturtle()









screen.exitonclick()