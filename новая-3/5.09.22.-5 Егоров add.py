class Vector:
    def __init__(self, *args):
        a = list(filter(lambda x: type(x) == int, args))
        self.values = sorted(a)

    def __str__(self):
        if len(self.values)>0:
            return f'Вектор{tuple(self.values)}'
        if len(self.values) == 0:
            return "Пустой вектор"

    def __add__(self, other):
        if not isinstance(other, (Vector, int)):
            raise AttributeError( f'Вектор нельзя сложить с {other}')
        if type(other)  == Vector:
            if len(self.values) == len(other.values):
                new_arr = list((self.values[x] + other.values[x]) for x in range(len(self.values)))
                return Vector(*new_arr)
            else:
                raise AttributeError ("Сложение векторов разной длины недопустимо")
        if type(other) == int:
            new_arr = []
            for x in self.values:
                new_arr.append(x+other)
            return Vector(*new_arr)

    def __mul__(self, other):
        if not isinstance(other, (Vector, int)):
            return print(f'Вектор нельзя умножать с {other}')
        if type(other)  == Vector:
            if len(self.values) == len(other.values):
                new_arr = list((self.values[x] * other.values[x]) for x in range(len(self.values)))
                return Vector(*new_arr)
            else:
                return print("Умножение векторов разной длины недопустимо")
        if type(other) == int:
            new_arr = []
            for x in self.values:
                new_arr.append(x*other)
            return Vector(*new_arr)





v1 = Vector(1,2,3)
# print(v1.arr)
# print(v1) # печатает "Вектор(1, 2, 3)"
print(v1+100)
v2 = Vector(3,4,5)
# print(v2) # печатает "Вектор(3, 4, 5)"
v3 = v1 + v2
print(v3) # печатает "Вектор(4, 6, 8)"
v4 = v3 + 5
print(v4) # печатает "Вектор(9, 11, 13)"
v5 = v1 * 2
# print(v5) # печатает "Вектор(2, 4, 6)"
# v1 + 'hi' # печатает "Вектор нельзя сложить с hi"




#
# d = Vector(1, 2.9, 3, "a", 6666)
# print(d.arr)
