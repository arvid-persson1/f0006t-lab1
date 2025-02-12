from typing import Callable, Optional, Sequence

import matplotlib as mpl
import matplotlib.pyplot as plt
from dataset import *
from numpy import linspace


class Line:
    def __init__(self, label: str, x: float):
        self.label = label
        self.x = x


class Curve:
    def __init__(
        self,
        label: str,
        left: float,
        right: float,
        function: Callable[[float], float],
        resolution: int = 100,
    ):
        self.label = label
        self.xs = linspace(left, right, resolution)
        self.ys = tuple(function(x) for x in self.xs)


def plot(
    data: Sequence[tuple[int, int]],
    title: Optional[str] = None,
    lines: Sequence[Line] = (),
    curves: Sequence[Curve] = (),
):
    bins, counts = zip(*data.data)
    plt.bar(bins, counts, width=data.diff)

    plt.xlabel("Energi (MeV)")
    plt.ylabel("Pulser")
    if title is not None:
        plt.title(title)

    colors = plt.get_cmap("plasma")
    colors = tuple(colors(i) for i in linspace(0.1, 0.7, len(lines) + len(curves)))

    for i, line in enumerate(lines):
        plt.axvline(line.x, label=line.label, color=colors[i])

    for i, curve in enumerate(curves):
        plt.plot(curve.xs, curve.ys, label=curve.label, color=colors[i + len(lines)])

    if lines or curves:
        plt.legend()

    plt.show()


def main():
    mpl.rc("font", **{"size": 24})

    nonzero = lambda e: e[1] != 0
    cesium.trim(nonzero)
    salt.trim(nonzero)
    mushrooms.trim(nonzero)

    plot(cesium)
    plot(
        cesium,
        lines=(
            Line("Centroid K-toppen", 0.624),
            Line("Centroid L-toppen", 0.657),
            Line("Approximativ maximal elektronenergi", 0.589066653628),
        ),
        curves=(
            Curve(
                "y = 3943x² - 4645x + 1387",
                0.12906977923622162,
                0.6034915918957416,
                lambda x: 3943.1267 * x**2 - 4645.5289 * x + 1386.6449,
            ),
        ),
    )
    plot(salt)
    plot(salt, lines=(Line("Centroid K-40", 1.455),))
    plot(mushrooms)
    plot(mushrooms, lines=(Line("Centroid Cs-137", 0.659),))


if __name__ == "__main__":
    main()
