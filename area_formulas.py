import math


# Calculating the area of a circle
def area_circle(radius: float) -> float:
    """

    :param radius: takes in float type
    :return: Returns the area of a circle with given input float. Returns a float.
    """
    area = math.pi * math.pow(radius, 2)
    return area


# Calculating the area of a rectangle
def area_rectangle(length: float, width: float) -> float:
    """

    :param length: takes in float type
    :param width: takes in float type
    :return: Returns the area of a rectangle with given input float. Returns a float
    """
    area = length * width
    return area


# Calculating the area of a square
def area_square(length: float) -> float:
    """

    :param length: Takes a float type
    :return: Returns the area of a square with given float input. Returns a float.
    """
    area = math.pow(length, 2)
    return area


# Calculating the area of a triangle
def area_triangle(base: float, height: float) -> float:
    """

    :param base: Input of type float. Is the base of the triangle.
    :param height: Input of type float. Is the height of the triangle.
    :return: Returns the area of a triangle with given float inputs. Returns a float.
    """
    area = base * height * 0.5
    return area
