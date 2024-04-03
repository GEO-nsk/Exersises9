x = int(input())
y = int(input())
s = [x, y]
coordinates = tuple(s)
other = (2, 7)

class Point:
    '''
    class of point

    parameters:
    coordinates - tuple with current coordinates of point
    '''

    def __init__(self, coordinates=(0, 0)):
        self.coordinates = coordinates

    def get_x(self):
        '''
        function returns first point's coordinat
        '''
        return self.coordinates[0]

    def get_y(self):
        '''
        function returns second point's coordinat
        '''
        return self.coordinates[1]

    def distance(self, other):
        '''
        function returns distance between point and other point

        :param other: coordinates of other point
        '''
        kat1 = self.coordinates[0] - other[0]
        kat2 = self.coordinates[1] - other[1]
        return (kat1 ** 2 + kat2 ** 2) ** 0.5

    def sum(self, other):
        '''
        function returns summury of coordinates

        :param other: coordinates of other point
        '''
        x1 = self.coordinates[0] + other[0]
        y1 = self.coordinates[1] + other[1]
        return Point((x1, y1))

    def __str__(self):
        return f'1 координата - {self.coordinates[0]}, 2 координата - {self.coordinates[1]}'

point1 = Point(coordinates)

point2 = point1.sum(other)

print(point1)
print(point2)
