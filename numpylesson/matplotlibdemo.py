# -*- encoding: utf-8 -*- #
__author__ = 'fzh'
import io
import numpy as np
from matplotlib import pyplot as plt

# x = np.linspace(0, 3, 20)
# y = np.linspace(0, 9, 20)
# plt.plot(x, y)
# plt.plot(x, y, 'o')
# plt.show()


# a = np.array([1, 2, 3, 4])
# b = a + 1
# print b
#
# x = np.array([[1, 1], [2, 2]])
# x.sum(axis=0)

data = np.loadtxt('populations.txt')
# print data
year, hares, lynxes, carrots = data.T
plt.axes([0.2, 0.1, 0.5, 0.8])
plt.plot(year, hares, year, lynxes, year, carrots)
plt.legend(('Hare', 'Lynx', 'Carrot'), loc=(1.05, 0.5))
plt.show()