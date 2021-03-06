# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

if __name__=="__main__":
    fig = plt.figure()
    ax = fig.add_subplot(111)
    u = np.linspace(0, 4, 1000)
    x, y = np.meshgrid(u, u)
    z = np.log(np.exp(x) + np.exp(y))
    ax.contourf(x, y, z, 20)
    plt.show()

