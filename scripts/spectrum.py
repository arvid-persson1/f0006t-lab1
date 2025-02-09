from typing import Optional, Sequence

import matplotlib as mpl
import matplotlib.pyplot as plt
from dataset import *
from numpy import linspace


def plot(
    data: Sequence[tuple[int, int]],
    title: Optional[str] = None,
    lines: Sequence[tuple[str, float]] = (),
):
    bins, counts = zip(*data.data)
    plt.bar(bins, counts, width=data.diff)

    plt.xlabel("Energi (MeV)")
    plt.ylabel("Pulser")
    if title is not None:
        plt.title(title)

    if lines:
        colors = plt.get_cmap("plasma")
        colors = tuple(colors(i) for i in linspace(0.1, 0.7, len(lines)))

        for i, (label, x) in enumerate(lines):
            plt.axvline(
                x,
                label=label,
                color=colors[i],
            )

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
            ("Centroid K-toppen", 0.624),
            ("Centroid L-toppen", 0.657),
            ("Approximativ maximal sönderfallsenergi", 0.68),
        ),
    )
    plot(salt)
    plot(salt, lines=(("Centroid K-40", 1.455),))
    plot(mushrooms)
    plot(mushrooms, lines=(("Centroid Cs-137", 0.659),))


if __name__ == "__main__":
    main()
