import numpy as np
import matplotlib.pyplot as plt

def throw(theta, y0):
    rx, ry = 0.0, y0
    vx, vy = np.cos(theta), np.sin(theta)
    ax, ay = [], []
    g = 1.0
    h = 0.001
    while ry >= 0.0:
        rx += vx * h
        ry += vy * h
        vy -= g * h
        ax.append(rx)
        ay.append(ry)
    return ax, ay

def plot(angles, y0=0.0):
    for theta in angles:
        nx, ny = throw(theta / 180.0 * np.pi, y0)
        plt.plot(nx, ny, label=str(theta)+' deg')
    plt.legend()
    plt.show()

angles = [40,60]
plot(angles, 0.5)