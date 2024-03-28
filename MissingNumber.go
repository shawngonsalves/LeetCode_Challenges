/*
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

 

Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
Example 2:

Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
 
*/

func missingNumber(nums []int) int {
    N := len(nums)
    sort.Ints(nums)

    for i:= 0; i< N; i++ {
        if i!= nums[i]{
            return i
        }
    }
    return N
    
}

// Runtime 11 ms Beats 86.36% of users with Go
// Memory 6.45 MB Beats 44.27% of users with Go

func missingNumber(nums []int) int {
    N := len(nums)
    expected_Sum := (N*(N+1))/2
    actual_Sum := 0

    for _, num:= range nums {
        actual_Sum += num
    }
    return expected_Sum - actual_Sum
    
}

//Runtime 9 ms Beats 93.23% of users with Go
//Memory 6.49 MB Beats 44.27% of users with Go