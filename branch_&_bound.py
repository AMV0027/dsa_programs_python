import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]
        
    def tsp(self):
        # Store all vertex apart from source vertex
        vertex = []
        for i in range(self.V):
            if i != 0:
                vertex.append(i)
        
        # Store minimum weight Hamiltonian Cycle
        min_path = sys.maxsize
        
        while True:
            # Store current Path weight(cost)
            current_pathweight = 0
            
            # Compute current path weight
            k = 0
            for i in range(len(vertex)):
                current_pathweight += self.graph[k][vertex[i]]
                k = vertex[i]
            current_pathweight += self.graph[k][0]
            
            # Update minimum
            min_path = min(min_path, current_pathweight)
            
            if not next_permutation(vertex):
                break
        
        return min_path

def next_permutation(L):
    n = len(L)
    
    i = n - 2
    while i >= 0 and L[i] >= L[i + 1]:
        i -= 1
    
    if i == -1:
        return False
    
    j = n - 1
    while L[j] <= L[i]:
        j -= 1
    
    L[i], L[j] = L[j], L[i]
    
    left = i + 1
    right = n - 1
    
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1
    
    return True

# Example usage:
g = Graph(4)
g.graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
print("Minimum cost:", g.tsp())