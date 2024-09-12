import sys
import time

import numpy as np


def main(args):
    start = time.perf_counter()
    n_points = 100
    x_min = 0
    x_max = 10
    y_min = 0
    y_max = 10
    data_file = 'data.csv'
    x = np.linspace(x_min, x_max, n_points)
    y = np.linspace(y_min, y_max, n_points) + np.random.normal(loc=0, size=n_points)
    data = np.vstack((x, y)).T
    np.savetxt(data_file, data, delimiter=',', newline='\n', header='LIGHTSABERS, WOOKIES')
    end = time.perf_counter()
    print(f'Run time: {end - start:.10f} s.')


if __name__ == "__main__":
    main(sys.argv[1:])
