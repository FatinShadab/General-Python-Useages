from numba import jit
from numba import cuda
import numpy as np
from timeit import default_timer as timer


# To run on CPU
def func(a):
    for i in range(10000000):
        a[i]+= 1
# To run on GPU
@jit
def func2(x):
    return (x+1)
if __name__=="__main__":
    n = 10000000
    a = np.ones(n, dtype = np.float64)
    print(a)
    start = timer()
    func(a)
    print("without GPU:", timer()-start)
    start = timer()
    print(func2(a))
    cuda.profile_stop()
    print("with GPU:", timer()-start)