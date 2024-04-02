class Point:

    def __init__(self, coordinates=(0, 0)):
        self.coordinates = coordinates

    def get_x(self):
        return self.coordinates[0]

    def get_y(self):
        return self.coordinates[1]

    def distance(self, other):
        kat1 = self.coordinates[0] - other[0]
        kat2 = self.coordinates[1] - other[1]
        return (kat1 ** 2 + kat2 ** 2) ** 0.5

    def sum(self, other):
        x1 = self.coordinates[0] + other[0]
        y1 = self.coordinates[1] + other[1]
        return (x1, y1)

    def __str__(self):
        return f'1 координата - {self.coordinates[0]}, 2 координата - {self.coordinates[1]}'
