# Moonlight
Matplotlib wave plotting and animation made easy

## Installation
- For pip release - `pip install moonlight`
- For source build - 
```bash
git clone https://github.com/CharlesAverill/moonlight.git moonlight
cd moonlight
python setup.py install
```

## Usage
```python
from moonlight import waves, utils

# Create a damped Sine wave with amplitude, period 2
sine = waves.Sine(amplitude=2, period=2,
                    decay_constant=.25)

# Set range of plot
utils.x_range(-3, 3)
utils.y_range(-4, 4)

# Move axes to center
utils.center_axes()

# Plot 2 periods of the wave (static)
sine.plot(2)
```

## Supported Waves
- `waves.Sine`
- `waves.Cosine`
- `waves.Tangent`
- `waves.Wave` - This is a parent class for the 
previous waves. Custom waves can be implemented by
inheriting this class.

### Wave parameters
- `amplitude: float = 1` - Initial wave amplitude
- `period: float = <varies by wave>` - Period of wave
- `offsets: Tuple(float [x], float [y]) = (0, 0)` - X- and Y- offsets of the wave
- `decay_constant: float = 0` - If nonzero, function will decay according to `e^(-<decay>x)wavefunc(x)`
- `resolution: int = 500` - Number of x-values that will be generated upon graphing.

## Wave operators
Waves can be operated on by each other and by scalar values.
```python
from moonlight.waves import Sine

s1 = Sine()
s2 = Sine(amplitude=2)

add_waves = s1 + s2 # sin(x) + 2sin(x) = 3sin(x)
add_scalar = s1 + 3 # sin(x) + 3

sub_waves = s1 - s2 # sin(x) - 2sin(x) = -sin(x)
sub_scalar = s1 - 3 # sin(x) - 3

mul_waves = s1 * s2 # sin(x) * 2sin(x) = 2sin(x)^2
mul_scalar = s1 * 3 # sin(x) * 3 = 3sin(x)

div_waves = s1 / s2 # sin(x) / 2sin(x) = 1/2
div_scalar = s1 / 3 # sin(x) / 3 = (1/3)sin(x)

call_waves = s1(s2) # sin(2sin(x))
call_scalar = s1(3) # sin(3) ≈ .14112
```