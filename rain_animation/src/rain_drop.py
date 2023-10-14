from dataclasses import dataclass
import numpy as np

from src._constants import SEED


@dataclass
class RainDrops:
    # TODO: add __post_init__ to check coherent size
    position: np.ndarray
    size: np.ndarray
    growth_rate: np.ndarray
    color: np.ndarray

    @property
    def n_drops(self):
        return len(self.growth_rate)


def build_rain_drop_collection(n_drops: int) -> RainDrops:
    np.random.seed(SEED)
    return RainDrops(
        position=np.random.uniform(0, 1, (n_drops, 2)),
        size=np.zeros(n_drops),
        growth_rate=np.random.uniform(50, 200, n_drops),
        color=np.zeros((n_drops, 4)),
    )
