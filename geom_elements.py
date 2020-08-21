import math  #importing math library

class Point:
    def __init__(self, coordinates):
        self.coordinates = coordinates
    def __add__(self, other):
        return Point([self.coordinates[0] + other.coordinates[0], self.coordinates[1] + other.coordinates[1], self.coordinates[2] + other.coordinates[2]])
    def __sub__(self, other):
        return Point([self.coordinates[0] - other.coordinates[0], self.coordinates[1] - other.coordinates[1], self.coordinates[2] - other.coordinates[2]])
    def __str__(self):
        return "({0},{1},{2})".format(self.coordinates[0], self.coordinates[1], self.coordinates[2])
    def modulus(self):
        return math.sqrt(self.coordinates[0]**2 + self.coordinates[1]**2 + self.coordinates[2]**2)

class Sphere:
    def __init__(self, center, radius):
        if isinstance(center, Point):
            self.center = center
        elif len(center) == 3:
            self.center = Point(center)
        else:
            raise Exception("The center coordinates must be tridimensional")
        self.radius = radius

    def get_radius(self):
        return self.radius

    def get_surface(self):
        self.area = 4 * math.pi * (self.radius*self.radius)            #compute serfice area
        return self.area

    def get_volume(self):
        self.volume = (4/3) * math.pi * (self.radius * self.radius * self.radius)  #compute volume
        return self.volume

    def is_inside(self, point):
        return (point-self.center).modulus() < self.radius