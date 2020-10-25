import numpy as np
from .Wave import Wave
from ..utils import dampen, plot_2D


class Cosine(Wave):
    def __init__(self,
                 amplitude: float = 1,
                 period: float = (2 * np.pi),
                 offsets: tuple = (0, 0),
                 decay_constant: float = 0,
                 resolution: int = 500):
        super().__init__(np.cos, amplitude, period, offsets, resolution)
        self.decay_constant = decay_constant

    def plot(self,
             periods: float = 1,
             line_width: float = 1):
        x = super().generate_x(periods=periods)
        dampened = dampen(self.decay_constant,
                          np.cos((2 * np.pi * (x + self.offsets[0]) / self.period)))
        y = (self.amplitude * dampened) + self.offsets[1]

        plot_2D(x, y, line_width)
