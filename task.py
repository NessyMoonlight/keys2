# Case-study #2
# Developers: Egor Lyamin, Maria Solovyova,
# Artemiy Borodin, Polina Selikhova
#

import ru_local as ru
def main():
    '''
    Main function.
    :return: None
    '''

    import math
    V_lake = int(input(ru.V_lake))
    m = float(input(ru.m))
    k = float(input(ru.k))
    A = V_lake
    t = float(input(ru.t))
    long_moon = 384467000

    if (long_moon % V_lake != 0):
        lake_for_moon = long_moon // V_lake + 1
    else:
        lake_for_moon = long_moon // V_lake


    T = 2 * math.pi * (m / k)** 0.5
    v = A * (2 * math.pi / T) * math.cos(2 * math.pi * t / T)
    a = -A * (2 * math.pi / T)** 2 * math.sin(2 * math.pi * t / T)
    print(long_moon// V_lake)
    print(f"{ru.load_speed} {t} {ru.sec} {v} {ru.mc}")
    print(f"{ru.load_acceleration} {t} {ru.sec} {a} {ru.mcc}")


if __name__ == '__main__':
    main()
