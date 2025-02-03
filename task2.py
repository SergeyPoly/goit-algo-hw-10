import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

def monte_carlo_integral(f, a, b, num_samples=10000):
    samples_x = np.random.uniform(a, b, num_samples)  # Генеруємо випадкові точки x
    samples_y = f(samples_x)  # Обчислюємо значення функції
    integral_estimate = (b - a) * np.mean(samples_y)  # Обчислення середнього значення

    return integral_estimate


# Обчислення методом Монте-Карло
monte_carlo_result = monte_carlo_integral(f, a, b)

# Аналітичний розрахунок за допомогою quad
quad_result, _ = quad(f, a, b)

# Виведення результатів
print(f"Обчислення методом Монте-Карло: {monte_carlo_result}")
print(f"Аналітичне значення (quad): {quad_result}")
print(f"Похибка: {abs(monte_carlo_result - quad_result)}")