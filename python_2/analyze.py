import numpy as np
import matplotlib.pyplot as plt

def analyze(filename):
    data = np.loadtxt(filename, delimiter=',')

    inflam_mean = np.mean(data, axis=0)
    inflam_min = np.min(data, axis=0)
    inflam_max = np.max(data, axis=0)

    fig = plt.figure(figsize=(10, 3))

    axes1 = fig.add_subplot(1, 3, 1)
    axes2 = fig.add_subplot(1, 3, 2)
    axes3 = fig.add_subplot(1, 3, 3)

    axes1.set_ylabel('average')
    axes1.plot(inflam_mean)

    axes2.set_ylabel('minimum')
    axes2.plot(inflam_min)

    axes3.set_ylabel('maximum')
    axes3.plot(inflam_max)

    fig.tight_layout()

    plt.show()
