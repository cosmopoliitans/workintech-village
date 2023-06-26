import math


class Silo:
    # constructor
    def __init__(self, radius, height, material, name, inside):
        self._radius = radius
        self._height = height
        self._material = material
        self._inside = inside
        self._name = name

# getter & setter
    def get_radius(self):
        return self._radius

    def set_radius(self, radius):
        self._radius = radius

    def get_height(self):
        return self._height

    def set_height(self, height):
        self._height = height

    def get_material(self):
        return self._material

    def set_material(self, material):
        self._material = material

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_inside(self):
        return self._inside

    def set_inside(self, inside):
        self._inside = inside

    def get_area(self):
        return math.pi * (self._radius ** 2)

    def get_volume(self):
        return self.get_area() * self._height
    
    def get_perimeter(self):
        return math.pi * 2 * self._radius

    def __str__(self):
        return f'Silonun radiusu: {self._radius}, yüksekliği: {self._height},\n materyali: {self._material}, adı: {self._name}, içindeki malzeme: {self._inside}\n'


yavi = Silo(3.75, 2, "Çelik", "elif's", "Buğday")
print(yavi)
area = yavi.get_area()
print(f'Silo alanı: {area}')
volume = yavi.get_volume()
print(f'Silo hacmi: {volume}')
perimeter = yavi.get_perimeter()
print(f'Silonun yere değen kısmın çevresi: {perimeter}')
