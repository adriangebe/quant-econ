import numpy as np

def compute_fixed_point(T, specs, v, error_tol=1e-3, max_iter=50, verbose=1):
    """
    Computes and returns T^k v, where T is an operator, v is an initial
    condition and k is the number of iterates. Provided that T is a
    contraction mapping or similar, T^k v will be an approximation to the
    fixed point.

    The convention for using this module is that T will be called as 
    
        new_v = T(specs, v).

    """
    iterate = 0 
    error = error_tol + 1
    while iterate <= max_iter and error > error_tol:
        new_v = T(specs, v)
        iterate += 1
        error = np.max(np.abs(new_v - v))
        if verbose:
            print "Computed iterate %d with error %f" % (iterate, error)
        v = new_v
    return v

