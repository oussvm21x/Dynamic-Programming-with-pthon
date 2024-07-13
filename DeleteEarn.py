def deleteNdEarn(nums) :
    num_counts = {}
    for num in nums:
        if num in num_counts:
            num_counts[num] += 1
        else:
            num_counts[num] = 1

    nums = list(set(nums))
    nums.sort()

    dp = [0]*len(nums)
    dp[0] = nums[0]*num_counts[nums[0]]
    dp[1] = nums[1]*num_counts[nums[1]] + dp[0] if abs(nums[1] - nums[0]) != 1 else max(dp[0], nums[1]*num_counts[nums[1]])
    for i in range(2, len(nums)):
        dp[i] = nums[i]*num_counts[nums[i]] + dp[i-1] if abs(nums[i] - nums[i-1]) != 1 else max(dp[i-1], nums[i]*num_counts[nums[i]] + dp[i-2])

    return dp[-1]