import time

def solve_knapsack_recursive(profits, weights, capacity):
    # Base case 1: There are no more items to process:
    if len(weights) == 0:
        return 0

    # Base case 2: We have reached a capacity of 0
    if capacity == 0:
        return 0

    include = 0
    exclude = 0
    # If it is possible to include this item
    if weights[0] <= capacity:
        include = profits[0] + solve_knapsack_recursive(profits[1:], weights[1:], capacity - weights[0])

    exclude = solve_knapsack_recursive(profits[1:], weights[1:], capacity)

    return max(include, exclude)

        




def solve_knapsack_tabulation(profits, weights, capacity):
    dp = [ [0] * (capacity + 1) for _ in range(len(profits))]

    for i in range(len(dp)):
        for j in range(len(dp[0])):

            include = 0
            exclude = 0
            
            # Are we allowed to include?
            if weights[i] <= j:

                include = profits[i]

                # If i == 0, don't try to read table
                if i != 0:
                    include += dp[i-1][j-weights[i]]
                    
            # Calculate exclude value
            if i != 0:
                exclude = dp[i-1][j]


            dp[i][j] = max(include, exclude)

    return dp[-1][-1]



def solve_knapsack(profits, weights, capacity):

    t1 = time.time()
    res1 = solve_knapsack_recursive(profits, weights, capacity)
    t2 = time.time()
    # print(f"The recursive solution took {t2-t1} seconds.")


    t1 = time.time()
    res2 = solve_knapsack_tabulation(profits, weights, capacity)
    t2 = time.time()
    # print(f"The bottom-up solution took {t2-t1} seconds.")

    return res1 if res2 == res1 else -1





  

def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5) == 16)
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6) == 17)
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7) == 22)
    print(solve_knapsack([ 20, 5, 10, 40, 15, 25 ], [ 1, 2, 3, 8, 7, 4 ], 10) == 60)
    print(solve_knapsack([ 20, 5, 10, 40, 15, 25 ], [ 1, 2, 3, 8, 7, 4 ], 0) == 0)



    # print(solve_knapsack([ i for i in range(0, 68, 3) ], [ i%3 for i in range(0, 68, 3) ], 100))





main()
