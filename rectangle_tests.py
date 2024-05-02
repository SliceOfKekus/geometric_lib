import unittest
import rectangle

class TestRectangle(unittest.TestCase):

    def test_area_negative_all_sides(self):
        '''
            Тест проверяет как функция rectangle.area вычисляет площадь с отрицательными сторонами

            Параметры:
            
            Возвращаемое значение:

        '''
        with self.assertRaises(ValueError):
            rectangle.area(-1, -1)


    def test_area_negative_one_side(self):
        '''
            Тест проверяет как функция rectangle.area вычисляет площадь с одной отрицательной стороной

            Параметры:
            
            Возвращаемое значение:

        '''
        with self.assertRaises(ValueError):
            rectangle.area(-1, 1)

        with self.assertRaises(ValueError):
            rectangle.area(1, -1)


    def test_area_zero_all_sides(self):
        '''
            Тест проверяет как функция rectangle.area вычисляет площадь с нулевыми сторонами

            Параметры:
            
            Возвращаемое значение:

        '''
        with self.assertRaises(ValueError):
            rectangle.area(0, 0)

    def test_area_zero_one_side(self):
        '''
            Тест проверяет как функция rectangle.area вычисляет площадь с одной нулевой стороной

            Параметры:
            
            Возвращаемое значение:

        '''
        with self.assertRaises(ValueError):
            rectangle.area(0, 1)

        with self.assertRaises(ValueError):
            rectangle.area(1, 0)


    def test_area_positive_sides(self):
        '''
            Тест проверяет как функция rectangle.area вычисляет площадь с одной нулевой стороной

            Параметры:
            
            Возвращаемое значение:

        '''
        res = rectangle.area(1, 1)
        self.assertEqual(res, 1)


    def test_perimeter_negative_all_sides(self):
        '''
            Тест проверяет как функция rectangle.perimeter вычисляет периметр с отрицательными сторонами

            Параметры:
            
            Возвращаемое значение:

        '''
        with self.assertRaises(ValueError):
            rectangle.perimeter(-1, -1)

    def test_perimeter_negative_one_side(self):
        '''
            Тест проверяет как функция rectangle.perimeter вычисляет периметр с одной отрицательной стороной

            Параметры:
            
            Возвращаемое значение:

        '''
        with self.assertRaises(ValueError):
            rectangle.perimeter(-1, 1)

        with self.assertRaises(ValueError):
            rectangle.perimeter(1, -1)


    def test_perimeter_zero_all_sides(self):
        '''
            Тест проверяет как функция rectangle.perimeter вычисляет периметр с нулевыми сторонами

            Параметры:
            
            Возвращаемое значение:

        '''
        with self.assertRaises(ValueError):
            rectangle.perimeter(0, 0)


    def test_perimeter_zero_one_side(self):
        '''
            Тест проверяет как функция rectangle.perimeter вычисляет периметр с одной нулевой стороной

            Параметры:
            
            Возвращаемое значение:

        '''
        with self.assertRaises(ValueError):
            rectangle.perimeter(1, 0)

        with self.assertRaises(ValueError):
            rectangle.perimeter(0, 1)


    def test_perimeter_positive_sides(self):
        '''
            Тест проверяет как функция rectangle.perimeter вычисляет периметр с положительными сторонами

            Параметры:
            
            Возвращаемое значение:

        '''
        res = rectangle.perimeter(1, 2)
        self.assertEqual(res, 6)