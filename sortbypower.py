'''
The power of an integer x is defined as the number of steps needed to transform x into 1 using the following steps:

if x is even then x = x / 2
if x is odd then x = 3 * x + 1
For example, the power of x = 3 is 7 because 3 needs 7 steps to become 1 (3 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1).

Given three integers lo, hi and k. The task is to sort all integers in the interval [lo, hi] by the power value in ascending order, if two or more integers have the same power value sort them by ascending order.

Return the k-th integer in the range [lo, hi] sorted by the power value.

Notice that for any integer x (lo <= x <= hi) it is guaranteed that x will transform into 1 using these steps and that the power of x is will fit in 32 bit signed integer.

'''

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        if lo - hi == 0:
            return lo
        hmap = {}
        for i in range(lo, hi + 1):
            temp = i
            steps = 0
            while (temp != 1):
                if temp % 2 == 1:
                    temp = temp * 3 + 1
                    steps += 1
                else:
                    temp = temp / 2
                    steps += 1
            hmap[i] = steps

        sorted_hmap = sorted(hmap.items(), key=operator.itemgetter(1))

        i1 = 0

        for i2 in sorted_hmap:
            if i1 == k - 1:
                return i2[0]
            i1 += 1

