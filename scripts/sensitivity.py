import matplotlib as mpl
import matplotlib.pyplot as plt


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __iter__(self):
        return iter((self.x, self.y))

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def coords(self) -> tuple[float, float]:
        return self.x, self.y


def main():
    mpl.rc("font", **{"size": 24})

    plt.xlim(0, 2.0)
    plt.ylim(0, 14)

    offset = Point(0.1 / 7, 0.1)

    p1a = Point(0.6, 5.6)
    p2a = Point(0.7, 5.0)
    plt.scatter(*p1a, color="r")
    plt.text(*(p1a + offset), p1a, fontsize=13)
    plt.scatter(*p2a, color="r")
    plt.text(*(p2a + offset), p2a, fontsize=13)
    plt.axline(p1a.coords(), p2a.coords(), color="r", label="y = -6x + 9,2")

    p1b = Point(1.4, 2.4)
    p2b = Point(1.55, 2.4)
    plt.scatter(*p1b, color="b")
    plt.text(*(p1b + offset), p1b, fontsize=13)
    plt.scatter(*p2b, color="b")
    plt.text(*(p2b + offset), p2b, fontsize=13)
    plt.axline(p1b.coords(), p2b.coords(), color="b", label="y = 2,4")

    plt.xlabel("Energi (MeV)")
    plt.ylabel("Känslighet (%)")

    plt.legend()
    # Aspect ratio is given in data coordinates, not image size.
    # Factor of 1/7 to adjust for x-y-axes ratio.
    plt.gca().set_aspect(4 / 5 / 7)
    plt.show()


if __name__ == "__main__":
    main()
