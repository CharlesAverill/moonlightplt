import numpy as np
from .Wave import Wave
from ..utils import dampen, plot_2D


class Sine(Wave):
    def __init__(self,
                 amplitude: float = 1,
                 period: float = (2 * np.pi),
                 offsets: tuple = (0, 0),
                 decay_constant: float = 0,
                 resolution: int = 500):
        super().__init__(np.sin, amplitude, period, offsets, resolution)
        self.decay_constant = decay_constant

    def generate_y(self, x):
        dampened = dampen(self.decay_constant,
                          np.sin((2 * np.pi * (x + self.offsets[0]) / self.period)))
        y = (self.amplitude * dampened) + self.offsets[1]
        return y

    def plot(self,
             periods: float = 1,
             line_width: float = 1):
        x = super().generate_x(periods=periods)
        y = self.generate_y(x)

        plot_2D(x, y, line_width)
