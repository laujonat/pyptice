
'''
Find longest palindromic substring

Manacher's Algorithm
'''


def longest_palondromic_substring(s):
    mid = len(s) // 2
    # initialize s[i][i] = False
    T = [[False for i in range(0, len(s))] for i in range(0, len(s))]

    for i in range(0, len(T)):
        T[i][i] = False

    mx = 1
    for l in range(2, len(s) + 1):
        length = 0
        for i in range(0, len(s) - l + 1):
            j = i + l - 1
            print(s[i], s[j])
            length = 0
            if l == 2:
                if s[i] == s[j]:
                    T[i][j] = True
                    length = 2
            else:
                if s[i] == s[j] and T[i + 1][j - 1] == True:
                    T[i][j] = True
                    print(T)
                    length = j - i + 1

            if length > mx:
                mx = length
    return mx


def longestPalindrome(s):
    res = ""
    for i in range(len(s)):
        # odd case, like "aba"
        tmp = helper(s, i, i)
        if len(tmp) > len(res):
            res = tmp
        # even case, like "abba"
        tmp = helper(s, i, i + 1)
        if len(tmp) > len(res):
            res = tmp
    return res

# get the longest palindrome, l, r are the middle indexes
# from inner to outer


def helper(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l + 1:r]


def n_squared(s):
    if s is None or len(s) < 1:
        return ""

    start = 0
    end = 0
    for i in range(0, len(s)):
        # odd case
        len1 = expand(s, i, i)
        # even case
        len2 = expand(s, i, i + 1)

        ll = max(len1, len2)
        print("i", i)
        print("end", end, "start", start)
        if ll > end - start:
            start = i - end - start // 2
            end = (i + ll) // 2

    return s[start:end + 1]


def expand(s, left, right):
    l = left
    r = right
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return r - l - 1


t1 = "babad"
# r = longest_palondromic_substring(t1)
# print(r)


r = n_squared(t1)
print(r)
