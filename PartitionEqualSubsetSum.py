def can_partition_recursive(nums, curr, S):
    # Base Case 1: If curr == S/2
    if curr == S/2:
        return True

    #Base Case 2: If we are out of nums to process
    if len(nums) == 0:
        return False

    if_excluded = can_partition_recursive(nums[1:], curr, S)

    if nums[0] + curr <= S/2:
        return if_excluded or can_partition_recursive(nums[1:], nums[0] + curr, S)

    return if_excluded


def can_partition_tabulation(nums, S):
    
    dp = [[False] * ((S//2) + 1) for _ in nums]


    for i in range(len(dp)):
        for j in range(len(dp[0])):
            
            # We want to know if we can sum up to equal subset at each cell

            # If we have a sum of zero we are trying to sum up to, we can
            if j == 0:
                dp[i][j] = True
                continue

            # Else, we need to see if we can sum up to the sum by either excluding this item or including this item
            exclude, include = False, False

            # If we exlcude the item, simply observe if we were able to build the cell above to be True
            if i != 0:
                exclude = dp[i-1][j]

            # If we include the item, simply observe if were able to build the cell with nums[i] less value

            if nums[i] <= j and i != 0:
                include = dp[i-1][j-nums[i]]


            dp[i][j] = include or exclude

    # for row in dp:
    #     print(row)
    return dp[-1][-1]




            

        

    


def can_partition(nums):
    S = sum(nums)
    if S%2 != 0:
        return False

    return can_partition_tabulation(nums, S)



def main():
  print(can_partition([1, 2, 3, 4]) == True)
  print(can_partition([1, 1, 3, 4, 7]) == True)
  print(can_partition([2, 3, 4, 6]) == False)
  print(can_partition([2, 3, 4, 6]) == False)
  print(can_partition([1, 5, 11,5]) == True)
  print(can_partition([1, 2, 3, 5]) == False)
  print(can_partition([7, 2, 3]) == False)

main()
