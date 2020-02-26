from typing import List

from vector import Vector


def sign(a):
    return 1 if a > 0 else (-1 if a < 0 else 0)


class Polygon:
    def __init__(self, points: List[Vector]):
        if len(points) < 3:
            raise ValueError("Polygon should contain at least 3 points")

        self.points = points[:]

    def __len__(self):
        return len(self.points)

    def __iter__(self):
        return self.points

    def is_convex(self):
        prev = self.points[-1]
        cross = None
        for i, curr in enumerate(self.points):
            next = self.points[(i + 1) % len(self.points)]
            new_cross = (next - curr).cross(curr - prev).z
            if new_cross == 0:
                return False

            if cross is None:
                cross = new_cross
            elif sign(cross) != sign(new_cross):
                return False

            prev = curr

        return True

    @staticmethod
    def from_string(value: str, dim=3):
        return Polygon(Vector.from_string(value, dim))
