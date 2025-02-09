from typing import Optional, Sequence

import matplotlib as mpl
import matplotlib.pyplot as plt
from dataset import *
from numpy import linspace


def plot(
    data: Sequence[tuple[int, int]],
    title: Optional[str] = None,
    centroids: Sequence[float] = (),
):
    bins, counts = zip(*data.data)
    plt.bar(bins, counts, width=data.diff)

    plt.xlabel("Energi (MeV)")
    plt.ylabel("Pulser")
    if title is not None:
        plt.title(title)

    if centroids:
        colors = plt.get_cmap("plasma")
        colors = tuple(colors(i) for i in linspace(0.1, 0.7, len(centroids)))

        for i, (label, centroid, std) in enumerate(centroids):
            plt.axvline(
                centroid,
                label=f"{label} (cent. {centroid}, std. {std})",
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
        centroids=(
            ("K-toppen", 0.624, 0.00735),
            ("L-toppen", 0.657, 0.00535),
        ),
    )
    plot(salt)
    plot(salt, centroids=(("K-40", 1.455, 0.0294),))
    plot(mushrooms)
    plot(mushrooms, centroids=(("Cs-137", 0.659, 0.0239),))


if __name__ == "__main__":
    main()
