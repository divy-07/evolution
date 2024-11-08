import math

from constants import NUM_DIRECTIONS


def sum_mod(params):
    return sum(params) % NUM_DIRECTIONS


def l2_norm(params):
    return math.isqrt(sum([x**2 for x in params])) % NUM_DIRECTIONS
