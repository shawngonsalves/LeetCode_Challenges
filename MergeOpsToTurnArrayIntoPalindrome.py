'''
Given an array of positive integers. 
We need to make the given array a ‘Palindrome’. 
The only allowed operation is”merging” (of two adjacent elements). 
Merging two adjacent elements means replacing them with their sum. The task is to find the minimum number of merge operations required to make the given array a ‘Palindrome’.

To make any array a palindrome, we can simply apply merge operation n-1 times where n is the size of the array 
(because a single-element array is always palindromic, similar to single-character string). In that case, the size of array will be reduced to 1. But in this problem, we are asked to do it in the minimum number of operations.

Input : arr[] = {15, 4, 15}
Output : 0
Array is already a palindrome. So we
do not need any merge operation.

Input : arr[] = {1, 4, 5, 1}
Output : 1
We can make given array palindrome with
minimum one merging (merging 4 and 5 to
make 9)

Input : arr[] = {11, 14, 15, 99}
Output : 3
We need to merge all elements to make
a palindrome.
'''

def findMinOps(arr):
    q = deque(arr)
    count = 0

    while len(q) > 2:
        if q[0] == q[-1]:
            q.popleft()
            q.pop()
        elif q[0] > q[-1]:
            a = q.pop() + q.pop()
            q.append(a)
            count += 1
        else:
            a = q.popleft() + q.popleft()
            q.appendleft(a)
            count += 1
    return count
