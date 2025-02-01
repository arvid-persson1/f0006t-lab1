from itertools import dropwhile, takewhile
from sys import argv
from typing import Iterable, Optional

import matplotlib.pyplot as plt
import numpy as np
from numpy.typing import ArrayLike


def parse(path: str, trim: bool = True) -> Iterable[tuple[int, int]]:
    with open(path, "r") as f:
        lines = f.readlines()

    filtered = dropwhile(lambda l: not l[0].isdigit(), lines)
    pairs = (l.split() for l in filtered)
    entries = ((int(x), int(y)) for x, y in pairs)

    if trim:
        entries = tuple(entries)

        start = next((i for i, x in enumerate(reversed(entries)) if x != 0), None)
        if start is None:
            return []

        end = next(len(entries) - i for i, x in enumerate(reversed(entries)) if x != 0)

        entries = entries[start:end]

    return entries


def plot(
    bins: ArrayLike,
    counts: ArrayLike,
    coeff: float = 1,
    offset: float = 0,
    title: Optional[str] = None,
):
    f = np.vectorize(lambda x: x * coeff + offset)
    plt.bar(f(bins), counts, width=coeff)

    plt.xlabel("Energi (MeV)")
    plt.ylabel("Pulser")
    if title:
        plt.title(title)

    plt.show()


def main():
    # Windas doesn't export the proper values for the x-axis, but uses some
    # internal integer representation. These are the results of fitting
    # those values to the images using linear regression.
    sets = (
        ("../data/cesium.asc", 0.00174419784066, -8.6097261836e-7),
        ("../data/salt.asc", 0.00609620691562, -0.0623730759475),
        ("../data/mushrooms.asc", 0.00609756097561, -0.0621951219512),
    )

    for path, a, b in sets:
        data = parse(path)
        bins, counts = zip(*data)
        plot(bins, counts, a, b)


if __name__ == "__main__":
    main()
