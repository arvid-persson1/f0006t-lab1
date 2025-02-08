from typing import Optional, Sequence

# from bisect import bisect_left
# from itertools import dropwhile, takewhile
# from sys import argv
# from typing import Optional
#
import matplotlib as mpl
import matplotlib.pyplot as plt
from dataset import Dataset
from numpy import linspace


def plot(
    data: Sequence[tuple[int, int]],
    title: Optional[str] = None,
    centroids: Sequence[float] = (),
):
    plt.bar(data.bins, data.counts, width=data.coeff)

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

    # Windas doesn't export the proper values for the x-axis, but uses some
    # internal integer representation. These are the results of fitting
    # those values to the images using linear regression.
    cesium = Dataset("../data/cesium.asc", 0.00174419784066, -8.6097261836e-7)
    salt = Dataset("../data/salt.asc", 0.00609620691562, -0.0623730759475)
    mushrooms = Dataset("../data/mushrooms.asc", 0.00609756097561, -0.0621951219512)

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
