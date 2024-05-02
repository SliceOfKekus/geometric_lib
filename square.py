def area(a):
    '''
    Вычисляет площадь квадрата по заданной длине стороны

        Параметры:
            a (float): длина стороны квадрата
        
        Возвращаемое значение:
            a * a (float): площадь квадрата
    '''
    if (a < 0):
        raise ValueError("length must be greater than zero")

    return a * a


def perimeter(a):
    '''
    Вычисляет периметр квадрата по заданной длине стороны

        Параметры:
            a (float): длина стороны квадрата
        
        Возвращаемое значение:
            4 * a (float): периметр квадрата
    '''
    if (a < 0):
        raise ValueError("length must be greater than zero")

    return 4 * a
