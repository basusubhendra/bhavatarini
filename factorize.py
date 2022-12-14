#!/usr/bin/python3
import sys
from mpmath import *
from pi import pi
from e import e
MAGIC=18
partition_sizes = [ 10, 8 ]

def get_zero_digit(iter1, digit):
    mp.prec=2048
    mp.dps=2048
    zero = str(zetazero(iter1).imag)
    idx = zero.index(".")
    zero = zero[idx - 2:]
    return zero[digit]

def _partition_(n):
    ctr = 0
    ll = len(n)
    partitions = []
    t = 0
    while ctr == 0 or ctr % ll != 0:
        partition = "" 
        for x in range(0, partition_sizes[t]):
            partition = partition + n[ctr]
            ctr = ctr + 1
        t = 1 - t
        partitions.append(partition)
    return partitions

def coverage(set1, set2):
    set_of_numbers = set(sorted(set2))
    nhits = 0
    for x in set_of_numbers:
        m = set2.count(x)
        idx = -1
        while m > 0 and x in set1[idx + 1:]:
            idx = set1.index(x, idx + 1)
            nhits = nhits + 1
            m = m - 1
    return nhits
    
if __name__ == "__main__":
    num = str(sys.argv[1])
    num = num.lstrip().rstrip()
    n_iter = int(sys.argv[2])
    l = len(num)
    n = num*MAGIC
    ll = len(n)
    partitions = _partition_(n)
    _ctr = -1
    total_l = 0
    for partition in partitions:
        total_l = total_l + len(partition)
    iter1 =0
    while iter1 < n_iter:
        result_set = []
        ctr = _ctr + 2
        n_partition = pi[ctr: ctr + total_l]
        r_partition = e[ctr:ctr + total_l][::-1]
        counter = 0
        prev_idx = 0
        for partition in partitions:
            set1 = "" 
            set2 = ""
            lp = len(partition)
            idx = 0
            while (idx+prev_idx) < prev_idx + lp:
                set1 = set1 + n_partition[idx + prev_idx]
                set2 = set2 + r_partition[idx + prev_idx]
                idx = idx + 1
            prev_idx = prev_idx + idx
            n_hits1 = coverage(set1, partition)
            n_hits2 = coverage(set2, partition)
            if n_hits1 == n_hits2 and n_hits1 > 0:
                result_set.append(get_zero_digit(iter1 + 1, counter))
            counter = counter + 1
        print(iter1 + 1, result_set)
        _ctr= _ctr + 2
        iter1 = iter1 + 1
