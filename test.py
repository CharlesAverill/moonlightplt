from moonlightplt.waves import Sine

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
