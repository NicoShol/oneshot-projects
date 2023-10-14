import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import src.animation as rainimation
import src.rain_drop as rain_drops
from src._constants import N_DROPS


def main() -> None:
    fig, ax = rainimation.build_canvas()
    rainDrops = rain_drops.build_rain_drop_collection(N_DROPS)
    scattering = rainimation.place_rain_drops_in_plot(ax, rainDrops)
    update = lambda frame_number: rainimation.update(
        frame_number, scattering, rainDrops
    )
    animation = FuncAnimation(fig, update, interval=10, save_count=100)
    plt.show()


if __name__ == "__main__":
    main()
