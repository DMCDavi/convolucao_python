import numpy as np

def do_convolution():
    x_begin = -1
    h_begin = 0
    x = [2, 0, -3, 1]
    h = [2, -1, 1]
    y = {}
    x_length = len(x)
    h_length = len(h)
    x_end = x_length + x_begin - 1
    h_end = h_length + h_begin - 1
    count = 0
    calc_begin = x_begin + h_begin
    calc_length = x_length + h_length - 1
    calc_end = calc_begin + calc_length

    x_dict = {}
    h_dict = {}
    sum = 0

    for n in range(x_length):
        x_dict[x_begin + n] = x[n]

    for n in range(h_length):
        h_dict[h_begin + n] = h[n]
    
    for n in range(calc_begin, calc_end):
        y_n = 0
        for k in range(x_begin, x_end):
            if k in x_dict.keys() and n - k in h_dict.keys():
                y_n += x_dict[k] * h_dict[n - k]
        y[n] = y_n

    print(y)


    
    
do_convolution()