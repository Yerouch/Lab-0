import math
distance = int(input("Введите расстояние до земли в метрах: "))
#v = a*t
#t = d/v
#v = a*d/v
#v^2 = a*S
velocity = math.sqrt(distance*9.8)
print("Скорость объекта при соприкосновении с землёй равна", velocity, "м/с.")
