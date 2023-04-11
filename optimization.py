import string
import numpy as np
import matplotlib.pyplot as plt
from load_data import load_data, add_average
from sort_plot import curve_fit, student_list
from scipy.optimize import fminbound



def mini(x: float, coef: list) -> float:
    """Returns the y value corresponding to x and polynomial represented by coefs
    """
    return np.polyval(coef, x)


def minus_mini(x: float, coef: list) -> float:
    """Returns the y value corresponding to x and polynomial represented by coefs
    """
    return mini(x, coef)


def minimum(generated_dictionary: dict, attribute: str) -> float:
    """takes a dictionary and a string as parameters and returns a tuple with the x and y coordinates of the local minimum from the values of the given attribute 

    preconditions: attributes must be keys from student_list, attributes must correspond to numerical values

    >>>minimum(add_average(student_age_dictionary('student-mat.csv')), 'Age'))
    (16.826580031595075, -10.81)
    """
    coef, interval = curve_fit(generated_dictionary, attribute, 2)
    find_min = fminbound(minus_mini, interval[0], interval[1], args=(coef,))
    return (find_min, round(minus_mini(find_min, coef), 2))



def maximum(student_data: dict, attribute: str) -> tuple:
    """Returns x and y coords of best attribute level in student_data, in terms of avg grade

    Preconditions: attributes must exist as a key in student_list(student_data).
                   attributes must correspond to numerical values
    """
    coefs, interval = curve_fit(student_data, attribute, 2)

    def maxi(x: float) -> float:
        """Returns the y value corresponding to x and polynomial represented by coefs
        """
        return numpy.polyval(coefs, x)

    def inverse_maxi(x: float) -> float:
        """Returns the y value corresponding to x and polynomial represented by coefs
        """
        return -(maxi(x))

    x_min = fminbound(inverse_maxi, interval[0], interval[1])
    y_min = maxi(x_min)

    maximum = (x_min, y_min)

    return maximum


if __name__ == "__main__":

    greatest_health_grade = maximum(
        "Health", add_average(load_data("student-mat.csv", "Age")))
    print(greatest_health_grade)
