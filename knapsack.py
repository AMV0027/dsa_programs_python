def knapsack(W, wt, val, n):

    if n == 0 or W == 0:
        return 0
    
    if (wt[n-1] > W):
        return knapsack(W, wt, val, n-1)
    
    else:
        return max(val[n-1]+knapsack(W-wt[n-1], wt, val, n-1), knapsack(W, wt, val, n-1))

if __name__ == '__main__':
    profit = []
    weight = []

    print("\n-------------\n")

    count = int(input("number of element : "))
    for i in range(count):
        num = int(input(f"profit {i} : "))
        profit.append(num)

    print("\n-------------\n")

    for i in range(count):
        num = int(input(f"weight {i} : "))
        weight.append(num)

    print("\n-------------\n")
    
    W = int(input("Enter maximum weight : "))

    print("\n-------------\n")

    n = len(profit)
    print (f"Maximum profit can be made : {knapsack(W, weight, profit, n)}") 

    print("\n-------------\n")