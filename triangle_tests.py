import unittest
import triangle

class TestTriangle(unittest.TestCase):

    def test_area_negative_side(self):
        '''
            Тест проверяет как функция triangle.area вычисляет площадь с отрицательнием основанием

            Параметры:
            
            Возвращаемое значение:

        '''
        with self.assertRaises(ValueError):
            triangle.area(-1, 1)


    def test_area_negative_height(self):
        '''
            Тест проверяет как функция triangle.area вычисляет площадь с отрицательной высотой

            Параметры:
            
            Возвращаемое значение:

        '''
        with self.assertRaises(ValueError):
            triangle.area(1, -1)


    def test_area_zero_side(self):
        '''
            Тест проверяет как функция triangle.area вычисляет площадь с отрицательным основанием

            Параметры:
            
            Возвращаемое значение:

        '''      
        with self.assertRaises(ValueError):
            triangle.area(0, 1)


    def test_area_zero_height(self):
        '''
            Тест проверяет как функция triangle.area вычисляет площадь с отрицательной высотой

            Параметры:
            
            Возвращаемое значение:

        '''
        with self.assertRaises(ValueError):
            triangle.area(1, 0)


    def test_area_positive_values(self):
        '''
            Тест проверяет как функция triangle.area вычисляет площадь с положительными высотой и основанием

            Параметры:
            
            Возвращаемое значение:

        '''
        res = triangle.area(1, 1)
        self.assertEqual(res, 0.5)


    def test_perimeter_negative_all_sides(self):
        '''
            Тест проверяет как функция triangle.perimeter вычисляет площадь с отрицательными сторонами

            Параметры:
            
            Возвращаемое значение:

        '''
        with self.assertRaises(ValueError):
            triangle.perimeter(-1, -1, -1)


    def test_perimeter_negative_one_side(self):
        '''
            Тест проверяет как функция triangle.perimeter вычисляет площадь с одной отрицательной стороной

            Параметры:
            
            Возвращаемое значение:

        '''
        with self.assertRaises(ValueError):
            triangle.perimeter(-1, 1, 1)
        with self.assertRaises(ValueError):
            triangle.perimeter(1, -1, 1)
        with self.assertRaises(ValueError):
            triangle.perimeter(1, 1, -1)


    def test_perimeter_negative_two_sides(self):
        '''
            Тест проверяет как функция triangle.perimeter вычисляет площадь с двумя отрицательными сторонами

            Параметры:
            
            Возвращаемое значение:

        '''
        with self.assertRaises(ValueError):
            triangle.perimeter(-1, -1, 1)
        with self.assertRaises(ValueError):
            triangle.perimeter(1, -1, -1)
        with self.assertRaises(ValueError):
            triangle.perimeter(-1, 1, -1)


    def test_perimeter_zero_all_sides(self):
        '''
            Тест проверяет как функция triangle.perimeter вычисляет площадь с нулевыми сторонами

            Параметры:
            
            Возвращаемое значение:

        '''
        with self.assertRaises(ValueError):
            triangle.perimeter(0, 0, 0)


    def test_perimeter_zero_one_side(self):
        '''
            Тест проверяет как функция triangle.perimeter вычисляет площадь с одной нулевой стороной

            Параметры:
            
            Возвращаемое значение:

        '''
        with self.assertRaises(ValueError):
            triangle.perimeter(0, 1, 1)
        with self.assertRaises(ValueError):
            triangle.perimeter(1, 0, 1)
        with self.assertRaises(ValueError):
            triangle.perimeter(1, 1, 0) 


    def test_perimeter_zero_two_sides(self):
        '''
            Тест проверяет как функция triangle.perimeter вычисляет площадь с двумя нулевыми сторонами

            Параметры:
            
            Возвращаемое значение:

        '''
        with self.assertRaises(ValueError):
            triangle.perimeter(0, 0, 1)
        with self.assertRaises(ValueError):
            triangle.perimeter(1, 0, 0)
        with self.assertRaises(ValueError):
            triangle.perimeter(0, 1, 0) 


    def test_perimeter_positive_sides(self):
        '''
            Тест проверяет как функция triangle.perimeter вычисляет площадь с положительными сторонами

            Параметры:
            
            Возвращаемое значение:

        '''
        res = triangle.perimeter(1, 1, 1)
        self.assertEqual(res, 3)
