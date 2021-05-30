import matplotlib.pyplot as plt
import numpy as np

n = np.array([i for i in range(0, 8)])
k = 4


y = [np.log(n), n, np.power(n, 2), np.power(n, 3), np.power(n, k)]

for i in range(0, len(y)):
    plt.plot(y[i])

plt.legend(["Logarithmic", "Linear", "Quadratic", "Cubic", "Polynomial"])

plt.show()
