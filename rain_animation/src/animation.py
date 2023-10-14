from typing import Tuple
import matplotlib.pyplot as plt
import numpy as np

import src.rain_drop as rain_drop


def build_canvas() -> Tuple[plt.figure, plt.Axes]:
    fig = plt.figure(figsize=(7, 7))
    ax = fig.add_axes([0, 0, 1, 1], frameon=False)
    ax.set_xlim(0, 1), ax.set_xticks([])
    ax.set_ylim(0, 1), ax.set_yticks([])
    return fig, ax


def place_rain_drops_in_plot(ax: plt.Axes, rainDrops: rain_drop.RainDrops) -> None:
    return ax.scatter(
        rainDrops.position[:, 0],
        rainDrops.position[:, 1],
        s=rainDrops.size,
        lw=0.5,
        edgecolors=rainDrops.color,
        facecolors="none",
    )


def _make_transparent(rainDrops) -> None:
    rainDrops.color[:, 3] -= 1.0 / rainDrops.n_drops
    rainDrops.color[:, 3] = np.clip(rainDrops.color[:, 3], 0, 1)


def _grow(rainDrops) -> None:
    rainDrops.size += rainDrops.growth_rate


def _reposition_old_drop(rainDrops, drop_index) -> None:
    rainDrops.position[drop_index] = np.random.uniform(0, 1, 2)
    rainDrops.size[drop_index] = 5
    rainDrops.color[drop_index] = (0, 0, 0, 1)
    rainDrops.growth_rate[drop_index] = np.random.uniform(50, 200)


def _update_scattering(scattering, rainDrops) -> None:
    scattering.set_edgecolors(rainDrops.color)
    scattering.set_sizes(rainDrops.size)
    scattering.set_offsets(rainDrops.position)


def update(frame_number, scattering, rainDrops):
    drop_index = frame_number % rainDrops.n_drops  # TODO: Explain this
    _make_transparent(rainDrops)
    _grow(rainDrops)
    _reposition_old_drop(rainDrops, drop_index)
    _update_scattering(scattering, rainDrops)
