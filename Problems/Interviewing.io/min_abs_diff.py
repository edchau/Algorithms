"""
Salesforce Question
https://www.careercup.com/question?id=5161552609542144
partition a set so its difference between the sums are 
the minimum absolute difference
"""

# This is similar to subset sum problem

def min_abs_diff(nums):
    target = sum(nums) // 2

    dp = [[] for _ in range(target+1)]

    for num in nums:
        for j in range(target, num-1, -1):
            curr = sum(dp[j-num])
            if not(num > target or num + curr > target):
                dp[j] = dp[j-num] + [num]
    partitions = [list(set(dp[target]) ^  nums), dp[target]]
    
    return partitions

"""
{1,2,3,4,90}
s1: 90 (sum 90)
s2: 1,2,3,4 (sum 10)

{1,2,3,14,15,16}
s1: 16,3,2,1 (sum 22)
s2: 15,14 (sum 29)
"""
test1 = {1, 2, 3, 4, 90}
test2 = {1, 2, 3, 14, 15, 16}

print(min_abs_diff(test1))
print(min_abs_diff(test2))