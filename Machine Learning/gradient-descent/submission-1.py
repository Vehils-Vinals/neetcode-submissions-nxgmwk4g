class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        a = init
        mini = a

        for i in range(iterations):
            new_a = a - 2*a*learning_rate
            if mini**2 > new_a ** 2:
                mini = new_a
            
            a = new_a
        if mini == 0:
            return 0.0
        return round(mini, 5)

            