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

if __name__ == "__main__":
    num = str(sys.argv[1])
    num = num.lstrip().rstrip()
    n_iter = int(sys.argv[2])
    l = len(num)
    n = num*MAGIC
    ll = len(n)
    partitions = _partition_(n)
    print(partitions)
    sys.exit(2)
