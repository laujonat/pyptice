'''
Compute the running median of a sequence of numbers. That is, given a stream
of numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two
middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should
print out:

2
1.5
2
3.5
2
2
2
'''


def median(rr):
    print("current median list", rr)
    length = len(rr)
    if length == 1:
        return rr[0]

    s = sorted(rr)
    m = int(length / 2)
    if length % 2 != 0:
        print(m / 2)
        return int(s[m])
    else:
        right = s[m]
        left = s[m - 1]
        return float((right + left) / 2)

# O(n)


def median_list(ll):
    result = []
    runner = []
    for v in enumerate(ll):
        runner.append(v[1])
        m = median(runner)
        result.append(m)

    return result


t1 = [2, 1, 5, 7, 2, 0, 5]
res = median_list(t1)
print(res)
