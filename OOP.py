
# задание 1

# class Point3D:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
# point1 = Point3D(1, 2, 3)
# point2 = Point3D(4, 5, 6)
#
# print("Значения координат для point1: x={}, y={}, z={}".format(point1.x, point1.y, point1.z))
# print("Значения координат для point2: x={}, y={}, z={}".format(point2.x, point2.y, point2.z))
#
# Point3D.x = 7
#
# print("Обновленные значения координат для point1: x={}, y={}, z={}".format(point1.x, point1.y, point1.z))
# print("Обновленные значения координат для point2: x={}, y={}, z={}".format(point2.x, point2.y, point2.z))
#
# point1.y = 8
#
# print("Измененные значения координат для point1: x={}, y={}, z={}".format(point1.x, point1.y, point1.z))
# print("Значения координат для point2: x={}, y={}, z={}".format(point2.x, point2.y, point2.z))




# задание 2

# class Kvadrat:
#     def __init__(self, storona):
#         self.storona = storona
#
#     def ploshad(self):
#         return self.storona ** 2
#
#     def perimetr(self):
#         return 4 * self.storona
# kvadrat1 = Kvadrat(5)
#
# ploshad = kvadrat1.ploshad()
# perimetr = kvadrat1.perimetr()
#
# print("Площадь квадрата:", ploshad)
# print("Периметр квадрата:", perimetr)




# задание 3

# class Treugolnik:
#     def __init__(self, katet_a, katet_b):
#         self.katet_a = katet_a
#         self.katet_b = katet_b
#
#     def ploshchad(self):
#         return 0.5 * self.katet_a * self.katet_b
#
#     def perimetr(self):
#         gipotenuza = (self.katet_a ** 2 + self.katet_b ** 2) ** 0.5
#         return self.katet_a + self.katet_b + gipotenuza
#
# treugolnik1 = Treugolnik(3, 5)
#
# ploshchad = treugolnik1.ploshchad()
# perimetr = treugolnik1.perimetr()
#
# print("Ploshchad' treugolnika:", ploshchad)
# print("Perimetr treugolnika:", perimetr)




# задание 4

# import math
#
# class Tochka:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def rasstoyanie_do(self, drugaya_tochka):
#         return math.sqrt((self.x - drugaya_tochka.x) ** 2 + (self.y - drugaya_tochka.y) ** 2)
#
# tochka_a = Tochka(2, 4)
# tochka_b = Tochka(6, 9)
# tochka_c = Tochka(6, 0)
#
# rasstoyanie_ab = tochka_a.rasstoyanie_do(tochka_b)
# rasstoyanie_bc = tochka_b.rasstoyanie_do(tochka_c)
# rasstoyanie_ca = tochka_c.rasstoyanie_do(tochka_a)
#
# perimetr = rasstoyanie_ab + rasstoyanie_bc + rasstoyanie_ca
#
# print("Rasstoyanie mezhdu tochek a i b:", rasstoyanie_ab)
# print("Rasstoyanie mezhdu tochek b i c:", rasstoyanie_bc)
# print("Rasstoyanie mezhdu tochek c i a:", rasstoyanie_ca)
# print("Perimetr treugolnika abc:", perimetr)




# задание 5

# class Chelovek:
#     def __init__(self, familia, imya, otchestvo, den_rogdeniya, mesyac_rogdeniya, god_rogdeniya, pol):
#         self.familia = familia
#         self.imya = imya
#         self.otchestvo = otchestvo
#         self.den_rogdeniya = den_rogdeniya
#         self.mesyac_rogdeniya = mesyac_rogdeniya
#         self.god_rogdeniya = god_rogdeniya
#         self.pol = pol
#
#     def izmenit_informaciyu(self, familia, imya, otchestvo, den_rogdeniya, mesyac_rogdeniya, god_rogdeniya, pol):
#         self.familia = familia
#         self.imya = imya
#         self.otchestvo = otchestvo
#         self.den_rogdeniya = den_rogdeniya
#         self.mesyac_rogdeniya = mesyac_rogdeniya
#         self.god_rogdeniya = god_rogdeniya
#         self.pol = pol
#
#     def poluchit_informaciyu(self):
#         return f"{self.familia} {self.imya} {self.otchestvo}, {self.den_rogdeniya}.{self.mesyac_rogdeniya}.{self.god_rogdeniya}, Пол: {self.pol}"
#
#     def __del__(self):
#         print(f"Объект {self.familia} {self.imya} {self.otchestvo} удален.")
#
# chelovek = Chelovek("Ivanov", "Ivan", "Ivanovich", 15, 10, 1980, "Male")
#
# print("Информация о человеке:")
# print(chelovek.poluchit_informaciyu())
#
# chelovek.izmenit_informaciyu("Petrov", "Petr", "Petrovich", 20, 5, 1990, "Male")
# print("Информация о человеке после изменений:")
# print(chelovek.poluchit_informaciyu())
#
# del chelovek


