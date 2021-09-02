"""
Salesforce Question
https://www.careercup.com/question?id=5161552609542144
"""

# This is similar to subset sum problem

def min_abs_diff(nums):
    target = sum(nums) // 2

    dp = [[] for _ in range(target+1)]
    end_point = target

    for num in nums:
        for j in range(target, num-1, -1):
            curr = sum(dp[j-num])
            if num > target or num + curr > target:
                end_point = j
                return dp[j-num] + [num]
            else:
                dp[j] = dp[j-num] + [num]
    partitions = [list(set(dp[end_point]) ^  nums), dp[end_point]]
    
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