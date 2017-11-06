#!/usr/bin/python

import random


def generate_bits(n):
    """Return bit of size n."""
    bits = [None] * n
    rnd = random.SystemRandom()
    for bitPos in range(n):
        bits[bitPos] = rnd.randint(0, 1)

    return bits
