import itertools
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
permutations = list(itertools.permutations(arr))
for permutation in permutations:
    if (permutation[1] < permutation[2] and permutation[4] < permutation[5] and permutation[7] < permutation[8]):
        frac1 = permutation[0] + permutation[1] / permutation[2]
        frac2 = permutation[3] + permutation[4] / permutation[5]
        frac3 = permutation[6] + permutation[7] / permutation[8]
        if (frac1 + frac2 == frac3):
            print(frac1, frac2, frac3)
            for i in permutation:
                print(i)
            print("----------------------------------------")
