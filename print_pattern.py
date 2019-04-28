'''
You a given a number N. You need to print the pattern for the given value of N.
for N=2 the pattern will be
2 2 1 1
2 1
for N=3 the pattern will be
3 3 3 2 2 2 1 1 1
3 3 2 2 1 1
3 2 1

Input Format:
The first line of input is the number of testcases T. The T test cases follow. The first line of each test case is an integer N.

Output Format:
For each test case, in a new line, print the required pattern in a singleline .
Note : Instead of printing new line print a "$" without quotes.

Your Task:
Since this is a function problem, you don't need to worry about the testcases. Your task is to complete the function printPat which takes one argument 'N' denoting the length of the pattern.

Constraints:
1 <= T <= 20
1 <= N <= 40

Example:
Input
2
2
3
Output
2 2 1 1 $2 1 $
3 3 3 2 2 2 1 1 1 $3 3 2 2 1 1 $3 2 1 $
'''

# def printPat(n):
#   start = n
#   result = []
#   while(n > 0):
#     i = start
#     row = []
#     while(i > 0):
#       for _ in range(n):
#         if not row and n != start:
#           row.append(" $" + str(i))
#         else:
#           row.append(i)
#       i -= 1
#     result += " ".join(map(str, row))
#     n -= 1
#   result.append(" $")
#   print("".join(map(str, result)))


def printPat(n):
    for i in range(n, 0, -1):
        for j in range(n, 0, -1):
            print((str(j) + ' ') * i, end='')
        print('$', end='')
    return ''


printPat(4)
