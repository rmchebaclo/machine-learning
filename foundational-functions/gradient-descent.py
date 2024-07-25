# minimize x^2 using gradient descent
def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
    for i in range(iterations):
        derivative = 2 * init
        init = init - learning_rate * derivative
    return round(init, 5)