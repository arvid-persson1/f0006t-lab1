from itertools import dropwhile
from typing import Callable, Sequence


class Dataset:
    def __init__(self, path: str, coeff: float = 1, offset: float = 0):
        data, time = parse(path)
        self.data = tuple((b * coeff + offset, c) for b, c in data)
        self.time = time
        self.diff = coeff

    def trim(self, pred: Callable[[tuple[float, int]], bool]):
        start = next((i for i, e in enumerate(self.data) if pred(e)), None)
        if start is None:
            self.data = []
            return

        l = len(self.data)
        end = next(l - i for i, e in enumerate(reversed(self.data)) if pred(e))

        self.data = self.data[start:end]


def parse(path: str) -> tuple[Sequence[tuple[float, int]], int]:
    with open(path, "r") as f:
        lines = iter(f.readlines())

    time = int(next(lines).split()[5])
    filtered = dropwhile(lambda l: not l[0].isdigit(), lines)
    pairs = (l.split() for l in filtered)
    entries = tuple((float(x), int(y)) for x, y in pairs)

    return entries, time


def trim_seq(
    seq: Sequence[tuple[float, int]],
    pred: Callable[[tuple[float, int]], bool],
) -> Sequence[tuple[float, int]]:
    start = next((i for i, x in enumerate(seq) if pred(x)), None)
    if start is None:
        return []

    end = next(len(seq) - i for i, x in enumerate(reversed(seq)) if pred(x))
    return seq[start:end]


# Windas doesn't export the proper values for the x-axis, but uses some
# internal integer representation. These are the results of fitting
# those values to the images using linear regression.
cesium = Dataset("../data/cesium.asc", 0.00174419784066, -8.6097261836e-7)
salt = Dataset("../data/salt.asc", 0.00609620691562, -0.0623730759475)
mushrooms = Dataset("../data/mushrooms.asc", 0.00609756097561, -0.0621951219512)
