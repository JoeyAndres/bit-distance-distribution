#!/usr/bin/python

import os

from hamming import *
from utility import *

def generate_histogram(n):
    bits_count = 2 ** n
    sample_size = 10000

    histogram = {}

    for dist in range(n + 1):
        histogram[dist] = 0

    for bits_index in range(sample_size):
        dist = Hamming.dist(generate_bits(n), generate_bits(n))
        histogram[dist] += 1

    return histogram


def serialize_histogram(category, n, histogram):
    histogram_csv_str = ""
    for dist in range(n+1):
        histogram_csv_str += "{0},{1}\n".format(dist, histogram[dist]);

    with open("results/{0}-{1}.csv".format(category, n), 'w+') as f:
        f.write(histogram_csv_str)


for n in range(8, 64 + 1):
    print "Generating distance histogram for bit size: {0}".format(n)
    histogram = generate_histogram(n)
    serialize_histogram('hamming', n, histogram)
