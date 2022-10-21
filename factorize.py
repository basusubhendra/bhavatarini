#!/usr/bin/python3
import sys
MAGIC=18
partition_sizes = [ 10, 8 ]

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
    set1 = list(set1)
    set2 = list(set2)
    l = len(set1)
    d = dict([])
    for x in range(0, l):
        d[x] = 0
    ctr = 0
    ctr2 = 0
    nhits = 0
    while ctr < len(set2):
        ss = set2[ctr]
        ctr2 = 0
        while ctr2 < len(set1):
            if int(ss) < int(set1[ctr2]):
                ctr2 = ctr2 + 1
            elif int(ss) == int(set1[ctr2]) and d[int(ss)] == 0:
                d[int(ss)] == 1
                ctr = ctr + 1
                nhits = nhits + 1
            ctr2 = ctr2 + 1
        ctr = ctr + 1
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
        n_partition = ""
        run_length = 0
        while run_length < total_l:
            ss = str(ctr)
            n_partition = n_partition + ss
            run_length = run_length + len(ss)
            if run_length > total_l:
                n_partition = n_partition[:total_l]
                break
            elif run_length == total_l:
                break
            ctr = ctr + 1
        r_partition = n_partition[::-1]
        counter = 0
        for partition in partitions:
            set_partition = set(sorted(list(partition)))
            set1 = []
            set2 = []
            idx = 0
            while idx < len(partition):
                set1.append(n_partition[idx])
                set2.append(r_partition[idx])
                idx = idx + 1
            n_hits1 = coverage(set1, set_partition)
            n_hits2 = coverage(set2, set_partition)
            if n_hits1 == n_hits2:
                result_set.append(counter + 1)
            counter = counter + 1
        print(iter1 + 1, result_set)
        iter1 = iter1 + 1
