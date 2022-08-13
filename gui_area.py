import turtle
import random
from math import sqrt, asin, acos, atan, pi, degrees
from tkinter import *
from area_formulas import *


class GUI:
    def __init__(self, window):
        """

        :param window: a tkinter window
        :return: A tkinter GUI and a turtle window, if nothing goes wrong.
        """

        self.window = window

        self.shape_frame = Frame(self.window)
        self.shape_radio_label = Label(self.shape_frame, text='Shape', font='Helvetica, 16')
        self.radio_default = StringVar()
        self.radio_default.set(None)

        self.radio_square = Radiobutton(self.shape_frame, text='Square', variable=self.radio_default, value='Square')
        self.radio_rectangle = Radiobutton(self.shape_frame, text='Rectangle', variable=self.radio_default, value='Rectangle')
        self.radio_triangle = Radiobutton(self.shape_frame, text='Triangle', variable=self.radio_default, value='Triangle')
        self.radio_circle = Radiobutton(self.shape_frame, text='Circle', variable=self.radio_default, value='Circle')

        self.shape_radio_label.pack(side='left', padx=10)
        self.radio_square.pack(side='left')
        self.radio_rectangle.pack(side='left')
        self.radio_triangle.pack(side='left')
        self.radio_circle.pack(side='left')
        self.shape_frame.pack(anchor='w', pady=10)

        self.shape_button_frame = Frame(self.window)
        self.shape_button = Button(self.shape_button_frame, text='Confirm shape?',
                                   command=lambda: clicked(self.radio_default.get()))
        self.shape_button_frame.pack(anchor='n')
        self.shape_button.pack(side='left', padx=10, pady=10)

        self.side_frame = Frame(self.window)
        self.side_label = Label(self.side_frame, text='Enter side length/radius length')
        self.side_entry_a = Entry(self.side_frame)
        self.side_entry_b = Entry(self.side_frame)

        self.side_label.pack(side='left')
        self.side_entry_a.pack(side='left')
        self.side_entry_b.pack(side='left')
        self.side_frame.pack(anchor='w')

        self.side_button_frame = Frame(self.window)
        self.side_button = Button(self.side_button_frame, text='Calculate',
                                  command=lambda: self.calculate())
        self.side_button.pack(side='left')
        self.side_button_frame.pack(anchor='n')

        self.area_frame = Frame(self.window)
        self.area_label = Label(self.area_frame, text='')
        self.area_label.pack(padx=10)
        self.area_frame.pack(anchor='n')

        def clicked(value: float | str) -> None:
            """

            :param value: value of the radio button selected before clicking this button
            :return: Does not return anything, but saves clicked radio button as selection
            """
            shape = self.shape_radio_label
            self.shape_radio_label = Label(self.shape_frame, text=value)
            self.shape_radio_label.pack()

    def calculate(self) -> None:
        """

        :return: None-type return, however will display value of area on GUI
        """

        try:
            shape = self.radio_default.get()
            if self.radio_default.get() == 'Rectangle' or self.radio_default.get() == 'Triangle':
                side1 = float(self.side_entry_a.get())
                side2 = float(self.side_entry_b.get())
                if type(side1) != float and type(side1) != int:
                    raise TypeError
                if type(side2) != float and type(side2) != int:
                    raise TypeError
                if side1 <= 0:
                    raise ValueError
                if side2 <= 0:
                    raise ValueError
            elif self.radio_default.get() == 'Square' or self.radio_default.get() == 'Circle':
                side1 = float(self.side_entry_a.get())
                if type(side1) != float and type(side1) != int:
                    raise TypeError
                if side1 <= 0:
                    raise ValueError
        except TypeError:
            self.area_label.config(text='Wrong type')
            self.area_label.pack(padx=10)
        except ValueError:
            self.area_label.config(text='Negative/zero value')
            self.area_label.pack(padx=10)
        else:
            if shape == 'Square':
                area = round(area_square(side1))
                self.area_label.config(text=area)
                self.area_label.pack(padx=10)
                t = turtle.Turtle()
                colors = ['red', 'blue', 'green', 'yellow', 'orange']
                t.color(random.choice(colors))
                t.pensize(10)
                t.shape('turtle')
                t.pendown()
                t.forward((side1 * 10))
                t.left(90)
                t.forward((side1 * 10))
                t.left(90)
                t.forward((side1 * 10))
                t.left(90)
                t.forward((side1 * 10))
                t.left(90)
                t.penup()
            elif shape == 'Rectangle':
                area = round(area_rectangle(side1, side2))
                self.area_label.config(text=area)
                self.area_label.pack(padx=10)
                t = turtle.Turtle()
                colors = ['red', 'blue', 'green', 'yellow', 'orange']
                t.color(random.choice(colors))
                t.pensize(10)
                t.shape('turtle')
                t.forward(side1 * 10)
                t.left(90)
                t.forward(side2 * 10)
                t.left(90)
                t.forward(side1 * 10)
                t.left(90)
                t.forward(side2 * 10)
                t.left(90)
            elif shape == 'Triangle':
                area = round(area_triangle(side1, side2))
                side_length = sqrt((((4 * area) / side1) ** 2 + side1 ** 2) / 4)
                base = side2
                height = side1
                alpha_rad = asin(side1 / side_length)
                angle_alpha = alpha_rad * (180 / pi)
                angle_beta = 180 - (2 * angle_alpha)
                self.area_label.config(text=area)
                self.area_label.pack(padx=10)
                t = turtle.Turtle()
                colors = ['red', 'blue', 'green', 'yellow', 'orange']
                t.color(random.choice(colors))
                t.pensize(10)
                t.shape('turtle')
                t.forward(side2 * 10)
                t.left(180 - angle_alpha)
                t.forward(side_length * 10)
                t.left(angle_beta)
                t.forward(side_length * 10)
                t.left(180 - angle_alpha)
            elif shape == 'Circle':
                area = round(area_circle(side1), 2)
                self.area_label.config(text=area)
                self.area_label.pack(padx=10)
                t = turtle.Turtle()
                colors = ['red', 'blue', 'green', 'yellow', 'orange']
                t.color(random.choice(colors))
                t.pensize(10)
                t.shape('turtle')
                t.circle(side1 * 10)

        self.side_entry_a.delete(0, END)
        self.side_entry_b.delete(0, END)
