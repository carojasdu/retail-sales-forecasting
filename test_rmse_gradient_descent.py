import numpy as np
import matplotlib.pyplot as plt

def fcn_prueba(x: float, y:float) -> float:
    return x**2 + y**2



if __name__ == '__main__':

    v = np.array([0.5, 0.5])
    alpha = 0.1
    h = 1e-5 

    condition = True
    i = 0
    vns = []
    while condition:
        dx = (fcn_prueba(v[0] + h, v[1]) - fcn_prueba(v[0], v[1])) / h
        dy = (fcn_prueba(v[0], v[1] + h) - fcn_prueba(v[0], v[1])) / h
        d = np.array([dx, dy])
        v = v - alpha * d
        print(v)
        print(d)
        if np.linalg.norm(d) < 1e-1 or i > 1000:
            condition = False
        i += 1
        vns.append(np.linalg.norm(v))

    plt.plot(vns)
    plt.show()
