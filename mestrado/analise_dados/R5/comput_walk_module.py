import random
def compute_walk(count: int, x0=0, step=1, seed=0) -> int:
    """
    Random walk
    count: number of steps
    x0   : initial position (default 0)
    step : step size (default 1)
    seed : seed for the initialization of the
	random generator (default 0)
    """
    random.seed(seed)
    x = x0
    walk = []
    for _ in range(count):
        if random.uniform(-1, +1) > 0:
            x += 1
        else:
            x -= 1
        walk.append(x)
    return walk