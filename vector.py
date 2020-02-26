from unittest import TestCase


class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def cross(self, other):
        return Vector(x=self.y * other.z - self.z * other.y,
                      y=self.z * other.x - self.x * other.z,
                      z=self.x * other.y - self.y * other.x)

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z

    def __sub__(self, other):
        return Vector(x=self.x - other.x, y=self.y - other.y, z=self.z - other.z)

    def __add__(self, other):
        return Vector(x=self.x + other.x, y=self.y + other.y, z=self.z + other.z)

    def __str__(self):
        return f'({self.x},{self.y},{self.z})'

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return isinstance(other, Vector) and self.x == other.x and self.y == other.y and self.z == other.z

    @staticmethod
    def from_string(value, dim):
        if dim not in [2, 3]:
            raise ValueError(f"Invalid dim: {dim}")

        values = [float(s) for s in value.split()]
        if len(values) % dim != 0:
            raise ValueError(f"Invalid input: {value}")

        ans = []
        i = 0
        while i < len(values):
            if dim == 2:
                ans.append(Vector(values[i], values[i + 1]))
            elif dim == 3:
                ans.append(Vector(values[i], values[i + 1], values[i + 2]))
            i += dim

        return ans


Vector.Zero = Vector()


class TestSolution(TestCase):
    def test_sub(self):
        a = Vector(1, 2, 3)
        b = Vector(2, 4, 6)
        self.assertEqual(Vector(-1, -2, -3), a - b)

    def test_add(self):
        a = Vector(1, 2, 3)
        b = Vector(2, 4, 6)
        self.assertEqual(Vector(3, 6, 9), a + b)

    def test_cross1(self):
        a = Vector(5, 1, 4)
        b = Vector(-1, 0, 2)
        self.assertEqual(Vector(2, -14, 1), a.cross(b))

    def test_cross2(self):
        a = Vector(2, 0, 0)
        b = Vector(2, 2, 0)
        self.assertEqual(Vector(0, 0, 4), a.cross(b))

    def test_cross3(self):
        a = Vector(1, 2, 3)
        self.assertEqual(Vector(0, 0, 0), a.cross(a))
