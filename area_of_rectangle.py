#! /usr/bin/env python3

"A script for calculating the area of a rectangle."

import sys

def string_to_float_or_int(string):
    """
    Returns the string as a number
    
    Parameters
    ----------
    number : int or float
        Number we want to convert to int or float based on presence of '.'

    Returns
    -------
    int or float
        The converted value in correct data type
    """
    if '.' in string:
        number = float(string)
    else:
        number = int(string)

    return number
        

def area_of_rectangle(height, width = None):
    """
    Returns the area of a rectangle.

    Parameters
    ----------
    height : int or float 
        The height of the rectangle.
    width : int or float
        The width of the rectangle. If `None` width is assumed to be equal to 
        the height.

    Returns
    -------
    int or float
        The area of the rectangle

    Examples
    --------
    >>> area_of_rectangle(7)
    49
    >>> area_of_rectangle (7, 2)
    14
    """

    #if width:
    #    width = height
#    import pdb; pdb.set_trace()
    area = height * width
    return area


if __name__ == '__main__':
    if (len(sys.argv) < 2) or (len(sys.argv) > 3):
        message = (
                  "{script_name}: Expecting one or two command-line arguments:\n"
                  "\tthe height of a square or the height and width of a "
                  "rectangle".format(script_name = sys.argv[0]))
        sys.exit(message)

    elif len(sys.argv) == 2:
        height = sys.argv[1]
        height = string_to_float_or_int(height)   
        width = height
        area = area_of_rectangle(height, width)
    else:
        height= sys.argv[1]
        height = string_to_float_or_int(height)
        width = sys.argv[2]
        width = string_to_float_or_int(width)
        area = area_of_rectangle(height, width)
 
    message = "The area of a {h} X {w} rectangle is {a}".format(
            h = height,
            w = width,
            a = area)
    print(message)
