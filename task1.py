import pulp

# Ініціалізація моделі
model = pulp.LpProblem("Maximize Production", pulp.LpMaximize)

# Визначення змінних
lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')  # Кількість "Лимонаду"
fruit_juice = pulp.LpVariable('Fruit Juice', lowBound=0, cat='Integer')  # Кількість "Фруктового соку"

# Функція цілі (максимізація загальної кількості вироблених напоїв)
model += lemonade + fruit_juice, "Total Drinks"

# Обмеження ресурсів
model += 2 * lemonade + 1 * fruit_juice <= 100  # Обмеження по воді
model += 1 * lemonade <= 50  # Обмеження по цукру
model += 1 * lemonade <= 30  # Обмеження по лимонному соку
model += 2 * fruit_juice <= 40  # Обмеження по фруктовому пюре

# Розв'язання моделі
model.solve()

# Вивід результатів
print("Виробляти 'Лимонаду':", lemonade.varValue)
print("Виробляти 'Фруктового соку':", fruit_juice.varValue)
print("Максимальна загальна кількість напоїв:", pulp.value(model.objective))
