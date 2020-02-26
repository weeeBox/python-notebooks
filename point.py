class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __iter__(self):
        yield self.x
        yield self.y

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return Point(self.x * other, self.y * other)

    def __getitem__(self, item):
        if item == 0:
            return self.x
        if item == 1:
            return self.y

        raise ValueError(f"Invalid index: {item}")

    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y

    def __str__(self):
        return f"({self.x},{self.y})"

    def __repr__(self):
        return str(self)


def point_list(points):
    if isinstance(points, str):
        values = points.split()
        if len(values) % 2 != 0:
            raise ValueError(f"Invalid value: {values}")

        i = 0
        res = []
        while i < len(values):
            x, y = int(values[i]), int(values[i + 1])
            res.append(Point(x, y))
            i += 2

        return res
    else:
        return list(Point(p[0], p[1]) for p in points)
