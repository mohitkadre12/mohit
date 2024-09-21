def three_sum(nums):
    nums.sort()  # Sorting the array
    triplets = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  

        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                triplets.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1  # Skiping duplicates
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1  # Skiping

                left += 1
                right -= 1
            elif total < 0:
                left += 1  # Increase sum
            else:
                right -= 1  # Decreasing sum

    return triplets

# Example data
nums = [-1, 0, 1, 2, -1, -4]
result = three_sum(nums)
print(result)
