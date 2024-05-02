import math

def area(r):
    '''
    Вычисляет площадь окружности по её заданному радиусу

        Параметры:
            r (float): длина радиуса окружности
        
        Возвращаемое значение:
            math.pi * r * r (float): площадь окружности
    '''
    if (r < 0):
        raise ValueError("length must be greater than zero")

    return math.pi * r * r


def perimeter(r):
    '''
    Вычисляет периметр окружности по её заданному радиусу

        Параметры:
            r (float): длина радиуса окружности
        
        Возвращаемое значение:
            2 * math.pi * r (float): периметр окружности
    '''
    if (r < 0):
        raise ValueError("length must be greater than zero")

    return 2 * math.pi * r

