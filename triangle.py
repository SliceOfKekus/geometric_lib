def area(a, h):
    '''
    Вычисляет площадь треугольника по заданной длине основания и заданной длине высоты, проведённой к этому основанию

        Параметры:
            a (float): длина основания
            h (float): длина высоты, проведённой к этому основанию
        
        Возвращаемое значение:
            a * h / 2 (float): площадь треугольника
    '''
    if (a <= 0 or h <= 0):
        raise ValueError("length must be greater than zero")

    return a * h / 2 

def perimeter(a, b, c): 
    '''
    Вычисляет периметр треугольника по заданных длинам всех его сторон

        Параметры:
            a (float): длина первой стороны
            b (float): длина второй стороны
            c (float): длина третьей стороны
        
        Возвращаемое значение:
            a + b + c (float): периметр треугольника
    '''
    if (a <= 0 or b <= 0 or c <= 0):
        raise ValueError("length must be greater than zero")

    return a + b + c