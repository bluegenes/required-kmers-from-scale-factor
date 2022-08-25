import sys
import math
import argparse

'''
Given k, scale_factor in (0, 1) and bias_threshold, returns the minimum number of
kmers required to make sure the bias is larger than the provided threshold.
Example: scale_factor = 0.1, threshold = 0.99, k = 21 will return 44. This means
we need >= 44 kmers to make sure the resulting bias factor >= 0.99, and hence the bias is <= 0.01
'''
def required_num_kmers(scale_factor, k, bias_threshold=0.99):
    num_kmers = math.ceil(math.log(1.0 - bias_threshold) / math.log(1.0 - scale_factor))
    return int(num_kmers)


def main(args):

    nkmers = required_num_kmers(args.scaled_fraction, args.ksize, args.bias_threshold)
    print("min num k-mers: ", nkmers)
    min_seq_len = nkmers * (1/args.scaled_fraction)
    print(f'min seq length: {min_seq_len:.0f}')


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument('--scaled-fraction', help='scaled, as fraction', default=0.001, type=float)
    p.add_argument('-s', '--scaled-number', type=int, help='scaled, as number. If given, used instead of --scaled_fraction', default=None)
    p.add_argument('-b', '--bias-threshold', help='threshold for bias', default=0.99, type=float)
    p.add_argument('-k', '--ksize', help='k-mer length', default=21)

    args = p.parse_args()
    # transform scaled number if needed
    if args.scaled_number:
        args.scaled_fraction= 1/args.scaled_number
    sys.exit(main(args))
