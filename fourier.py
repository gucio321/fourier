#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
import math
from abc import ABC, abstractmethod

########################################
# Uzupełnij poniższy kod towimi danymi #
########################################


# granice przedziału
#p = math.pi
#a = -p
#b = p

class fourier(ABC):
    def __init__(self):
        self.a = -math.pi
        self.b = math.pi

        self.precision = 100 # skok na osi x
        self.k = 500 # liczba składowych rozwinięcia (keep as large as possible)
        self.t = 0.1 # czas odświeżania wykresu

    # Needs to be implemented by child class
    @abstractmethod
    def f(self, x):
        pass

    def a0(self, x):
        pass

    @abstractmethod
    def an(self, n, x):
        pass

    @abstractmethod
    def bn(self, n, x):
        pass

    def fourier(self, x, n):
        return np.cos(n*x)*self.an(n, x) + np.sin(n*x)*self.bn(n, x)

    @staticmethod
    def run(deploy : fourier):
        x = np.linspace(deploy.a, deploy.b, deploy.precision)
        y_org = deploy.f(x)
        y = [deploy.a0(xn) for xn in x]
        plt.plot(x, y_org)
        myplot, = plt.plot(x, y)
    
        try:
            for i in range(1,deploy.k+1):
                y += deploy.fourier(x,i)
                myplot.set_ydata(y)
                # add current i in legend
                plt.legend(["f(x)" ,f'g(x, n = {i:.0f})'])
                plt.draw()
                plt.pause(deploy.t)
        except KeyboardInterrupt:
            print("Exiting...")

# Ad 42.9 - Stankiewicz
class example(fourier):
    def __init__(self):
        super().__init__()
        self.a = 0
        self.b = 2*math.pi
    # funkcja bazowa
    def f(self, x):
        return (math.pi - x)/2

    def a0(self, x):
        return 0

    def an(self, n, x):
        return 0

    def bn(self, n, x):
        return 1/n

if __name__ == "__main__":
    fourier.run(example())
