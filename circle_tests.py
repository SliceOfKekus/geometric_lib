import unittest
import circle

class TestCircle(unittest.TestCase):

    def test_area_negative_radius(self):
        '''
            Тест проверяет как функция circle.area отрабатывает с отрицательным радиусом

            Параметры:
            
            Возвращаемое значение:

        '''
        with self.assertRaises(ValueError):
            circle.area(-1)


    def test_area_zero_radius(self):
        '''
            Тест проверяет как функция circle.area вычисляет площадь круга с нулевым радиусом

            Параметры:
            
            Возвращаемое значение:

        '''
        res = circle.area(0)
        self.assertEqual(res, 0.0)


    def test_area_positive_radius(self):
        '''
            Тест проверяет как функция circle.area вычисляет площадь круга с положительным радиусом

            Параметры:
            
            Возвращаемое значение:

        '''
        res = circle.area(2)
        self.assertAlmostEqual(res, 12.56, places = 1)


    def test_perimeter_negative_radius(self):
        '''
            Тест проверяет как функция circle.perimeter отрабатывает с отрицательным радиусом

            Параметры:
            
            Возвращаемое значение:

        '''
        with self.assertRaises(ValueError):
            circle.perimeter(-1)


    def test_perimeter_zero_radius(self):
        '''
            Тест проверяет как функция circle.perimeter отрабатывает с нулевым радиусом

            Параметры:
            
            Возвращаемое значение:

        '''
        res = circle.perimeter(0)
        self.assertEqual(res, 0.0)


    def test_perimeter_positive_radius(self):
        '''
            Тест проверяет как функция circle.perimeter отрабатывает с положительным радиусом

            Параметры:
            
            Возвращаемое значение:

        '''
        res = circle.perimeter(2)
        self.assertAlmostEqual(res, 12.56, places = 1)
