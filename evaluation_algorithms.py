"""
The functions in this file convert a list of parameters into a single value in [0,1].
These are used to determine the creature's evaluation which can then be used to
determine the creature's next move, etc using other algorithms.
"""

import math
from typing import List


def sigmoid(params: List[int]) -> float:
    return 1 / (1 + math.exp(-sum(params)))
