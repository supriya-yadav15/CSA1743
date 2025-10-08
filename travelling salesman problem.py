import itertools
import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def tsp_bruteforce(cities):
    n = len(cities)
    # Create distance matrix
    dist_matrix = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                dist_matrix[i][j] = euclidean_distance(cities[i], cities[j])
    
    best_tour = None
    min_distance = float('inf')
    
    for perm in itertools.permutations(range(1, n)):
        tour = [0] + list(perm) + [0]
        distance = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
        if distance < min_distance:
            min_distance = distance
            best_tour = tour
    
    return best_tour, min_distance

if __name__ == "__main__":
    cities = [
        [0, 0],
        [1, 5],
        [5, 2],
        [6, 6],
        [8, 3]
    ]

    tour, total_distance = tsp_bruteforce(cities)
    print("Best Tour:", tour)
    print("Minimum Distance:", total_distance)
