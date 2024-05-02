import unittest
import square

class TestSquare(unittest.TestCase):

    def test_area_negative_side(self):
        '''
            Тест проверяет как функция square.area вычисляет площадь с отрицательной стороной

            Параметры:
            
            Возвращаемое значение:

        '''
        with self.assertRaises(ValueError):
            square.area(-1)


    def test_area_zero_side(self):
        '''
            Тест проверяет как функция square.area вычисляет площадь с нулевой стороной

            Параметры:
            
            Возвращаемое значение:

        '''       
        res = square.area(0)
        self.assertEqual(res, 0)


    def test_area_positive_side(self):
        '''
            Тест проверяет как функция square.area вычисляет площадь с нулевой стороной

            Параметры:
            
            Возвращаемое значение:

        '''
        res = square.area(1)
        self.assertEqual(res, 1)


    def test_perimeter_negative_side(self):
        '''
            Тест проверяет как функция square.perimeter вычисляет площадь с отрицательной стороной

            Параметры:
            
            Возвращаемое значение:

        '''
        with self.assertRaises(ValueError):
            square.area(-1)

    def test_perimeter_zero_side(self):
        '''
            Тест проверяет как функция square.perimeter вычисляет площадь с нулевой стороной

            Параметры:
            
            Возвращаемое значение:

        '''
        res = square.perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_positive_side(self):
        '''
            Тест проверяет как функция square.perimeter вычисляет площадь с положительной стороной

            Параметры:
            
            Возвращаемое значение:

        '''
        res = square.perimeter(1)
        self.assertEqual(res, 4)
