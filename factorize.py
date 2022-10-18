#!/usr/bin/python3
import sys
from gmpy2 import *
from mpmath import *
from pi import *
from e import *

def characterize(num):
    ctr = 0
    l = len(num)
    triplets = []
    while ctr % l != 0 or ctr == 0:
         triplet = []
         zero_counter = 0
         for x in range(0, 3):
             nn = num[(ctr + x) % l]
             if nn == '0':
                 zero_counter = zero_counter + 1
             triplet.append(nn)
         triplet = "".join(triplet)
         triplets.append(triplet)
         if ((ctr + 3) % l == 0):
             break
         ctr = ctr + (3 - (zero_counter % 3))
    return triplets
        
def getNextPosition(triplets, triplet_counter, pp, position):
    while True:
        position = pp.index(triplets[triplet_counter], position + 1)
        if (position + 1 + 3) % 3 == 0:
            break
    zero_index = (position + 1 + 3) / 3
    return zero_index, position

def _characterize_(zs):
    zero_count = zs.count("0")
    return zero_count, set(sorted(list(zs)))

def getBinaryMatch(triplet, _zip, _zie):
    mp.prec=256
    mp.dps=256
    zz1 = str(zetazero(_zip).imag)
    idx1 = zz1.index(".")
    zz1 = zz1[idx1-2:]
    zz1 = zz1.replace(".","")
    zz2 = str(zetazero(_zie).imag)
    idx2 = zz2.index(".")
    zz2 = zz2[idx2-2:]
    zz2 = zz2.replace(".","")
    ctr = 0
    max_number_of_matches, set_of_numbers = _characterize_(triplet)
    number_of_matches = 0
    counter = 0
    while number_of_matches < max_number_of_matches:
        zero_snippet1 = zz1[ctr:(ctr + 3)]
        zero_snippet2 = zz2[ctr:(ctr + 3)]
        m, set1 = _characterize_(zero_snippet1)
        m, set2 = _characterize_(zero_snippet2)
        if sorted(list(set1.union(set2)))== sorted(list(set_of_numbers)):
            number_of_matches = number_of_matches + 1
        ctr = ctr + 3
        counter = counter + 1
    return bin(counter)[2:]

def is_divisible_by(num, x):
    nz = gmpy2.mpz(num)
    xz = gmpy2.mpz(str(x))
    remainder = str(gmpy2.f_mod(num, xz))
    if remainder == "0":
        return True
    else:
        return False
    return False

def quotient(num, x):
    nz = gmpy2.mpz(num)
    xz = gmpy2.mpz(str(x))
    qz = gmpy2.f_div(nz, xz)
    return str(qz)

if __name__ == "__main__":
    num = str(sys.argv[1])
    #print(num)
    triplets = characterize(num)
    ll = len(triplets)
    #print(triplets)
    position_pi = -1
    position_e = -1
    zero_index_pi = 0
    zero_index_e = 0
    higher_factor = ""
    triplet_counter = 0
    while triplet_counter < ll:
        zero_index_pi, position_pi = getNextPosition(triplets, triplet_counter, pi, position_pi)
        zero_index_e, position_e  = getNextPosition(triplets, triplet_counter, e, position_e)
        input([zero_index_pi, zero_index_e])
        sys.exit(2)
        triplet_counter = triplet_counter + 1
        binary_snippet = getBinaryMatch(triplets[triplet_counter], zero_index_pi, zero_index_e)
        higher_factor = higher_factor + binary_snippet
    #Reversing the higher factor binary string
    decimal_version_of_higher_factor = int(higher_factor[::-1], 2)
    if is_divisible_by(num, decimal_version_of_higher_factor):
        print(num + "\t=\t" + decimal_version_of_higher_factor + "\tX\t" + quotient(num, decimal_version_of_higher_factor) + "\n")
    else:
        print(num + "\tis not a semi-prime (a product of exactly two primes.)")
