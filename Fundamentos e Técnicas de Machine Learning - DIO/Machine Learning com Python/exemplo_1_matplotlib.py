# -*- coding: utf-8 -*-
"""EXEMPLO-1-MATPLOTLIB.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PYZ50PJMxErW7knE06PGOpxS5e87iAcs
"""

import matplotlib

from sklearn.datasets import make_regression
x, y = make_regression(n_samples = 200, n_features = 1, noise = 30)
import matplotlib.pyplot as plt

plt.scatter(x, y)
plt.show()