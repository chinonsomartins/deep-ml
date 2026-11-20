
def matrix_dot_vector(a, b):

    results = []
    
    if len(a[0]) != len(b):
        
        return -1

    for row in a:

        total = 0

        for i in range(len(row)):
            total += row[i] * b[i]

        results.append(total)
    return results

print(matrix_dot_vector([[1, 2, 3], [2, 4, 5], [6, 8, 9]], [1, 2, 3]))

