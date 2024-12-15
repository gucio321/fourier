#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
import math

########################################
# Uzupełnij poniższy kod towimi danymi #
########################################

# funkcja bazowa
def f(x):
    return (math.pi - x)/2

# rozwinięcie fourierowskie:
a0 = 0

def fourier(x, n):
    return np.sin(n*x)/n

# inne parametry. Można zostawić:
precision = 100 # skok na osi x
k = 500 # liczba składowych rozwinięcia (keep as large as possible)
t = 0.1 # czas odświeżania wykresu

def main():
    x = np.linspace(0, 2*math.pi, precision)
    y_org = (math.pi - x)/2
    y = [a0]*precision
    plt.plot(x, y_org)
    myplot, = plt.plot(x, y)
    
    for i in range(1,k+1):
        y += np.sin(i*x)/i
        myplot.set_ydata(y)
        # add current i in legend
        plt.legend(["f(x)" ,f'g(x, n = {i:.0f})'])
        plt.draw()
        plt.pause(t)

if __name__ == "__main__":
    main()
