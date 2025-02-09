from dataset import *
from numpy import log

YEAR_S = 31557600


def calc_activity(
    data: Dataset, left: float, right: float, halflife: float, share_gamma: float
) -> float:
    assert halflife > 0
    assert 0 <= share_gamma <= 1
    assert left <= right

    data.trim(lambda e: left < e[0] < right)

    def frequency(pulses: int) -> float:
        assert pulses >= 0

        return pulses / data.time

    def sensitivity(energy: float) -> float:
        assert energy > 0

        # These values are estimates by approximating the graph given in the
        # instructions by linear functions on certain intervals.

        # Fit to area 0.6-0.7
        if 0.5 < energy < 0.8:
            return (-6 * energy + 9.2) / 100
        # Fit to area 1.4-1.55
        elif 1.3 < energy < 1.6:
            return 2.4 / 100
        # Other energy levels unused
        else:
            raise ValueError

    activity_gamma = sum(frequency(c) / sensitivity(b) for b, c in data.data)
    activity = activity_gamma / share_gamma
    return activity


def calc_apm(activity: float, mass: float) -> float:
    assert activity >= 0
    assert mass > 0

    return activity / mass


def calc_substance(activity: float, halflife: float) -> int:
    assert activity >= 0
    assert halflife > 0

    decay = log(2) / halflife
    substance = activity / decay
    return round(substance)


def run(
    data: Dataset,
    halflife: float,
    left: float,
    right: float,
    share_gamma: float,
    mass: float,
):
    activity = calc_activity(data, left, right, halflife, share_gamma)
    print(f"Activity per mass: {calc_apm(activity, mass):.3e}")
    print(f"Number of atoms:   {calc_substance(activity, halflife):.3e}")


def main():
    print("Mushrooms")
    run(mushrooms, 30.08 * YEAR_S, 0.58, 0.75, 0.851, 18.0e-3)

    print()

    print("Salt")
    run(salt, 1.248e9 * YEAR_S, 1.39, 1.53, 0.1067, 70.0e-3)


if __name__ == "__main__":
    main()
