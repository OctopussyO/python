# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


"""
class Triangle:
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C
        self.AB = ((self.A[0]-self.B[0])**2 + (self.A[1]-self.B[1])**2)**0.5
        self.BC = ((self.B[0]-self.C[0])**2 + (self.B[1]-self.C[1])**2)**0.5
        self.AC = ((self.A[0]-self.C[0])**2 + (self.A[1]-self.C[1])**2)**0.5

    def perimetr(self):
        return self.AB + self.BC + self.AC

    def height(self, line):
        return 2 * self.area() / line

    def area(self):
        p = self.perimetr() / 2
        return (p * (p - self.AB) * (p - self.BC) * (p - self.AC))**0.5


dots = [list(map(int, input('Введите координаты точки через пробел: ').split(' '))) for _ in range(3)]

A, B, C = dots[0], dots[1], dots[2]

tr1 = Triangle(A, B, C)
print(tr1.AB, tr1.BC, tr1.AC)
print(tr1.perimetr())
print(tr1.height(tr1.BC))
print(tr1.area())

"""

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class EqTrapezoid:
    def __init__(self, A, B, C, D):
        self.A = A
        self.B = B
        self.C = C
        self.D = D

    def lines(self):
        self.AB = ((self.A[0]-self.B[0])**2 + (self.A[1]-self.B[1])**2)**0.5
        self.BC = ((self.B[0]-self.C[0])**2 + (self.B[1]-self.C[1])**2)**0.5
        self.CD = ((self.C[0]-self.D[0])**2 + (self.C[1]-self.D[1])**2)**0.5
        self.AD = ((self.A[0]-self.D[0])**2 + (self.A[1]-self.D[1])**2)**0.5
        return 'AB = {}, BC = {}, CD = {}, AD = {}'.format(self.AB, self.BC, self.CD, self.AD)

    def is_equal(self):
        if self.AB == self.CD or self.BC == self.AD:
            bool = True
            print('Трапеция равнобочная')
        else:
            bool = False
            print('Трапеция не является равнобочной')
        return bool

    def perimetrT(self):
        return self.AB + self.BC + self.CD + self.AD

    def squareT(self):
        if self.is_equal() == True:
            if self.AB == self.CD:
                square = ((self.BC + self.AD) / 4) * (4 * self.AB ** 2 - (self.BC + self.AD)**2)
            if self.BC == self.AD:
                square = ((self.AB + self.CD) / 4) * (4 * self.BC ** 2 - (self.AB + self.CD)**2)
            return square
        else:
            return ("Не могу вычислить площадь")



print("Требуется последовательно ввести координаты точек: ")
dots = [list(map(int, input('Координаты точки: ').split(' '))) for _ in range(4)]

A, B, C, D = dots[0], dots[1], dots[2], dots[3]

print(A, B, C, D)

trap1=EqTrapezoid(A, B, C, D)
print(trap1.lines())
trap1.is_equal()
print(trap1.perimetrT())
print(trap1.squareT())


