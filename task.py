import math
V_lake = int(input("Введите объем озера в м^3"))
m = float(input("Введите массу груза (кг): "))
k = float(input("Введите коэффициент жесткости пружины (Н/м): "))
A = V_lake
t = float(input("Введите момент времени (с): "))
long_moon = 384467000

if (long_moon % V_lake != 0):
    lake_for_moon = long_moon // V_lake + 1
else:
    lake_for_moon = long_moon // V_lake


T = 2 * math.pi * (m / k)  0.5
v = A * (2 * math.pi / T) * math.cos(2 * math.pi * t / T)
a = -A * (2 * math.pi / T)  2 * math.sin(2 * math.pi * t / T)
print(long_moon// V_lake)
print(f"Скорость груза в момент времени {t} сек: {v} м/с")
print(f"Максимальное ускорение груза в момент времени {t} сек: {a} м/с^2")