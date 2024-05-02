# Общее описание решения
Библиотека geometricLib предназначена для вычисления площади и периметра одной из поддерживаемых библиотекой фигур.
## Поддерживаемые фигуры
- Круг
- Прямоугольник
- Квадрат
- Треугольник

# Описание функций
## rectangle
1. ### ```def area(a, b):```
Вычисляет площадь прямоугольника.

Входные данные:
- a (float): длина первой стороны
- b (float): длина второй стороны
Возвращаемое значение:
- a * b (float): произведение двух сторон

Пример вызова функции

```
import rectangle
    
a = 10
b = 20
area = rectangle.area(a, b)
print(area) # out - 200
```

2. ### ```def perimeter(a, b):```
Вычисляет периметр прямоугольника.

Входные данные:
- a (float): длина первой стороны
- b (float): длина второй стороны
Возвращаемое значение:
- 2 * a + 2 * b (float): сумма удвоенного произведения каждой из сторон

Пример вызова функции

```
import rectangle
    
a = 10
b = 20
perimeter = rectangle.perimeter(a, b)
print(perimeter) # out - 60
```

## circle
1. ### ```def area(r):```
Вычисляет площадь окружности.

Входные данные:
- r (float): длина радиуса
Возвращаемое значение:
- π * r * r (float): площадь окружности

Пример вызова функции

```
import circle

radius = 1
area = circle.area(radius)
print(area) # out - 3.141592653589793
```

2. ### ```def perimeter(a, b):```
Вычисляет периметр окружности.

Входные данные:
- r (float): длина радиуса
Возвращаемое значение:
- 2 * π * r (float): периметр окружности

Пример вызова функции

```
import circle

radius = 1
perimeter = circle.perimeter(radius)
print(perimeter) # out - 6.283185307179586
```

## triangle
1. ### ```def area(a, h):```
Вычисляет площадь треугольника по заданной длине основания и заданной длине высоты, проведённой к этому основанию.

Входные данные:
- a (float): длина основания
- h (float): длина высоты, проведённой к этому основанию
Возвращаемое значение:
- a * h / 2 (float): площадь треугольника

Пример вызова функции

```
import triangle

a = 3
h = 3
area = triangle.area(a, h)
print(area) # out - 4.5
```

2. ### ```def perimeter(a, b, c):```
Вычисляет периметр треугольника

Входные данные:
- a (float): длина первой стороны
- b (float): длина второй стороны
- c (float): длина третьей стороны
Возвращаемое значение:
- a + b + c (float): периметр треугольника

Пример вызова функции

```
import triangle

a = 3
b = 4
c = 5
perimeter = triangle.perimeter(a, b, c)
print(perimeter) # out - 12
```

## square
1. ### ```def area(a):```
Вычисляет площадь квадрата

Входные данные:
- a (float): длина стороны
Возвращаемое значение:
- a * a (float): площадь квадрата

Пример вызова функции

```
import square

a = 3
area = square.area(a)
print(area) # out - 9
```

2. ### ```def perimeter(a):```
Вычисляет периметр квадрата

Входные данные:
- a (float): длина стороны квадрата
Возвращаемое значение:
- 4 * a (float): периметр квадрата

Пример вызова функции

```
import square

a = 3
perimeter = square.perimeter(a)
print(perimeter) # out - 12
```

# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

# История изменения проекта
- Добавлена поддержка круга и квадрата ([commit: 8ba9aeb](https://github.com/SliceOfKekus/geometric_lib/commit/8ba9aeb3cea847b63a91ac378a2a6db758682460))
- Добавлена документация ([commit: d078c8d](https://github.com/SliceOfKekus/geometric_lib/commit/d078c8d9ee6155f3cb0e577d28d337b791de28e2))
- Добавлена поддержка треугольника и прямоугольника ([commit: e0151ad](https://github.com/SliceOfKekus/geometric_lib/commit/c7c5562d6870c38a16baa5eb17983580db02d321))