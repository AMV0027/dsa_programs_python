dp = [[-1 for i in range(100)] for j in range(100)]

def matrixMemoised(p,i,j):
    if (i==j):
        return 0
    if(dp[i][j] != -1):
        return dp[i][j]
    dp[i][j] = float('inf')

    for k in range(i,j):
        dp[i][j] = min(dp[i][j], matrixMemoised(p,i,k) + matrixMemoised(p, k+1, j) + p[i-1] * p[k] * p[j])

    return dp[i][j]

def matrixChainOrder(p,n):
    i = 1
    j = n-1
    return matrixMemoised(p,i,j)

arr = [1,2,3,4]

n = len(arr)
print(f"minimum number of multiplication is { matrixChainOrder(arr,n) }")