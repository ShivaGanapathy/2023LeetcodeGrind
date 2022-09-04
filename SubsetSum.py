def can_partition(num, target_sum):

    max_val = sum(num)

    if max_val < target_sum:
        return False

    dp = [ [False]  * (target_sum + 1) for i in num]
    dp[0][0] = True


    for i in range(len(dp)):
        for j in range(len(dp[0])):

            
            
            if j == 0 or j == num[i]:
                dp[i][j] = True
                continue

         
    

            # We want to know if it is possible to create the desired subset sum by including or excluding
            include, exclude = False, False



            if i != 0:
                
                if num[i] <= j:
                    include = dp[i-1][j-num[i]]


                exclude = dp[i-1][j]

            
            dp[i][j] = include or exclude


    return dp[-1][-1]





print(can_partition([1,2,3,4,5], 5) == True)
print(can_partition([1,2,3,4,5], 9) == True)
print(can_partition([1,2,3,4,5], 100) == False)
print(can_partition([1,2,3,4,5], 8) == True)
print(can_partition([1, 2], 1) == True)
print(can_partition([1,2,5], 4) == False)
print(can_partition([1, 2, 8, 16], 13) == False)
