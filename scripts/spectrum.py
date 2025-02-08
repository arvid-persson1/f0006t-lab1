from bisect import bisect_left
from itertools import dropwhile, takewhile
from sys import argv
from typing import Optional, Sequence

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.typing import ColorType
from numpy.typing import ArrayLike

mpl.rc("font", **{"size": 24})


def parse(path: str, trim: bool = True) -> Sequence[tuple[int, int]]:
    with open(path, "r") as f:
        lines = f.readlines()

    filtered = dropwhile(lambda l: not l[0].isdigit(), lines)
    pairs = (l.split() for l in filtered)
    entries = tuple((int(x), int(y)) for x, y in pairs)

    if trim:
        start = next((i for i, x in enumerate(reversed(entries)) if x != 0), None)
        if start is None:
            return []

        end = next(len(entries) - i for i, x in enumerate(reversed(entries)) if x != 0)

        entries = entries[start:end]

    return entries


def plot(
    data: Sequence[tuple[int, int]],
    coeff: float = 1,
    offset: float = 0,
    title: Optional[str] = None,
    centroids: Sequence[float] = (),
):
    bins, counts = zip(*data)

    f = np.vectorize(lambda x: x * coeff + offset)
    plt.bar(f(bins), counts, width=coeff)

    plt.xlabel("Energi (MeV)")
    plt.ylabel("Pulser")
    if title is not None:
        plt.title(title)

    if centroids:
        colors = plt.get_cmap("plasma")
        colors = tuple(colors(i) for i in np.linspace(0.1, 0.7, len(centroids)))

        for i, (label, centroid, std) in enumerate(centroids):
            plt.axvline(
                centroid,
                label=f"{label} (cent. {centroid}, std. {std})",
                color=colors[i],
            )

        plt.legend()

    plt.show()


def main():
    cesium = parse("../data/cesium.asc")
    salt = parse("../data/salt.asc")
    mushrooms = parse("../data/mushrooms.asc")

    # Windas doesn't export the proper values for the x-axis, but uses some
    # internal integer representation. These are the results of fitting
    # those values to the images using linear regression.

    plots = (
        {
            "data": cesium,
            "coeff": 0.00174419784066,
            "offset": -8.6097261836e-7,
        },
        {
            "data": cesium,
            "coeff": 0.00174419784066,
            "offset": -8.6097261836e-7,
            "centroids": (
                ("K-toppen", 0.624, 0.00735),
                ("L-toppen", 0.657, 0.00535),
            ),
        },
        {
            "data": salt,
            "coeff": 0.00609620691562,
            "offset": -0.0623730759475,
        },
        {
            "data": salt,
            "coeff": 0.00609620691562,
            "offset": -0.0623730759475,
            "centroids": (("K-40", 1.455, 0.0294),),
        },
        {
            "data": mushrooms,
            "coeff": 0.00609756097561,
            "offset": -0.0621951219512,
        },
        {
            "data": mushrooms,
            "coeff": 0.00609756097561,
            "offset": -0.0621951219512,
            "centroids": (("Cs-137", 0.659, 0.0239),),
        },
    )

    for p in plots:
        plot(**p)


if __name__ == "__main__":
    main()
