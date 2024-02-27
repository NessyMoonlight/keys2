# Case-study #2:
# Lake pillar
# Developers: Polina Selikhova, Maria Solovyova,
# Artemiy Borodin, Egor Lyamin.
#

import ru_local as ru
def main():
    '''
    Main function.
    :return: None
    '''

    import math

    #the user enters variables
    mass = float(input(ru.MASS_CARGO))
    koef = float(input(ru.STIFFNESS_COEFFICIENT))
    amplitude = float(input(ru.AMPLITUDE))
    time = float(input(ru.TIME))

    #calculating the necessary values according
    # to the formulas of physics
    period = 2 * math.pi * (mass / koef)** 0.5
    speed = abs((amplitude * (2 * math.pi / period) *
             math.cos(2 * math.pi * time / period)))
    max_boost = (-amplitude * (2 * math.pi / period)** 2
                 * math.sin(2 * math.pi * time / period))

    #output of the received values
    print(f"{ru.CARGO_SPEED} {time} {ru.SEC} {speed} {ru.MS}")
    print(f"{ru.CARGO_ACCELERATION} {time} {ru.SEC} {max_boost} {ru.MSS}")


if __name__ == '__main__':
    main()
